---
chunk_id: "book-ca4fca8dd8-chunk-1093"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1093
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 18.2
Open-Universe Probability Models
653
type Researcher, Paper, Citation
random String Name(Researcher)
random String Title(Paper)
random Paper PubCited(Citation)
random String Text(Citation)
random Boolean Professor(Researcher)
origin Researcher Author(Paper)
#Researcher ∼OM(3,1)
Name(r) ∼NamePrior()
Professor(r) ∼Boolean(0.2)
#Paper(Author= r) ∼if Professor(r) then OM(1.5,0.5) else OM(1,0.5)
Title(p) ∼PaperTitlePrior()
CitedPaper(c) ∼UniformChoice({Paper p})
Text(c) ∼HMMGrammar(Name(Author(CitedPaper(c))),Title(CitedPaper(c)))
Figure 18.5 An OUPM for citation information extraction. For simplicity the model assumes
one author per paper and omits details of the grammar and error models.
In order to solve the problem using a probabilistic approach, we need a generative model
for the domain. That is, we ask how these citation strings come to be in the world. The
process begins with researchers, who have names. (We don’t need to worry about how the
researchers came into existence; we just need to express our uncertainty about how many
there are.) These researchers write some papers, which have titles; people cite the papers,
combining the authors’ names and the paper’s title (with errors) into the text of the citation
according to some grammar. The basic elements of this model are shown in Figure 18.5,
covering the case where papers have just one author.9
Given just citation strings as evidence, probabilistic inference on this model to pick
out the most likely explanation for the data produces an error rate 2 to 3 times lower than
CiteSeer’s (Pasula et al., 2003). The inference process also exhibits a form of collective,
knowledge-driven disambiguation: the more citations for a given paper, the more accurately
each of them is parsed, because the parses have to agree on the facts about the paper.
Nuclear treaty monitoring
Verifying the Comprehensive Nuclear-Test-Ban Treaty requires ﬁnding all seismic events on
Earth above a minimum magnitude. The UN CTBTO maintains a network of sensors, the
International Monitoring System (IMS); its automated processing software, based on 100
years of seismology research, has a detection failure rate of about 30%. The NET-VISA
system (Arora et al., 2013), based on an OUPM, signiﬁcantly reduces detection failures.
The NET-VISA model (Figure 18.6) expresses the relevant geophysics directly. It de-
scribes distributions over the number of events in a given time interval (most of which are
9
The multi-author case has the same overall structure but is a bit more complicated. The parts of the model
not shown—the NamePrior, rTitlePrior, and HMMGrammar—are traditional probability models. For exam-
ple, the NamePrior is a mixture of a categorical distribution over actual names and a letter trigram model (see
Section 24.1) to cover names not previously seen, both trained from data in the U.S. Census database.
