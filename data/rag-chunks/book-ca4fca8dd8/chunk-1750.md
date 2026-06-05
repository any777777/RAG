---
chunk_id: "book-ca4fca8dd8-chunk-1750"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1750
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 29.1
AI Components
1065
Selecting actions
The primary difﬁculty in action selection in the real world is coping with long-term plans—
such as graduating from college in four years—that consist of billions of primitive steps.
Search algorithms that consider sequences of primitive actions scale only to tens or perhaps
hundreds of steps. It is only by imposing hierarchical structure on behavior that we humans
cope at all. We saw in Section 11.4 how to use hierarchical representations to handle problems
of this scale; furthermore, work in hierarchical reinforcement learning has succeeded in
combining these ideas with the MDP formalism described in Chapter 16.
As yet, these methods have not been extended to the partially observable case (POMDPs).
Moreover, algorithms for solving POMDPs are typically using the same atomic state repre-
sentation we used for the search algorithms of Chapter 3. There is clearly a great deal of
work to do here, but the technical foundations are largely in place for making progress. The
main missing element is an effective method for constructing the hierarchical representations
of state and behavior that are necessary for decision making over long time scales.
Deciding what we want
Chapter 3 introduced search algorithms to ﬁnd a goal state. But goal-based agents are brittle
when the environment is uncertain, and when there are multiple factors to consider. In princi-
ple, utility-maximization agents address those issues in a completely general way. The ﬁelds
of economics and game theory, as well as AI, make use of this insight: just declare what you
want to optimize, and what each action does, and we can compute the optimal action.
In practice, however, we now realize that the task of picking the right utility function is a
challenging problem in its own right. Imagine, for example, the complex web of interacting
preferences that must be understood by an agent operating as an ofﬁce assistant for a human
being. The problem is exacerbated by the fact that each human is different, so an agent just
“out of the box” will not have enough experience with any one individual to learn an accurate
preference model; it will necessarily need to operate under preference uncertainty. Further
complexity arises if we want to ensure that our agents are acting in a way that is fair and
equitable for society, rather than just one individual.
We do not yet have much experience with building complex real-world preference mod-
els, let alone probability distributions over such models. Although there are factored for-
malisms, similar to Bayes nets, that are intended to decompose preferences over complex
states, it has proven difﬁcult to use these formalisms in practice. One reason may be that
preferences over states are really compiled from preferences over state histories, which are
described by reward functions (see Chapter 16). Even if the reward function is simple, the
corresponding utility function may be very complex.
This suggests that we take seriously the task of knowledge engineering for reward func-
tions as a way of conveying to our agents what we want them to do. The idea of inverse
reinforcement learning (Section 23.6) is one approach to this problem when we have an
expert who can perform a task, but not explain it. We could also use better languages for
expressing what we want. For example, in robotics, linear temporal logic makes it easier to
say what things we want to happen in the near future, what things we want to avoid, and what
states we want to persist forever (Littman et al., 2017). We need better ways of saying what
we want and better ways for robots to interpret the information we provide.
