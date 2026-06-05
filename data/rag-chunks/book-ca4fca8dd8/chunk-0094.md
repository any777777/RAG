---
chunk_id: "book-ca4fca8dd8-chunk-0094"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 94
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 2.2
Good Behavior: The Concept of Rationality
57
2.2 Good Behavior: The Concept of Rationality
A rational agent is one that does the right thing. Obviously, doing the right thing is better
Rational agent
than doing the wrong thing, but what does it mean to do the right thing?
2.2.1 Performance measures
Moral philosophy has developed several different notions of the “right thing,” but AI has
generally stuck to one notion called consequentialism: we evaluate an agent’s behavior by its
Consequentialism
consequences. When an agent is plunked down in an environment, it generates a sequence of
actions according to the percepts it receives. This sequence of actions causes the environment
to go through a sequence of states. If the sequence is desirable, then the agent has performed
well. This notion of desirability is captured by a performance measure that evaluates any
Performance
measure
given sequence of environment states.
Humans have desires and preferences of their own, so the notion of rationality as applied
to humans has to do with their success in choosing actions that produce sequences of envi-
ronment states that are desirable from their point of view. Machines, on the other hand, do not
have desires and preferences of their own; the performance measure is, initially at least, in the
mind of the designer of the machine, or in the mind of the users the machine is designed for.
We will see that some agent designs have an explicit representation of (a version of) the per-
formance measure, while in other designs the performance measure is entirely implicit—the
agent may do the right thing, but it doesn’t know why.
Recalling Norbert Wiener’s warning to ensure that “the purpose put into the machine is
the purpose which we really desire” (page 51), notice that it can be quite hard to formulate
a performance measure correctly. Consider, for example, the vacuum-cleaner agent from the
preceding section. We might propose to measure performance by the amount of dirt cleaned
up in a single eight-hour shift. With a rational agent, of course, what you ask for is what
you get. A rational agent can maximize this performance measure by cleaning up the dirt,
then dumping it all on the ﬂoor, then cleaning it up again, and so on. A more suitable per-
formance measure would reward the agent for having a clean ﬂoor. For example, one point
could be awarded for each clean square at each time step (perhaps with a penalty for elec-
tricity consumed and noise generated). As a general rule, it is better to design performance ◀
measures according to what one actually wants to be achieved in the environment, rather
than according to how one thinks the agent should behave.
Even when the obvious pitfalls are avoided, some knotty problems remain. For example,
the notion of “clean ﬂoor” in the preceding paragraph is based on average cleanliness over
time. Yet the same average cleanliness can be achieved by two different agents, one of which
does a mediocre job all the time while the other cleans energetically but takes long breaks.
Which is preferable might seem to be a ﬁne point of janitorial science, but in fact it is a
deep philosophical question with far-reaching implications. Which is better—a reckless life
of highs and lows, or a safe but humdrum existence? Which is better—an economy where
everyone lives in moderate poverty, or one in which some live in plenty while others are very
poor? We leave these questions as an exercise for the diligent reader.
For most of the book, we will assume that the performance measure can be speciﬁed
correctly. For the reasons given above, however, we must accept the possibility that we might
put the wrong purpose into the machine—precisely the King Midas problem described on
