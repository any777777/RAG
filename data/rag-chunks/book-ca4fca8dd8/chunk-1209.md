---
chunk_id: "book-ca4fca8dd8-chunk-1209"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1209
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.9
Developing Machine Learning Systems
729
A machine learning system is still a piece of software, and you can build trust with all the
typical tools for verifying and validating any software system:
• Source control: Systems for version control, build, and bug/issue tracking.
• Testing: Unit tests for all the components covering simple canonical cases as well
as tricky adversarial cases, fuzz tests (where random inputs are generated), regression
tests, load tests, and system integration tests: these are all important for any software
system. For machine learning, we also have tests on the training, validation, and test
data sets.
• Review: Code walk-throughs and reviews, privacy reviews, fairness reviews (see Sec-
tion 28.3.3), and other legal compliance reviews.
• Monitoring: Dashboards and alerts to make sure that the system is up and running and
is continuing to performing at a high level of accuracy.
• Accountability: What happens when the system is wrong? What is the process for
complaining about or appealing the system’s decision? How can we track who was
responsible for the error? Society expects (but doesn’t always get) accountability for
important decisions made by banks, politicians, and the law, and they should expect
accountability from software systems including machine learning systems.
In addition, there are some factors that are especially important for machine learning systems,
as we shall detail below.
Interpretability: We say that a machine learning model is interpretable if you can in-
Interpretability
spect the actual model and understand why it got a particular answer for a given input, and
how the answer would change when the input changes.18 Decision tree models are consid-
ered to be highly interpretable; we can understand that following the path Patrons=Full and
WaitEstimate=0–10 in a decision tree leads to a decision to wait. A decision tree is inter-
pretable for two reasons. First, we humans have experience in understanding IF/THEN rules.
(In contrast, it is very difﬁcult for humans to get an intuitive understanding of the result of a
matrix multiply followed by an activation function, as is done in some neural network mod-
els.) Second, the decision tree was in a sense constructed to be interpretable—the root of the
tree was chosen to be the attribute with the highest information gain.
Linear regression models are also considered to be interpretable; we can examine a model
for predicting the rent on an apartment and see that for each bedroom added, the rent increases
by $500, according to the model. This idea of “If I change x, how will the output change?” is
at the core of interpretability. Of course, correlation is not causation, so interpretable models
are answering what is the case, but not necessarily why it is the case.
Explainability: An explainable model is one that can help you understand “why was this
Explainability
output produced for this input?” In our terminology, interpretability derives from inspecting
the actual model, whereas explainability can be provided by a separate process. That is, the
model itself can be a hard-to-understand black box, but an explanation module can summarize
what the model does. For a neural network image-recognition system that classiﬁes a picture
as dog, if we tried to interpret the model directly, the best we could come away with would be
something like “after processing the convolutional layers, the activation for the dog output in
the softmax layer was higher than any other class.” That’s not a very compelling argument.
18 This terminology is not universally accepted; some authors use “interpretable” and “explainable” as synonyms,
both referring to reaching some kind of understanding of a model.
