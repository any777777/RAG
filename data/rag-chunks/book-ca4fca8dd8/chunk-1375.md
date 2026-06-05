---
chunk_id: "book-ca4fca8dd8-chunk-1375"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1375
confidence: "first-pass"
extraction_method: "structured-local"
---

836
Chapter 22
Deep Learning
Bibliographical and Historical Notes
The literature on neural networks is vast. Cowan and Sharp (1988b, 1988a) survey the early
history, beginning with the work of McCulloch and Pitts (1943). (As mentioned in Chap-
ter 1, John McCarthy has pointed to the work of Nicolas Rashevsky (1936, 1938) as the
earliest mathematical model of neural learning.) Norbert Wiener, a pioneer of cybernetics
and control theory (Wiener, 1948), worked with McCulloch and Pitts and inﬂuenced a num-
ber of young researchers, including Marvin Minsky, who may have been the ﬁrst to develop
a working neural network in hardware, in 1951 (see Minsky and Papert, 1988, pp. ix–x).
Alan Turing (1948) wrote a research report titled Intelligent Machinery that begins with the
sentence “I propose to investigate the question as to whether it is possible for machinery to
show intelligent behaviour” and goes on to describe a recurrent neural network architecture
he called “B-type unorganized machines” and an approach to training them. Unfortunately,
the report went unpublished until 1969, and was all but ignored until recently.
The perceptron, a one-layer neural network with a hard-threshold activation function, was
popularized by Frank Rosenblatt (1957). After a demonstration in July 1958, the New York
Times described it as “the embryo of an electronic computer that [the Navy] expects will be
able to walk, talk, see, write, reproduce itself and be conscious of its existence.” Rosenblatt
(1960) later proved the perceptron convergence theorem, although it had been foreshadowed
by purely mathematical work outside the context of neural networks (Agmon, 1954; Motzkin
and Schoenberg, 1954). Some early work was also done on multilayer networks, including
Gamba perceptrons (Gamba et al., 1961) and madalines (Widrow, 1962). Learning Ma-
chines (Nilsson, 1965) covers much of this early work and more. The subsequent demise
of early perceptron research efforts was hastened (or, the authors later claimed, merely ex-
plained) by the book Perceptrons (Minsky and Papert, 1969), which lamented the ﬁeld’s lack
of mathematical rigor. The book pointed out that single-layer perceptrons could represent
only linearly separable concepts and noted the lack of effective learning algorithms for mul-
tilayer networks. These limitations were already well known (Hawkins, 1961) and had been
acknowledged by Rosenblatt himself (Rosenblatt, 1962).
The papers collected by Hinton and Anderson (1981), based on a conference in San
Diego in 1979, can be regarded as marking a renaissance of connectionism. The two-volume
“PDP” (Parallel Distributed Processing) anthology (Rumelhart and McClelland, 1986) helped
to spread the gospel, so to speak, particularly in the psychology and cognitive science com-
munities. The most important development of this period was the back-propagation algorithm
for training multilayer networks.
The back-propagation algorithm was discovered independently several times in different
contexts (Kelley, 1960; Bryson, 1962; Dreyfus, 1962; Bryson and Ho, 1969; Werbos, 1974;
Parker, 1985) and Stuart Dreyfus (1990) calls it the “Kelley–Bryson gradient procedure.”
Although Werbos had applied it to neural networks, this idea did not become widely known
until a paper by David Rumelhart, Geoff Hinton, and Ron Williams (1986) appeared in Nature
giving a nonmathematical presentation of the algorithm. Mathematical respectability was
enhanced by papers showing that multilayer feedforward networks are (subject to technical
conditions) universal function approximators (Cybenko, 1988, 1989). The late 1980s and
early 1990s saw a huge growth in neural network research: the number of papers mushroomed
by a factor of 200 between 1980–84 and 1990–94.
