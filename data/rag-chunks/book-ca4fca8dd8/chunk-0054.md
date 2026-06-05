---
chunk_id: "book-ca4fca8dd8-chunk-0054"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 54
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 1.3
The History of Artiﬁcial Intelligence
35
processing. The problem of understanding language turned out to be considerably more
complex than it seemed in 1957. Understanding language requires an understanding of the
subject matter and context, not just an understanding of the structure of sentences. This might
seem obvious, but it was not widely appreciated until the 1960s. Much of the early work in
knowledge representation (the study of how to put knowledge into a form that a computer
can reason with) was tied to language and informed by research in linguistics, which was
connected in turn to decades of work on the philosophical analysis of language.
1.3 The History of Artiﬁcial Intelligence
One quick way to summarize the milestones in AI history is to list the Turing Award winners:
Marvin Minsky (1969) and John McCarthy (1971) for deﬁning the foundations of the ﬁeld
based on representation and reasoning; Allen Newell and Herbert Simon (1975) for symbolic
models of problem solving and human cognition; Ed Feigenbaum and Raj Reddy (1994) for
developing expert systems that encode human knowledge to solve real-world problems; Judea
Pearl (2011) for developing probabilistic reasoning techniques that deal with uncertainty in
a principled manner; and ﬁnally Yoshua Bengio, Geoffrey Hinton, and Yann LeCun (2019)
for making “deep learning” (multilayer neural networks) a critical part of modern computing.
The rest of this section goes into more detail on each phase of AI history.
1.3.1 The inception of artiﬁcial intelligence (1943–1956)
The ﬁrst work that is now generally recognized as AI was done by Warren McCulloch and
Walter Pitts (1943). Inspired by the mathematical modeling work of Pitts’s advisor Nicolas
Rashevsky (1936, 1938), they drew on three sources: knowledge of the basic physiology
and function of neurons in the brain; a formal analysis of propositional logic due to Russell
and Whitehead; and Turing’s theory of computation. They proposed a model of artiﬁcial
neurons in which each neuron is characterized as being “on” or “off,” with a switch to “on”
occurring in response to stimulation by a sufﬁcient number of neighboring neurons. The
state of a neuron was conceived of as “factually equivalent to a proposition which proposed
its adequate stimulus.” They showed, for example, that any computable function could be
computed by some network of connected neurons, and that all the logical connectives (AND,
OR, NOT, etc.) could be implemented by simple network structures. McCulloch and Pitts also
suggested that suitably deﬁned networks could learn. Donald Hebb (1949) demonstrated a
simple updating rule for modifying the connection strengths between neurons. His rule, now
called Hebbian learning, remains an inﬂuential model to this day.
Hebbian learning
Two undergraduate students at Harvard, Marvin Minsky (1927–2016) and Dean Ed-
monds, built the ﬁrst neural network computer in 1950. The SNARC, as it was called, used
3000 vacuum tubes and a surplus automatic pilot mechanism from a B-24 bomber to simulate
a network of 40 neurons. Later, at Princeton, Minsky studied universal computation in neural
networks. His Ph.D. committee was skeptical about whether this kind of work should be con-
sidered mathematics, but von Neumann reportedly said, “If it isn’t now, it will be someday.”
There were a number of other examples of early work that can be characterized as AI,
including two checkers-playing programs developed independently in 1952 by Christopher
Strachey at the University of Manchester and by Arthur Samuel at IBM. However, Alan Tur-
ing’s vision was the most inﬂuential. He gave lectures on the topic as early as 1947 at the
London Mathematical Society and articulated a persuasive agenda in his 1950 article “Com-
