---
chunk_id: "book-ca4fca8dd8-chunk-1213"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1213
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.9
Developing Machine Learning Systems
731
Tests for Features and Data
(1) Feature expectations are captured in a schema. (2) All features are beneﬁcial. (3) No fea-
ture’s cost is too much. (4) Features adhere to meta-level requirements. (5) The data pipeline
has appropriate privacy controls. (6) New features can be added quickly. (7) All input feature
code is tested.
Tests for Model Development
(1) Every model speciﬁcation undergoes a code review. (2) Every model is checked in to a
repository. (3) Ofﬂine proxy metrics correlate with actual metrics (4) All hyperparameters
have been tuned. (5) The impact of model staleness is known. (6) A simpler model is not
better. (7) Model quality is sufﬁcient on all important data slices. The model has been tested
for considerations of inclusion.
Tests for Machine Learning Infrastructure
(1) Training is reproducible. (2) Model speciﬁcation code is unit tested. (3) The full ML
pipeline is integration tested. (4) Model quality is validated before attempting to serve it.
(5) The model allows debugging by observing the step-by-step computation of training or
inference on a single example. (6) Models are tested via a canary process before they enter
production serving environments. (7) Models can be quickly and safely rolled back to a pre-
vious serving version.
Monitoring Tests for Machine Learning
(1) Dependency changes result in notiﬁcation. (2) Data invariants hold in training and serv-
ing inputs. (3) Training and serving features compute the same values. (4) Models are not
too stale. (5) The model is numerically stable. (6) The model has not experienced regres-
sions in training speed, serving latency, throughput, or RAM usage. (7) The model has not
experienced a regression in prediction quality on served data.
Figure 19.28 A set of criteria to see how well you are doing at deploying your machine
learning model with sufﬁcient tests. Abridged from Breck et al. (2016), who also provide a
scoring metric.
been tested in actual use. Different systems have different requirements for freshness: some
problems beneﬁt from a new model every day, or even every hour, while other problems can
keep the same model for months. If you are deploying a new model every hour, it will be
impractical to run a heavy test suite and a manual review process for each update. You will
need to automate the testing and release process so that small changes can be automatically
approved, but larger changes trigger appropriate review. You can consider the tradeoff be-
tween an online model where new data incrementally modiﬁes the existing model, versus an
ofﬂine model where each new release requires building a new model from scratch.
It it is not just that the data will be changing—for example, new words will be used in
spam email messages. It is also that the entire data schema may change—you might start
out classifying spam email, and need to adapt to classify spam text messages, spam voice
messages, spam videos, etc. Figure 19.28 gives a general rubric to guide the practitioner in
choosing the appropriate level of testing and monitoring.
