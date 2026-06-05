---
chunk_id: "book-ca4fca8dd8-chunk-0038"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 38
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 1.2
The Foundations of Artiﬁcial Intelligence
27
don census data in 1662. Ronald Fisher is considered the ﬁrst modern statistician (Fisher,
1922). He brought together the ideas of probability, experiment design, analysis of data, and
computing—in 1919, he insisted that he couldn’t do his work without a mechanical calculator
called the MILLIONAIRE (the ﬁrst calculator that could do multiplication), even though the
cost of the calculator was more than his annual salary (Ross, 2012).
The history of computation is as old as the history of numbers, but the ﬁrst nontrivial
algorithm is thought to be Euclid’s algorithm for computing greatest common divisors. The
Algorithm
word algorithm comes from Muhammad ibn Musa al-Khwarizmi, a 9th century mathemati-
cian, whose writings also introduced Arabic numerals and algebra to Europe. Boole and
others discussed algorithms for logical deduction, and, by the late 19th century, efforts were
under way to formalize general mathematical reasoning as logical deduction.
Kurt G¨odel (1906–1978) showed that there exists an effective procedure to prove any true
statement in the ﬁrst-order logic of Frege and Russell, but that ﬁrst-order logic could not cap-
ture the principle of mathematical induction needed to characterize the natural numbers. In
1931, G¨odel showed that limits on deduction do exist. His incompleteness theorem showed
Incompleteness
theorem
that in any formal theory as strong as Peano arithmetic (the elementary theory of natural
numbers), there are necessarily true statements that have no proof within the theory.
This fundamental result can also be interpreted as showing that some functions on the
integers cannot be represented by an algorithm—that is, they cannot be computed. This
motivated Alan Turing (1912–1954) to try to characterize exactly which functions are com-
putable—capable of being computed by an effective procedure. The Church–Turing thesis
Computability
proposes to identify the general notion of computability with functions computed by a Turing
machine (Turing, 1936). Turing also showed that there were some functions that no Turing
machine can compute. For example, no machine can tell in general whether a given program
will return an answer on a given input or run forever.
Although computability is important to an understanding of computation, the notion of
tractability has had an even greater impact on AI. Roughly speaking, a problem is called
Tractability
intractable if the time required to solve instances of the problem grows exponentially with
the size of the instances. The distinction between polynomial and exponential growth in
complexity was ﬁrst emphasized in the mid-1960s (Cobham, 1964; Edmonds, 1965). It is
important because exponential growth means that even moderately large instances cannot be
solved in any reasonable time.
The theory of NP-completeness, pioneered by Cook (1971) and Karp (1972), provides a
NP-completeness
basis for analyzing the tractability of problems: any problem class to which the class of NP-
complete problems can be reduced is likely to be intractable. (Although it has not been proved
that NP-complete problems are necessarily intractable, most theoreticians believe it.) These
results contrast with the optimism with which the popular press greeted the ﬁrst computers—
“Electronic Super-Brains” that were “Faster than Einstein!” Despite the increasing speed of
computers, careful use of resources and necessary imperfection will characterize intelligent
systems. Put crudely, the world is an extremely large problem instance!
1.2.3 Economics
• How should we make decisions in accordance with our preferences?
• How should we do this when others may not go along?
• How should we do this when the payoff may be far in the future?
