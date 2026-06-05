---
chunk_id: "book-ca4fca8dd8-chunk-1441"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1441
confidence: "first-pass"
extraction_method: "structured-local"
---

870
Chapter 23
Reinforcement Learning
• Apprenticeship learning through observation of expert behavior can be an effective
solution when a correct reward function is hard to specify. Imitation learning formu-
lates the problem as supervised learning of a policy from the expert’s state–action pairs.
Inverse reinforcement learning infers reward information from the expert’s behavior.
Reinforcement learning continues to be one of the most active areas of machine learning re-
search. It frees us from manual construction of behaviors and from labeling the vast data sets
required for supervised learning, or having to hand-code control strategies. Applications in
robotics promise to be particularly valuable; these will require methods for handling continu-
ous, high-dimensional, partially observable environments in which successful behaviors may
consist of thousands or even millions of primitive actions.
We have presented a variety of approaches to reinforcement learning because there is
(at least so far) no single best approach. The question of model-based versus model-free
methods is, at its heart, a question about the best way to represent the agent function. This
is an issue at the foundations of artiﬁcial intelligence. As we stated in Chapter 1, one of
the key historical characteristics of much AI research is its (often unstated) adherence to the
knowledge-based approach. This amounts to an assumption that the best way to represent
the agent function is to build a representation of some aspects of the environment in which
the agent is situated. Some argue that with access to sufﬁcient data, model-free methods
can succeed in any domain. Perhaps this is true in theory, but of course, the universe may
not contain enough data to make it true in practice. (For example, it is not easy to imagine
how a model-free approach would enable one to design and build, say, the LIGO gravity-
wave detector.) Our intuition, for what it’s worth, is that as the environment becomes more
complex, the advantages of a model-based approach become more apparent.
Bibliographical and Historical Notes
It seems likely that the key idea of reinforcement learning—that animals do more of what
they are rewarded for and less of what they are punished for—played a signiﬁcant role in
the domestication of dogs at least 15,000 years ago. The early foundations of our scientiﬁc
understanding of reinforcement learning include the work of the Russian physiologist Ivan
Pavlov, who won the Nobel Prize in 1904, and that of the American psychologist Edward
Thorndike—particularly his book Animal Intelligence (1911). Hilgard and Bower (1975)
provide a good survey.
Alan Turing (1948, 1950) proposed reinforcement learning as an approach for teaching
computers; he considered it a partial solution, writing, “The use of punishments and rewards
can at best be a part of the teaching process.” Arthur Samuel’s checkers program (1959,
1967) was the ﬁrst successful use of machine learning of any kind. Samuel suggested most
of the modern ideas in reinforcement learning, including temporal-difference learning and
function approximation. He experimented with multilayer representations of value functions,
similar to today’s deep RL. In the end, he found that a simple linear evaluation function over
handcrafted features worked best. This may have been a consequence of working with a
computer roughly 100 billion times less powerful than a modern tensor processing unit.
Around the same time, researchers in adaptive control theory (Widrow and Hoff, 1960),
building on work by Hebb (1949), were training simple networks using the delta rule. Thus,
