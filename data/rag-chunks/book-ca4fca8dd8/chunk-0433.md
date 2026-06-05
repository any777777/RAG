---
chunk_id: "book-ca4fca8dd8-chunk-0433"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 433
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
265
• The set of possible models, given a ﬁxed propositional vocabulary, is ﬁnite, so en-
tailment can be checked by enumerating models. Efﬁcient model-checking inference
algorithms for propositional logic include backtracking and local search methods and
can often solve large problems quickly.
• Inference rules are patterns of sound inference that can be used to ﬁnd proofs. The
resolution rule yields a complete inference algorithm for knowledge bases that are
expressed in conjunctive normal form. Forward chaining and backward chaining
are very natural reasoning algorithms for knowledge bases in Horn form.
• Local search methods such as WALKSAT can be used to ﬁnd solutions. Such algo-
rithms are sound but not complete.
• Logical state estimation involves maintaining a logical sentence that describes the set
of possible states consistent with the observation history. Each update step requires
inference using the transition model of the environment, which is built from successor-
state axioms that specify how each ﬂuent changes.
• Decisions within a logical agent can be made by SAT solving: ﬁnding possible models
specifying future action sequences that reach the goal. This approach works only for
fully observable or sensorless environments.
• Propositional logic does not scale to environments of unbounded size because it lacks
the expressive power to deal concisely with time, space, and universal patterns of rela-
tionships among objects.
Bibliographical and Historical Notes
John McCarthy’s paper “Programs with Common Sense” (McCarthy, 1958, 1968) promul-
gated the notion of agents that use logical reasoning to mediate between percepts and actions.
It also raised the ﬂag of declarativism, pointing out that telling an agent what it needs to know
is an elegant way to build software. Allen Newell’s (1982) article “The Knowledge Level”
makes the case that rational agents can be described and analyzed at an abstract level deﬁned
by the knowledge they possess rather than the programs they run.
Logic itself had its origins in ancient Greek philosophy and mathematics. Plato discussed
the syntactic structure of sentences, their truth and falsity, their meaning, and the validity of
logical arguments. The ﬁrst known systematic study of logic was Aristotle’s Organon. His
syllogisms were what we now call inference rules, although they lacked the compositionality
Syllogism
of our current rules.
The Megarian and Stoic schools began the systematic study of the basic logical connec-
tives in the ﬁfth century BCE. Truth tables are due to Philo of Megara. The Stoics took ﬁve
basic inference rules as valid without proof, including the rule we now call Modus Ponens.
They derived a number of other rules from these ﬁve, using, among other principles, the
deduction theorem (page 240) and were clearer about proof than was Aristotle (Mates, 1953).
The idea of reducing logical inference to a purely mechanical process is due to Wilhelm
Leibniz (1646–1716). George Boole (1847) introduced the ﬁrst comprehensive and work-
able system of formal logic in his book The Mathematical Analysis of Logic. Boole’s logic
was closely modeled on the ordinary algebra of real numbers and used substitution of logi-
cally equivalent expressions as its primary inference method. Although it didn’t handle all of
