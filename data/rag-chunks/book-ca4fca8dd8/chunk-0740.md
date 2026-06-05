---
chunk_id: "book-ca4fca8dd8-chunk-0740"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 740
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 447

Section 13.3
Exact Inference in Bayesian Networks
447
P( j|a)
.90
P(m|a)
.70
.01
P(m|¬a)
.05
P( j|¬a)
P( j|a)
.90
P(m|a)
.70
.01
P(m|¬a)
.05
P( j|¬a)
P(b)
.001
P(e)
.002
P(¬e)
.998
P(a|b,e)
.95
.06
P(¬a|b,¬e)
.05
P(¬a|b,e)
.94
P(a|b,¬e)
Figure 13.10 The structure of the expression shown in Equation (13.5). The evaluation
proceeds top down, multiplying values along each path and summing at the “+” nodes. Notice
the repetition of the paths for j and m.
function ENUMERATION-ASK(X,e,bn) returns a distribution over X
inputs: X, the query variable
e, observed values for variables E
bn, a Bayes net with variables vars
Q(X)←a distribution over X, initially empty
for each value xi of X do
Q(xi)←ENUMERATE-ALL(vars,exi)
where exi is e extended with X = xi
return NORMALIZE(Q(X))
function ENUMERATE-ALL(vars,e) returns a real number
if EMPTY?(vars) then return 1.0
V ←FIRST(vars)
if V is an evidence variable with value v in e
then return P(v| parents(V)) × ENUMERATE-ALL(REST(vars),e)
else return ∑v P(v| parents(V)) × ENUMERATE-ALL(REST(vars), ev)
where ev is e extended with V = v
Figure 13.11 The enumeration algorithm for exact inference in Bayes nets.

## Page 448
