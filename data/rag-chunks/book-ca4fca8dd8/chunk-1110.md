---
chunk_id: "book-ca4fca8dd8-chunk-1110"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1110
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
665
• Given an RPM, the objects in each possible world correspond to the constant symbols in
the RPM, and the basic random variables are all possible instantiations of the predicate
symbols with objects replacing each argument. Thus, the set of possible worlds is ﬁnite.
• RPMs provide very concise models for worlds with large numbers of objects and can
handle relational uncertainty.
• Open-universe probability models (OUPMs) build on the full semantics of ﬁrst-order
logic, allowing for new kinds of uncertainty such as identity and existence uncertainty.
• Generative programs are representations of probability models—including OUPMs—
as executable programs in a probabilistic programming language or PPL. A gener-
ative program represents a distribution over execution traces of the program. PPLs
typically provide universal expressive power for probability models.
Bibliographical and Historical Notes
Hailperin (1984) and Howson (2003) recount the long history of attempts to connect proba-
bility and logic, going back to Leibniz’s Nouveaux Essais in 1704. These attempts usually
involved probabilities attached directly to logical sentences. The ﬁrst rigorous treatment was
Gaifman’s propositional probability logic (Gaifman, 1964b). The idea is that a probability
Probability logic
assertion P(φ) ≥p is a constraint on the distribution over possible worlds, just as an ordinary
logical sentence is a constraint on the possible worlds themselves. Any distribution P that
satisﬁes the constraint is a model, in the standard logical sense, of the probability assertion,
and one probability assertion entails another just when the models of the ﬁrst are a subset of
the models of the second.
Within such a logic, one can prove, for example, that P(α ∧β) ≤P(α ⇒β). Satisﬁa-
bility of sets of probability assertions can be determined in the propositional case by linear
programming (Hailperin, 1984; Nilsson, 1986). Thus, we have a “probability logic” in the
same sense as “temporal logic”—a logical system specialized for probabilistic reasoning.
To apply probability logic to tasks such as proving interesting theorems in probability the-
ory, a more expressive language was needed. Gaifman (1964a) proposed a ﬁrst-order prob-
ability logic, with possible worlds being ﬁrst-order model structures and with probabilities
attached to sentences of (function-free) ﬁrst-order logic. Scott and Krauss (1966) extended
Gaifman’s results to allow inﬁnite nesting of quantiﬁers and inﬁnite sets of sentences.
Within AI, the most direct descendant of these ideas appears in probabilistic logic pro-
grams (Lukasiewicz, 1998), in which a probability range is attached to each ﬁrst-order Horn
clause and inference is performed by solving linear programs, as suggested by Hailperin.
Halpern (1990) and Bacchus (1990) also built on Gaifman’s approach, exploring some of
the basic knowledge representation issues from the perspective of AI rather than probability
theory and mathematical logic.
The subﬁeld of probabilistic databases also has logical sentences labeled with proba-
Probabilistic
databases
bilities (Dalvi et al., 2009)—but in this case probabilities are attached directly to the tuples
of the database. (In AI and statistics, probability is attached to general relationships, whereas
observations are viewed as incontrovertible evidence.) Although probabilistic databases can
model complex dependencies, in practice one often ﬁnds such systems using global indepen-
dence assumptions across tuples.
