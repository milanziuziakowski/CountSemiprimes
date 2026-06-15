# CountSemi — Mathematical notes

This document explains mathematical background, asymptotics and algorithms for counting semiprimes (numbers with exactly two prime factors, counted with multiplicity).

Definitions

- A semiprime (also called 2-almost-prime) is a positive integer n = p*q where p and q are primes. If p=q the semiprime is a square of a prime.

Notation

- Let \(\pi(x)\) be the prime counting function: the number of primes \(\le x\).
- Let \(\Pi_2(x)\) denote the number of semiprimes \(\le x\).

Asymptotic distribution

Classical results on k-almost-primes (Landau, de Bruijn, Sathe–Selberg) give, for k=2:

\[\Pi_2(x) \sim \frac{x\log\log x}{\log x}\quad (x\to\infty).\]

More precisely there are constants and lower-order terms; the rough intuition is that semiprimes are rarer than primes by a factor \(\approx \log x/\log\log x\).

Dirichlet-convolution viewpoint

Let the indicator of primes be \(1_{\mathbb{P}}(n)\). The indicator of semiprimes (with order disregarded) can be written as a convolution-like sum over prime pairs:

\[1_{\mathrm{semi}}(n)=\sum_{p\,q\;:\;pq=n}1,\]

so

\[\Pi_2(x)=\sum_{p\le x}\#\{q:\;q\text{ prime},\;q\le x/p\;\text{and}\;pq\le x\}.\]

Algorithmic counting (practical formulas)

Two common approaches in code:

1) Sieve-based smallest-prime-factor (spf) table up to x. For each n, compute the total number of prime factors (with multiplicity) by repeated division using spf. Count those with exactly two factors. Complexity: O(x log log x) memory/time trade-offs; linear variants exist.

2) Use primes up to x and for each prime p, add contribution of primes q with p\le q\le x/p (avoiding double-counting). This uses a prime list and repeated evaluations of \(\pi(\cdot)\) (which can be approximated or computed by segmented sieve). Complexity: roughly O(\pi(x) + x/log x) with good prime enumeration.

Example high-level pseudocode (sieve spf approach):

- Build spf[2..x] using modified sieve — for each prime p mark multiples if not already marked.
- For n in [2..x]:
  - Let t = n, count = 0
  - While t > 1: count += 1; t = t / spf[t]
  - If count == 2: increment semiprime counter

This is fast and simple for typical contest/library sizes (e.g., x up to 10^7..10^8 depending on memory/time available).

Complexity notes

- Time: building spf is O(x log log x) (sieve cost). Counting factors per number is proportional to number of prime factors — on average small. Overall practical time is close to O(x). Memory: O(x) for spf array.

References and further reading

- Landau, "Handbuch der Lehre von der Verteilung der Primzahlen" (classical results on k-almost-primes)
- Sathe–Selberg theorem and de Bruijn's estimates for k-almost-primes
- Standard algorithm references: competitive programming tutorials on semiprimes and smallest-prime-factor sieve

Notes

- For exact mathematical constants and sharper error terms consult analytic number theory texts. This note focuses on practical, implementable formulas for code accompaniment.