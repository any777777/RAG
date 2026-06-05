---
chunk_id: "book-ca4fca8dd8-chunk-0977"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 977
confidence: "first-pass"
extraction_method: "structured-local"
---

590
Chapter 17
Multiagent Decision Making
subplan constructed for each body may need to include explicit communicative actions with
other bodies. For example, multiple reconnaissance robots covering a wide area may often
be out of radio contact with each other and should share their ﬁndings during times when
communication is feasible.
17.1.2 Multiple decision makers
The second possibility is that the other actors in the environment are also decision makers:
they each have preferences and choose and execute their own plan. We call them counter-
parts. In this case, we can distinguish two further possibilities.
Counterparts
• The ﬁrst is that, although there are multiple decision makers, they are all pursuing a
common goal. This is roughly the situation of workers in a company, in which different
Common goal
decision makers are pursuing, one hopes, the same goals on behalf of the company. The
main problem faced by the decision makers in this setting is the coordination problem:
Coordination
problem
they need to ensure that they are all pulling in the same direction, and not accidentally
fouling up each other’s plans.
• The second possibility is that the decision makers each have their own personal pref-
erences, which they each will pursue to the best of their abilities. It could be that the
preferences are diametrically opposed, as is the case in zero-sum games such as chess
(see Chapter 6). But most multiagent encounters are more complicated than that, with
more complex preferences.
When there are multiple decision makers, each pursuing their own preferences, an agent must
take into account the preferences of other agents, as well as the fact that these other agents
are also taking into account the preferences of other agents, and so on. This brings us into the
realm of game theory: the theory of strategic decision making. It is this strategic aspect of
Game theory
reasoning—players each taking into account how other players may act—that distinguishes
game theory from decision theory. In the same way that decision theory provides the theoret-
ical foundation for decision making in single-agent AI, game theory provides the theoretical
foundation for decision making in multiagent systems.
The use of the word “game” here is also not ideal: a natural inference is that game the-
ory is mainly concerned with recreational pursuits, or artiﬁcial scenarios. Nothing could be
further from the truth. Game theory is the theory of strategic decision making. It is used
Strategic decision
making
in decision making situations including the auctioning of oil drilling rights and wireless fre-
quency spectrum rights, bankruptcy proceedings, product development and pricing decisions,
and national defense—situations involving billions of dollars and many lives. Game theory
in AI can be used in two main ways:
1. Agent design: Game theory can be used by an agent to analyze its possible decisions
Agent design
and compute the expected utility for each of these (under the assumption that other
agents are acting rationally, according to game theory). In this way, game-theoretic
techniques can determine the best strategy against a rational player and the expected
return for each player.
2. Mechanism design: When an environment is inhabited by many agents, it might be
Mechanism design
possible to deﬁne the rules of the environment (i.e., the game that the agents must
play) so that the collective good of all agents is maximized when each agent adopts the
game-theoretic solution that maximizes its own utility. For example, game theory can
