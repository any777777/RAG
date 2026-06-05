---
chunk_id: "book-ca4fca8dd8-chunk-1265"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1265
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
767
allow it to outperform linear regression, neural nets, and decision trees. Most impressively,
King et al. (2009) endowed a robot with the ability to perform molecular biology experiments
and extended ILP techniques to include experiment design, thereby creating an autonomous
scientist that actually discovered new knowledge about the functional genomics of yeast. For
all these examples it appears that the ability both to represent relations and to use background
knowledge contribute to ILP’s high performance. The fact that the rules found by ILP can be
interpreted by humans contributes to the acceptance of these techniques in biology journals
rather than just computer science journals.
ILP has made contributions to other sciences besides biology. One of the most impor-
tant is natural language processing, where ILP has been used to extract complex relational
information from text.
Summary
This chapter has investigated various ways in which prior knowledge can help an agent to
learn from new experiences. Because much prior knowledge is expressed in terms of rela-
tional models rather than attribute-based models, we have also covered systems that allow
learning of relational models. The important points are:
• The use of prior knowledge in learning leads to a picture of cumulative learning, in
which learning agents improve their learning ability as they acquire more knowledge.
• Prior knowledge helps learning by eliminating otherwise consistent hypotheses and by
“ﬁlling in” the explanation of examples, thereby allowing for shorter hypotheses. These
contributions often result in faster learning from fewer examples.
• Understanding the different logical roles played by prior knowledge, as expressed by
entailment constraints, helps to deﬁne a variety of learning techniques.
• Explanation-based learning (EBL) extracts general rules from single examples by ex-
plaining the examples and generalizing the explanation. It provides a deductive method
for turning ﬁrst-principles knowledge into useful, efﬁcient, special-purpose expertise.
• Relevance-based learning (RBL) uses prior knowledge in the form of determinations
to identify the relevant attributes, thereby generating a reduced hypothesis space and
speeding up learning. RBL also allows deductive generalizations from single examples.
• Knowledge-based inductive learning (KBIL) ﬁnds inductive hypotheses that explain
sets of observations with the help of background knowledge.
• Inductive logic programming (ILP) techniques perform KBIL on knowledge that is
expressed in ﬁrst-order logic. ILP methods can learn relational knowledge that is not
expressible in attribute-based systems.
• ILP can be done with a top-down approach of reﬁning a very general rule or through a
bottom-up approach of inverting the deductive process.
• ILP methods naturally generate new predicates with which concise new theories can be
expressed and show promise as general-purpose scientiﬁc theory formation systems.
