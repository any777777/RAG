---
chunk_id: "book-ca4fca8dd8-chunk-1097"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1097
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 18.3
Keeping Track of a Complex World
655
0
100
200
300
400
500
600
+ 1.1040359× 109
−30
−20
−10
0
10
20
30
1.0 - 2.0 Hz
0
100
200
300
400
500
600
Time (s)
+ 1.1040359× 109
−1
0
1
2
3
4
5
STA (1.5s) / LTA (60s)
ASAR – se
(a)
(b)
Figure 18.7 (a) Top: Example of seismic waveform recorded at Alice Springs, Australia.
Bottom: the waveform after processing to detect the arrival times of seismic waves. Blue lines
are the automatically detected arrivals; red lines are the true arrivals. (b) Location estimates
for the DPRK nuclear test of February 12, 2013: UN CTBTO Late Event Bulletin (green
triangle at top left); NET-VISA (blue square in center). The entrance to the underground
test facility (small “x”) is 0.75km from NET-VISA’s estimate. Contours show NET-VISA’s
posterior location distribution. Courtesy of CTBTO Preparatory Commission.
cess (citation, seismic propagation). The percepts are ambiguous as to their origin, but when
multiple percepts are hypothesized to have originated with the same unknown object, that
object’s properties can be inferred more accurately.
The same structure and reasoning patterns hold for areas such as database deduplication
and natural language understanding. In some cases, inferring an object’s existence involves
grouping percepts together—a process that resembles the clustering task in machine learning.
In other cases, an object may generate no percepts at all and still have its existence inferred—
as happened, for example, when observations of Uranus led to the discovery of Neptune. The
existence of the unobserved object follows from its effects on the behavior and properties of
observed objects.
18.3 Keeping Track of a Complex World
Chapter 14 considered the problem of keeping track of the state of the world, but covered
only the case of atomic representations (HMMs) and factored representations (DBNs and
Kalman ﬁlters). This makes sense for worlds with a single object—perhaps a single patient
in the intensive care unit or a single bird ﬂying through the forest. In this section, we see what
happens when two or more objects generate the observations. What makes this case different
from plain old state estimation is that there is now the possibility of uncertainty about which
object generated which observation. This is the identity uncertainty problem of Section 18.2
(page 648), now viewed in a temporal context. In the control theory literature, this is the data
association problem—that is, the problem of associating observation data with the objects
Data association
that generated them. Although we could view this as yet another example of open-universe
probabilistic modeling, it is important enough in practice to deserve its own section.
