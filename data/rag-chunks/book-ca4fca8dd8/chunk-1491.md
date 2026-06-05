---
chunk_id: "book-ca4fca8dd8-chunk-1491"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1491
confidence: "first-pass"
extraction_method: "structured-local"
---

900
Chapter 24
Natural Language Processing
4. The acoustic model: for spoken communication, the likelihood that a particular se-
quence of sounds will be generated, given that the speaker has chosen a given string
of words. (For handwritten or typed communication, we have the problem of optical
character recognition.)
24.6 Natural Language Tasks
Natural language processing is a big ﬁeld, deserving an entire textbook or two of its own
(Goldberg, 2017; Jurafsky and Martin, 2020). In this section we brieﬂy describe some of the
main tasks; you can use the references to get more details.
Speech recognition is the task of transforming spoken sound into text. We can then
Speech recognition
perform further tasks (such as question answering) on the resulting text. Current systems
have a word error rate of about 3% to 5% (depending on details of the test set), similar
to human transcribers. The challenge for a system using speech recognition is to respond
appropriately even when there are errors on individual words.
Top systems today use a combination of recurrent neural networks and hidden Markov
models (Hinton et al., 2012; Yu and Deng, 2016; Deng, 2016; Chiu et al., 2017; Zhang et al.,
2017). The introduction of deep neural nets for speech in 2011 led to an immediate and
dramatic improvement of about 30% in error rate—this from a ﬁeld that seemed to be mature
and was previously progressing at only a few percent per year. Deep neural networks are a
good ﬁt because the problem of speech recognition has a natural compositional breakdown:
waveforms to phonemes to words to sentences. They will be covered in the next chapter.
Text-to-speech synthesis is the inverse process—going from text to sound. Taylor (2009)
Text-to-speech
gives a book-length overview. The challenge is to pronounce each word correctly, and to make
the ﬂow of each sentence seem natural, with the right pauses and emphasis.
Another area of development is in synthesizing different voices—starting with a choice
between a generic male or female voice, then allowing for regional dialects, and even imi-
tating celebrity voices. As with speech recognition, the introduction of deep recurrent neu-
ral networks led to a large improvement, with about 2/3 of listeners saying that the neural
WaveNet system (van den Oord et al., 2016a) sounded more natural than the previous non-
neural system.
Machine translation transforms text in one language to another. Systems are usually
trained using a bilingual corpus: a set of paired documents, where one member of the pair is
in, say, English, and the other is in, say, French. The documents do not need to be annotated
in any way; the machine translation system learns to align sentences and phrases and then
when presented with a novel sentence in one language, can generate a translation to the other.
Systems in the early 2000s used n-gram models, and achieved results that were usually
good enough to get across the meaning of a text, but contained syntactic errors in most sen-
tences. One problem was the limit on the length of the n-grams: even with a large limit of
7, it was difﬁcult for information to ﬂow from one end of the sentence to the other. Another
problem was that all the information in an n-gram model is at the level of individual words.
Such a system could learn that “black cat” translates to “chat noir,” but it could not learn the
rule that adjectives generally come before the noun in English and after the noun in French.
Recurrent neural sequence-to-sequence models (Sutskever et al., 2015) got around the
problem. They could generalize better (because they could use word embeddings rather than
