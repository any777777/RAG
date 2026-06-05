---
chunk_id: "book-ca4fca8dd8-chunk-0147"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 147
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.2
Example Problems
87
of square root, ﬂoor, and factorial operations can reach any desired positive integer. For
example, we can reach 5 from 4 as follows:
j
v
u
u
t
srqp
(4!)!
k
= 5.
The problem deﬁnition is simple:
• States: Positive real numbers.
• Initial state: 4.
• Actions: Apply square root, ﬂoor, or factorial operation (factorial for integers only).
• Transition model: As given by the mathematical deﬁnitions of the operations.
• Goal state: The desired positive integer.
• Action cost: Each action costs 1.
The state space for this problem is inﬁnite: for any integer greater than 2 the factorial oper-
ator will always yield a larger integer. The problem is interesting because it explores very
large numbers: the shortest path to 5 goes through (4!)! = 620,448,401,733,239,439,360,000.
Inﬁnite state spaces arise frequently in tasks involving the generation of mathematical expres-
sions, circuits, proofs, programs, and other recursively deﬁned objects.
3.2.2 Real-world problems
We have already seen how the route-ﬁnding problem is deﬁned in terms of speciﬁed lo-
cations and transitions along edges between them. Route-ﬁnding algorithms are used in a
variety of applications. Some, such as Web sites and in-car systems that provide driving
directions, are relatively straightforward extensions of the Romania example. (The main
complications are varying costs due to trafﬁc-dependent delays, and rerouting due to road
closures.) Others, such as routing video streams in computer networks, military operations
planning, and airline travel-planning systems, involve much more complex speciﬁcations.
Consider the airline travel problems that must be solved by a travel-planning Web site:
• States: Each state obviously includes a location (e.g., an airport) and the current time.
Furthermore, because the cost of an action (a ﬂight segment) may depend on previous
segments, their fare bases, and their status as domestic or international, the state must
record extra information about these “historical” aspects.
• Initial state: The user’s home airport.
• Actions: Take any ﬂight from the current location, in any seat class, leaving after the
current time, leaving enough time for within-airport transfer if needed.
• Transition model: The state resulting from taking a ﬂight will have the ﬂight’s desti-
nation as the new location and the ﬂight’s arrival time as the new time.
• Goal state: A destination city. Sometimes the goal can be more complex, such as
“arrive at the destination on a nonstop ﬂight.”
• Action cost: A combination of monetary cost, waiting time, ﬂight time, customs and
immigration procedures, seat quality, time of day, type of airplane, frequent-ﬂyer re-
ward points, and so on.
