---
chunk_id: "book-ca4fca8dd8-chunk-0677"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 677
confidence: "first-pass"
extraction_method: "structured-local"
---

406
Chapter 12
Quantifying Uncertainty
function DT-AGENT(percept) returns an action
persistent: belief state, probabilistic beliefs about the current state of the world
action, the agent’s action
update belief state based on action and percept
calculate outcome probabilities for actions,
given action descriptions and current belief state
select action with highest expected utility
given probabilities of outcomes and utility information
return action
Figure 12.1 A decision-theoretic agent that selects rational actions.
brieﬂy on optimal decisions in backgammon; it is in fact a completely general principle for
single-agent decision making.
Figure 12.1 sketches the structure of an agent that uses decision theory to select actions.
The agent is identical, at an abstract level, to the agents described in Chapters 4 and 7 that
maintain a belief state reﬂecting the history of percepts to date. The primary difference is
that the decision-theoretic agent’s belief state represents not just the possibilities for world
states but also their probabilities. Given the belief state and some knowledge of the effects of
actions, the agent can make probabilistic predictions of action outcomes and hence select the
action with the highest expected utility.
This chapter and the next concentrate on the task of representing and computing with
probabilistic information in general. Chapter 14 deals with methods for the speciﬁc tasks
of representing and updating the belief state over time and predicting outcomes. Chapter 18
looks at ways of combining probability theory with expressive formal languages such as ﬁrst-
order logic and general-purpose programming languages. Chapter 15 covers utility theory in
more depth, and Chapter 16 develops algorithms for planning sequences of actions in stochas-
tic environments. Chapter 17 covers the extension of these ideas to multiagent environments.
12.2 Basic Probability Notation
For our agent to represent and use probabilistic information, we need a formal language.
The language of probability theory has traditionally been informal, written by human mathe-
maticians for other human mathematicians. Appendix A includes a standard introduction to
elementary probability theory; here, we take an approach more suited to the needs of AI and
connect it with the concepts of formal logic.
12.2.1 What probabilities are about
Like logical assertions, probabilistic assertions are about possible worlds. Whereas logical
assertions say which possible worlds are strictly ruled out (all those in which the assertion is
false), probabilistic assertions talk about how probable the various worlds are. In probability
theory, the set of all possible worlds is called the sample space. The possible worlds are
Sample space
mutually exclusive and exhaustive—two possible worlds cannot both be the case, and one
