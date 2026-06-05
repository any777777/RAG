---
chunk_id: "book-ca4fca8dd8-chunk-1503"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1503
confidence: "first-pass"
extraction_method: "structured-local"
---

906
Chapter 24
Natural Language Processing
Durme and Pasca (2008). Freitag and McCallum (2000) discuss HMMs for Information
Extraction. Conditional random ﬁelds have also been used for this task (Lafferty et al., 2001;
McCallum, 2003); a tutorial with practical guidance is given by Sutton and McCallum (2007).
Sarawagi (2007) gives a comprehensive survey.
Two early inﬂuential approaches to automated knowledge engineering for NLP were by
Riloff (1993), who showed that an automatically constructed dictionary performed almost
as well as a carefully handcrafted domain-speciﬁc dictionary, and by Yarowsky (1995), who
showed that the task of word sense classiﬁcation could be accomplished through unsupervised
training on a corpus of unlabeled text with accuracy as good as supervised methods.
The idea of simultaneously extracting templates and examples from a handful of labeled
examples was developed independently and simultaneously by Blum and Mitchell (1998),
who called it cotraining, and by Brin (1998), who called it DIPRE (Dual Iterative Pattern
Relation Extraction). You can see why the term cotraining has stuck. Similar early work,
under the name of bootstrapping, was done by Jones et al. (1999). The method was advanced
by the QXTRACT (Agichtein and Gravano, 2003) and KNOWITALL (Etzioni et al., 2005)
systems. Machine reading was introduced by Mitchell (2005) and Etzioni et al. (2006) and is
the focus of the TEXTRUNNER project (Banko et al., 2007; Banko and Etzioni, 2008).
This chapter has focused on natural language sentences, but it is also possible to do
information extraction based on the physical structure or geometric layout of text rather than
on the linguistic structure. Lists, tables, charts, graphs, diagrams, etc., whether encoded in
HTML or accessed through the visual analysis of pdf documents, are home to data that can
be extracted and consolidated (Hurst, 2000; Pinto et al., 2003; Cafarella et al., 2008).
Ken Church (2004) shows that natural language research has cycled between concentrat-
ing on the data (empiricism) and concentrating on theories (rationalism); he describes the ad-
vantages of having good language resources and evaluation schemes, but wonders if we have
gone too far (Church and Hestness, 2019). Early linguists concentrated on actual language
usage data, including frequency counts. Noam Chomsky (1956) demonstrated the limitations
of ﬁnite-state models, leading to an emphasis on theoretical studies of syntax, disregarding
actual language performance. This approach dominated for twenty years, until empiricism
made a comeback based on the success of work in statistical speech recognition (Jelinek,
1976). Today, the emphasis on empirical language data continues, and there is heightened
interest in models that consider higher-level constructs, such as syntactic and semantic rela-
tions, not just sequences of words. There is also a strong emphasis on deep learning neural
network models of language, which we will cover in Chapter 25.
Work on applications of language processing is presented at the biennial Applied Natural
Language Processing conference (ANLP), the conference on Empirical Methods in Natural
Language Processing (EMNLP), and the journal Natural Language Engineering. A broad
range of NLP work appears in the journal Computational Linguistics and its conference,
ACL, and in the International Computational Linguistics (COLING) conference. Jurafsky
and Martin (2020) give a comprehensive introduction to speech and NLP.
