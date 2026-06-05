---
chunk_id: "book-ca4fca8dd8-chunk-1292"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1292
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 788

788
Chapter 21
Learning Probabilistic Models
 0  0.2 0.4 0.6 0.8  1  0 0.2 0.4 0.6 0.8 1
Density
 0  0.2 0.4 0.6 0.8  1  0 0.2 0.4 0.6 0.8 1
Density
 0  0.2 0.4 0.6 0.8  1  0 0.2 0.4 0.6 0.8 1
Density
(a)
(b)
(c)
Figure 21.9 Density estimation using k-nearest-neighbors, applied to the data in Fig-
ure 21.8(b), for k=3, 10, and 40 respectively. k = 3 is too spiky, 40 is too smooth, and
10 is just about right. The best value for k can be chosen by cross-validation.
Figure 21.10 Density estimation using kernels for the data in Figure 21.8(b), using Gaussian
kernels with w=0.02, 0.07, and 0.20 respectively. w=0.07 is about right.
still have the problem of choosing a suitable value for kernel width w; Figure 21.10 shows
values that are too small, just right, and too large. A good value of w can be chosen by using
cross-validation.
21.3 Learning with Hidden Variables: The EM Algorithm
The preceding section dealt with the fully observable case. Many real-world problems have
hidden variables (sometimes called latent variables), which are not observable in the data.
Latent variable
For example, medical records often include the observed symptoms, the physician’s diagno-
sis, the treatment applied, and perhaps the outcome of the treatment, but they seldom contain
a direct observation of the disease itself! (Note that the diagnosis is not the disease; it is
a causal consequence of the observed symptoms, which are in turn caused by the disease.)
One might ask, “If the disease is not observed, could we construct a model based only on
the observed variables?” The answer appears in Figure 21.11, which shows a small, ﬁctitious
diagnostic model for heart disease. There are three observable predisposing factors and three
observable symptoms (which are too depressing to name). Assume that each variable has
three possible values (e.g., none, moderate, and severe). Removing the hidden variable from
 0  0.2 0.4 0.6 0.8  1  0 0.2 0.4 0.6 0.8 1
Density
 0  0.2 0.4 0.6 0.8  1  0 0.2 0.4 0.6 0.8 1
Density
 0  0.2 0.4 0.6 0.8  1  0 0.2 0.4 0.6 0.8 1
Density
(a)
(b)
(c)

## Page 789
