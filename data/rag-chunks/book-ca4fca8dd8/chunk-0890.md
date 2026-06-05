---
chunk_id: "book-ca4fca8dd8-chunk-0890"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 890
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 15.6
The Value of Information
539
(c)
P(U | Ej)
U1
U2
U
(b)
P(U | Ej)
U1
U2
U
(a)
P(U | Ej)
U1
U2
U
Figure 15.8 Three generic cases for the value of information. In (a), a1 will almost certainly
remain superior to a2, so the information is not needed. In (b), the choice is unclear and the
information is crucial. In (c), the choice is unclear, but because it makes little difference, the
information is less valuable. (Note: The fact that U2 has a high peak in (c) means that its
expected value is known with higher certainty than U1.)
given this information, a1 is clearly preferable, because it is quite possible that a2 is blocked
by snow, whereas it is unlikely that anything blocks a1. U1 is therefore clearly higher than
U2. It is possible to obtain satellite reports E j on the actual state of each road that would give
new expectations, U′
1 and U′
2, for the two crossings. The distributions for these expectations
are shown in Figure 15.8(a). Obviously, in this case, it is not worth the expense of obtaining
satellite reports, because it is unlikely that the information derived from them will change the
plan. With no change, information has no value.
Now suppose that we are choosing between two different winding dirt roads of slightly
different lengths and we are carrying a seriously injured passenger. Then, even when U1
and U2 are quite close, the distributions of U′
1 and U′
2 are very broad. There is a signiﬁcant
possibility that the second route will turn out to be clear while the ﬁrst is blocked, and in this
case the difference in utilities will be very high. The VPI formula indicates that it might be
worthwhile getting the satellite reports. Such a situation is shown in Figure 15.8(b).
Finally, suppose that we are choosing between the two dirt roads in summertime, when
blockage by snow is unlikely. In this case, satellite reports might show one route to be more
scenic than the other because of ﬂowering alpine meadows, or perhaps wetter because of re-
cent rain. It is therefore quite likely that we would change our plan if we had the information.
In this case, however, the difference in value between the two routes is still likely to be very
small, so we will not bother to obtain the reports. This situation is shown in Figure 15.8(c).
In sum, information has value to the extent that it is likely to cause a change of plan and ◀
to the extent that the new plan will be signiﬁcantly better than the old plan.
15.6.3 Properties of the value of information
One might ask whether it is possible for information to be deleterious: can it actually have
negative expected value? Intuitively, one should expect this to be impossible. After all, one
could in the worst case just ignore the information and pretend that one has never received
it. This is conﬁrmed by the following theorem, which applies to any decision-theoretic agent
using any decision network with possible observations E j:
