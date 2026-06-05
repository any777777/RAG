---
chunk_id: "book-ca4fca8dd8-chunk-0927"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 927
confidence: "first-pass"
extraction_method: "structured-local"
---

560
Chapter 16
Making Complex Decisions
In other words, Q′(s,a) satisﬁes the Bellman equation for MDP M′. Now we can extract the
optimal policy for M′ using Equation (16.7):
π∗
M′(s) = argmax
a
Q′(s,a) = argmax
a
Q(s,a)−Φ(s) = argmax
a
Q(s,a) = π∗
M(s).
The function Φ(s) is often called a potential, by analogy to the electrical potential (volt-
age) that gives rise to electric ﬁelds. The term γΦ(s′) −Φ(s) functions as a gradient of the
potential. Thus, if Φ(s) has higher value in states that have higher utility, the addition of
γΦ(s′)−Φ(s) to the reward has the effect of leading the agent “uphill” in utility.
At ﬁrst sight, it may seem rather counterintuitive that we can modify the reward in this
way without changing the optimal policy. It helps if we remember that all policies are optimal
with a reward function that is zero everywhere. This means, according to the shaping theorem,
that all policies are optimal for any potential-based reward of the form R(s,a,s′) = γΦ(s′)−
Φ(s). Intuitively, this is because with such a reward it doesn’t matter which way the agent
goes from A to B. (This is easiest to see when γ =1: along any path the sum of rewards
collapses to Φ(B)−Φ(A), so all paths are equally good.) So adding a potential-based reward
to any other reward shouldn’t change the optimal policy.
The ﬂexibility afforded by the shaping theorem means that we can actually help out the
agent by making the immediate reward more directly reﬂect what the agent should do. In
fact, if we set Φ(s)=U(s), then the greedy policy πG with respect to the modiﬁed reward R′
is also an optimal policy:
πG(s) = argmax
a
∑
s′
P(s′ |s,a)R′(s,a,s′)
= argmax
a
∑
s′
P(s′ |s,a)[R(s,a,s′)+γΦ(s′)−Φ(s)]
= argmax
a
∑
s′
P(s′ |s,a)[R(s,a,s′)+γU(s′)−U(s)]
= argmax
a
∑
s′
P(s′ |s,a)[R(s,a,s′)+γU(s′)]
= π∗(s)
(by Equation (16.4)).
Of course, in order to set Φ(s)=U(s), we would need to know U(s); so there is no free lunch,
but there is still considerable value in deﬁning a reward function that is helpful to the extent
possible. This is precisely what animal trainers do when they provide a small treat to the
animal for each step in the target sequence.
16.1.4 Representing MDPs
The simplest way to represent P(s′ |s,a) and R(s,a,s′) is with big, three-dimensional tables
of size |S|2|A|. This is ﬁne for small problems such as the 4×3 world, for which the tables
have 112 ×4=484 entries each. In some cases, the tables are sparse—most entries are zero
because each state s can transition to only a bounded number of states s′—which means the
tables are of size O(|S∥A|). For larger problems, even sparse tables are far too big.
Just as in Chapter 15, where Bayesian networks were extended with action and utility
nodes to create decision networks, we can represent MDPs by extending dynamic Bayesian
networks (DBNs, see Chapter 14) with decision, reward, and utility nodes to create dynamic
decision networks, or DDNs. DDNs are factored representations in the terminology of
Dynamic decision
network
