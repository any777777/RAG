---
chunk_id: "book-ca4fca8dd8-chunk-0885"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 885
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 536

536
Chapter 15
Making Simple Decisions
U
Airport Site
Quietness
Frugality
Litigation
Construction
Air Traffic
Safety
Figure 15.6 A decision network for the airport-siting problem.
U
Airport Site
Litigation
Construction
Air Traffic
Figure 15.7 A simpliﬁed representation of the airport-siting problem. Chance nodes corre-
sponding to outcome states have been factored out.
For example, in Figure 15.6, a change in aircraft noise levels can be reﬂected by a change
in the conditional probability table associated with the Quietness node, whereas a change in
the weight accorded to noise pollution in the utility function can be reﬂected by a change
in the utility table. In the action-utility diagram, Figure 15.7, on the other hand, all such
changes have to be reﬂected by changes to the action-utility table. Essentially, the action-
utility formulation is a compiled version of the original formulation, obtained by summing
out the outcome state variables.
15.5.2 Evaluating decision networks
Actions are selected by evaluating the decision network for each possible setting of the deci-
sion node. Once the decision node is set, it behaves exactly like a chance node that has been
set as an evidence variable. The algorithm for evaluating decision networks is the following:

## Page 537
