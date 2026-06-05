---
chunk_id: "book-ca4fca8dd8-chunk-0211"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 211
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 127

Bibliographical and Historical Notes
127
keeping track of the best alternative path appeared earlier in Bratko’s (2009) elegant Prolog
implementation of A∗and in the DTA∗algorithm (Russell and Wefald, 1991). The latter work
also discusses metalevel state spaces and metalevel learning.
The MA∗algorithm appeared in Chakrabarti et al. (1989). SMA∗, or Simpliﬁed MA∗,
emerged from an attempt to implement MA∗(Russell, 1992). Kaindl and Khorsand (1994)
applied SMA∗to produce a bidirectional search algorithm that was substantially faster than
previous algorithms. Korf and Zhang (2000) describe a divide-and-conquer approach, and
Zhou and Hansen (2002) introduce memory-bounded A∗graph search and a strategy for
switching to breadth-ﬁrst search to increase memory-efﬁciency (Zhou and Hansen, 2006).
The idea that admissible heuristics can be derived by problem relaxation appears in the
seminal paper by Held and Karp (1970), who used the minimum-spanning-tree heuristic to
solve the TSP. (See Exercise 3.MSTR.) The automation of the relaxation process was imple-
mented successfully by Prieditis (1993). There is a growing literature on the application of
machine learning to discover heuristic functions (Samadi et al., 2008; Arfaee et al., 2010;
Thayer et al., 2011; Lelis et al., 2012).
The use of pattern databases to derive admissible heuristics is due to Gasser (1995) and
Culberson and Schaeffer (1996, 1998); disjoint pattern databases are described by Korf and
Felner (2002); a similar method using symbolic patterns is due to Edelkamp (2009). Fel-
ner et al. (2007) show how to compress pattern databases to save space. The probabilistic
interpretation of heuristics was investigated by Pearl (1984) and Hansson and Mayer (1989).
Pearl’s (1984) Heuristics and Edelkamp and Schr¨odl’s (2012) Heuristic Search are inﬂu-
ential textbooks on search. Papers about new search algorithms appear at the International
Symposium on Combinatorial Search (SoCS) and the International Conference on Automated
Planning and Scheduling (ICAPS), as well as in general AI conferences such as AAAI and
IJCAI, and journals such as Artiﬁcial Intelligence and Journal of the ACM.

## Page 128
