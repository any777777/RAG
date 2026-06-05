---
chunk_id: "book-ca4fca8dd8-chunk-1497"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1497
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
903
1991), Kneser–Ney smoothing (1995, 2004), and stupid backoff (Brants et al., 2007). Chen
and Goodman (1996) and Goodman (2001) survey smoothing techniques.
Simple n-gram letter and word models are not the only possible probabilistic models. The
latent Dirichlet allocation model (Blei et al., 2002; Hoffman et al., 2011) is a probabilistic
text model that views a document as a mixture of topics, each with its own distribution of
words. This model can be seen as an extension and rationalization of the latent semantic
indexing model of Deerwester et al. (1990) and is also related to the multiple-cause mixture
model of (Sahami et al., 1996). And of course there is great interest in non-probabilistic
language models, such as the deep learning models covered in Chapter 25.
Joulin et al. (2016) give a bag of tricks for efﬁcient text classiﬁcation. Joachims (2001)
uses statistical learning theory and support vector machines to give a theoretical analysis of
when classiﬁcation will be successful. Apt´e et al. (1994) report an accuracy of 96% in clas-
sifying Reuters news articles into the “Earnings” category. Koller and Sahami (1997) report
accuracy up to 95% with a naive Bayes classiﬁer, and up to 98.6% with a Bayes classiﬁer.
Schapire and Singer (2000) show that simple linear classiﬁers can often achieve accu-
racy almost as good as more complex models, and run faster. Zhang et al. (2016) describe a
character-level (rather than word-level) text classiﬁer. Witten et al. (1999) describe compres-
sion algorithms for classiﬁcation, and show the deep connection between the LZW compres-
sion algorithm and maximum-entropy language models.
Wordnet (Fellbaum, 2001) is a publicly available dictionary of about 100,000 words and
phrases, categorized into parts of speech and linked by semantic relations such as synonym,
antonym, and part-of. Charniak (1996) and Klein and Manning (2001) discuss parsing with
treebank grammars. The British National Corpus (Leech et al., 2001) contains 100 million
words, and the World Wide Web contains several trillion words; Franz and Brants (2006)
describe the publicly available Google n-gram corpus of 13 million unique words from a
trillion words of Web text. Buck et al. (2014) describe a similar data set from the Common
Crawl project. The Penn Treebank (Marcus et al., 1993; Bies et al., 2015) provides parse
trees for a 3-million-word corpus of English.
Many of the n-gram model techniques are also used in bioinformatics problems. Bio-
statistics and probabilistic NLP are coming closer together, as each deals with long, structured
sequences chosen from an alphabet.
Early part-of-speech (POS) taggers used a variety of techniques, including rule sets (Brill,
1992), n-grams (Church, 1988), decision trees (M`arquez and Rodr´ıguez, 1998), HMMs
(Brants, 2000), and logistic regression (Ratnaparkhi, 1996). Historically, a logistic regres-
sion model was also called a “maximum entropy Markov model” or MEMM, so some work
is under that name. Jurafsky and Martin (2020) have a good chapter on POS tagging. Ng and
Jordan (2002) compare discriminative and generative models for classiﬁcation tasks.
Like semantic networks, context-free grammars were ﬁrst discovered by ancient Indian
grammarians (especially Panini, ca. 350 BCE) studying Shastric Sanskrit (Ingerman, 1967).
They were reinvented by Noam Chomsky (1956) for the analysis of English and indepen-
dently by John Backus (1959) and Peter Naur for the analysis of Algol-58.
Probabilistic context-free grammars were ﬁrst investigated by Booth (1969) and Sa-
lomaa (1969). Algorithms for PCFGs are presented in the excellent short monograph by
Charniak (1993) and the excellent long textbooks by Manning and Sch¨utze (1999) and Juraf-
sky and Martin (2020). Baker (1979) introduces the inside–outside algorithm for learning a
