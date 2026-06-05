---
chunk_id: "book-ca4fca8dd8-chunk-0953"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 953
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 16.3
Bandit Problems
577
One might reason as follows: “If there are n disjoint MDPs then it is obvious that an
optimal policy overall is built from the optimal solutions of the individual MDPs. Given
its optimal policy πi, each MDP becomes a Markov reward process where there is only one
action πi(s) in each state s. So we have reduced the n-armed bandit superprocess to an n-
armed bandit process.” For example, if a real-estate developer has one construction crew and
several shopping centers to build, it seems to be just common sense that one should devise
the optimal construction plan for each shopping center and then solve the bandit problem to
decide where to send the crew each day.
While this sounds highly plausible, it is incorrect. In fact, the globally optimal policy for a
BSP may include actions that are locally suboptimal from the point of view of the constituent
MDP in which they are taken. The reason for this is that the availability of other MDPs in
which to act changes the balance between short-term and long-term rewards in a component
MDP. In fact, it tends to lead to greedier behavior in each MDP (seeking short-term rewards)
because aiming for long-term reward in one MDP would delay rewards in all the other MDPs.
For example, suppose the locally optimal construction schedule for one shopping center
has the ﬁrst shop available for rent by week 15, whereas a suboptimal schedule costs more but
has the ﬁrst shop available by week 5. If there are four shopping centers to build, it might be
better to use the locally suboptimal schedule in each so that rents start coming in from weeks
5, 10, 15, and 20, rather than weeks 15, 30, 45, and 60. In other words, what would be only a
10-week delay for a single MDP turns into a 40-week delay for the fourth MDP. In general,
the globally and locally optimal policies necessarily coincide only when the discount factor
is 1; in that case, there is no cost to delaying rewards in any MDP.
The next question is how to solve BSPs. Obviously, the globally optimal solution for a
BSP could be computed by converting it into a global MDP on the Cartesian-product state
space. The number of states would be exponential in the number of arms of the BSP, so this
would be horrendously impractical.
Instead, we can take advantage of the loose nature of the interaction between the arms.
This interaction arises only from the agent’s limited ability to attend to the arms simultane-
ously. To some extent, the interaction can be modeled by the notion of opportunity cost:
Opportunity cost
how much utility is given up per time step by not devoting that time step to another arm.
The higher the opportunity cost, the more necessary it is to generate early rewards in a given
arm. In some cases, an optimal policy in a given arm is unaffected by the opportunity cost.
(Trivially, this is true in a Markov reward process because there is only one policy.) In that
case, an optimal policy can be applied, converting that arm into a Markov reward process.
Such an optimal policy, if it exists, is called a dominating policy. It turns out that by
Dominating policy
adding actions to states, it is always possible to create a relaxed version of an MDP (see
Section 3.6.2) so that it has a dominating policy, which thus gives an upper bound on the
value of acting in the arm. A lower bound can be computed by solving each arm separately
(which may yield a suboptimal policy overall) and then computing the Gittins indices. If the
lower bound for acting in one arm is higher than the upper bounds for all other actions, then
the problem is solved; if not, then a combination of look-ahead search and recomputation of
bounds is guaranteed to eventually identify an optimal policy for the BSP. With this approach,
relatively large BSPs (1040 states or more) can be solved in a few seconds.
