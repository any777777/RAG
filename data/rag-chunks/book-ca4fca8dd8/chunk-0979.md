---
chunk_id: "book-ca4fca8dd8-chunk-0979"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 979
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.1
Properties of Multiagent Environments
591
help design the protocols for a collection of Internet trafﬁc routers so that each router
has an incentive to act in such a way that global throughput is maximized. Mechanism
design can also be used to construct intelligent multiagent systems that solve complex
problems in a distributed fashion.
Game theory provides a range of different models, each with its own set of underlying as-
sumptions; it is important to choose the right model for each setting. The most important
distinction is whether we should consider it a cooperative game or not:
• In a cooperative game, it is possible to have a binding agreement between agents,
Cooperative game
thereby enabling robust cooperation. In the human world, legal contracts and social
norms help establish such binding agreements. In the world of computer programs, it
may be possible to inspect source code to make sure it will follow an agreement. We
use cooperative game theory to analyze this situation.
• If binding agreements are not possible, we have a non-cooperative game. Although
Non-cooperative
game
this term suggests that the game is inherently competitive, and that cooperation is not
possible, that need not be the case: non-cooperative simply means that there is no cen-
tral agreement that binds all agents and guarantees cooperation. But it could well be
that agents independently decide to cooperate, because it is in their own best interests.
We use non-cooperative game theory to analyze this situation.
Some environments will combine multiple different dimensions. For example, a package
delivery company may do centralized, ofﬂine planning for the routes of its trucks and planes
each day, but leave some aspects open for autonomous decisions by drivers and pilots who
can respond individually to trafﬁc and weather situations. Also, the goals of the company
and its employees are brought into alignment, to some extent, by the payment of incentives
Incentive
(salaries and bonuses)—a sure sign that this is a true multiagent system.
17.1.3 Multiagent planning
For the time being, we will treat the multieffector, multibody, and multiagent settings in the
same way, labeling them generically as multiactor settings, using the generic term actor to
Multiactor
Actor
cover effectors, bodies, and agents. The goal of this section is to work out how to deﬁne
transition models, correct plans, and efﬁcient planning algorithms for the multiactor setting.
A correct plan is one that, if executed by the actors, achieves the goal. (In the true multiagent
setting, of course, the agents may not agree to execute any particular plan, but at least they
will know what plans would work if they did agree to execute them.)
A key difﬁculty in attempting to come up with a satisfactory model of multiagent action
is that we must somehow deal with the thorny issue of concurrency, by which we simply
Concurrency
mean that the plans of each agent may be executed simultaneously. If we are to reason about
the execution of multiactor plans, then we will ﬁrst need a model of multiactor plans that
embodies a satisfactory model of concurrent action.
In addition, multiactor action raises a whole set of issues that are not a concern in single-
agent planning. In particular, agents must take into account the way in which their own ◀
actions interact with the actions of other agents. For example, an agent will need to consider
whether the actions performed by other agents might clobber the preconditions of its own
actions, whether the resources it makes use of while executing its policy are sharable, or may
