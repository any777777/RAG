---
chunk_id: "book-ca4fca8dd8-chunk-0697"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 697
confidence: "first-pass"
extraction_method: "structured-local"
---

418
Chapter 12
Quantifying Uncertainty
probability that any patient has meningitis is 1/50,000, and the prior probability that any
patient has a stiff neck is 1%. Letting s be the proposition that the patient has a stiff neck and
m be the proposition that the patient has meningitis, we have
P(s|m) = 0.7
P(m) = 1/50000
P(s) = 0.01
P(m|s) = P(s|m)P(m)
P(s)
= 0.7×1/50000
0.01
= 0.0014.
(12.14)
That is, we expect only 0.14% of patients with a stiff neck to have meningitis. Notice that
even though a stiff neck is quite strongly indicated by meningitis (with probability 0.7), the
probability of meningitis in patients with stiff necks remains small. This is because the prior
probability of stiff necks (from any cause) is much higher than the prior for meningitis.
Section 12.3 illustrated a process by which one can avoid assessing the prior probability
of the evidence (here, P(s)) by instead computing a posterior probability for each value of the
query variable (here, m and ¬m) and then normalizing the results. The same process can be
applied when using Bayes’ rule. We have
P(M |s) = α⟨P(s|m)P(m),P(s|¬m)P(¬m)⟩.
Thus, to use this approach we need to estimate P(s|¬m) instead of P(s). There is no free
lunch—sometimes this is easier, sometimes it is harder. The general form of Bayes’ rule with
normalization is
P(Y |X) = αP(X |Y)P(Y),
(12.15)
where α is the normalization constant needed to make the entries in P(Y |X) sum to 1.
One obvious question to ask about Bayes’ rule is why one might have available the con-
ditional probability in one direction, but not the other. In the meningitis domain, perhaps the
doctor knows that a stiff neck implies meningitis in 1 out of 5000 cases; that is, the doctor has
quantitative information in the diagnostic direction from symptoms to causes. Such a doctor
has no need to use Bayes’ rule.
Unfortunately, diagnostic knowledge is often more fragile than causal knowledge. If there
▶
is a sudden epidemic of meningitis, the unconditional probability of meningitis, P(m), will
go up. The doctor who derived the diagnostic probability P(m|s) directly from statistical
observation of patients before the epidemic will have no idea how to update the value, but
the doctor who computes P(m|s) from the other three values will see that P(m|s) should go
up proportionately with P(m). Most important, the causal information P(s|m) is unaffected
by the epidemic, because it simply reﬂects the way meningitis works. The use of this kind
of direct causal or model-based knowledge provides the crucial robustness needed to make
probabilistic systems feasible in the real world.
12.5.2 Using Bayes’ rule: Combining evidence
We have seen that Bayes’ rule can be useful for answering probabilistic queries conditioned
on one piece of evidence—for example, the stiff neck. In particular, we have argued that
probabilistic information is often available in the form P(effect|cause). What happens when
we have two or more pieces of evidence? For example, what can a dentist conclude if her
