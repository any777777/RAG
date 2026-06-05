---
chunk_id: "book-ca4fca8dd8-chunk-1103"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1103
confidence: "first-pass"
extraction_method: "structured-local"
---

660
Chapter 18
Probabilistic Programming
function GENERATE-IMAGE() returns an image with some letters
letters←GENERATE-LETTERS(10)
return RENDER-NOISY-IMAGE(letters,32,128)
function GENERATE-LETTERS(λ) returns a vector of letters
n ∼Poisson(λ)
letters←[]
for i = 1 to n do
letters[i] ∼UniformChoice({a,b,c,···})
return letters
function RENDER-NOISY-IMAGE(letters,width,height) returns a noisy image of the letters
clean image←RENDER(letters,width,height,text top = 10,text left = 10)
noisy image←[]
noise variance ∼UniformReal(0.1, 1)
for row = 1 to width do
for col = 1 to height do
noisy image[row,col] ∼N(clean image[row,col],noise variance)
return noisy image
Figure 18.11 Generative program for an open-universe probability model for optical charac-
ter recognition. The generative program produces degraded images containing sequences of
letters by generating each sequence, rendering it into a 2D image, and incorporating additive
noise at each pixel.
18.4 Programs as Probability Models
Many probabilistic programming languages have been built on the insight that probability
models can be deﬁned using executable code in any programming language that incorporates
a source of randomness. For such models, the possible worlds are execution traces and the
probability of any such trace is the probability of the random choices required for that trace
to happen. PPLs created in this way inherit all of the expressive power of the underlying lan-
guage, including complex data structures, recursion, and, in some cases, higher-order func-
tions. Many PPLs are in fact computationally universal: they can represent any probability
distribution that can be sampled from by a probabilistic Turing machine that halts.
18.4.1 Example: Reading text
We illustrate this approach to probabilistic modeling and inference via the problem of writing
a program that reads degraded text. These kinds of models can be built for reading text that
has been smudged or blurred due to water damage, or spotted due to aging of the paper on
which it is printed. They can also be built for breaking some kinds of CAPTCHAs.
Figure 18.11 shows a generative program containing two components: (i) a way to gen-
erate a sequence of letters; and (ii) a way to generate a noisy, blurry rendering of these letters
using an off-the-shelf graphics library. Figure 18.12(top) shows example images generated
by invoking GENERATE-IMAGE nine times.

## Page 661
