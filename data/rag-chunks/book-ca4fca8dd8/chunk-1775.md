---
chunk_id: "book-ca4fca8dd8-chunk-1775"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1775
confidence: "first-pass"
extraction_method: "structured-local"
---

APPENDIX B
NOTES ON LANGUAGES AND
ALGORITHMS
B.1 Deﬁning Languages with Backus–Naur Form (BNF)
In this book we deﬁne several languages, including the languages of propositional logic (235),
ﬁrst-order logic (276), and a subset of English (page 893). A formal language is deﬁned as
a set of strings where each string is a sequence of symbols. The languages we are interested
in consist of an inﬁnite set of strings, so we need a concise way to characterize the set.
We do that with a grammar. The particular type of grammar we use is called a context-
free grammar, because each expression has the same form in any context. We write our
Context-free
grammar
grammars in a formalism called Backus–Naur form (BNF). There are four components to a
Backus–Naur form
(BNF)
BNF grammar:
• A set of terminal symbols. These are the symbols or words that make up the strings of
Terminal symbol
the language. They could be letters (A, B, C, ...) or words (a, aardvark, abacus, ...),
or whatever symbols are appropriate for the domain.
• A set of nonterminal symbols that categorize subphrases of the language. For exam-
Nonterminal symbol
ple, the nonterminal symbol NounPhrase in English denotes an inﬁnite set of strings
including “you” and “the big slobbery dog.”
• A start symbol, which is the nonterminal symbol that denotes the complete set of
Start symbol
strings of the language. In English, this is Sentence; for arithmetic, it might be Expr,
and for programming languages it is Program.
• A set of rewrite rules, of the form LHS →RHS, where LHS is a nonterminal sym-
Rewrite rules
bol and RHS is a sequence of zero or more symbols. These can be either terminal or
nonterminal symbols, or the symbol ϵ, which is used to denote the empty string.
A rewrite rule of the form
Sentence →NounPhrase VerbPhrase
means that whenever we have two strings categorized as a NounPhrase and a VerbPhrase, we
can append them together and categorize the result as a Sentence. As an abbreviation, the two
rules (S →A) and (S →B) can be written (S →A | B). To illustrate these concepts, here is
a BNF grammar for simple arithmetic expressions:
Expr
→Expr Operator Expr | ( Expr ) | Number
Number
→Digit | Number Digit
Digit
→0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
Operator →+ | −| ÷ | ×

## Page 1082
