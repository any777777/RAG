---
chunk_id: "book-ca4fca8dd8-chunk-0062"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 62
confidence: "first-pass"
extraction_method: "structured-local"
---

40
Chapter 1
Introduction
decision by the British government to end support for AI research in all but two universities.
(Oral tradition paints a somewhat different and more colorful picture, with political ambitions
and personal animosities whose description is beside the point.)
A third difﬁculty arose because of some fundamental limitations on the basic structures
being used to generate intelligent behavior. For example, Minsky and Papert’s book Percep-
trons (1969) proved that, although perceptrons (a simple form of neural network) could be
shown to learn anything they were capable of representing, they could represent very little.
In particular, a two-input perceptron could not be trained to recognize when its two inputs
were different. Although their results did not apply to more complex, multilayer networks,
research funding for neural-net research soon dwindled to almost nothing. Ironically, the new
back-propagation learning algorithms that were to cause an enormous resurgence in neural-
net research in the late 1980s and again in the 2010s had already been developed in other
contexts in the early 1960s (Kelley, 1960; Bryson, 1962).
1.3.4 Expert systems (1969–1986)
The picture of problem solving that had arisen during the ﬁrst decade of AI research was of
a general-purpose search mechanism trying to string together elementary reasoning steps to
ﬁnd complete solutions. Such approaches have been called weak methods because, although
Weak method
general, they do not scale up to large or difﬁcult problem instances. The alternative to weak
methods is to use more powerful, domain-speciﬁc knowledge that allows larger reasoning
steps and can more easily handle typically occurring cases in narrow areas of expertise. One
might say that to solve a hard problem, you have to almost know the answer already.
The DENDRAL program (Buchanan et al., 1969) was an early example of this approach.
It was developed at Stanford, where Ed Feigenbaum (a former student of Herbert Simon),
Bruce Buchanan (a philosopher turned computer scientist), and Joshua Lederberg (a Nobel
laureate geneticist) teamed up to solve the problem of inferring molecular structure from the
information provided by a mass spectrometer. The input to the program consists of the ele-
mentary formula of the molecule (e.g., C6H13NO2) and the mass spectrum giving the masses
of the various fragments of the molecule generated when it is bombarded by an electron beam.
For example, the mass spectrum might contain a peak at m = 15, corresponding to the mass
of a methyl (CH3) fragment.
The naive version of the program generated all possible structures consistent with the
formula, and then predicted what mass spectrum would be observed for each, comparing this
with the actual spectrum. As one might expect, this is intractable for even moderate-sized
molecules. The DENDRAL researchers consulted analytical chemists and found that they
worked by looking for well-known patterns of peaks in the spectrum that suggested common
substructures in the molecule. For example, the following rule is used to recognize a ketone
(C=O) subgroup (which weighs 28):
if M is the mass of the whole molecule and there are two peaks at x1 and x2 such that
(a) x1 +x2 = M +28; (b) x1 −28 is a high peak; (c) x2 −28 is a high peak; and
(d) At least one of x1 and x2 is high
then there is a ketone subgroup.
Recognizing that the molecule contains a particular substructure reduces the number of pos-
sible candidates enormously. According to its authors, DENDRAL was powerful because it
embodied the relevant knowledge of mass spectroscopy not in the form of ﬁrst principles but
