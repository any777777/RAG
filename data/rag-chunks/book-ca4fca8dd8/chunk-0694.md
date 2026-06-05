---
chunk_id: "book-ca4fca8dd8-chunk-0694"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 694
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 416

416
Chapter 12
Quantifying Uncertainty
Weather
Toothache
Catch
Cavity
decomposes
      into
Weather
Toothache
Catch
Cavity
decomposes
       into
Coin1
Coinn
Coin1
Coinn
(a)
(b)
Figure 12.4 Two examples of factoring a large joint distribution into smaller distributions,
using absolute independence. (a) Weather and dental problems are independent. (b) Coin
ﬂips are independent.
does not inﬂuence the dental variables. Therefore, the following assertion seems reasonable:
P(cloud|toothache,catch,cavity) = P(cloud).
(12.10)
From this, we can deduce
P(toothache,catch,cavity,cloud) = P(cloud)P(toothache,catch,cavity).
A similar equation exists for every entry in P(Toothache,Catch,Cavity,Weather). In fact, we
can write the general equation
P(Toothache,Catch,Cavity,Weather) = P(Toothache,Catch,Cavity)P(Weather).
Thus, the 32-element table for four variables can be constructed from one 8-element table
and one 4-element table. This decomposition is illustrated schematically in Figure 12.4(a).
The property we used in Equation (12.10) is called independence (also marginal inde-
Independence
pendence and absolute independence). In particular, the weather is independent of one’s
dental problems. Independence between propositions a and b can be written as
P(a|b)=P(a)
or
P(b|a)=P(b)
or
P(a∧b)=P(a)P(b).
(12.11)
All these forms are equivalent (Exercise 12.INDI). Independence between variables X and Y
can be written as follows (again, these are all equivalent):
P(X |Y)=P(X)
or
P(Y |X)=P(Y)
or
P(X,Y)=P(X)P(Y).
Independence assertions are usually based on knowledge of the domain. As the toothache–
weather example illustrates, they can dramatically reduce the amount of information nec-
essary to specify the full joint distribution. If the complete set of variables can be divided
into independent subsets, then the full joint distribution can be factored into separate joint
distributions on those subsets. For example, the full joint distribution on the outcome of n in-
dependent coin ﬂips, P(C1,...,Cn), has 2n entries, but it can be represented as the product of
n single-variable distributions P(Ci). In a more practical vein, the independence of dentistry
and meteorology is a good thing, because otherwise the practice of dentistry might require
intimate knowledge of meteorology, and vice versa.

## Page 417
