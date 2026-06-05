---
chunk_id: "book-ca4fca8dd8-chunk-1215"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1215
confidence: "first-pass"
extraction_method: "structured-local"
---

732
Chapter 19
Learning from Examples
Summary
This chapter introduced machine learning, and focused on supervised learning from exam-
ples. The main points were:
• Learning takes many forms, depending on the nature of the agent, the component to be
improved, and the available feedback.
• If the available feedback provides the correct answer for example inputs, then the learn-
ing problem is called supervised learning. The task is to learn a function y = h(x).
Learning a function whose output is a continuous or ordered value (like weight) is
called regression; learning a function with a small number of possible output categories
is called classiﬁcation;
• We want to learn a function that not only agrees with the data but also is likely to agree
with future data. We need to balance agreement with the data against simplicity of the
hypothesis.
• Decision trees can represent all Boolean functions. The information-gain heuristic
provides an efﬁcient method for ﬁnding a simple, consistent decision tree.
• The performance of a learning algorithm can be visualized by a learning curve, which
shows the prediction accuracy on the test set as a function of the training set size.
• When there are multiple models to choose from, model selection can pick good values
of hyperparameters, as conﬁrmed by cross-validation on validation data. Once the
hyperparameter values are chosen, we build our best model using all the training data.
• Sometimes not all errors are equal. A loss function tells us how bad each error is; the
goal is then to minimize loss over a validation set.
• Computational learning theory analyzes the sample complexity and computational
complexity of inductive learning. There is a tradeoff between the expressiveness of the
hypothesis space and the ease of learning.
• Linear regression is a widely used model. The optimal parameters of a linear regres-
sion model can be calculated exactly, or can be found by gradient descent search, which
is a technique that can be applied to models that do not have a closed-form solution.
• A linear classiﬁer with a hard threshold—also known as a perceptron—can be trained
by a simple weight update rule to ﬁt data that are linearly separable. In other cases,
the rule fails to converge.
• Logistic regression replaces the perceptron’s hard threshold with a soft threshold de-
ﬁned by a logistic function. Gradient descent works well even for noisy data that are
not linearly separable.
• Nonparametric models use all the data to make each prediction, rather than trying to
summarize the data with a few parameters. Examples include nearest neighbors and
locally weighted regression.
• Support vector machines ﬁnd linear separators with maximum margin to improve
the generalization performance of the classiﬁer. Kernel methods implicitly transform
the input data into a high-dimensional space where a linear separator may exist, even if
the original data are nonseparable.
