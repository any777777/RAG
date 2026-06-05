---
chunk_id: "book-ca4fca8dd8-chunk-1201"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1201
confidence: "first-pass"
extraction_method: "structured-local"
---

724
Chapter 19
Learning from Examples
If you deploy a system to users, your users will provide feedback—perhaps by clicking
on one item and ignoring the others. You will need a strategy for dealing with this data.
That involves a review with privacy experts (see Section 28.3.2) to make sure that you get
the proper permission for the data you collect, and that you have processes for insuring the
integrity of the user’s data, and that they understand what you will do with it. You also need
to ensure that your processes are fair and unbiased (see Section 28.3.3). If there is data that
you feel is too sensitive to collect but that would be useful for a machine learning model,
consider a federated learning approach where the data stays on the user’s device, but model
parameters are shared in a way that does not reveal private data.
It is good practice to maintain data provenance for all your data. For each column in
Data provenance
your data set, you should know the exact deﬁnition, where the data come from, what the
possible values are, and who has worked on it. Were there periods of time in which a data
feed was interrupted? Did the deﬁnition of some data source evolve over time? You’ll need
to know this if you want to compare results across time periods.
This is particularly true if you are relying on data that are produced by someone else—
their needs and yours might diverge, and they might end up changing the way the data are
produced, or might stop updating it all together. You need to monitor your data feeds to catch
this. Having a reliable, ﬂexible, secure, data-handling pipeline is more critical to success than
the exact details of the machine learning algorithm. Provenance is also important for legal
reasons, such as compliance with privacy law.
For any task there will be questions about the data: Is this the right data for my task?
Does it capture enough of the right inputs to give us a chance of learning a model? Does it
contain the outputs I want to predict? If not, can I build an unsupervised model? Or can I
label a portion of the data and then do semisupervised learning? Is it relevant data? It is great
to have 14 million photos, but if all your users are specialists interested in a speciﬁc topic,
then a general database won’t help—you’ll need to collect photos on the speciﬁc topic. How
much training data is enough? (Do I need to collect more data? Can I discard some data to
make computation faster?) The best way to answer this is to reason by analogy to a similar
project with known training set size.
Once you get started you can draw a learning curve (see Figure 19.7) to see if more data
will help, or if learning has already plateaued. There are endless ad hoc, unjustiﬁed rules of
thumb for the number of training examples you’ll need: millions for hard problems; thou-
sands for average problems; hundreds or thousands for each class in a classiﬁcation problem;
10 times more examples than parameters of the model; 10 times more examples than input
features; O(d logd) examples for d input features; more examples for nonlinear models than
for linear models; more examples if greater accuracy is required; fewer examples if you use
regularization; enough examples to achieve the statistical power necessary to reject the null
hypothesis in classiﬁcation. All these rules come with caveats—as does the sensible rule that
suggests trying what has worked in the past for similar problems.
You should think defensively about your data. Could there be data entry errors? What can
be done with missing data ﬁelds? If you collect data from your customers (or other people)
could some of the people be adversaries out to game the system? Are there spelling errors
or inconsistent terminology in text data? (For example, do “Apple,” “AAPL,” and “Apple
Inc.” all refer to the same company?) You will need a process to catch and correct all these
potential sources of data error.
