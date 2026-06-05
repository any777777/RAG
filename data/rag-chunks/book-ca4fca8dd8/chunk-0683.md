---
chunk_id: "book-ca4fca8dd8-chunk-0683"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 683
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 12.2
Basic Probability Notation
409
ambiguity is possible, it is common to use a value by itself to stand for the proposition that a
particular variable has that value; thus, sun can stand for Weather=sun.3
The preceding examples all have ﬁnite ranges. Variables can have inﬁnite ranges, too—
either discrete (like the integers) or continuous (like the reals). For any variable with an
ordered range, inequalities are also allowed, such as NumberOfAtomsInUniverse ≥1070.
Finally, we can combine these sorts of elementary propositions (including the abbreviated
forms for Boolean variables) by using the connectives of propositional logic. For example,
we can express “The probability that the patient has a cavity, given that she is a teenager with
no toothache, is 0.1” as follows:
P(cavity|¬toothache∧teen) = 0.1.
In probability notation, it is also common to use a comma for conjunction, so we could write
P(cavity|¬toothache,teen).
Sometimes we will want to talk about the probabilities of all the possible values of a random
variable. We could write:
P(Weather=sun) = 0.6
P(Weather=rain) = 0.1
P(Weather=cloud) = 0.29
P(Weather=snow) = 0.01,
but as an abbreviation we will allow
P(Weather)=⟨0.6,0.1,0.29,0.01⟩,
where the bold P indicates that the result is a vector of numbers, and where we assume
a predeﬁned ordering ⟨sun,rain,cloud,snow⟩on the range of Weather. We say that the P
statement deﬁnes a probability distribution for the random variable Weather—that is, an
Probability
distribution
assignment of a probability for each possible value of the random variable. (In this case, with
a ﬁnite, discrete range, the distribution is called a categorical distribution.) The P notation
Categorical
distribution
is also used for conditional distributions: P(X |Y) gives the values of P(X =xi |Y =yj) for
each possible i, j pair.
For continuous variables, it is not possible to write out the entire distribution as a vector,
because there are inﬁnitely many values. Instead, we can deﬁne the probability that a random
variable takes on some value x as a parameterized function of x, usually called a probability
density function. For example, the sentence
Probability density
function
P(NoonTemp=x) = Uniform(x;18C,26C)
expresses the belief that the temperature at noon is distributed uniformly between 18 and 26
degrees Celsius.
Probability density functions (sometimes called pdfs) differ in meaning from discrete
distributions. Saying that the probability density is uniform from 18C to 26C means that
there is a 100% chance that the temperature will fall somewhere in that 8C-wide region and
a 50% chance that it will fall in any 4C-wide sub-region, and so on. We write the probability
density for a continuous random variable X at value x as P(X =x) or just P(x); the intuitive
3
These conventions taken together lead to a potential ambiguity in notation when summing over values of a
Boolean variable: P(a) is the probability that A is true, whereas in the expression ∑a P(a) it just refers to the
probability of one of the values a of A.
