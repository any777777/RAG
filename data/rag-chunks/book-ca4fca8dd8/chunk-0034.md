---
chunk_id: "book-ca4fca8dd8-chunk-0034"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 34
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 1.2
The Foundations of Artiﬁcial Intelligence
25
Building on the work of Ludwig Wittgenstein (1889–1951) and Bertrand Russell (1872–
1970), the famous Vienna Circle (Sigmund, 2017), a group of philosophers and mathemati-
cians meeting in Vienna in the 1920s and 1930s, developed the doctrine of logical positivism.
Logical positivism
This doctrine holds that all knowledge can be characterized by logical theories connected, ul-
timately, to observation sentences that correspond to sensory inputs; thus logical positivism
Observation
sentence
combines rationalism and empiricism.
The conﬁrmation theory of Rudolf Carnap (1891–1970) and Carl Hempel (1905–1997)
Conﬁrmation theory
attempted to analyze the acquisition of knowledge from experience by quantifying the degree
of belief that should be assigned to logical sentences based on their connection to observations
that conﬁrm or disconﬁrm them. Carnap’s book The Logical Structure of the World (1928)
was perhaps the ﬁrst theory of mind as a computational process.
The ﬁnal element in the philosophical picture of the mind is the connection between
knowledge and action. This question is vital to AI because intelligence requires action as well
as reasoning. Moreover, only by understanding how actions are justiﬁed can we understand
how to build an agent whose actions are justiﬁable (or rational).
Aristotle argued (in De Motu Animalium) that actions are justiﬁed by a logical connection
between goals and knowledge of the action’s outcome:
But how does it happen that thinking is sometimes accompanied by action and sometimes
not, sometimes by motion, and sometimes not? It looks as if almost the same thing
happens as in the case of reasoning and making inferences about unchanging objects. But
in that case the end is a speculative proposition ... whereas here the conclusion which
results from the two premises is an action. ... I need covering; a cloak is a covering. I
need a cloak. What I need, I have to make; I need a cloak. I have to make a cloak. And
the conclusion, the “I have to make a cloak,” is an action.
In the Nicomachean Ethics (Book III. 3, 1112b), Aristotle further elaborates on this topic,
suggesting an algorithm:
We deliberate not about ends, but about means. For a doctor does not deliberate whether
he shall heal, nor an orator whether he shall persuade, ... They assume the end and con-
sider how and by what means it is attained, and if it seems easily and best produced
thereby; while if it is achieved by one means only they consider how it will be achieved
by this and by what means this will be achieved, till they come to the ﬁrst cause, ... and
what is last in the order of analysis seems to be ﬁrst in the order of becoming. And if we
come on an impossibility, we give up the search, e.g., if we need money and this cannot
be got; but if a thing appears possible we try to do it.
Aristotle’s algorithm was implemented 2300 years later by Newell and Simon in their Gen-
eral Problem Solver program. We would now call it a greedy regression planning system
(see Chapter 11). Methods based on logical planning to achieve deﬁnite goals dominated the
ﬁrst few decades of theoretical research in AI.
Thinking purely in terms of actions achieving goals is often useful but sometimes inap-
plicable. For example, if there are several different ways to achieve a goal, there needs to be
some way to choose among them. More importantly, it may not be possible to achieve a goal
with certainty, but some action must still be taken. How then should one decide? Antoine Ar-
nauld (1662), analyzing the notion of rational decisions in gambling, proposed a quantitative
formula for maximizing the expected monetary value of the outcome. Later, Daniel Bernoulli
(1738) introduced the more general notion of utility to capture the internal, subjective value
Utility
