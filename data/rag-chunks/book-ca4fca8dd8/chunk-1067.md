---
chunk_id: "book-ca4fca8dd8-chunk-1067"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1067
confidence: "first-pass"
extraction_method: "structured-local"
---

638
Chapter 17
Multiagent Decision Making
get a better estimate of the value of a strategy. Waugh et al. (2009) found that the abstraction
approach is vulnerable to making systematic errors in approximating the equilibrium solution:
it works for some games but not others. Brown and Sandholm (2019) showed that, at least
in the case of multiplayer Texas hold ’em poker, these vulnerabilities can be overcome by
sufﬁcient computing power. They used a 64-core server running for 8 days to compute a
baseline strategy for their Pluribus program. With that strategy they were able to defeat
human champion opponents.
Game theory and MDPs are combined in the theory of Markov games, also called stochas-
tic games (Littman, 1994; Hu and Wellman, 1998). Shapley (1953b) actually described the
value iteration algorithm independently of Bellman, but his results were not widely appre-
ciated, perhaps because they were presented in the context of Markov games. Evolutionary
game theory (Smith, 1982; Weibull, 1995) looks at strategy drift over time: if your opponent’s
strategy is changing, how should you react?
Textbooks on game theory from an economics point of view include those by Myerson
(1991), Fudenberg and Tirole (1991), Osborne (2004), and Osborne and Rubinstein (1994).
From an AI perspective we have Nisan et al. (2007) and Leyton-Brown and Shoham (2008).
See (Sandholm, 1999) for a useful survey of multiagent decision making.
Multiagent RL is distinguished from distributed RL by the presence of agents who cannot
coordinate their actions (except by explicit communicative acts) and who may not share the
same utility function. Thus, multiagent RL deals with sequential game-theoretic problems or
Markov games, as deﬁned in Chapter 16. What causes problems is the fact that, while an
agent is learning to defeat its opponent’s policy, the opponent is changing its policy to defeat
the agent. Thus, the environment is nonstationary (see page 555).
Littman (1994) noted this difﬁculty when introducing the ﬁrst RL algorithms for zero-
sum Markov games. Hu and Wellman (2003) present a Q-learning algorithm for general-
sum games that converges when the Nash equilibrium is unique; when there are multiple
equilibria, the notion of convergence is not so easy to deﬁne (Shoham et al., 2004).
Assistance games were introduced under the heading of cooperative inverse reinforce-
ment learning by Hadﬁeld-Menell et al. (2017a). Malik et al. (2018) introduced an efﬁcient
POMDP solver designed speciﬁcally for assistance games. They are related to principal–
agent games in economics, in which a principal (e.g., an employer) and an agent (e.g., an
Principal–agent
game
employee) need to ﬁnd a mutually beneﬁcial arrangement despite having widely different
preferences. The primary differences are that (1) the robot has no preferences of its own, and
(2) the robot is uncertain about the human preferences it needs to optimize.
Cooperative games were ﬁrst studied by von Neumann and Morgenstern (1944). The
notion of the core was introduced by Donald Gillies (1959), and the Shapley value by Lloyd
Shapley (1953a). A good introduction to the mathematics of cooperative games is Peleg and
Sudholter (2002). Simple games in general are discussed in detail by Taylor and Zwicker
(1999). For an introduction to the computational aspects of cooperative game theory, see
Chalkiadakis et al. (2011).
Many compact representation schemes for cooperative games have been developed over
the past three decades, starting with the work of Deng and Papadimitriou (1994). The most
inﬂuential of these schemes is the marginal contribution networks model, which was intro-
duced by Ieong and Shoham (2005). The approach to coalition formation that we describe
was developed by Sandholm et al. (1999); Rahwan et al. (2015) survey the state of the art.
