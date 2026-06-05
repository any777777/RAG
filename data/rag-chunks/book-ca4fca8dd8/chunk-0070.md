---
chunk_id: "book-ca4fca8dd8-chunk-0070"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 70
confidence: "first-pass"
extraction_method: "structured-local"
---

44
Chapter 1
Introduction
become somewhat separate from core AI. The process of reintegration has yielded signiﬁ-
cant beneﬁts both in terms of applications—for example, the deployment of practical robots
expanded greatly during this period—and in a better theoretical understanding of the core
problems of AI.
1.3.7 Big data (2001–present)
Remarkable advances in computing power and the creation of the World Wide Web have
facilitated the creation of very large data sets—a phenomenon sometimes known as big data.
Big data
These data sets include trillions of words of text, billions of images, and billions of hours of
speech and video, as well as vast amounts of genomic data, vehicle tracking data, clickstream
data, social network data, and so on.
This has led to the development of learning algorithms specially designed to take advan-
tage of very large data sets. Often, the vast majority of examples in such data sets are un-
labeled; for example, in Yarowsky’s (1995) inﬂuential work on word-sense disambiguation,
occurrences of a word such as “plant” are not labeled in the data set to indicate whether they
refer to ﬂora or factory. With large enough data sets, however, suitable learning algorithms
can achieve an accuracy of over 96% on the task of identifying which sense was intended in a
sentence. Moreover, Banko and Brill (2001) argued that the improvement in performance ob-
tained from increasing the size of the data set by two or three orders of magnitude outweighs
any improvement that can be obtained from tweaking the algorithm.
A similar phenomenon seems to occur in computer vision tasks such as ﬁlling in holes in
photographs—holes caused either by damage or by the removal of ex-friends. Hays and Efros
(2007) developed a clever method for doing this by blending in pixels from similar images;
they found that the technique worked poorly with a database of only thousands of images but
crossed a threshold of quality with millions of images. Soon after, the availability of tens of
millions of images in the ImageNet database (Deng et al., 2009) sparked a revolution in the
ﬁeld of computer vision.
The availability of big data and the shift towards machine learning helped AI recover
commercial attractiveness (Havenstein, 2005; Halevy et al., 2009). Big data was a crucial fac-
tor in the 2011 victory of IBM’s Watson system over human champions in the Jeopardy! quiz
game, an event that had a major impact on the public’s perception of AI.
1.3.8 Deep learning (2011–present)
The term deep learning refers to machine learning using multiple layers of simple, adjustable
Deep learning
computing elements. Experiments were carried out with such networks as far back as the
1970s, and in the form of convolutional neural networks they found some success in hand-
written digit recognition in the 1990s (LeCun et al., 1995). It was not until 2011, however,
that deep learning methods really took off. This occurred ﬁrst in speech recognition and then
in visual object recognition.
In the 2012 ImageNet competition, which required classifying images into one of a thou-
sand categories (armadillo, bookshelf, corkscrew, etc.), a deep learning system created in
Geoffrey Hinton’s group at the University of Toronto (Krizhevsky et al., 2013) demonstrated
a dramatic improvement over previous systems, which were based largely on handcrafted
features. Since then, deep learning systems have exceeded human performance on some vi-
sion tasks (and lag behind in some other tasks). Similar gains have been reported in speech
