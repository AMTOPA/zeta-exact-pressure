#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

#include "candidate_config.hpp"

namespace {
constexpr int Q = candidate_config::gaps;
constexpr int GRID = 4000;
using Range = std::pair<int, int>;

struct Box {
    std::array<Range, Q> gap{};
    int depth = 0;
};

inline double down(double x) {
    return std::nextafter(x, -std::numeric_limits<double>::infinity());
}
inline double up(double x) {
    return std::nextafter(x, std::numeric_limits<double>::infinity());
}
inline long double ldown(long double x) {
    return std::nextafterl(x, -std::numeric_limits<long double>::infinity());
}
inline long double lup(long double x) {
    return std::nextafterl(x, std::numeric_limits<long double>::infinity());
}

struct Interval {
    long double lo;
    long double hi;
};

Interval point(long double x) { return {x, x}; }
Interval add(Interval a, Interval b) { return {ldown(a.lo + b.lo), lup(a.hi + b.hi)}; }
Interval neg(Interval a) { return {-a.hi, -a.lo}; }
Interval sub(Interval a, Interval b) { return add(a, neg(b)); }
Interval mul(Interval a, Interval b) {
    const long double p[4] = {a.lo*b.lo, a.lo*b.hi, a.hi*b.lo, a.hi*b.hi};
    return {
        ldown(*std::min_element(p, p + 4)),
        lup(*std::max_element(p, p + 4))
    };
}
Interval square(Interval a) {
    const long double hi = std::max(a.lo*a.lo, a.hi*a.hi);
    const long double lo = (a.lo <= 0 && a.hi >= 0)
        ? 0
        : std::min(a.lo*a.lo, a.hi*a.hi);
    return {lo == 0 ? 0 : ldown(lo), lup(hi)};
}
Interval div_positive(Interval a, Interval b) {
    if (!(b.lo > 0)) throw std::runtime_error("interval division by nonpositive denominator");
    return mul(a, {ldown(1.0L / b.hi), lup(1.0L / b.lo)});
}
long double abs_upper(Interval a) {
    return lup(std::max(std::fabs(a.lo), std::fabs(a.hi)));
}
Interval rational_interval(std::int64_t num, std::int64_t den) {
    const long double q = static_cast<long double>(num) / static_cast<long double>(den);
    return {ldown(q), lup(q)};
}

std::vector<double> read_f64(const std::string& path) {
    std::ifstream in(path, std::ios::binary | std::ios::ate);
    if (!in) throw std::runtime_error("cannot open " + path);
    const auto bytes = static_cast<std::size_t>(in.tellg());
    if (bytes % sizeof(double) != 0) throw std::runtime_error("bad table size: " + path);
    in.seekg(0);
    std::vector<double> out(bytes / sizeof(double));
    in.read(reinterpret_cast<char*>(out.data()), static_cast<std::streamsize>(bytes));
    if (!in) throw std::runtime_error("short read: " + path);
    return out;
}

bool file_exists(const std::string& path) {
    std::ifstream in(path, std::ios::binary);
    return static_cast<bool>(in);
}

class MinTree {
public:
    MinTree() = default;
    explicit MinTree(const std::vector<double>& values) { reset(values); }

    void reset(const std::vector<double>& values) {
        size_ = 1;
        while (size_ < values.size()) size_ <<= 1;
        tree_.assign(2 * size_, std::numeric_limits<double>::infinity());
        for (std::size_t i = 0; i < values.size(); ++i) tree_[size_ + i] = values[i];
        for (std::size_t i = size_ - 1; i > 0; --i)
            tree_[i] = std::min(tree_[2 * i], tree_[2 * i + 1]);
        count_ = values.size();
    }

    double query(int left, int right, bool nonnegative_fallback) const {
        if (left < 0 || right < left)
            return -std::numeric_limits<double>::infinity();
        if (static_cast<std::size_t>(right) >= count_)
            return nonnegative_fallback ? 0.0 : -std::numeric_limits<double>::infinity();
        std::size_t l = static_cast<std::size_t>(left) + size_;
        std::size_t r = static_cast<std::size_t>(right) + size_;
        double ans = std::numeric_limits<double>::infinity();
        while (l <= r) {
            if (l & 1U) ans = std::min(ans, tree_[l++]);
            if (!(r & 1U)) ans = std::min(ans, tree_[r--]);
            l >>= 1U;
            r >>= 1U;
        }
        return ans;
    }

    std::size_t count() const { return count_; }

private:
    std::size_t size_ = 0;
    std::size_t count_ = 0;
    std::vector<double> tree_;
};

struct PairWeight {
    int i;
    int j;
    double lower;
    double upper;
    Interval interval;
};

struct Stats {
    std::uint64_t nodes = 0;
    std::uint64_t pruned = 0;
    std::uint64_t splits = 0;
    std::uint64_t convex = 0;
    std::uint64_t tangent = 0;
    int max_depth = 0;
};

bool prove_positive_definite(
    const Box& box,
    const std::array<int, Q + 1>& prefix_lo,
    const std::array<int, Q + 1>& prefix_hi,
    const std::vector<PairWeight>& pairs,
    const MinTree& second_min
) {
    std::array<std::array<Interval, Q>, Q> matrix{};
    for (int r = 0; r < Q; ++r)
        for (int c = 0; c < Q; ++c)
            matrix[r][c] = point(0);

    for (const auto& p : pairs) {
        const int span = p.j - p.i;
        const int left = prefix_lo[p.j] - prefix_lo[p.i];
        const int right = prefix_hi[p.j] - prefix_hi[p.i] + span - 1;
        const double s = second_min.query(left, right, false);
        if (!std::isfinite(s)) return false;

        const double scalar = s >= 0
            ? down(p.lower * s)
            : down(p.upper * s);
        const Interval term = point(static_cast<long double>(scalar));
        for (int r = p.i; r < p.j; ++r)
            for (int c = p.i; c < p.j; ++c)
                matrix[r][c] = add(matrix[r][c], term);
    }

    std::array<std::array<Interval, Q>, Q> L{};
    std::array<Interval, Q> D{};
    for (int r = 0; r < Q; ++r)
        for (int c = 0; c < Q; ++c)
            L[r][c] = point(0);

    for (int col = 0; col < Q; ++col) {
        Interval pivot = matrix[col][col];
        for (int k = 0; k < col; ++k)
            pivot = sub(pivot, mul(square(L[col][k]), D[k]));
        if (!(pivot.lo > 0)) return false;
        D[col] = pivot;
        L[col][col] = point(1);
        for (int row = col + 1; row < Q; ++row) {
            Interval value = matrix[row][col];
            for (int k = 0; k < col; ++k)
                value = sub(value, mul(mul(L[row][k], L[col][k]), D[k]));
            L[row][col] = div_positive(value, pivot);
        }
    }
    return true;
}

long double tangent_lower_bound(
    const Box& box,
    const std::vector<PairWeight>& pairs,
    const std::array<Interval, Q>& pressure,
    const std::vector<double>& w_mid_lo,
    const std::vector<double>& w_mid_hi,
    const std::vector<double>& d_mid_lo,
    const std::vector<double>& d_mid_hi
) {
    std::array<int, Q> mid_num{};
    std::array<int, Q + 1> prefix_mid{};
    std::array<Interval, Q> gradient{};
    Interval value = point(0);

    for (int c = 0; c < Q; ++c) {
        mid_num[c] = box.gap[c].first + box.gap[c].second + 1;
        prefix_mid[c + 1] = prefix_mid[c] + mid_num[c];
        const long double xq = static_cast<long double>(mid_num[c]) / (2.0L * GRID);
        const Interval x = {ldown(xq), lup(xq)};
        value = add(value, mul(pressure[c], x));
        gradient[c] = pressure[c];
    }

    for (const auto& p : pairs) {
        const int index = prefix_mid[p.j] - prefix_mid[p.i];
        if (index < 0 || static_cast<std::size_t>(index) >= w_mid_lo.size())
            return -std::numeric_limits<long double>::infinity();
        const Interval w = {
            static_cast<long double>(w_mid_lo[index]),
            static_cast<long double>(w_mid_hi[index])
        };
        const Interval derivative = {
            static_cast<long double>(d_mid_lo[index]),
            static_cast<long double>(d_mid_hi[index])
        };
        value = add(value, mul(p.interval, w));
        const Interval slope = mul(p.interval, derivative);
        for (int c = p.i; c < p.j; ++c)
            gradient[c] = add(gradient[c], slope);
    }

    long double lower = value.lo;
    for (int c = 0; c < Q; ++c) {
        const long double radius = lup(
            static_cast<long double>(box.gap[c].second - box.gap[c].first + 1)
            / (2.0L * GRID)
        );
        lower = ldown(lower - lup(abs_upper(gradient[c]) * radius));
    }
    return lower;
}

} // namespace

int main(int argc, char** argv) {
    try {
        std::int64_t target_num = candidate_config::target_num;
        std::int64_t target_den = candidate_config::target_den;
        std::string table_dir = "tables";
        std::uint64_t max_nodes = 0;
        if (argc >= 3) {
            target_num = std::stoll(argv[1]);
            target_den = std::stoll(argv[2]);
        }
        if (argc >= 4) table_dir = argv[3];
        if (argc >= 5) max_nodes = static_cast<std::uint64_t>(std::stoull(argv[4]));
        if (target_num <= 0 || target_den <= 0) throw std::runtime_error("target must be positive");

        for (int span = 1; span <= Q; ++span) {
            std::int64_t total = 0;
            for (const auto& p : candidate_config::pairs)
                if (p.j - p.i == span) total += p.num;
            if (total != candidate_config::span_capacity_num)
                throw std::runtime_error("pair span capacity mismatch");
        }

        std::int64_t pressure_total = 0;
        for (auto n : candidate_config::pressure_num) pressure_total += n;
        if (pressure_total != candidate_config::pressure_total_num)
            throw std::runtime_error("pressure total mismatch");

        const double target = static_cast<double>(target_num) / static_cast<double>(target_den);
        const double target_up = up(target);

        const auto lower_values = read_f64(table_dir + "/w_lower.bin");
        MinTree wmin(lower_values);

        const bool accelerated =
            file_exists(table_dir + "/w_second_lower.bin") &&
            file_exists(table_dir + "/w_mid_lower.bin") &&
            file_exists(table_dir + "/w_mid_upper.bin") &&
            file_exists(table_dir + "/w_prime_mid_lower.bin") &&
            file_exists(table_dir + "/w_prime_mid_upper.bin");

        std::vector<double> second_values;
        MinTree second_min;
        std::vector<double> w_mid_lo, w_mid_hi, d_mid_lo, d_mid_hi;
        if (accelerated) {
            second_values = read_f64(table_dir + "/w_second_lower.bin");
            second_min.reset(second_values);
            w_mid_lo = read_f64(table_dir + "/w_mid_lower.bin");
            w_mid_hi = read_f64(table_dir + "/w_mid_upper.bin");
            d_mid_lo = read_f64(table_dir + "/w_prime_mid_lower.bin");
            d_mid_hi = read_f64(table_dir + "/w_prime_mid_upper.bin");
            if (second_values.size() != lower_values.size() ||
                w_mid_lo.size() != w_mid_hi.size() ||
                w_mid_lo.size() != d_mid_lo.size() ||
                w_mid_lo.size() != d_mid_hi.size())
                throw std::runtime_error("accelerator table size mismatch");
        }

        std::array<double, Q> pressure_lo{};
        std::array<Interval, Q> pressure_interval{};
        for (int i = 0; i < Q; ++i) {
            pressure_lo[i] = down(static_cast<double>(candidate_config::pressure_num[i]) /
                                  static_cast<double>(candidate_config::pressure_den));
            pressure_interval[i] = rational_interval(
                candidate_config::pressure_num[i], candidate_config::pressure_den);
        }
        const double min_pressure = *std::min_element(pressure_lo.begin(), pressure_lo.end());
        const int required_cells = static_cast<int>(std::ceil(target_up * GRID / min_pressure)) + 1;
        if (static_cast<int>(wmin.count()) < required_cells) {
            std::cerr << "table_too_short=true have=" << wmin.count()
                      << " required=" << required_cells << "\n";
            return 2;
        }

        std::vector<PairWeight> pairs;
        pairs.reserve(candidate_config::pairs.size());
        for (const auto& p : candidate_config::pairs) {
            const double lo = down(static_cast<double>(p.num) /
                                   static_cast<double>(candidate_config::pair_den));
            const double hi = up(static_cast<double>(p.num) /
                                 static_cast<double>(candidate_config::pair_den));
            pairs.push_back({p.i, p.j, lo, hi,
                rational_interval(p.num, candidate_config::pair_den)});
        }

        std::array<double, Q> adjacent{};
        for (const auto& p : pairs)
            if (p.j == p.i + 1) adjacent[p.i] = p.lower;

        std::array<std::vector<Range>, Q> components;
        for (int c = 0; c < Q; ++c) {
            bool active = false;
            int first = 0;
            int last = -2;
            for (int idx = 0; idx < static_cast<int>(wmin.count()); ++idx) {
                double one = down(pressure_lo[c] * static_cast<double>(idx) / GRID);
                if (adjacent[c] > 0.0)
                    one = down(one + down(adjacent[c] * lower_values[idx]));
                if (one < target_up) {
                    if (!active || idx > last + 1) {
                        if (active) components[c].push_back({first, last});
                        first = idx;
                        active = true;
                    }
                    last = idx;
                }
            }
            if (active) components[c].push_back({first, last});
            if (components[c].empty()) {
                std::cout << "VERIFIED=true reason=empty_component\n";
                return 0;
            }
        }

        std::vector<Box> initial;
        Box seed;
        std::function<void(int)> build = [&](int c) {
            if (c == Q) {
                initial.push_back(seed);
                return;
            }
            for (const auto& r : components[c]) {
                seed.gap[c] = r;
                build(c + 1);
            }
        };
        build(0);

        std::cout << "target=" << std::setprecision(17) << target
                  << " table_cells=" << wmin.count()
                  << " required_cells=" << required_cells
                  << " initial_boxes=" << initial.size()
                  << " accelerated=" << (accelerated ? "true" : "false")
                  << " components=";
        for (int i = 0; i < Q; ++i)
            std::cout << components[i].size() << (i + 1 == Q ? '\n' : ',');

        Stats stats;
        std::vector<Box> stack;
        stack.reserve(1024);
        for (const auto& root : initial) {
            stack.clear();
            stack.push_back(root);
            while (!stack.empty()) {
                if (max_nodes && stats.nodes >= max_nodes) {
                    std::cout << "INCONCLUSIVE=true reason=node_limit nodes=" << stats.nodes
                              << " pruned=" << stats.pruned << " splits=" << stats.splits
                              << " convex=" << stats.convex << " tangent=" << stats.tangent
                              << " max_depth=" << stats.max_depth << "\n";
                    return 3;
                }

                Box box = stack.back();
                stack.pop_back();
                ++stats.nodes;
                stats.max_depth = std::max(stats.max_depth, box.depth);

                std::array<int, Q + 1> prefix_lo{};
                std::array<int, Q + 1> prefix_hi{};
                double lower = 0.0;
                for (int c = 0; c < Q; ++c) {
                    prefix_lo[c + 1] = prefix_lo[c] + box.gap[c].first;
                    prefix_hi[c + 1] = prefix_hi[c] + box.gap[c].second;
                    lower = down(lower + down(pressure_lo[c] *
                        static_cast<double>(box.gap[c].first) / GRID));
                }
                if (lower >= target_up) {
                    ++stats.pruned;
                    continue;
                }

                for (const auto& p : pairs) {
                    const int span = p.j - p.i;
                    const int left = prefix_lo[p.j] - prefix_lo[p.i];
                    const int right = prefix_hi[p.j] - prefix_hi[p.i] + span - 1;
                    const double w = wmin.query(left, right, true);
                    if (!std::isfinite(w))
                        throw std::runtime_error("invalid lower-table query");
                    lower = down(lower + down(p.lower * w));
                }
                if (lower >= target_up) {
                    ++stats.pruned;
                    continue;
                }

                if (accelerated && prove_positive_definite(
                        box, prefix_lo, prefix_hi, pairs, second_min)) {
                    ++stats.convex;
                    const long double tangent = tangent_lower_bound(
                        box, pairs, pressure_interval,
                        w_mid_lo, w_mid_hi, d_mid_lo, d_mid_hi);
                    if (tangent >= static_cast<long double>(target_up)) {
                        ++stats.pruned;
                        ++stats.tangent;
                        continue;
                    }
                }

                int split = 0;
                int width = box.gap[0].second - box.gap[0].first;
                for (int c = 1; c < Q; ++c) {
                    const int w = box.gap[c].second - box.gap[c].first;
                    if (w > width) {
                        width = w;
                        split = c;
                    }
                }
                if (width == 0) {
                    std::cout << "INCONCLUSIVE=true reason=terminal_cell lower="
                              << std::setprecision(17) << lower << " box=";
                    for (const auto& r : box.gap)
                        std::cout << '[' << r.first << ',' << r.second << ']';
                    std::cout << " nodes=" << stats.nodes
                              << " convex=" << stats.convex << " tangent=" << stats.tangent
                              << "\n";
                    return 3;
                }

                const int lo = box.gap[split].first;
                const int hi = box.gap[split].second;
                const int mid = lo + (hi - lo) / 2;
                Box left_box = box;
                Box right_box = box;
                left_box.depth = right_box.depth = box.depth + 1;
                left_box.gap[split] = {lo, mid};
                right_box.gap[split] = {mid + 1, hi};
                stack.push_back(right_box);
                stack.push_back(left_box);
                ++stats.splits;
            }
        }

        std::cout << "VERIFIED=true nodes=" << stats.nodes
                  << " pruned=" << stats.pruned
                  << " splits=" << stats.splits
                  << " convex=" << stats.convex
                  << " tangent=" << stats.tangent
                  << " max_depth=" << stats.max_depth << "\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << "\n";
        return 2;
    }
}
