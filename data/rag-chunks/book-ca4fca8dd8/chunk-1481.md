---
chunk_id: "book-ca4fca8dd8-chunk-1481"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1481
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 894

894
Chapter 24
Natural Language Processing
Exp(op(x1,x2)) →Exp(x1) Operator(op) Exp(x2)
Exp(x) →( Exp(x) )
Exp(x) →Number(x)
Number(x) →Digit(x)
Number(10×x1 +x2) →Number(x1) Digit(x2)
Operator(+) →+
Operator(−) →-
Operator(×) →×
Operator(÷) →÷
Digit(0) →0
Digit(1) →1
...
Figure 24.10 A grammar for arithmetic expressions, augmented with semantics. Each vari-
able xi represents the semantics of a constituent.
24.4.1 Semantic interpretation
To show how to add semantics to a grammar, we start with an example that is simpler than En-
glish: the semantics of arithmetic expressions. Figure 24.10 shows a grammar for arithmetic
expressions, where each rule is augmented with a single argument indicating the semantic
interpretation of the phrase. The semantics of a digit such as “3” is the digit itself. The se-
mantics of the expression “3 + 4” is the operator “+” applied to the semantics of the phrases
“3” and “4.” The grammar rules obey the principle of compositional semantics—the se-
Compositional
semantics
mantics of a phrase is a function of the semantics of the subphrases. Figure 24.11 shows the
parse tree for 3+(4÷2) according to this grammar. The root of the parse tree is Exp(5), an
expression whose semantic interpretation is 5.
Now let’s move on to the semantics of English, or at least a tiny portion of it. We will use
ﬁrst-order logic for our semantic representation. So the simple sentence “Ali loves Bo” should
get the semantic representation Loves(Ali,Bo). But what about the constituent phrases? We
can represent the NP “Ali” with the logical term Ali. But the VP “loves Bo” is neither a logical
term nor a complete logical sentence. Intuitively, “loves Bo” is a description that might or
might not apply to a particular person. (In this case, it applies to Ali.) This means that
“loves Bo” is a predicate that, when combined with a term that represents a person, yields a
complete logical sentence.
Using the λ-notation (see page 277), we can represent “loves Bo” as the predicate
λx Loves(x,Bo).
Now we need a rule that says “an NP with semantics n followed by a VP with semantics pred
yields a sentence whose semantics is the result of applying pred to n:”
S(pred(n)) →NP(n) VP(pred).
The rule tells us that the semantic interpretation of “Ali loves Bo” is
(λx Loves(x,Bo))(Ali),

## Page 895
