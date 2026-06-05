---
chunk_id: "book-ca4fca8dd8-chunk-0098"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 98
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 2.2
Good Behavior: The Concept of Rationality
59
not otherwise engaged, so, being rational, I start to cross the street. Meanwhile, at 33,000
feet, a cargo door falls off a passing airliner,3 and before I make it to the other side of the
street I am ﬂattened. Was I irrational to cross the street? It is unlikely that my obituary would
read “Idiot attempts to cross street.”
This example shows that rationality is not the same as perfection. Rationality maximizes
expected performance, while perfection maximizes actual performance. Retreating from a
requirement of perfection is not just a question of being fair to agents. The point is that if we
expect an agent to do what turns out after the fact to be the best action, it will be impossible
to design an agent to fulﬁll this speciﬁcation—unless we improve the performance of crystal
balls or time machines.
Our deﬁnition of rationality does not require omniscience, then, because the rational
choice depends only on the percept sequence to date. We must also ensure that we haven’t
inadvertently allowed the agent to engage in decidedly underintelligent activities. For exam-
ple, if an agent does not look both ways before crossing a busy road, then its percept sequence
will not tell it that there is a large truck approaching at high speed. Does our deﬁnition of
rationality say that it’s now OK to cross the road? Far from it!
First, it would not be rational to cross the road given this uninformative percept sequence:
the risk of accident from crossing without looking is too great. Second, a rational agent should
choose the “looking” action before stepping into the street, because looking helps maximize
the expected performance. Doing actions in order to modify future percepts—sometimes
called information gathering—is an important part of rationality and is covered in depth in
Information
gathering
Chapter 15. A second example of information gathering is provided by the exploration that
must be undertaken by a vacuum-cleaning agent in an initially unknown environment.
Our deﬁnition requires a rational agent not only to gather information but also to learn as
Learning
much as possible from what it perceives. The agent’s initial conﬁguration could reﬂect some
prior knowledge of the environment, but as the agent gains experience this may be modiﬁed
and augmented. There are extreme cases in which the environment is completely known a
priori and completely predictable. In such cases, the agent need not perceive or learn; it
simply acts correctly.
Of course, such agents are fragile. Consider the lowly dung beetle. After digging its nest
and laying its eggs, it fetches a ball of dung from a nearby heap to plug the entrance. If the
ball of dung is removed from its grasp en route, the beetle continues its task and pantomimes
plugging the nest with the nonexistent dung ball, never noticing that it is missing. Evolu-
tion has built an assumption into the beetle’s behavior, and when it is violated, unsuccessful
behavior results.
Slightly more intelligent is the sphex wasp. The female sphex will dig a burrow, go out
and sting a caterpillar and drag it to the burrow, enter the burrow again to check all is well,
drag the caterpillar inside, and lay its eggs. The caterpillar serves as a food source when the
eggs hatch. So far so good, but if an entomologist moves the caterpillar a few inches away
while the sphex is doing the check, it will revert to the “drag the caterpillar” step of its plan
and will continue the plan without modiﬁcation, re-checking the burrow, even after dozens of
caterpillar-moving interventions. The sphex is unable to learn that its innate plan is failing,
and thus will not change it.
3
See N. Henderson, “New door latches urged for Boeing 747 jumbo jets,” Washington Post, August 24, 1989.
