---
chunk_id: "book-ca4fca8dd8-chunk-1768"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1768
confidence: "first-pass"
extraction_method: "structured-local"
---

Section A.1
Complexity Analysis and O() Notation
1075
The second problem is that algorithms tend to resist exact analysis. In that case, it is
necessary to fall back on an approximation. We say that the SUMMATION algorithm is O(n),
meaning that its measure is at most a constant times n, with the possible exception of a few
small values of n. More formally,
T(n) is O(f(n)) if T(n) ≤k f(n) for some k, for all n > n0 .
The O() notation gives us what is called an asymptotic analysis. We can say without ques-
Asymptotic analysis
tion that, as n asymptotically approaches inﬁnity, an O(n) algorithm is better than an O(n2)
algorithm. A single benchmark ﬁgure could not substantiate such a claim.
The O() notation abstracts over constant factors, which makes it easier to use, but less
precise, than the T() notation. For example, an O(n2) algorithm will always be worse than
an O(n) in the long run, but if the two algorithms are T(n2 +1) and T(100n+1000), then the
O(n2) algorithm is actually better for n < 110.
Despite this drawback, asymptotic analysis is the most widely used tool for analyzing
algorithms. It is precisely because the analysis abstracts over both the exact number of oper-
ations (by ignoring the constant factor k) and the exact content of the input (by considering
only its size n) that the analysis becomes mathematically feasible. The O() notation is a good
compromise between precision and ease of analysis.
A.1.2 NP and inherently hard problems
The analysis of algorithms and the O() notation allow us to talk about the efﬁciency of a
particular algorithm. However, they have nothing to say about whether there could be a better
algorithm for the problem at hand. The ﬁeld of complexity analysis analyzes problems rather
Complexity analysis
than algorithms. The ﬁrst gross division is between problems that can be solved in polynomial
time and problems that cannot be solved in polynomial time, no matter what algorithm is
used. The class of polynomial problems—those which can be solved in time O(nk) for some
k—is called P. These are sometimes called “easy” problems, because the class contains those
P
problems with running times like O(logn) and O(n). But it also contains those with time
O(n1000), so the name “easy” should not be taken too literally.
Another important class of problems is NP, the class of nondeterministic polynomial
NP
problems. A problem is in this class if there is some algorithm that can guess a solution and
then verify whether a guess is correct in polynomial time. The idea is that if you have an
arbitrarily large number of processors so that you can try all the guesses at once, or if you are
very lucky and always guess right the ﬁrst time, then the NP problems become P problems.
One of the biggest open questions in computer science is whether the class NP is equivalent
to the class P when one does not have the luxury of an inﬁnite number of processors or
omniscient guessing. Most computer scientists are convinced that P ̸= NP; that NP problems
are inherently hard and have no polynomial-time algorithms. But this has never been proven.
Those who are interested in deciding whether P = NP look at a subclass of NP called the
NP-complete problems. The word “complete” is used here in the sense of “most extreme”
NP-complete
and thus refers to the hardest problems in the class NP. It has been proven that either all
the NP-complete problems are in P or none of them is. This makes the class theoretically
interesting, but the class is also of practical interest because many important problems are
known to be NP-complete. An example is the satisﬁability problem: given a sentence of
propositional logic, is there an assignment of truth values to the proposition symbols of the
sentence that makes it true? Unless a miracle occurs and P = NP, there can be no algorithm
