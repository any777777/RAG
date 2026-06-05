---
chunk_id: "book-ca4fca8dd8-chunk-1728"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1728
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 28.3
The Ethics of AI
1053
determinations: analysts build an AND/OR tree of possible failures and assign probabilities
to each root cause, allowing for calculations of overall failure probability. These techniques
can and should be applied to all safety-critical engineered systems, including AI systems.
The ﬁeld of software engineering is aimed at producing reliable software, but the em-
phasis has historically been on correctness, not safety. Correctness means that the software
faithfully implements the speciﬁcation. But safety goes beyond that to insist that the speciﬁ-
cation has considered any feasible failure modes, and is designed to degrade gracefully even
in the face of unforeseen failures. For example, the software for a self-driving car wouldn’t
be considered safe unless it can handle unusual situations. For example, what if the power to
the main computer dies? A safe system will have a backup computer with a separate power
supply. What if a tire is punctured at high speed? A safe system will have tested for this, and
will have software to correct for the resulting loss of control.
An agent designed as a utility maximizer, or as a goal achiever, can be unsafe if it has
the wrong objective function. Suppose we give a robot the task of fetching a coffee from
the kitchen. We might run into trouble with unintended side effects—the robot might rush
Unintended side
eﬀect
to accomplish the goal, knocking over lamps and tables along the way. In testing, we might
notice this kind of behavior and modify the utility function to penalize such damage, but it is
difﬁcult for the designers and testers to anticipate all possible side effects ahead of time.
One way to deal with this is to design a robot to have low impact (Armstrong and Levin-
Low impact
stein, 2017): instead of just maximizing utility, maximize the utility minus a weighted sum-
mary of all changes to the state of the world. In this way, all other things being equal, the
robot prefers not to change those things whose effect on utility is unknown; so it avoids
knocking over the lamp not because it knows speciﬁcally that knocking the lamp will cause
it to fall over and break, but because it knows in general that disruption might be bad. This
can be seen as a version of the physician’s creed “ﬁrst, do no harm,” or as an analog to regu-
larization in machine learning: we want a policy that achieves goals, but we prefer policies
that take smooth, low-impact actions to get there. The trick is how to measure impact. It
is not acceptable to knock over a fragile lamp, but perfectly ﬁne if the air molecules in the
room are disturbed a little, or if some bacteria in the room are inadvertently killed. It is cer-
tainly not acceptable to harm pets and humans in the room. We need to make sure that the
robot knows the differences between these cases (and many subtle cases in between) through
a combination of explicit programming, machine learning over time, and rigorous testing.
Utility functions can go wrong due to externalities, the word used by economists for
factors that are outside of what is measured and paid for. The world suffers when green-
house gases are considered as externalities—companies and countries are not penalized for
producing them, and as a result everyone suffers. Ecologist Garrett Hardin (1968) called the
exploitation of shared resources the tragedy of the commons. We can mitigate the tragedy
by internalizing the externalities—making them part of the utility function, for example with
a carbon tax—or by using the design principles that economist Elinor Ostrom identiﬁed as
being used by local people throughout the world for centuries (work that won her the Nobel
Prize in Economics in 2009):
• Clearly deﬁne the shared resource and who has access.
• Adapt to local conditions.
• Allow all parties to participate in decisions.
