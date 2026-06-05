---
chunk_id: "book-ca4fca8dd8-chunk-0854"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 854
confidence: "first-pass"
extraction_method: "structured-local"
---

516
Chapter 14
Probabilistic Reasoning over Time
tional biology (Krogh et al., 1994; Baldi et al., 1994), ﬁnancial economics (Bhar and Hamori,
2004) and other ﬁelds. There have been several extensions to the basic HMM model: for ex-
ample, the Hierarchical HMM (Fine et al., 1998) and Layered HMM (Oliver et al., 2004)
introduce structure back into the model, replacing the single state variable of HMMs.
Dynamic Bayesian networks (DBNs) can be viewed as a sparse encoding of a Markov
process and were ﬁrst used in AI by Dean and Kanazawa (1989b), Nicholson and Brady
(1992), and Kjaerulff (1992). The last work extends the HUGIN Bayes net system to ac-
commodate dynamic Bayesian networks. The book by Dean and Wellman (1991) helped
popularize DBNs and the probabilistic approach to planning and control within AI. Murphy
(2002) provides a thorough analysis of DBNs.
Dynamic Bayesian networks have become popular for modeling a variety of complex mo-
tion processes in computer vision (Huang et al., 1994; Intille and Bobick, 1999). Like HMMs,
they have found applications in speech recognition (Zweig and Russell, 1998; Livescu et al.,
2003), robot localization (Theocharous et al., 2004), and genomics (Murphy and Mian, 1999;
Li et al., 2011). Other application areas include gesture analysis (Suk et al., 2010), driver
fatigue detection (Yang et al., 2010), and urban trafﬁc modeling (Hoﬂeitner et al., 2012).
The link between HMMs and DBNs, and between the forward–backward algorithm and
Bayesian network propagation, was explicated by Smyth et al. (1997). A further uniﬁcation
with Kalman ﬁlters (and other statistical models) appears in Roweis and Ghahramani (1999).
Procedures exist for learning the parameters (Binder et al., 1997a; Ghahramani, 1998) and
structures (Friedman et al., 1998) of DBNs. Continuous-time Bayesian networks (Nodel-
man et al., 2002) are the discrete-state, continuous-time analog of DBNs, avoiding the need
to choose a particular duration for time steps.
The ﬁrst sampling algorithms for ﬁltering (also called sequential Monte Carlo methods)
were developed in the control theory community by Handschin and Mayne (1969), and the re-
sampling idea that is the core of particle ﬁltering appeared in a Russian control journal (Zarit-
skii et al., 1975). It was later reinvented in statistics as sequential importance sampling
with resampling, or SIR (Rubin, 1988; Liu and Chen, 1998), in control theory as particle ﬁl-
tering (Gordon et al., 1993; Gordon, 1994), in AI as survival of the ﬁttest (Kanazawa et al.,
1995), and in computer vision as condensation (Isard and Blake, 1996).
The paper by Kanazawa et al. (1995) includes an improvement called evidence reversal
Evidence reversal
whereby the state at time t + 1 is sampled conditional on both the state at time t and the
evidence at time t +1. This allows the evidence to inﬂuence sample generation directly and
was proved by Doucet (1997) and Liu and Chen (1998) to reduce the approximation error.
Particle ﬁltering has been applied in many areas, including tracking complex motion pat-
terns in video (Isard and Blake, 1996), predicting the stock market (de Freitas et al., 2000),
and diagnosing faults on planetary rovers (Verma et al., 2004). Since its invention, tens of
thousands of papers have been published on applications and variants of the algorithm. Scal-
able implementations on parallel hardware have become important; although one might think
it straightforward to distribute N particles across up to N processor threads, the basic algo-
rithm requires synchronized communication among threads for the resampling step (Hendeby
et al., 2010). The particle cascade algorithm (Paige et al., 2015) removes the synchroniza-
tion requirement, resulting in much faster parallel computation.
The Rao-Blackwellized particle ﬁlter is due to Doucet et al. (2000) and Murphy and
Russell (2001); its application to practical localization and mapping problems in robotics is
