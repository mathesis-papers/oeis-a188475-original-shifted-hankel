# Barry's shifted Hankel conjecture and an extension of Cigler's formula

**Authors:** Haobo Ma, Wenlin Zhang

We prove Paul Barry's shifted Hankel conjecture in OEIS A188475, revision 2 (April 1, 2011): for every n>=0, det[q(i+j+2)]_(0<=i,j<=n)=(2n^3+3n^2+n+3)/3, by a moment-matrix cofactor argument extending Cigler's unit-descent formula (2011, Theorem A*). The same calculation gives both adjacent shifts and a parameter formula det[q_lambda(i+j+2)]_(i,j<N)=1+lambda*sum(k^2,k=0..N-1) for every complex lambda, with q_lambda defined by its Catalan generating function. A direct bijection relates the source's nonexchangeable subsequences to Callan's restricted Grand Dyck paths.

- PDF: [frozen public file](paper.pdf)
- License: CC-BY-4.0
- Version: 4
- Mathesis record: [oeis-a188475-original-shifted-hankel](https://mathesis-omega-research.apps.chrono-ai.fun/papers/oeis-a188475-original-shifted-hankel?version=4)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Barry's shifted Hankel conjecture and an extension of Cigler's formula. Mathesis, version 4. https://mathesis-omega-research.apps.chrono-ai.fun/papers/oeis-a188475-original-shifted-hankel?version=4

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/c6d80ec1ad5920a0470d7ff831c17f6303e6e578/D5/S3/Combinatorics/CatalanPowerHankel/BarryA188475.lean) | No public receipt |
| Corollary (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/c6d80ec1ad5920a0470d7ff831c17f6303e6e578/D5/S3/Combinatorics/CatalanPowerHankel/BarryA188475.lean) | No public receipt |
| Corollary (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/c6d80ec1ad5920a0470d7ff831c17f6303e6e578/D5/S3/Combinatorics/CatalanPowerHankel/BarryA188475.lean) | No public receipt |
| Corollary (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/c6d80ec1ad5920a0470d7ff831c17f6303e6e578/D5/S3/Combinatorics/CatalanPowerHankel/BarryA188475.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).
