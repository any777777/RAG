---
chunk_id: "book-ca4fca8dd8-chunk-1449"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1449
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 24
NATURAL LANGUAGE PROCESSING
In which we see how a computer can use natural language to communicate with humans
and learn from what they have written.
About 100,000 years ago, humans learned how to speak, and about 5,000 years ago they
learned to write. The complexity and diversity of human language sets Homo sapiens apart
from all other species. Of course there are other attributes that are uniquely human: no other
species wears clothes, creates art, or spends two hours a day on social media in the way that
humans do. But when Alan Turing proposed his test for intelligence, he based it on language,
not art or haberdashery, perhaps because of its universal scope and because language captures
so much of intelligent behavior: a speaker (or writer) has the goal of communicating some
knowledge, then plans some language that represents the knowledge, and acts to achieve
the goal. The listener (or reader) perceives the language, and infers the intended meaning.
This type of communication via language has allowed civilization to grow; it is our main
means of passing along cultural, legal, scientiﬁc, and technological knowledge. There are
three primary reasons for computers to do natural language processing (NLP):
Natural language
processing (NLP)
• To communicate with humans. In many situations it is convenient for humans to use
speech to interact with computers, and in most situations it is more convenient to use
natural language rather than a formal language such as ﬁrst-order predicate calculus.
• To learn.
Humans have written down a lot of knowledge using natural language.
Wikipedia alone has 30 million pages of facts such as “Bush babies are small nocturnal
primates,” whereas there are hardly any sources of facts like this written in formal logic.
If we want our system to know a lot, it had better understand natural language.
• To advance the scientiﬁc understanding of languages and language use, using the tools
of AI in conjunction with linguistics, cognitive psychology, and neuroscience.
In this chapter we examine various mathematical models for language, and discuss the tasks
that can be achieved using them.
24.1 Language Models
Formal languages, such as ﬁrst-order logic, are precisely deﬁned, as we saw in Chapter 8. A
grammar deﬁnes the syntax of legal sentences and semantic rules deﬁne the meaning.
Natural languages, such as English or Chinese, cannot be so neatly characterized:
• Language judgments vary from person to person and time to time. Everyone agrees that
“Not to be invited is sad” is a grammatical sentence of English, but people disagree on
the grammaticality of “To be not invited is sad.”
