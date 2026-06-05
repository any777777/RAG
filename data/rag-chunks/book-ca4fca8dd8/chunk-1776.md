---
chunk_id: "book-ca4fca8dd8-chunk-1776"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1776
confidence: "first-pass"
extraction_method: "structured-local"
---

1082
Appendix B
Notes on Languages and Algorithms
We cover languages and grammars in more detail in Chapter 24. Be aware that other books
use slightly different notations for BNF; for example, you might see ⟨Digit⟩instead of Digit
for a nonterminal, ‘word’ instead of word for a terminal, or ::= instead of →in a rule.
B.2 Describing Algorithms with Pseudocode
The algorithms in this book are described in pseudocode. Most of the pseudocode should
Pseudocode
be familiar to programmers who use languages like Java, C++, or especially Python. In
some places we use mathematical formulas or ordinary English to describe parts that would
otherwise be more cumbersome. A few idiosyncrasies should be noted:
• Persistent variables: We use the keyword persistent to say that a variable is given an
initial value the ﬁrst time a function is called and retains that value (or the value given to
it by a subsequent assignment statement) on all subsequent calls to the function. Thus,
persistent variables are like global variables in that they outlive a single call to their
function; but they are accessible only within the function. The agent programs in the
book use persistent variables for memory. Programs with persistent variables can be
implemented as objects in object-oriented languages such as C++, Java, Python, and
Smalltalk. In functional languages, they can be implemented by functional closures
over an environment containing the required variables.
• Functions as values: Functions have capitalized names, and variables have lowercase
italic names. So most of the time, a function call looks like FN(x). However, we allow
the value of a variable to be a function; for example, if the value of the variable f is the
square root function, then f(9) returns 3.
• Indentation is signiﬁcant: Indentation is used to mark the scope of a loop or con-
ditional, as in the languages Python and CoffeeScript, and unlike Java, C++, and Go
(which use braces) or Lua and Ruby (which use end).
• Destructuring assignment: The notation “x,y←pair” means that the right-hand side
must evaluate to a two-element collection, and the ﬁrst element is assigned to x and the
second to y. The same idea is used in “for x,y in pairs do” and can be used to swap two
variables: “x,y←y,x”
• Default values for parameters: The notation “function F(x,y=0) returns a number”
means that y is an optional argument with default value 0; that is, the calls F(3, 0) and
F(3) are equivalent.
• yield: a function that contains the keyword yield is a generator that generates a se-
Generator
quence of values, one each time the yield expression is encountered. After yielding, the
function continues execution with the next statement. The languages Python, Ruby, C#,
and Javascript (ECMAScript) have this same feature.
• Loops: There are four kinds of loops:
– “for x in c do” executes the loop with the variable x bound to successive elements
of the collection c.
– “for i = 1 to n do” executes the loop with i bound to successive integers from 1 to
n inclusive.
– “while condition do” means the condition is evaluated before each iteration of the
loop, and the loop exits if the condition is false.
