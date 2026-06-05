---
chunk_id: "book-ca4fca8dd8-chunk-1501"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1501
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
905
Close after that was Winograd’s (1972) SHRDLU, which handled questions and commands
about a blocks-world scene, and Woods’s (1973) LUNAR, which answered questions about
the rocks brought back from the moon by the Apollo program.
Banko et al. (2002) present the ASKMSR question-answering system; a similar system is
due to Kwok et al. (2001). Pasca and Harabagiu (2001) discuss a contest-winning question-
answering system.
Modern approaches to semantic interpretation usually assume that the mapping from
syntax to semantics will be learned from examples (Zelle and Mooney, 1996; Zettlemoyer and
Collins, 2005; Zhao and Huang, 2015). The ﬁrst important result on grammar induction was
a negative one: Gold (1967) showed that it is not possible to reliably learn an exactly correct
context-free grammar, given a set of strings from that grammar. Prominent linguists, such as
Chomsky (1957) and Pinker (2003), have used Gold’s result to argue that there must be an
innate universal grammar that all children have from birth. The so-called Poverty of the
Universal grammar
Stimulus argument says that children aren’t given enough input to learn a CFG, so they must
already “know” the grammar and be merely tuning some of its parameters.
While this argument continues to hold sway throughout much of Chomskyan linguistics,
it has been dismissed by other linguists (Pullum, 1996; Elman et al., 1997) and most computer
scientists. As early as 1969, Horning showed that it is possible to learn, in the sense of PAC
learning, a probabilistic context-free grammar. Since then, there have been many convincing
empirical demonstrations of language learning from positive examples alone, such as learn-
ing semantic grammars with inductive logic programming (Muggleton and De Raedt, 1994;
Mooney, 1999), the Ph.D. theses of Sch¨utze (1995) and de Marcken (1996), and the entire
line of modern language processing systems based on the transformer model (Section 25.4).
There is an annual International Conference on Grammatical Inference (ICGI).
James Baker’s DRAGON system (Baker, 1975) could be considered the ﬁrst succesful
speech recognition system. It was the ﬁrst to use HMMs for speech. After several decades
of systems based on probabilistic language models, the ﬁeld began to switch to deep neural
networks (Hinton et al., 2012). Deng (2016) describes how the introduction of deep learning
enabled rapid improvement in speech recognition, and reﬂects on the implications for other
NLP tasks. Today deep learning is the dominant approach for all large-scale speech recogni-
tion systems. Speech recognition can be seen as the ﬁrst application area that highlighted the
success of deep learning, with computer vision following shortly thereafter.
Interest in the ﬁeld of information retrieval was spurred by widespread usage of Internet
searching. Croft et al. (2010) and Manning et al. (2008) provide textbooks that cover the
basics. The TREC conference hosts an annual competition for IR systems and publishes
proceedings with results.
Brin and Page (1998) describe the PageRank algorithm, which takes into account the
links between pages, and give an overview of the implementation of a Web search engine.
Silverstein et al. (1998) investigate a log of a billion Web searches. The journal Information
Retrieval and the proceedings of the annual ﬂagship SIGIR conference cover recent develop-
ments in the ﬁeld.
Information extraction has been pushed forward by the annual Message Understanding
Conferences (MUC), sponsored by the U.S. government. Surveys of template-based systems
are given by Roche and Schabes (1997), Appelt (1999), and Muslea (1999). Large databases
of facts were extracted by Craven et al. (2000), Pasca et al. (2006), Mitchell (2007), and
