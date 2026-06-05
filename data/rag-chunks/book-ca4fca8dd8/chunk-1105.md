---
chunk_id: "book-ca4fca8dd8-chunk-1105"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1105
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 662

662
Chapter 18
Probabilistic Programming
Figure 18.13 Noisy input image (top) and inference results (bottom) produced by three runs,
each of 25 MCMC iterations, with the model from Figure 18.11. Note that the inference
process correctly identiﬁes the sequence of letters.
Figure 18.14 Top: extremely noisy input image. Bottom left: with three inference results
from 25 MCMC iterations with the independent-letter model from Figure 18.11. Bottom
right: three inference results with the letter bigram model from Figure 18.15. Both mod-
els exhibit ambiguity in the results, but the latter model’s results reﬂect prior knowledge of
plausible letter sequences.
function GENERATE-MARKOV-LETTERS(λ) returns a vector of letters
n ∼Poisson(λ)
letters←[]
letter probs←MARKOV-INITIAL()
for i = 1 to n do
letters[i] ∼Categorical(letter probs)
letter probs←MARKOV-TRANSITION(letters[i])
return letters
Figure 18.15 Generative program for an improved optical character recognition model that
generates letters according to a letter bigram model whose pairwise letter frequencies are
estimated from a list of English words.

## Page 663
