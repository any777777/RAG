---
chunk_id: "book-ca4fca8dd8-chunk-0528"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 528
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 9.5
Resolution
323
G¨odel’s Incompleteness Theorem
By slightly extending the language of ﬁrst-order logic to allow for the mathemat-
ical induction schema in arithmetic, Kurt G¨odel was able to show, in his incom-
pleteness theorem, that there are true arithmetic sentences that cannot be proved.
The proof of the incompleteness theorem is somewhat beyond the scope of
this book, occupying, as it does, at least 30 pages, but we can give a hint here. We
begin with the logical theory of numbers. In this theory, there is a single constant,
0, and a single function, S (the successor function). In the intended model, S(0)
denotes 1, S(S(0)) denotes 2, and so on; the language therefore has names for all
the natural numbers. The vocabulary also includes the function symbols +, ×, and
Expt (exponentiation) and the usual set of logical connectives and quantiﬁers.
The ﬁrst step is to notice that the set of sentences that we can write in this lan-
guage can be enumerated. (Imagine deﬁning an alphabetical order on the symbols
and then arranging, in alphabetical order, each of the sets of sentences of length 1,
2, and so on.) We can then number each sentence α with a unique natural number
#α (the G¨odel number). This is crucial: number theory contains a name for each
of its own sentences. Similarly, we can number each possible proof P with a G¨odel
number G(P), because a proof is simply a ﬁnite sequence of sentences.
Now suppose we have a recursively enumerable set A of sentences that are true
statements about the natural numbers. Recalling that A can be named by a given
set of integers, we can imagine writing in our language a sentence α(j,A) of the
following sort:
∀i i is not the G¨odel number of a proof of the sentence whose G¨odel
number is j, where the proof uses only premises in A.
Then let σ be the sentence α(#σ,A), that is, a sentence that states its own unprov-
ability from A. (That this sentence always exists is true but not entirely obvious.)
Now we make the following ingenious argument: Suppose that σ is provable
from A; then σ is false (because σ says it cannot be proved). But then we have a
false sentence that is provable from A, so A cannot consist of only true sentences—
a violation of our premise. Therefore, σ is not provable from A. But this is exactly
what σ itself claims; hence σ is a true sentence.
So, we have shown (barring 291
2 pages) that for any set of true sentences of
number theory, and in particular any set of basic axioms, there are other true sen-
tences that cannot be proved from those axioms. This establishes, among other
things, that we can never prove all the theorems of mathematics within any given
system of axioms. Clearly, this was an important discovery for mathematics. Its
signiﬁcance for AI has been widely debated, beginning with speculations by G¨odel
himself. We take up the debate in Chapter 28.
