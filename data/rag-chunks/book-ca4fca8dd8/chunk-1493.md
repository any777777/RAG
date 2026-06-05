---
chunk_id: "book-ca4fca8dd8-chunk-1493"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1493
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
901
n-gram counts of speciﬁc words) and could form compositional models throughout the vari-
ous levels of the deep network to effectively pass information along. Subsequent work using
the attention-focusing mechanism of the transformer model (Vaswani et al., 2018) increased
performance further, and a hybrid model incorporating aspects of both these models does
better still, approaching human-level performance on some language pairs (Wu et al., 2016b;
Chen et al., 2018).
Information extraction is the process of acquiring knowledge by skimming a text and
Information
extraction
looking for occurrences of particular classes of objects and for relationships among them.
A typical task is to extract instances of addresses from Web pages, with database ﬁelds for
street, city, state, and zip code; or instances of storms from weather reports, with ﬁelds for
temperature, wind speed, and precipitation. If the source text is well structured (for ex-
ample, in the form of a table), then simple techniques such as regular expressions can ex-
tract the information (Cafarella et al., 2008). It gets harder if we are trying to extract all
facts, rather than a speciﬁc type (such as weather reports); Banko et al. (2007) describe the
TEXTRUNNER system that performs extraction over an open, expanding set of relations. For
free-form text, techniques include hidden Markov models and rule-based learning systems
(as used in TEXTRUNNER and NELL (Never-Ending Language Learning) (Mitchell et al.,
2018)). More recent systems use recurrent neural networks, taking advantage of the ﬂexibility
of word embeddings. You can ﬁnd an overview in Kumar (2017).
Information retrieval is the task of ﬁnding documents that are relevant and important
Information retrieval
for a given query. Internet search engines such as Google and Baidu perform this task billions
of times a day. Three good textbooks on the subject are Manning et al. (2008), Croft et al.
(2010), and Baeza-Yates and Ribeiro-Neto (2011).
Question Answering is a different task, in which the query really is a question, such as
Question Answering
“Who founded the U.S. Coast Guard?” and the response is not a ranked list of documents but
rather an actual answer: “Alexander Hamilton.” There have been question-answering systems
since the 1960s that rely on syntactic parsing as discussed in this chapter, but only since
2001 have such systems used Web information retrieval to radically increase their breadth of
coverage. Katz (1997) describes the START parser and question answerer. Banko et al. (2002)
describe ASKMSR, which was less sophisticated in terms of its syntactic parsing ability, but
more aggressive in using Web search and sorting through the results. For example, to answer
“Who founded the U.S. Coast Guard?” it would search for queries such as [* founded the
U.S. Coast Guard] and [the U.S. Coast Guard was founded by *], and then examine the
multiple resulting Web pages to pick out a likely response, knowing that the query word
“who” suggests that the answer should be a person. The Text REtrieval Conference (TREC)
gathers research on this topic and has hosted competitions on an annual basis since 1991
(Allan et al., 2017). Recently we have seen other test sets, such as the AI2 ARC test set of
basic science questions (Clark et al., 2018).
Summary
The main points of this chapter are as follows:
• Probabilistic language models based on n-grams recover a surprising amount of infor-
mation about a language. They can perform well on such diverse tasks as language
