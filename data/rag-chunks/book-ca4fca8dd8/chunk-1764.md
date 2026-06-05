---
chunk_id: "book-ca4fca8dd8-chunk-1764"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1764
confidence: "first-pass"
extraction_method: "structured-local"
---

1072
Chapter 29
The Future of AI
A human being should be able to change a diaper, plan an invasion, butcher a hog,
conn a ship, design a building, write a sonnet, balance accounts, build a wall, set
a bone, comfort the dying, take orders, give orders, cooperate, act alone, solve
equations, analyse a new problem, pitch manure, program a computer, cook a
tasty meal, ﬁght efﬁciently, die gallantly. Specialization is for insects.
So far, no AI system measures up to either of these lists, and some proponents of general or
human-level AI (HLAI) insist that continued work on speciﬁc tasks (or on individual com-
ponents) will not be enough to reach mastery on a wide variety of tasks; that we will need a
fundamentally new approach. It seems to us that numerous new breakthroughs will indeed be
necessary, but overall, AI as a ﬁeld has made a reasonable exploration/exploitation tradeoff,
assembling a portfolio of components, improving on particular tasks, while also exploring
promising and sometimes far-out new ideas.
It would have been a mistake to tell the Wright brothers in 1903 to stop work on their
single-task airplane and design an “artiﬁcial general ﬂight” machine that can take off verti-
cally, ﬂy faster than sound, carry hundreds of passengers, and land on the moon. It also would
have been a mistake to follow up their ﬁrst ﬂight with an annual competition to make spruce
wood biplanes incrementally better.
We have seen that work on components can spur new ideas; for example, generative
adversarial networks (GANs) and transformer language models each opened up new areas of
research. We have also seen steps towards “diversity of behaviour.” For example, machine
translation systems in the 1990s were built one at a time for each language pair (such as
French to English), but today a single system can identifying the input text as being one of a
hundred languages, and translate it into any of 100 target languages. Another natural language
system can perform ﬁve distinct tasks with one joint model (Hashimoto et al., 2016).
AI engineering
The ﬁeld of computer programming started with a few extraordinary pioneers. But it didn’t
reach the status of a major industry until a practice of software engineering was developed,
with a powerful collection of widely available tools, and a thriving ecosystem of teachers,
students, practitioners, entrepreneurs, investors, and customers.
The AI industry has not yet reached that level of maturity. We do have a variety of pow-
erful tools and frameworks, such as TensorFlow, Keras, PyTorch, CAFFE, Scikit-Learn and
SCIPY. But many of the most promising approaches, such as GANs and deep reinforcement
learning, have proven to be difﬁcult to work with—they require experience and a degree of
ﬁddling to get them to train properly in a new domain. We don’t have enough experts to do
this across all the domains where we need it, and we don’t yet have the tools and ecosystem
to let less-expert practitioners succeed.
Google’s Jeff Dean sees a future where we will want machine learning to handle millions
of tasks; it won’t be feasible to develop each of them from scratch, so he suggests that rather
than building each new system from scratch, we should start with a single huge system and,
for each new task, extract from it the parts that are relevant to the task. We have seen some
steps in this direction, such as the transformer language models (e.g., BERT, GPT-2) with
billions of parameters, and an “outrageously large” ensemble neural network architecture
that scales up to 68 billion parameters in one experiment (Shazeer et al., 2017). Much work
remains to be done.
