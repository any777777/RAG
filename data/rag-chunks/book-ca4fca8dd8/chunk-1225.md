---
chunk_id: "book-ca4fca8dd8-chunk-1225"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1225
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
737
of doing data science. Tukey (1977) introduced exploratory data analysis, and Gelman
(2004) gives an updated view of the process. Bien et al. (2011) describe the process of
choosing prototypes for interpretability, and Kim et al. (2017) show how to ﬁnd critics that
are maximally distant from the prototypes using a metric called maximum mean discrepancy.
Wattenberg et al. (2016) describe how to use t-SNE. To get a comprehensive view of how
well your deployed machine learning system is doing, Breck et al. (2016) offer a checklist
of 28 tests that you can apply to get an overall ML test score. Riley (2019) describes three
common pitfalls of ML development.
Banko and Brill (2001), Halevy et al. (2009), and Gandomi and Haider (2015) discuss
the advantages of using the large amounts of data that are now available. Lyman and Varian
(2003) estimated that about 5 exabytes (5 × 1018 bytes) of data was produced in 2002, and
that the rate of production is doubling every 3 years; Hilbert and Lopez (2011) estimated
2 × 1021 bytes for 2007, indicating an acceleration. Guyon and Elisseeff (2003) discuss the
problem of feature selection with large data sets.
Doshi-Velez and Kim (2017) propose a framework for interpretable machine learning
or explainable AI (XAI). Miller et al. (2017) point out that there are two kinds of expla-
nations, one for the designers of an AI system and one for the users, and we need to be
clear what we are aiming for. The LIME system (Ribeiro et al., 2016) builds interpretable
linear models that approximate whatever machine learning system you have. A similar sys-
tem, SHAP (Lundberg and Lee, 2018) (Shapley Additive exPlanations), uses the notion of a
Shapley value (page 618) to determine the contribution of each feature.
The idea that we could apply machine learning to the task of solving machine learning
problems is a tantalizing one. Thrun and Pratt (2012) give an early overview of the ﬁeld
in an edited collection titled Learning to Learn. Recently the ﬁeld has adopted the name
automated machine learning (AutoML); Hutter et al. (2019) give an overview.
Automated machine
learning (AutoML)
Kanter and Veeramachaneni (2015) describe a system for doing automated feature selec-
tion. Bergstra and Bengio (2012) describe a system for searching the space of hyperparam-
eters, as do Thornton et al. (2013) and Berm´udez-Chac´on et al. (2015). Wong et al. (2019)
show how transfer learning can speed up AutoML for deep learning models. Competitions
have been organized to see which systems are best at AutoML tasks (Guyon et al., 2015).
(Steinruecken et al., 2019) describe a system called the Automatic Statistician: you give it
some data and it writes a report, mixing text, charts, and calculations. The major cloud com-
puting providers have included AutoML as part of their offerings. Some researchers prefer
the term metalearning: for example, the MAML (Model-Agnostic Meta-Learning) system
(Finn et al., 2017) works with any model that can be trained by gradient descent; it trains a
core model so that it will be easy to ﬁne-tune the model with new data on new tasks.
Despite all this work, we still don’t have a complete system for automatically solving
machine learning problems. To do that with supervised machine learning we would need to
start with a data set of (xj,yj) examples. Here the input xj is a speciﬁcation of the problem,
in the form that a problem is initially encountered: a vague description of the goals, and
some data to work with, perhaps with a vague plan for how to acquire more data. The output
yi would be a complete running machine learning program, along with a methodology for
maintaining the program: gathering more data, cleaning it, testing and monitoring the system,
etc. One would expect we would need a data set of thousands of such examples. But no such
data set exists, so existing AutoML systems are limited in what they can accomplish.
