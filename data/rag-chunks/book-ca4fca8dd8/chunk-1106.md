---
chunk_id: "book-ca4fca8dd8-chunk-1106"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1106
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 18.4
Programs as Probability Models
663
18.4.3 Inference results
Let’s apply this model to interpret images of letters that have been degraded with additive
noise. Figure 18.13 shows a degraded image, along with results from three independent
MCMC runs. For each run, we show a rendering of the letters contained in the trace after
stopping the Markov chain. In all three cases the result is the letter sequence uncertainty,
suggesting that the posterior distribution is highly concentrated on the correct interpretation.
Now let’s degrade the text further, blurring it enough that it is difﬁcult for people to read.
Figure 18.14 shows the inference results on this more challenging input. This time, although
MCMC inference appears to have converged on (what we know to be) the correct number
of letters, the ﬁrst letter is misidentiﬁed as a q and there is uncertainty about ﬁve of the ten
following letters.
At this point, there are many possible ways to interpret the results. It could be that MCMC
inference has mixed well and the results are a good reﬂection of the true posterior given the
model and the image; in that case, the uncertainty in some of the letters and the error in the
ﬁrst letter are unavoidable. To get better results, we might need to improve the text model
or reduce the noise level. It could also be that MCMC inference has not mixed properly: if
we ran 300 chains for 25 thousand or 25 million iterations, we might ﬁnd a quite different
distribution of results, perhaps indicating that the ﬁrst letter is probably u rather than q.
Running more inference could be costly in terms of dollars and waiting time. Moreover,
there is no foolproof test for convergence of Monte Carlo inference methods. We could
try to improve the inference algorithm, perhaps by designing a better proposal distribution
for MCMC or using bottom-up clues from the image to suggest better initial hypotheses.
These improvements require additional thought, implementation, and debugging. The third
alternative is to improve the model. For example, we could incorporate knowledge about
English words, such as the probabilities of letter pairs. We now consider this option.
18.4.4 Improving the generative program to incorporate a Markov model
Probabilistic programming languages are modular in a way that makes it easy to explore
improvements to the underlying model. Figure 18.15 shows the generative program for an
improved model that generates letters sequentially rather than independently. This generative
program uses a Markov model that draws each letter given the previous letter, with transition
probabilities estimated from a reference list of English words.
Figure 18.12 shows twelve sampled images produced by this generative program. Notice
that the letter sequences are signiﬁcantly more English-like than those generated from the
program in Figure 18.11. The right-hand panel in Figure 18.14 shows inference results from
this Markov model applied to the high-noise image. The interpretations more closely match
the generating trace, though there is still some uncertainty.
18.4.5 Inference in generative programs
As with OUPMs, exact inference in generative programs is usually prohibitively expensive
or impossible. On the other hand, it is easy to see how to perform rejection sampling: run the
program, keep just the traces that agree with the evidence, and count the different query an-
swers found in those traces. Likelihood weighting is also straightforward: for each generated
trace, keep track of the weight of the trace by multiplying all the probabilities of the values
observed along the way.
