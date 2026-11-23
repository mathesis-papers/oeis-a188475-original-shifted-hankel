# Barry's shifted Hankel conjecture and an extension of Cigler's formula

Haobo Ma (ChronoAI Pte Ltd, Singapore), then Wenlin Zhang (National University
of Singapore; ChronoAI Pte Ltd, Singapore). CC BY 4.0.

For the positive-index Catalan recurrence in OEIS A137398, the determinant
`det[q(i+j+2)]_(0<=i,j<=n)` is `(2*n^3+3*n^2+n+3)/3` for every `n>=0`.
The complete written proof, both adjacent shifts, and a one-parameter
extension are in `note.tex` and `note.pdf`. If
`F_lambda(z)=z^2*C(z)^2/(1-lambda*z^2*C(z)^2)` and `q_lambda(r)=[z^r]F_lambda`,
the order-`N` determinant of `q_lambda(i+j+2)` is
`1+lambda*sum(k^2,k=0..N-1)` for every complex `lambda` and `N>=1`.
The original recurrence is `lambda=2`. Both adjacent determinants are
independent of `lambda`.

The specialization `lambda=1` is credited to Cigler (2011), Theorem A*,
and Chang--Hu--Zhang (2013), Theorem 3.5. The original conjecture requires
`lambda=2`. The note states the exact distinction between these moment series.

Mu and Wang, *Hankel determinants of shifted Catalan-like numbers*,
Discrete Mathematics 340(6) (2017), 1389–1396,
doi:10.1016/j.disc.2016.09.035, is closely related work whose relationship
to the cubic identity remains unresolved. Overlap is not excluded;
no priority claim is made.

A direct membership-word bijection identifies the nonexchangeable
subsequences with Callan's restricted Grand Dyck paths. Exchanges use the
order inherited from the ground sequence, as in the OEIS examples.
The historical index translation and the continued-fraction normalization
are explained in the note. The displayed OEIS triangle is outside its coverage.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively run `pdflatex note.tex` twice. The bibliography is included in
the TeX source; no BibTeX database or external figures are needed.

## Exact finite checks

Python 3.9 or newer, with no third-party packages:

```sh
python3 verify.py > checks.json
```

The checks cover the cubic for `0<=n<=24`, both adjacent shifts for matrix
orders `1..25`, moment coefficients through degree 52, and polynomial
orthogonality for every pair of degrees `0..16`. They use exact integer
arithmetic, with no numerical rounding. `checks.json` records these ranges.
They also check the three determinant formulas at `lambda=-3,0,1,2,5`
for orders `1..12`, and independently enumerate restricted paths and
nonexchangeable subsequence pairs for semilengths `1..8`.
The general theorem and corollaries have full written proofs in the note.

## Formal statement

The pinned `.lean` source is:

https://github.com/the-omega-institute/trureturing/blob/c6d80ec1ad5920a0470d7ff831c17f6303e6e578/D5/S3/Combinatorics/CatalanPowerHankel/BarryA188475.lean

`BarryA188475.result` states both all-index equalities for the definitions
`BarryA188475.q` and `BarryA188475.hankel`. Its statement covers the main
theorem for matrices of order `n+1`. The adjacent-shift corollaries,
parameter family, and combinatorial interpretations have written proofs
and the finite checks described above; they are outside that declaration's statement.

## Files

- `note.tex`: complete mathematical source and bibliography.
- `note.pdf`: readable typeset note.
- `verify.py`: exact finite checker.
- `checks.json`: finite-check results and ranges.
- `metadata.json`: authorship, license, problem identity, and formal statement URL.

## License

Copyright 2026 Haobo Ma and Wenlin Zhang. Creative Commons Attribution 4.0
International: https://creativecommons.org/licenses/by/4.0/.
