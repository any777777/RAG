---
chunk_id: "book-ca4fca8dd8-chunk-0064"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 64
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 1.3
The History of Artiﬁcial Intelligence
41
in efﬁcient “cookbook recipes” (Feigenbaum et al., 1971). The signiﬁcance of DENDRAL
was that it was the ﬁrst successful knowledge-intensive system: its expertise derived from
large numbers of special-purpose rules. In 1971, Feigenbaum and others at Stanford began
the Heuristic Programming Project (HPP) to investigate the extent to which the new method-
ology of expert systems could be applied to other areas.
Expert systems
The next major effort was the MYCIN system for diagnosing blood infections. With about
450 rules, MYCIN was able to perform as well as some experts, and considerably better than
junior doctors. It also contained two major differences from DENDRAL. First, unlike the
DENDRAL rules, no general theoretical model existed from which the MYCIN rules could be
deduced. They had to be acquired from extensive interviewing of experts. Second, the rules
had to reﬂect the uncertainty associated with medical knowledge. MYCIN incorporated a
calculus of uncertainty called certainty factors (see Chapter 13), which seemed (at the time)
Certainty factor
to ﬁt well with how doctors assessed the impact of evidence on the diagnosis.
The ﬁrst successful commercial expert system, R1, began operation at the Digital Equip-
ment Corporation (McDermott, 1982). The program helped conﬁgure orders for new com-
puter systems; by 1986, it was saving the company an estimated $40 million a year. By 1988,
DEC’s AI group had 40 expert systems deployed, with more on the way. DuPont had 100 in
use and 500 in development. Nearly every major U.S. corporation had its own AI group and
was either using or investigating expert systems.
The importance of domain knowledge was also apparent in the area of natural language
understanding. Despite the success of Winograd’s SHRDLU system, its methods did not ex-
tend to more general tasks: for problems such as ambiguity resolution it used simple rules
that relied on the tiny scope of the blocks world.
Several researchers, including Eugene Charniak at MIT and Roger Schank at Yale, sug-
gested that robust language understanding would require general knowledge about the world
and a general method for using that knowledge. (Schank went further, claiming, “There is
no such thing as syntax,” which upset a lot of linguists but did serve to start a useful dis-
cussion.) Schank and his students built a series of programs (Schank and Abelson, 1977;
Wilensky, 1978; Schank and Riesbeck, 1981) that all had the task of understanding natural
language. The emphasis, however, was less on language per se and more on the problems of
representing and reasoning with the knowledge required for language understanding.
The widespread growth of applications to real-world problems led to the development of
a wide range of representation and reasoning tools. Some were based on logic—for example,
the Prolog language became popular in Europe and Japan, and the PLANNER family in the
United States. Others, following Minsky’s idea of frames (1975), adopted a more structured
Frames
approach, assembling facts about particular object and event types and arranging the types
into a large taxonomic hierarchy analogous to a biological taxonomy.
In 1981, the Japanese government announced the “Fifth Generation” project, a 10-year
plan to build massively parallel, intelligent computers running Prolog. The budget was to
exceed a $1.3 billion in today’s money. In response, the United States formed the Micro-
electronics and Computer Technology Corporation (MCC), a consortium designed to assure
national competitiveness. In both cases, AI was part of a broad effort, including chip design
and human-interface research. In Britain, the Alvey report reinstated the funding removed by
the Lighthill report. However, none of these projects ever met its ambitious goals in terms of
new AI capabilities or economic impact.
