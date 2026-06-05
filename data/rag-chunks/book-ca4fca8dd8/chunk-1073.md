---
chunk_id: "book-ca4fca8dd8-chunk-1073"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1073
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 18.1
Relational Probability Models
643
Recommendation(C1, B1)
Honest(C1)
Kindness(C1)
Quality(B1)
Recommendation(C1, B1)
Honest(C1)
Kindness(C1)
Quality(B1)
Recommendation(C2, B1)
Honest(C2)
Kindness(C2)
Quality(B2)
Recommendation(C1, B2)
Recommendation(C2, B2)
(a)
(b)
Figure 18.2 (a) Bayes net for a single customer C1 recommending a single book B1.
Honest(C1) is Boolean, while the other variables have integer values from 1 to 5. (b) Bayes
net with two customers and two books.
In this section, we avoid this issue by considering the database semantics deﬁned in
Section 8.2.8 (page 282). The database semantics makes the unique names assumption—
here, we adopt it for the constant symbols. It also assumes domain closure—there are no
more objects beyond those that are named. We can then guarantee a ﬁnite set of possible
worlds by making the set of objects in each world be exactly the set of constant symbols that
are used; as shown in Figure 18.1 (bottom), there is no uncertainty about the mapping from
symbols to objects or about the objects that exist.
We will call models deﬁned in this way relational probability models, or RPMs.1 The
Relational
probability model
most signiﬁcant difference between the semantics of RPMs and the database semantics intro-
duced in Section 8.2.8 is that RPMs do not make the closed-world assumption—in a proba-
bilistic reasoning system we can’t just assume that every unknown fact is false.
18.1.1 Syntax and semantics
Let us begin with a simple example: suppose that an online book retailer would like to pro-
vide overall evaluations of products based on recommendations received from its customers.
The evaluation will take the form of a posterior distribution over the quality of the book, given
the available evidence. The simplest solution is to base the evaluation on the average recom-
mendation, perhaps with a variance determined by the number of recommendations, but this
fails to take into account the fact that some customers are kinder than others and some are
less honest than others. Kind customers tend to give high recommendations even to fairly
mediocre books, while dishonest customers give very high or very low recommendations for
reasons other than quality—they might be paid to promote some publisher’s books.2
For a single customer C1 recommending a single book B1, the Bayes net might look like
the one shown in Figure 18.2(a). (Just as in Section 9.1, expressions with parentheses such
as Honest(C1) are just fancy symbols—in this case, fancy names for random variables.) With
1
The name relational probability model was given by Pfeffer (2000) to a slightly different representation, but
the underlying ideas are the same.
2
A game theorist would advise a dishonest customer to avoid detection by occasionally recommending a good
book from a competitor. See Chapter 17.
