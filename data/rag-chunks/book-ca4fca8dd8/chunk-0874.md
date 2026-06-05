---
chunk_id: "book-ca4fca8dd8-chunk-0874"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 874
confidence: "first-pass"
extraction_method: "structured-local"
---

530
Chapter 15
Making Simple Decisions
15.4 Multiattribute Utility Functions
Decision making in the ﬁeld of public policy involves high stakes, in both money and lives.
For example, in deciding what levels of harmful emissions to allow from a power plant,
policy makers must weigh the prevention of death and disability against the beneﬁt of the
power and the economic burden of mitigating the emissions. Picking a site for a new airport
requires consideration of the disruption caused by construction; the cost of land; the distance
from centers of population; the noise of ﬂight operations; safety issues arising from local
topography and weather conditions; and so on. Problems like these, in which outcomes are
characterized by two or more attributes, are handled by multiattribute utility theory. In
Multiattribute utility
theory
essence, it’s the theory of comparing apples to oranges.
Let the attributes be X=X1,...,Xn and let x=⟨x1,...,xn⟩be a complete vector of assign-
ments, where each xi is either a numeric value or a discrete value with an assumed ordering
on values. The analysis is easier if we arrange it so that higher values of an attribute always
correspond to higher utilities: utilities are monotonically increasing. That means that we can’t
use, say, the number of deaths, d as an attribute; we would have to use −d. It also means that
we can’t use the room temperature, t, as an attribute. If the utility function for temperature
has a peak at 70◦F and falls off monotonically on either side, then we could split the attribute
into two pieces. We could use t −70 to measure whether the room is warm enough, and
70−t to measure whether it is cool enough; both of these attributes would be monotonically
increasing until they reach their maximum utility value at 0; the utility curve is ﬂat from that
point on, meaning that you dont’t get any more “warm enough” above 70◦F, nor any more
“cool enough” below 70◦F.
The attributes in the airport problem could be:
• Throughput, measured by the number of ﬂights per day;
• Safety, measured by minus the expected number of deaths per year;
• Quietness, measured by minus the number of people living under the ﬂight paths;
• Frugality, measured by the negative cost of construction.
We begin by examining cases in which decisions can be made without combining the attribute
values into a single utility value. Then we look at cases in which the utilities of attribute
combinations can be speciﬁed very concisely.
15.4.1 Dominance
Suppose that airport site S1 costs less, generates less noise pollution, and is safer than site S2.
One would not hesitate to reject S2. We then say that there is strict dominance of S1 over
Strict dominance
S2. In general, if an option is of lower value on all attributes than some other option, it need
not be considered further. Strict dominance is often very useful in narrowing down the ﬁeld
of choices to the real contenders, although it seldom yields a unique choice. Figure 15.4(a)
shows a schematic diagram for the two-attribute case.
That is ﬁne for the deterministic case, in which the attribute values are known for sure.
What about the general case, where the outcomes are uncertain? A direct analog of strict
dominance can be constructed, where, despite the uncertainty, all possible concrete outcomes
for S1 strictly dominate all possible outcomes for S2. (See Figure 15.4(b).) Of course, this
will probably occur even less often than in the deterministic case.
