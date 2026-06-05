---
chunk_id: "book-ca4fca8dd8-chunk-0371"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 371
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.1
Knowledge-Based Agents
227
function KB-AGENT(percept) returns an action
persistent: KB, a knowledge base
t, a counter, initially 0, indicating time
TELL(KB, MAKE-PERCEPT-SENTENCE(percept,t))
action←ASK(KB, MAKE-ACTION-QUERY(t))
TELL(KB, MAKE-ACTION-SENTENCE(action,t))
t←t + 1
return action
Figure 7.1 A generic knowledge-based agent. Given a percept, the agent adds the percept
to its knowledge base, asks the knowledge base for the best action, and tells the knowledge
base that it has in fact taken that action.
of logic. It also comes with well-developed inference technologies, which we describe in
sections 7.5 and 7.6. Finally, Section 7.7 combines the concept of knowledge-based agents
with the technology of propositional logic to build some simple agents for the wumpus world.
7.1 Knowledge-Based Agents
The central component of a knowledge-based agent is its knowledge base, or KB. A knowl-
Knowledge base
edge base is a set of sentences. (Here “sentence” is used as a technical term. It is related
Sentence
but not identical to the sentences of English and other natural languages.) Each sentence is
expressed in a language called a knowledge representation language and represents some
Knowledge
representation
language
assertion about the world. When the sentence is taken as being given without being derived
from other sentences, we call it an axiom.
Axiom
There must be a way to add new sentences to the knowledge base and a way to query
what is known. The standard names for these operations are TELL and ASK, respectively.
Both operations may involve inference—that is, deriving new sentences from old. Inference
Inference
must obey the requirement that when one ASKs a question of the knowledge base, the answer
should follow from what has been told (or TELLed) to the knowledge base previously. Later
in this chapter, we will be more precise about the crucial word “follow.” For now, take it to
mean that the inference process should not make things up as it goes along.
Figure 7.1 shows the outline of a knowledge-based agent program. Like all our agents,
it takes a percept as input and returns an action. The agent maintains a knowledge base, KB,
which may initially contain some background knowledge.
Background
knowledge
Each time the agent program is called, it does three things. First, it TELLs the knowledge
base what it perceives. Second, it ASKs the knowledge base what action it should perform. In
the process of answering this query, extensive reasoning may be done about the current state
of the world, about the outcomes of possible action sequences, and so on. Third, the agent
program TELLs the knowledge base which action was chosen, and returns the action so that
it can be executed.
The details of the representation language are hidden inside three functions that imple-
ment the interface between the sensors and actuators on one side and the core representation
and reasoning system on the other. MAKE-PERCEPT-SENTENCE constructs a sentence as-
