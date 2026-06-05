---
chunk_id: "book-ca4fca8dd8-chunk-1124"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1124
confidence: "first-pass"
extraction_method: "structured-local"
---

674
Chapter 19
Learning from Examples
Then we can say that the prior probability P(h) is high for a smooth degree-1 or -2 polynomial
and lower for a degree-12 polynomial with large, sharp spikes. We allow unusual-looking
functions when the data say we really need them, but we discourage them by giving them a
low prior probability.
Why not let H be the class of all computer programs, or all Turing machines? The
problem is that there is a tradeoff between the expressiveness of a hypothesis space and the
▶
computational complexity of ﬁnding a good hypothesis within that space. For example, ﬁtting
a straight line to data is an easy computation; ﬁtting high-degree polynomials is somewhat
harder; and ﬁtting Turing machines is undecidable. A second reason to prefer simple hypoth-
esis spaces is that presumably we will want to use h after we have learned it, and computing
h(x) when h is a linear function is guaranteed to be fast, while computing an arbitrary Turing
machine program is not even guaranteed to terminate.
For these reasons, most work on learning has focused on simple representations. In recent
years there has been great interest in deep learning (Chapter 22), where representations are
not simple but where the h(x) computation still takes only a bounded number of steps to
compute with appropriate hardware.
We will see that the expressiveness–complexity tradeoff is not simple: it is often the case,
as we saw with ﬁrst-order logic in Chapter 8, that an expressive language makes it possible
for a simple hypothesis to ﬁt the data, whereas restricting the expressiveness of the language
means that any consistent hypothesis must be complex.
19.2.1 Example problem: Restaurant waiting
We will describe a sample supervised learning problem in detail: the problem of deciding
whether to wait for a table at a restaurant. This problem will be used throughout the chapter
to demonstrate different model classes. For this problem the output, y, is a Boolean variable
that we will call WillWait; it is true for examples where we do wait for a table. The input, x,
is a vector of ten attribute values, each of which has discrete values:
1. Alternate: whether there is a suitable alternative restaurant nearby.
2. Bar: whether the restaurant has a comfortable bar area to wait in.
3. Fri/Sat: true on Fridays and Saturdays.
4. Hungry: whether we are hungry right now.
5. Patrons: how many people are in the restaurant (values are None, Some, and Full).
6. Price: the restaurant’s price range ($, $$, $$$).
7. Raining: whether it is raining outside.
8. Reservation: whether we made a reservation.
9. Type: the kind of restaurant (French, Italian, Thai, or burger).
10. WaitEstimate: host’s wait estimate: 0–10, 10–30, 30–60, or >60 minutes.
A set of 12 examples, taken from the experience of one of us (SR), is shown in Figure 19.2.
Note how skimpy these data are: there are 26 × 32 × 42 = 9,216 possible combinations of
values for the input attributes, but we are given the correct output for only 12 of them; each of
the other 9,204 could be either true or false; we don’t know. This is the essence of induction:
we need to make our best guess at these missing 9,204 output values, given only the evidence
of the 12 examples.
