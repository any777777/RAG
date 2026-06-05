---
chunk_id: "book-ca4fca8dd8-chunk-0892"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 892
confidence: "first-pass"
extraction_method: "structured-local"
---

540
Chapter 15
Making Simple Decisions
The expected value of information is nonnegative:
▶
∀j VPI(E j) ≥0.
The theorem follows directly from the deﬁnition of VPI, and we leave the proof as an exercise
(Exercise 15.NNVP). It is, of course, a theorem about expected value, not actual value. Ad-
ditional information can easily lead to a plan that turns out to be worse than the original plan
if the information happens to be misleading. For example, a medical test that gives a false
positive result may lead to unnecessary surgery; but that does not mean that the test shouldn’t
be done.
It is important to remember that VPI depends on the current state of information. It can
change as more information is acquired. For any given piece of evidence E j, the value of
acquiring it can go down (e.g., if another variable strongly constrains the posterior for E j) or
up (e.g., if another variable provides a clue on which E j builds, enabling a new and better
plan to be devised). Thus, VPI is not additive. That is,
VPI(E j,Ek) ̸= VPI(E j)+VPI(Ek)
(in general).
VPI is, however, order-independent. That is,
VPI(E j,Ek) = VPI(E j)+VPI(Ek|E j) = VPI(Ek)+VPI(Ej|Ek) = VPI(Ek,E j)
where the notation VPI(·|E) denotes the VPI calculated according to the posterior distribution
where E is already observed. Order independence distinguishes sensing actions from ordinary
actions and simpliﬁes the problem of calculating the value of a sequence of sensing actions.
We return to this question in the next section.
15.6.4 Implementation of an information-gathering agent
A sensible agent should ask questions in a reasonable order, should avoid asking questions
that are irrelevant, should take into account the importance of each piece of information in
relation to its cost, and should stop asking questions when that is appropriate. All of these
capabilities can be achieved by using the value of information as a guide.
Figure 15.9 shows the overall design of an agent that can gather information intelligently
before acting. For now, we assume that with each observable evidence variable E j, there is
an associated cost, C(E j), which reﬂects the cost of obtaining the evidence through tests,
consultants, questions, or whatever. The agent requests what appears to be the most efﬁcient
observation in terms of utility gain per unit cost. We assume that the result of the action
Request(E j) is that the next percept provides the value of E j. If no observation is worth its
cost, the agent selects a “real” action.
The agent algorithm we have described implements a form of information gathering that
is called myopic. This is because it uses the VPI formula shortsightedly, calculating the value
Myopic
of information as if only a single evidence variable will be acquired. Myopic control is based
on the same heuristic idea as greedy search and often works well in practice. (For example,
it has been shown to outperform expert physicians in selecting diagnostic tests.) However,
if there is no single evidence variable that will help a lot, a myopic agent might hastily take
an action when it would have been better to request two or more variables ﬁrst and then take
action. The next section considers the possibility of obtaining multiple observations.
