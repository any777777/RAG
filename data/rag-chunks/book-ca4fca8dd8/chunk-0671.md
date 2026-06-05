---
chunk_id: "book-ca4fca8dd8-chunk-0671"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 671
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 12
QUANTIFYING UNCERTAINTY
In which we see how to tame uncertainty with numeric degrees of belief.
12.1 Acting under Uncertainty
Agents in the real world need to handle uncertainty, whether due to partial observability,
Uncertainty
nondeterminism, or adversaries. An agent may never know for sure what state it is in now or
where it will end up after a sequence of actions.
We have seen problem-solving and logical agents handle uncertainty by keeping track of
a belief state—a representation of the set of all possible world states that it might be in—and
generating a contingency plan that handles every possible eventuality that its sensors may
report during execution. This approach works on simple problems, but it has drawbacks:
• The agent must consider every possible explanation for its sensor observations, no mat-
ter how unlikely. This leads to a large belief-state full of unlikely possibilities.
• A correct contingent plan that handles every eventuality can grow arbitrarily large and
must consider arbitrarily unlikely contingencies.
• Sometimes there is no plan that is guaranteed to achieve the goal—yet the agent must
act. It must have some way to compare the merits of plans that are not guaranteed.
Suppose, for example, that an automated taxi has the goal of delivering a passenger to the
airport on time. The taxi forms a plan, A90, that involves leaving home 90 minutes before the
ﬂight departs and driving at a reasonable speed. Even though the airport is only 5 miles away,
a logical agent will not be able to conclude with absolute certainty that “Plan A90 will get us
to the airport in time.” Instead, it reaches the weaker conclusion “Plan A90 will get us to the
airport in time, as long as the car doesn’t break down, and I don’t get into an accident, and
the road isn’t closed, and no meteorite hits the car, and ... .” None of these conditions can be
deduced for sure, so we can’t infer that the plan succeeds. This is the logical qualiﬁcation
problem (page 259), for which we so far have seen no real solution.
Nonetheless, in some sense A90 is in fact the right thing to do. What do we mean by this?
As we discussed in Chapter 2, we mean that out of all the plans that could be executed, A90
is expected to maximize the agent’s performance measure (where the expectation is relative
to the agent’s knowledge about the environment). The performance measure includes getting
to the airport in time for the ﬂight, avoiding a long, unproductive wait at the airport, and
avoiding speeding tickets along the way. The agent’s knowledge cannot guarantee any of
these outcomes for A90, but it can provide some degree of belief that they will be achieved.
Other plans, such as A180, might increase the agent’s belief that it will get to the airport
on time, but also increase the likelihood of a long, boring wait. The right thing to do—the ◀
rational decision—therefore depends on both the relative importance of various goals and
