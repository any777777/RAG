---
chunk_id: "book-ca4fca8dd8-chunk-0775"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 775
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 13.5
Causal Networks
467
The network’s structure and conditional probabilities remain ﬁxed throughout the com-
putation, so there is an opportunity to compile the network into model-speciﬁc inference code
that carries out just the inference computations needed for that speciﬁc network. (In case this
sounds familiar, it is the same idea used in the compilation of logic programs in Chapter 9.)
For example, suppose we want to Gibbs-sample the Earthquake variable in the burglary net-
work of Figure 13.2. According to the GIBBS-ASK algorithm in Figure 13.20, we need to
perform the following computation:
set the value of Earthquake in x by sampling from P(Earthquake|mb(Earthquake))
where the latter distribution is computed according to Equation (13.10), repeated here:
P(xi |mb(Xi)) = αP(xi | parents(Xi))
∏
Yj∈Children(Xi)
P(yj | parents(Yj)).
This computation, in turn, requires looking up the parents and children of Earthquake in
the Bayes net structure; looking up their current values; using those values to index into
the corresponding CPTs (which also have to be found from the Bayes net); and multiplying
together all the appropriate rows from those CPTs to form a new distribution from which to
sample. Finally, as noted on page 454, the sampling step itself has to construct the cumulative
version of the discrete distribution and then ﬁnd the value therein that corresponds to a random
number sampled from [0,1].
If, instead, we compile the network, we obtain model-speciﬁc sampling code for the
Earthquake variable that looks like this:
r←a uniform random sample from [0,1]
if Alarm= true
then if Burglary= true
then return [r < 0.0020212]
else return [r < 0.36755]
else if Burglary= true
then return [r < 0.0016672]
else return [r < 0.0014222]
Here, Bayes net variables Alarm, Burglary, and so on become ordinary program variables
with values that comprise the current state of the Markov chain. The numerical threshold
expressions evaluate to true or false and represent the precomputed Gibbs distributions for
each combination of values in the Markov blanket of Earthquake. The code is not especially
pretty—typically, it will be roughly as large as the Bayes net itself—but it is incredibly efﬁ-
cient. Compared to GIBBS-ASK, the compiled code will typically be 2–3 orders of magnitude
faster. It can perform tens of millions of sampling steps per second on an ordinary laptop,
and its speed is limited largely by the cost of generating random numbers.
13.5 Causal Networks
We have discussed several advantages of keeping node ordering in Bayes nets compatible
with the direction of causation. In particular, we noted the ease with which conditional prob-
abilities can be assessed if such ordering is maintained, as well as the compactness of the
resultant network structure. We noted however that, in principle, any node ordering permits
