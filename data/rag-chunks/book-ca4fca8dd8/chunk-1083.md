---
chunk_id: "book-ca4fca8dd8-chunk-1083"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1083
confidence: "first-pass"
extraction_method: "structured-local"
---

648
Chapter 18
Probabilistic Programming
will be identical; effective caching schemes have yielded speedups of three orders of magni-
tude for large networks.
Third, MCMC inference algorithms have some interesting properties when applied to
RPMs with relational uncertainty. MCMC works by sampling complete possible worlds,
so in each state the relational structure is completely known. In the example given earlier,
each MCMC state would specify the value of Author(B2), and so the other potential authors
are no longer parents of the recommendation nodes for B2. For MCMC, then, relational
uncertainty causes no increase in network complexity; instead, the MCMC process includes
transitions that change the relational structure, and hence the dependency structure, of the
unrolled network.
Finally, it may be possible in some cases to avoid grounding the model altogether. Reso-
lution theorem provers and logic programming systems avoid propositionalizing by instanti-
ating the logical variables only as needed to make the inference go through; that is, they lift
the inference process above the level of ground propositional sentences and make each lifted
step do the work of many ground steps.
The same idea can be applied in probabilistic inference. For example, in the variable
elimination algorithm, a lifted factor can represent an entire set of ground factors that assign
probabilities to random variables in the RPM, where those random variables differ only in the
constant symbols used to construct them. The details of this method are beyond the scope of
this book, but references are given at the end of the chapter.
18.2 Open-Universe Probability Models
We argued earlier that database semantics was appropriate for situations in which we know
exactly the set of relevant objects that exist and can identify them unambiguously. (In partic-
ular, all observations about an object are correctly associated with the constant symbol that
names it.) In many real-world settings, however, these assumptions are simply untenable.
For example, a book retailer might use an ISBN (International Standard Book Number) as a
constant symbol to name each book, even though a given “logical” book (e.g., “Gone With
the Wind”) may have several ISBNs corresponding to hardcover, paperback, large print, reis-
sues, and so on. It would make sense to aggregate recommendations across multiple ISBNs,
but the retailer may not know for sure which ISBNs are really the same book. (Note that we
are not reifying the individual copies of the book, which might be necessary for used-book
sales, car sales, and so on.) Worse still, each customer is identiﬁed by a login ID, but a dis-
honest customer may have thousands of IDs! In the computer security ﬁeld, these multiple
IDs are called sybils and their use to confound a reputation system is called a sybil attack.5
Sybil
Sybil attack
Thus, even a simple application in a relatively well-deﬁned, online domain involves both ex-
istence uncertainty (what are the real books and customers underlying the observed data)
Existence
uncertainty
and identity uncertainty (which logical terms really refer to the same object).
Identity uncertainty
The phenomena of existence and identity uncertainty extend far beyond online book-
sellers. In fact they are pervasive:
• A vision system doesn’t know what exists, if anything, around the next corner, and may
not know if the object it sees now is the same one it saw a few minutes ago.
5
The name “Sybil” comes from a famous case of multiple personality disorder.
