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

class MinTree {
public:
    explicit MinTree(const std::vector<double>& values) {
        size_ = 1;
        while (size_ < values.size()) size_ <<= 1;
        tree_.assign(2 * size_, std::numeric_limits<double>::infinity());
        for (std::size_t i = 0; i < values.size(); ++i) tree_[size_ + i] = values[i];
        for (std::size_t i = size_ - 1; i > 0; --i)
            tree_[i] = std::min(tree_[2 * i], tree_[2 * i + 1]);
        count_ = values.size();
    }

    double query(int left, int right) const {
        if (left < 0 || right < left)
            return -std::numeric_limits<double>::infinity();
        // W=(K/K(0))^2 is globally nonnegative.  If a requested distance
        // interval extends past the tabulated region, zero is therefore a
        // rigorous lower bound for the whole interval.
        if (static_cast<std::size_t>(right) >= count_) return 0.0;
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
};

struct Stats {
    std::uint64_t nodes = 0;
    std::uint64_t pruned = 0;
    std::uint64_t splits = 0;
    int max_depth = 0;
};

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
        if (pressure_total != 6000000LL)
            throw std::runtime_error("pressure total mismatch");

        const double target = static_cast<double>(target_num) / static_cast<double>(target_den);
        const double target_up = up(target);

        const auto lower_values = read_f64(table_dir + "/w_lower.bin");
        MinTree wmin(lower_values);

        std::array<double, Q> pressure_lo{};
        for (int i = 0; i < Q; ++i)
            pressure_lo[i] = down(static_cast<double>(candidate_config::pressure_num[i]) /
                                  static_cast<double>(candidate_config::pressure_den));
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
            pairs.push_back({p.i, p.j,
                down(static_cast<double>(p.num) / static_cast<double>(candidate_config::pair_den))});
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
                  << " initial_boxes=" << initial.size() << " components=";
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

                bool table_ok = true;
                for (const auto& p : pairs) {
                    const int span = p.j - p.i;
                    const int left = prefix_lo[p.j] - prefix_lo[p.i];
                    const int right = prefix_hi[p.j] - prefix_hi[p.i] + span - 1;
                    const double w = wmin.query(left, right);
                    if (!std::isfinite(w)) {
                        table_ok = false;
                        break;
                    }
                    lower = down(lower + down(p.lower * w));
                }
                if (!table_ok) {
                    std::cout << "INCONCLUSIVE=true reason=table_range nodes=" << stats.nodes << "\n";
                    return 3;
                }
                if (lower >= target_up) {
                    ++stats.pruned;
                    continue;
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
                    std::cout << " nodes=" << stats.nodes << "\n";
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
                  << " max_depth=" << stats.max_depth << "\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << "\n";
        return 2;
    }
}
