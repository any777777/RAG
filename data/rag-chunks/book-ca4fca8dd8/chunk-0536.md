---
chunk_id: "book-ca4fca8dd8-chunk-0536"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 536
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
327
Learning: We can improve a theorem prover by learning from experience. Given a collection
Learning
of previously-proved theorems, train a machine learning system to answer the question: given
a set of premises and a goal to prove, what proof steps are similar to steps that were successful
in the past? The DEEPHOL system (Bansal et al., 2019) does exactly that, using deep neural
networks (see Chapter 22) to build models (called embeddings) of goals and premises, and
using them to make selections. Training can use both human- and computer-generated proofs
as examples, starting from a collection of 10,000 proofs.
Practical uses of resolution theorem provers
We have shown how ﬁrst-order logic can represent a simple real-world scenario involving
concepts like selling, weapons, and citizenship. But complex real-world scenarios have too
much uncertainty and too many unknowns. Logic has proven to be more successful for sce-
narios involving formal, strictly deﬁned concepts, such as the synthesis and veriﬁcation of
Synthesis
Veriﬁcation
both hardware and software. Theorem-proving research is carried out in the ﬁelds of hard-
ware design, programming languages, and software engineering—not just in AI.
In the case of hardware, the axioms describe the interactions between signals and cir-
cuit elements. (See Section 8.4.2 on page 291 for an example.) Logical reasoners designed
specially for veriﬁcation have been able to verify entire CPUs, including their timing prop-
erties (Srivas and Bickford, 1990). The AURA theorem prover has been applied to design
circuits that are more compact than any previous design (Wojciechowski and Wojcik, 1983).
In the case of software, reasoning about programs is quite similar to reasoning about
actions, as in Chapter 7: axioms describe the preconditions and effects of each statement.
The formal synthesis of algorithms was one of the ﬁrst uses of theorem provers, as outlined
by Cordell Green (1969a), who built on earlier ideas by Herbert Simon (1963). The idea
is to constructively prove a theorem to the effect that “there exists a program p satisfying a
certain speciﬁcation.” Although fully automated deductive synthesis, as it is called, has not
yet become feasible for general-purpose programming, hand-guided deductive synthesis has
been successful in designing several novel and sophisticated algorithms. Synthesis of special-
purpose programs, such as scientiﬁc computing code, is also an active area of research.
Similar techniques are now being applied to software veriﬁcation by systems such as the
SPIN model checker (Holzmann, 1997). For example, the Remote Agent spacecraft control
program was veriﬁed before and after ﬂight (Havelund et al., 2000). The RSA public key
encryption algorithm and the Boyer–Moore string-matching algorithm have been veriﬁed this
way (Boyer and Moore, 1984).
Summary
We have presented an analysis of logical inference in ﬁrst-order logic and a number of algo-
rithms for doing it.
• A ﬁrst approach uses inference rules (universal instantiation and existential instan-
tiation) to propositionalize the inference problem. Typically, this approach is slow,
unless the domain is small.
• The use of uniﬁcation to identify appropriate substitutions for variables eliminates the
instantiation step in ﬁrst-order proofs, making the process more efﬁcient in many cases.
