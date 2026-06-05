---
chunk_id: "book-ca4fca8dd8-chunk-0864"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 864
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 15.3
Utility Functions
523
15.3.1 Utility assessment and utility scales
If we want to build a decision-theoretic system that helps a human make decisions or acts on
his or her behalf, we must ﬁrst work out what the human’s utility function is. This process,
often called preference elicitation, involves presenting choices to the human and using the
Preference elicitation
observed preferences to pin down the underlying utility function.
Equation (15.2) says that there is no absolute scale for utilities, but it is helpful, nonethe-
less, to establish some scale on which utilities can be recorded and compared for any particu-
lar problem. A scale can be established by ﬁxing the utilities of any two particular outcomes,
just as we ﬁx a temperature scale by ﬁxing the freezing point and boiling point of water.
Typically, we ﬁx the utility of a “best possible prize” at U(S) = u⊤and a “worst possible
catastrophe” at U(S) = u⊥. (Both of these should be ﬁnite.) Normalized utilities use a scale
Normalized utilities
with u⊥= 0 and u⊤= 1. With such a scale, an England fan might assign a utility of 1 to
England winning the World Cup and a utility of 0 to England failing to qualify.
Given a utility scale between u⊤and u⊥, we can assess the utility of any particular prize
S by asking the agent to choose between S and a standard lottery [p,u⊤; (1 −p),u⊥]. The
Standard lottery
probability p is adjusted until the agent is indifferent between S and the standard lottery.
Assuming normalized utilities, the utility of S is given by p. Once this is done for each prize,
the utilities for all lotteries involving those prizes are determined. Suppose, for example,
we want to know how much our England fan values the outcome of England reaching the
semi-ﬁnal and then losing. We compare that outcome to a standard lottery with probability p
of winning the trophy and probability 1 −p of an ignominious failure to qualify. If there is
indifference at p=0.3, then 0.3 is the value of reaching the semi-ﬁnal and then losing.
In medical, transportation, environmental and other decision problems, people’s lives are
at stake. (Yes, there are things more important than England’s fortunes in the World Cup.) In
such cases, u⊥is the value assigned to immediate death (or in the really worst cases, many
deaths). Although nobody feels comfortable with putting a value on human life, it is a fact ◀
that tradeoffs on matters of life and death are made all the time. Aircraft are given a complete
overhaul at intervals, rather than after every trip. Cars are manufactured in a way that trades
off costs against accident survival rates. We tolerate a level of air pollution that kills four
million people a year.
Paradoxically, a refusal to put a monetary value on life can mean that life is undervalued.
Ross Shachter describes a government agency that commissioned a study on removing as-
bestos from schools. The decision analysts performing the study assumed a particular dollar
value for the life of a school-age child, and argued that the rational choice under that assump-
tion was to remove the asbestos. The agency, morally outraged at the idea of setting the value
of a life, rejected the report out of hand. It then decided against asbestos removal—implicitly
asserting a lower value for the life of a child than that assigned by the analysts.
Currently several agencies of the U.S. government, including the Environmental Protec-
tion Agency, the Food and Drug Administration, and the Department of Transportation, use
the value of a statistical life to determine the costs and beneﬁts of regulations and interven-
Value of a statistical
life
tions. Typical values in 2019 are roughly $10 million.
Some attempts have been made to ﬁnd out the value that people place on their own lives.
One common “currency” used in medical and safety analysis is the micromort, a one in a
Micromort
million chance of death. If you ask people how much they would pay to avoid a risk—for
