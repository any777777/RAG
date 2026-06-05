---
chunk_id: "book-ca4fca8dd8-chunk-0852"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 852
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
515
can be achieved using simple, recursive algorithms whose run time is linear in the length
of the sequence.
• Three families of temporal models were studied in more depth: hidden Markov mod-
els, Kalman ﬁlters, and dynamic Bayesian networks (which include the other two as
special cases).
• Unless special assumptions are made, as in Kalman ﬁlters, exact inference with many
state variables is intractable. In practice, the particle ﬁltering algorithm and its descen-
dants are an effective family of approximation algorithms.
Bibliographical and Historical Notes
Many of the basic ideas for estimating the state of dynamical systems came from the mathe-
matician C. F. Gauss (1809), who formulated a deterministic least-squares algorithm for the
problem of estimating orbits from astronomical observations. A. A. Markov (1913) devel-
oped what was later called the Markov assumption in his analysis of stochastic processes;
he estimated a ﬁrst-order Markov chain on letters from the text of Eugene Onegin. The gen-
eral theory of Markov chains and their mixing times is covered by Levin et al. (2008).
Signiﬁcant classiﬁed work on ﬁltering was done during World War II by Wiener (1942)
for continuous-time processes and by Kolmogorov (1941) for discrete-time processes. Al-
though this work led to important technological developments over the next 20 years, its
use of a frequency-domain representation made many calculations quite cumbersome. Direct
state-space modeling of the stochastic process turned out to be simpler, as shown by Peter
Swerling (1959) and Rudolf Kalman (1960). The latter paper described what is now known
as the Kalman ﬁlter for forward inference in linear systems with Gaussian noise; Kalman’s
results had, however, been obtained previously by the Danish astronomer Thorvold Thiele
(1880) and by the Russian physicist Ruslan Stratonovich (1959). After a visit to NASA
Ames Research Center in 1960, Kalman saw the applicability of the method to the tracking
of rocket trajectories, and the ﬁlter was later implemented for the Apollo missions.
Key results on smoothing were derived by Rauch et al. (1965), and the impressively
named Rauch–Tung–Striebel smoother is still a standard technique today. Many early results
are gathered in Gelb (1974). Bar-Shalom and Fortmann (1988) give a more modern treatment
with a Bayesian ﬂavor, as well as many references to the vast literature on the subject. Chat-
ﬁeld (1989) and Box et al. (2016) cover the control theory approach to time series analysis.
The hidden Markov model and associated algorithms for inference and learning, includ-
ing the forward–backward algorithm, were developed by Baum and Petrie (1966). The Viterbi
algorithm ﬁrst appeared in (Viterbi, 1967). Similar ideas also appeared independently in the
Kalman ﬁltering community (Rauch et al., 1965).
The forward–backward algorithm was one of the main precursors of the general formu-
lation of the EM algorithm (Dempster et al., 1977); see also Chapter 21. Constant-space
smoothing appears in Binder et al. (1997b), as does the divide-and-conquer algorithm devel-
oped in Exercise 14.ISLE. Constant-time ﬁxed-lag smoothing for HMMs ﬁrst appeared in
Russell and Norvig (2003).
HMMs have found many applications in language processing (Charniak, 1993), speech
recognition (Rabiner and Juang, 1993), machine translation (Och and Ney, 2003), computa-
