---
chunk_id: "book-ca4fca8dd8-chunk-0815"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 815
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 14.3
Hidden Markov Models
491
m message at each time step using Equation (14.11). The progress of this computation is
shown in Figure 14.5(b).
At the end of the observation sequence, m1:t will contain the probability for the most
likely sequence reaching each of the ﬁnal states. One can thus easily select the ﬁnal state of
the most likely sequence overall (the state outlined in bold at step 5). In order to identify the
actual sequence, as opposed to just computing its probability, the algorithm will also need to
record, for each state, the best state that leads to it; these are indicated by the bold arrows in
Figure 14.5(b). The optimal sequence is identiﬁed by following these bold arrows backwards
from the best ﬁnal state.
The algorithm we have just described is called the Viterbi algorithm, after its inventor,
Viterbi algorithm
Andrew Viterbi. Like the ﬁltering algorithm, its time complexity is linear in t, the length of
the sequence. Unlike ﬁltering, which uses constant space, its space requirement is also linear
in t. This is because the Viterbi algorithm needs to keep the pointers that identify the best
sequence leading to each state.
One ﬁnal practical point: numerical underﬂow is a signiﬁcant issue for the Viterbi algo-
rithm. In Figure 14.5(b), the probabilities are getting smaller and smaller—and this is just a
toy example. Real applications in DNA analysis or message decoding may have thousands or
millions of steps. One possible solution is simply to normalize m at each step; this rescaling
does not affect correctness because max(cx,cy)=c · max(x,y). A second solution is to use
log probabilities everywhere and replace multiplication by addition. Again, correctness is
unaffected because the log function is monotonic, so max(logx,logy)= logmax(x,y).
14.3 Hidden Markov Models
The preceding section developed algorithms for temporal probabilistic reasoning using a gen-
eral framework that was independent of the speciﬁc form of the transition and sensor models
and independent of the nature of the state and evidence variables. In this and the next two
sections, we discuss more concrete models and applications that illustrate the power of the
basic algorithms and in some cases allow further improvements.
We begin with the hidden Markov model, or HMM. An HMM is a temporal probabilis-
Hidden Markov
model
tic model in which the state of the process is described by a single, discrete random variable.
The possible values of the variable are the possible states of the world. The umbrella example
described in the preceding section is therefore an HMM, since it has just one state variable:
Raint. What happens if you have a model with two or more state variables? You can still ﬁt
it into the HMM framework by combining the variables into a single “megavariable” whose
values are all possible tuples of values of the individual state variables. We will see that the
restricted structure of HMMs allows for a simple and elegant matrix implementation of all
the basic algorithms.6
Although HMMs require the state to be a single, discrete variable, there is no correspond-
ing restriction on the evidence variables. This is because the evidence variables are always
observed, which means that there is no need to keep track of any distribution over their val-
ues. (If a variable is not observed, it can simply be dropped from the model for that time
step.) There can be many evidence variables, both discrete and continuous.
6
The reader unfamiliar with basic operations on vectors and matrices might wish to consult Appendix A before
proceeding with this section.
