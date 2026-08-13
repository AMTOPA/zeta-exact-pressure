# Banded-Gram insertion audit

Date: 2026-08-13

This note isolates the analytic compatibility question for the banded-Gram
profile from the already-imported exact pressure-multiplicity refinement.

## 1. Local-to-block pair counting preserves six-band information

The positioned-pressure predecessor sums `m-6` translated seven-point local
inequalities.  Every local pair has index span at most six and, for each span
`s=1,...,6`, the exact pair weights sum to capacity 2.  Therefore the summed
pair term is bounded above already by

\[
E_6=2\sum_{1\le j-i\le6}|G_{ij}|^2,
\]

not merely by the larger unrestricted energy

\[
E=2\sum_{i<j}|G_{ij}|^2.
\]

The predecessor replaced the banded quantity by total energy because its next
analytic input was the unrestricted profile `h_m(E)`.  Retaining `E_6` is a
refinement of that same counting step; it does not alter the local certificate.

## 2. What shifted-block averaging actually needs

The predecessor block argument first proves, for every principal `m`-block,

\[
\operatorname{tr}\Psi(G_B)+\eta P_B\ge R-o(1).
\]

Only after this block inequality is established does spectral pinching and
shifted-partition averaging enter.  Thus the averaging layer does not require
that `R` originate from the unrestricted total-energy profile.  Any valid
blockwise inequality of the displayed form can be inserted at the same point.

The proposed banded profile supplies such an inequality from

\[
\Delta(G_B)\ge g_6(E_6)
\]

and the supporting-line lower bounds relating `E_6` to the retained exact
pressure `P_B`.

## 3. Exact pressure multiplicity is a separate imported refinement

The factor `m-6` in the final pressure penalty is not part of the new
banded-Gram claim.  It comes from the earlier exact-pressure refinement
(`AMTOPA/zeta-exact-pressure-673262`): if

\[
P_B=\sum_{j=1}^{m-1}c_jg_j,
\]

then direct double counting gives

\[
\sum_{j=1}^{m-1}c_j=(m-6)B.
\]

Across all `m` shifted partitions a fixed global gap occupies each internal
block position exactly once, giving the exact global pressure factor
`B(m-6)/m`.  The current root scalar-Gram baseline already relies on this
refinement.

## 4. Remaining review question

Relative to the current root baseline, the genuinely new analytic step is
therefore:

1. verify the matrix inequality `tr Psi(G) >= g_q(E_q)`;
2. verify the supporting-line / concavity conversion to a block inequality
   `tr Psi(G_B)+eta P_B >= R`;
3. confirm that spectral pinching can then be applied exactly as in the imported
   block argument, with no hidden invocation of total off-diagonal energy after
   the block inequality has already been obtained.

Numerical interval certification and exact rational endpoint checks do not
resolve these three analytic questions; they are the intended scope of issue
#5.
