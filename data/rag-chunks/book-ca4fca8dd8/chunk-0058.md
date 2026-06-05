---
chunk_id: "book-ca4fca8dd8-chunk-0058"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 58
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 1.3
The History of Artiﬁcial Intelligence
37
Newell and Simon followed up their success with LT with the General Problem Solver,
or GPS. Unlike LT, this program was designed from the start to imitate human problem-
solving protocols. Within the limited class of puzzles it could handle, it turned out that the
order in which the program considered subgoals and possible actions was similar to that in
which humans approached the same problems. Thus, GPS was probably the ﬁrst program to
embody the “thinking humanly” approach. The success of GPS and subsequent programs as
models of cognition led Newell and Simon (1976) to formulate the famous physical symbol
system hypothesis, which states that “a physical symbol system has the necessary and suf-
Physical symbol
system
ﬁcient means for general intelligent action.” What they meant is that any system (human or
machine) exhibiting intelligence must operate by manipulating data structures composed of
symbols. We will see later that this hypothesis has been challenged from many directions.
At IBM, Nathaniel Rochester and his colleagues produced some of the ﬁrst AI programs.
Herbert Gelernter (1959) constructed the Geometry Theorem Prover, which was able to prove
theorems that many students of mathematics would ﬁnd quite tricky. This work was a precur-
sor of modern mathematical theorem provers.
Of all the exploratory work done during this period, perhaps the most inﬂuential in the
long run was that of Arthur Samuel on checkers (draughts). Using methods that we now call
reinforcement learning (see Chapter 23), Samuel’s programs learned to play at a strong am-
ateur level. He thereby disproved the idea that computers can do only what they are told to:
his program quickly learned to play a better game than its creator. The program was demon-
strated on television in 1956, creating a strong impression. Like Turing, Samuel had trouble
ﬁnding computer time. Working at night, he used machines that were still on the testing ﬂoor
at IBM’s manufacturing plant. Samuel’s program was the precursor of later systems such
as TD-GAMMON (Tesauro, 1992), which was among the world’s best backgammon players,
and ALPHAGO (Silver et al., 2016), which shocked the world by defeating the human world
champion at Go (see Chapter 6).
In 1958, John McCarthy made two important contributions to AI. In MIT AI Lab Memo
No. 1, he deﬁned the high-level language Lisp, which was to become the dominant AI pro-
Lisp
gramming language for the next 30 years. In a paper entitled Programs with Common Sense,
he advanced a conceptual proposal for AI systems based on knowledge and reasoning. The
paper describes the Advice Taker, a hypothetical program that would embody general knowl-
edge of the world and could use it to derive plans of action. The concept was illustrated with
simple logical axioms that sufﬁce to generate a plan to drive to the airport. The program was
also designed to accept new axioms in the normal course of operation, thereby allowing it
to achieve competence in new areas without being reprogrammed. The Advice Taker thus
embodied the central principles of knowledge representation and reasoning: that it is useful
to have a formal, explicit representation of the world and its workings and to be able to ma-
nipulate that representation with deductive processes. The paper inﬂuenced the course of AI
and remains relevant today.
1958 also marked the year that Marvin Minsky moved to MIT. His initial collaboration
with McCarthy did not last, however. McCarthy stressed representation and reasoning in for-
mal logic, whereas Minsky was more interested in getting programs to work and eventually
developed an anti-logic outlook. In 1963, McCarthy started the AI lab at Stanford. His plan
to use logic to build the ultimate Advice Taker was advanced by J. A. Robinson’s discov-
ery in 1965 of the resolution method (a complete theorem-proving algorithm for ﬁrst-order
