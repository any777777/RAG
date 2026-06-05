---
chunk_id: "book-ca4fca8dd8-chunk-0589"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 589
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
357
The creation of comprehensive taxonomies or classiﬁcations dates back to ancient times.
Aristotle (384–322 BCE) strongly emphasized classiﬁcation and categorization schemes. His
Organon, a collection of works on logic assembled by his students after his death, included a
treatise called Categories in which he attempted to construct what we would now call an upper
ontology. He also introduced the notions of genus and species for lower-level classiﬁcation.
Our present system of biological classiﬁcation, including the use of “binomial nomenclature”
(classiﬁcation via genus and species in the technical sense), was invented by the Swedish
biologist Carolus Linnaeus, or Carl von Linne (1707–1778). The problems associated with
natural kinds and inexact category boundaries have been addressed by Wittgenstein (1953),
Quine (1953), Lakoff (1987), and Schwartz (1977), among others.
See Chapter 25 for a discussion of deep neural network representations of words and
concepts that escape some of the problems of a strict ontology, but also sacriﬁce some of the
precision. We still don’t know the best way to combine the advantages of neural networks
and logical semantics for representation.
Interest in larger-scale ontologies is increasing, as documented by the Handbook on On-
tologies (Staab, 2004). The OPENCYC project (Lenat and Guha, 1990; Matuszek et al.,
2006) has released a 150,000-concept ontology, with an upper ontology similar to the one in
Figure 10.1 as well as speciﬁc concepts like “OLED Display” and “iPhone,” which is a type
of “cellular phone,” which in turn is a type of “consumer electronics,” “phone,” “wireless
communication device,” and other concepts. The NEXTKB project extends CYC and other
resources including FrameNet and WordNet into a knowledge base with almost 3 million
facts, and provides a reasoning engine, FIRE to go with it (Forbus et al., 2010).
The DBPEDIA project extracts structured data from Wikipedia, speciﬁcally from In-
foboxes: the attribute/value pairs that accompany many Wikipedia articles (Wu and Weld,
2008; Bizer et al., 2007). As of 2015, DBPEDIA contained 400 million facts about 4 mil-
lion objects in the English version alone; counting all 110 languages yields 1.5 billion facts
(Lehmann et al., 2015).
The IEEE working group P1600.1 created SUMO, the Suggested Upper Merged Ontol-
ogy (Niles and Pease, 2001; Pease and Niles, 2002), with about 1000 terms in the upper
ontology and links to over 20,000 domain-speciﬁc terms. Stoffel et al. (1997) describe algo-
rithms for efﬁciently managing a very large ontology. A survey of techniques for extracting
knowledge from Web pages is given by Etzioni et al. (2008).
On the Web, representation languages are emerging. RDF (Brickley and Guha, 2004)
allows for assertions to be made in the form of relational triples and provides some means for
evolving the meaning of names over time. OWL (Smith et al., 2004) is a description logic
that supports inferences over these triples. So far, usage seems to be inversely proportional
to representational complexity: the traditional HTML and CSS formats account for over 99%
of Web content, followed by the simplest representation schemes, such as RDFa (Adida and
Birbeck, 2008), and microformats (Khare, 2006; Patel-Schneider, 2014) which use HTML
and XHTML markup to add attributes to text on web pages. Usage of sophisticated RDF and
OWL ontologies is not yet widespread, and the full vision of the Semantic Web (Berners-
Lee et al., 2001) has not been realized. The conferences on Formal Ontology in Information
Systems (FOIS) covers both general and domain-speciﬁc ontologies.
The taxonomy used in this chapter was developed by the authors and is based in part
on their experience in the CYC project and in part on work by Hwang and Schubert (1993)
