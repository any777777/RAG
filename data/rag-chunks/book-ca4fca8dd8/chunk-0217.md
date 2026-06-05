---
chunk_id: "book-ca4fca8dd8-chunk-0217"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 217
confidence: "first-pass"
extraction_method: "structured-local"
---

132
Chapter 4
Search in Complex Environments
generated initial states, until a goal is found. It is complete with probability 1, because it will
eventually generate a goal state as the initial state. If each hill-climbing search has a probabil-
ity p of success, then the expected number of restarts required is 1/p. For 8-queens instances
with no sideways moves allowed, p ≈0.14, so we need roughly 7 iterations to ﬁnd a goal (6
failures and 1 success). The expected number of steps is the cost of one successful iteration
plus (1−p)/p times the cost of failure, or roughly 22 steps in all. When we allow sideways
moves, 1/0.94 ≈1.06 iterations are needed on average and (1×21)+(0.06/0.94)×64 ≈25
steps. For 8-queens, then, random-restart hill climbing is very effective indeed. Even for
three million queens, the approach can ﬁnd solutions in seconds.1
The success of hill climbing depends very much on the shape of the state-space land-
scape: if there are few local maxima and plateaus, random-restart hill climbing will ﬁnd a
good solution very quickly. On the other hand, many real problems have a landscape that
looks more like a widely scattered family of balding porcupines on a ﬂat ﬂoor, with miniature
porcupines living on the tip of each porcupine needle. NP-hard problems (see Appendix A)
typically have an exponential number of local maxima to get stuck on. Despite this, a reason-
ably good local maximum can often be found after a small number of restarts.
4.1.2 Simulated annealing
A hill-climbing algorithm that never makes “downhill” moves toward states with lower value
(or higher cost) is always vulnerable to getting stuck in a local maximum. In contrast, a purely
random walk that moves to a successor state without concern for the value will eventually
stumble upon the global maximum, but will be extremely inefﬁcient. Therefore, it seems
reasonable to try to combine hill climbing with a random walk in a way that yields both
efﬁciency and completeness.
Simulated annealing is such an algorithm. In metallurgy, annealing is the process used
Simulated annealing
to temper or harden metals and glass by heating them to a high temperature and then gradually
cooling them, thus allowing the material to reach a low-energy crystalline state. To explain
simulated annealing, we switch our point of view from hill climbing to gradient descent (i.e.,
minimizing cost) and imagine the task of getting a ping-pong ball into the deepest crevice in
a very bumpy surface. If we just let the ball roll, it will come to rest at a local minimum. If we
shake the surface, we can bounce the ball out of the local minimum—perhaps into a deeper
local minimum, where it will spend more time. The trick is to shake just hard enough to
bounce the ball out of local minima but not hard enough to dislodge it from the global mini-
mum. The simulated-annealing solution is to start by shaking hard (i.e., at a high temperature)
and then gradually reduce the intensity of the shaking (i.e., lower the temperature).
The overall structure of the simulated-annealing algorithm (Figure 4.5) is similar to hill
climbing. Instead of picking the best move, however, it picks a random move. If the move
improves the situation, it is always accepted. Otherwise, the algorithm accepts the move with
some probability less than 1. The probability decreases exponentially with the “badness”
of the move—the amount ∆E by which the evaluation is worsened. The probability also
decreases as the “temperature” T goes down: “bad” moves are more likely to be allowed at
the start when T is high, and they become more unlikely as T decreases. If the schedule
lowers T to 0 slowly enough, then a property of the Boltzmann distribution, e∆E/T, is that
1
Luby et al. (1993) suggest restarting after a ﬁxed number of steps and show that this can be much more efﬁcient
than letting each search continue indeﬁnitely.
