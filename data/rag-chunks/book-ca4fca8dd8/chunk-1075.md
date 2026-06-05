---
chunk_id: "book-ca4fca8dd8-chunk-1075"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1075
confidence: "first-pass"
extraction_method: "structured-local"
---

644
Chapter 18
Probabilistic Programming
two customers and two books, the Bayes net looks like the one in Figure 18.2(b). For larger
numbers of books and customers, it is quite impractical to specify a Bayes net by hand.
Fortunately, the network has a lot of repeated structure. Each Recommendation(c,b) vari-
able has as its parents the variables Honest(c), Kindness(c), and Quality(b). Moreover, the
conditional probability tables (CPTs) for all the Recommendation(c,b) variables are identi-
cal, as are those for all the Honest(c) variables, and so on. The situation seems tailor-made
for a ﬁrst-order language. We would like to say something like
Recommendation(c,b) ∼RecCPT(Honest(c),Kindness(c),Quality(b))
which means that a customer’s recommendation for a book depends probabilistically on the
customer’s honesty and kindness and the book’s quality according to a ﬁxed CPT.
Like ﬁrst-order logic, RPMs have constant, function, and predicate symbols. We will also
assume a type signature for each function—that is, a speciﬁcation of the type of each argu-
Type signature
ment and the function’s value. (If the type of each object is known, many spurious possible
worlds are eliminated by this mechanism; for example, we need not worry about the kindness
of each book, books recommending customers, and so on.) For the book-recommendation
domain, the types are Customer and Book, and the type signatures for the functions and pred-
icates are as follows:
Honest : Customer →{true,false}
Kindness : Customer →{1,2,3,4,5}
Quality : Book →{1,2,3,4,5}
Recommendation : Customer×Book →{1,2,3,4,5}
The constant symbols will be whatever customer and book names appear in the retailer’s data
set. In the example given in Figure 18.2(b), these were C1, C2 and B1, B2.
Given the constants and their types, together with the functions and their type signatures,
the basic random variables of the RPM are obtained by instantiating each function with
Basic random
variable
each possible combination of objects. For the book recommendation model, the basic random
variables include Honest(C1), Quality(B2), Recommendation(C1,B2), and so on. These are
exactly the variables appearing in Figure 18.2(b). Because each type has only ﬁnitely many
instances (thanks to the domain closure assumption), the number of basic random variables
is also ﬁnite.
To complete the RPM, we have to write the dependencies that govern these random vari-
ables. There is one dependency statement for each function, where each argument of the
function is a logical variable (i.e., a variable that ranges over objects, as in ﬁrst-order logic).
For example, the following dependency states that, for every customer c, the prior probability
of honesty is 0.99 true and 0.01 false:
Honest(c) ∼⟨0.99,0.01⟩
Similarly, we can state prior probabilities for the kindness value of each customer and the
quality of each book, each on the 1–5 scale:
Kindness(c) ∼⟨0.1,0.1,0.2,0.3,0.3⟩
Quality(b) ∼⟨0.05,0.2,0.4,0.2,0.15⟩
Finally, we need the dependency for recommendations: for any customer c and book b, the
score depends on the honesty and kindness of the customer and the quality of the book:
Recommendation(c,b) ∼RecCPT(Honest(c),Kindness(c),Quality(b))
