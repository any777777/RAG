---
chunk_id: "book-ca4fca8dd8-chunk-0131"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 131
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 2.4
The Structure of Agents
77
In an atomic representation each state of the world is indivisible—it has no internal
Atomic
representation
structure. Consider the task of ﬁnding a driving route from one end of a country to the other
via some sequence of cities (we address this problem in Figure 3.1 on page 82). For the pur-
poses of solving this problem, it may sufﬁce to reduce the state of the world to just the name of
the city we are in—a single atom of knowledge, a “black box” whose only discernible prop-
erty is that of being identical to or different from another black box. The standard algorithms
underlying search and game-playing (Chapters 3, 4, and 6), hidden Markov models (Chap-
ter 14), and Markov decision processes (Chapter 16) all work with atomic representations.
A factored representation splits up each state into a ﬁxed set of variables or attributes,
Factored
representation
Variable
Attribute
each of which can have a value. Consider a higher-ﬁdelity description for the same driving
Value
problem, where we need to be concerned with more than just atomic location in one city or
another; we might need to pay attention to how much gas is in the tank, our current GPS
coordinates, whether or not the oil warning light is working, how much money we have for
tolls, what station is on the radio, and so on. While two different atomic states have nothing in
common—they are just different black boxes—two different factored states can share some
attributes (such as being at some particular GPS location) and not others (such as having lots
of gas or having no gas); this makes it much easier to work out how to turn one state into an-
other. Many important areas of AI are based on factored representations, including constraint
satisfaction algorithms (Chapter 5), propositional logic (Chapter 7), planning (Chapter 11),
Bayesian networks (Chapters 12, 13, 14, 15, and 18), and various machine learning algorithms.
For many purposes, we need to understand the world as having things in it that are re-
lated to each other, not just variables with values. For example, we might notice that a large
truck ahead of us is reversing into the driveway of a dairy farm, but a loose cow is block-
ing the truck’s path. A factored representation is unlikely to be pre-equipped with the at-
tribute TruckAheadBackingIntoDairyFarmDrivewayBlockedByLooseCow with value true or
false. Instead, we would need a structured representation, in which objects such as cows
Structured
representation
and trucks and their various and varying relationships can be described explicitly (see Fig-
ure 2.16(c)). Structured representations underlie relational databases and ﬁrst-order logic
(Chapters 8, 9, and 10), ﬁrst-order probability models (Chapter 18), and much of natural lan-
guage understanding (Chapters 24 and 25). In fact, much of what humans express in natural
language concerns objects and their relationships.
As we mentioned earlier, the axis along which atomic, factored, and structured repre-
sentations lie is the axis of increasing expressiveness. Roughly speaking, a more expressive
Expressiveness
representation can capture, at least as concisely, everything a less expressive one can capture,
plus some more. Often, the more expressive language is much more concise; for example, the
rules of chess can be written in a page or two of a structured-representation language such
as ﬁrst-order logic but require thousands of pages when written in a factored-representation
language such as propositional logic and around 1038 pages when written in an atomic lan-
guage such as that of ﬁnite-state automata. On the other hand, reasoning and learning become
more complex as the expressive power of the representation increases. To gain the beneﬁts
of expressive representations while avoiding their drawbacks, intelligent systems for the real
world may need to operate at all points along the axis simultaneously.
Another axis for representation involves the mapping of concepts to locations in physical
memory, whether in a computer or in a brain. If there is a one-to-one mapping between
concepts and memory locations, we call that a localist representation. On the other hand,
Localist
representation
