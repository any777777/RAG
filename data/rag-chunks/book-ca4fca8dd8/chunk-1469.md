---
chunk_id: "book-ca4fca8dd8-chunk-1469"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1469
confidence: "first-pass"
extraction_method: "structured-local"
---

886
Chapter 24
Natural Language Processing
Unfortunately, the grammar overgenerates: that is, it generates sentences that are not gram-
Overgeneration
matical, such as “Me go I.” It also undergenerates: there are many sentences of English that
Undergeneration
it rejects, such as “I think the wumpus is smelly.” We will see how to learn a better grammar
later; for now we concentrate on what we can do with this very simple grammar.
24.2.1 The lexicon of E0
The lexicon, or list of allowable words, is deﬁned in Figure 24.3. Each of the lexical cate-
Lexicon
gories ends in ... to indicate that there are other words in the category. For nouns, names,
verbs, adjectives, and adverbs, it is infeasible even in principle to list all the words. Not only
are there tens of thousands of members in each class, but new ones—like humblebrag or
microbiome—are being added constantly. These ﬁve categories are called open classes. Pro-
Open class
nouns, relative pronouns, articles, prepositions, and conjunctions are called closed classes;
Closed class
they have a small number of words (a dozen or so), and change over the course of centuries,
not months. For example, “thee” and “thou” were commonly used pronouns in the 17th cen-
tury, were on the decline in the 19th century, and are seen today only in poetry and some
regional dialects.
24.3 Parsing
Parsing is the process of analyzing a string of words to uncover its phrase structure, according
Parsing
to the rules of a grammar. We can think of it as a search for a valid parse tree whose leaves
are the words of the string. Figure 24.4 shows that we can start with the S symbol and search
top down, or we can start with the words and search bottom up. Pure top-down or bottom-up
parsing strategies can be inefﬁcient, however, because they can end up repeating effort in
areas of the search space that lead to dead ends. Consider the following two sentences:
Have the students in section 2 of Computer Science 101 take the exam.
Have the students in section 2 of Computer Science 101 taken the exam?
Even though they share the ﬁrst 10 words, these sentences have very different parses, because
the ﬁrst is a command and the second is a question. A left-to-right parsing algorithm would
have to guess whether the ﬁrst word is part of a command or a question and will not be able
to tell if the guess is correct until at least the eleventh word, take or taken. If the algorithm
guesses wrong, it will have to backtrack all the way to the ﬁrst word and reanalyze the whole
sentence under the other interpretation.
To avoid this source of inefﬁciency we can use dynamic programming: every time we
analyze a substring, store the results so we won’t have to reanalyze it later. For example, once
we discover that “the students in section 2 of Computer Science 101” is an NP, we can record
that result in a data structure known as a chart. An algorithm that does this is called a chart
parser. Because we are dealing with context-free grammars, any phrase that was found in
Chart parser
the context of one branch of the search tree can work just as well in any other branch of the
search tree. There are many types of chart parsers; we describe a probabilistic version of a
bottom-up chart parsing algorithm called the CYK algorithm, after its inventors, Ali Cocke,
CYK algorithm
Daniel Younger, and Tadeo Kasami.2
2
Sometimes the authors are credited in the order CKY.
