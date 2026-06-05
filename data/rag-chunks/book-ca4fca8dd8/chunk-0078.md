---
chunk_id: "book-ca4fca8dd8-chunk-0078"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 78
confidence: "first-pass"
extraction_method: "structured-local"
---

48
Chapter 1
Introduction
Game playing: When Deep Blue defeated world chess champion Garry Kasparov in
1997, defenders of human supremacy placed their hopes on Go. Piet Hut, an astrophysicist
and Go enthusiast, predicted that it would take “a hundred years before a computer beats
humans at Go—maybe even longer.” But just 20 years later, ALPHAGO surpassed all human
players (Silver et al., 2017). Ke Jie, the world champion, said, “Last year, it was still quite
human-like when it played. But this year, it became like a god of Go.” ALPHAGO beneﬁted
from studying hundreds of thousands of past games by human Go players, and from the
distilled knowledge of expert Go players that worked on the team.
A followup program, ALPHAZERO, used no input from humans (except for the rules
of the game), and was able to learn through self-play alone to defeat all opponents, human
and machine, at Go, chess, and shogi (Silver et al., 2018). Meanwhile, human champions
have been beaten by AI systems at games as diverse as Jeopardy! (Ferrucci et al., 2010),
poker (Bowling et al., 2015; Moravˇc´ık et al., 2017; Brown and Sandholm, 2019), and the
video games Dota 2 (Fernandez and Mahlmann, 2018), StarCraft II (Vinyals et al., 2019),
and Quake III (Jaderberg et al., 2019).
Image understanding: Not content with exceeding human accuracy on the challenging
ImageNet object recognition task, computer vision researchers have taken on the more dif-
ﬁcult problem of image captioning. Some impressive examples include “A person riding a
motorcycle on a dirt road,” “Two pizzas sitting on top of a stove top oven,” and “A group
of young people playing a game of frisbee” (Vinyals et al., 2017b). Current systems are far
from perfect, however: a “refrigerator ﬁlled with lots of food and drinks” turns out to be a
no-parking sign partially obscured by lots of small stickers.
Medicine: AI algorithms now equal or exceed expert doctors at diagnosing many condi-
tions, particularly when the diagnosis is based on images. Examples include Alzheimer’s dis-
ease (Ding et al., 2018), metastatic cancer (Liu et al., 2017; Esteva et al., 2017), ophthalmic
disease (Gulshan et al., 2016), and skin diseases (Liu et al., 2019c). A systematic review and
meta-analysis (Liu et al., 2019a) found that the performance of AI programs, on average, was
equivalent to health care professionals. One current emphasis in medical AI is in facilitating
human–machine partnerships. For example, the LYNA system achieves 99.6% overall accu-
racy in diagnosing metastatic breast cancer—better than an unaided human expert—but the
combination does better still (Liu et al., 2018; Steiner et al., 2018).
The widespread adoption of these techniques is now limited not by diagnostic accuracy
but by the need to demonstrate improvement in clinical outcomes and to ensure transparency,
lack of bias, and data privacy (Topol, 2019). In 2017, only two medical AI applications were
approved by the FDA, but that increased to 12 in 2018, and continues to rise.
Climate science: A team of scientists won the 2018 Gordon Bell Prize for a deep learning
model that discovers detailed information about extreme weather events that were previously
buried in climate data. They used a supercomputer with specialized GPU hardware to exceed
the exaop level (1018 operations per second), the ﬁrst machine learning program to do so
(Kurth et al., 2018). Rolnick et al. (2019) present a 60-page catalog of ways in which machine
learning can be used to tackle climate change.
These are just a few examples of artiﬁcial intelligence systems that exist today. Not
magic or science ﬁction—but rather science, engineering, and mathematics, to which this
book provides an introduction.
