---
chunk_id: "book-ca4fca8dd8-chunk-1401"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1401
confidence: "first-pass"
extraction_method: "structured-local"
---

850
Chapter 23
Reinforcement Learning
state s, and let N(s,a) be the number of times action a has been tried in state s. Suppose
we are using value iteration in an ADP learning agent; then we need to rewrite the update
equation (Equation (16.10) on page 563) to incorporate the optimistic estimate:
U+(s) ←max
a
f

∑
s′ P(s′ |s,a)[R(s,a,s′)+γU+(s′)], N(s,a)

.
(23.5)
Here, f is the exploration function. The function f(u,n) determines how greed (preference
Exploration function
for high values of the utility u) is traded off against curiosity (preference for actions that have
not been tried often and have a low count n). The function should be increasing in u and
decreasing in n. Obviously, there are many possible functions that ﬁt these conditions. One
particularly simple deﬁnition is
f(u,n) =
 R+
if n < Ne
u
otherwise,
where R+ is an optimistic estimate of the best possible reward obtainable in any state and
Ne is a ﬁxed parameter. This will have the effect of making the agent try each state–action
pair at least Ne times. The fact that U+ rather than U appears on the right-hand side of
Equation (23.5) is very important. As exploration proceeds, the states and actions near the
start state might well be tried a large number of times. If we used U, the more pessimistic
utility estimate, then the agent would soon become disinclined to explore further aﬁeld. The
use of U+ means that the beneﬁts of exploration are propagated back from the edges of
unexplored regions, so that actions that lead toward unexplored regions are weighted more
highly, rather than just actions that are themselves unfamiliar.
The effect of this exploration policy can be seen clearly in Figure 23.7(b), which shows
a rapid convergence toward zero policy loss, unlike with the greedy approach. A very nearly
optimal policy is found after just 18 trials. Notice that the RMS error in the utility estimates
does not converge as quickly. This is because the agent stops exploring the unrewarding
parts of the state space fairly soon, visiting them only “by accident” thereafter. However, it
makes perfect sense for the agent not to care about the exact utilities of states that it knows
are undesirable and can be avoided. There is not much point in learning about the best radio
station to listen to while falling off a cliff.
23.3.2 Safe exploration
So far we have assumed that an agent is free to explore as it wishes—that any negative rewards
serve only to improve its model of the world. That is, if we play a game of chess and lose,
we suffer no damage (except perhaps to our pride), and whatever we learned will make us
a better player in the next game. Similarly, in a simulation environment for a self-driving
car, we could explore the limits of the car’s performance, and any accidents give us more
information. If the car crashes, we just hit the reset button.
Unfortunately, the real world is less forgiving. If you are a baby sunﬁsh, your probability
of surviving to adulthood is about 0.00000001. Many actions are irreversible, in the sense
deﬁned for online search agents in Section 4.5: no subsequent sequence of actions can restore
the state to what it was before the irreversible action was taken. In the worst case, the agent
enters an absorbing state where no actions have any effect and no rewards are received.
Absorbing state
In many practical settings, we cannot afford to have our agents taking irreversible actions
or entering absorbing states. For example, an agent learning to drive in a real car should avoid
