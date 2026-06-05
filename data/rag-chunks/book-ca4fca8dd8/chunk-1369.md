---
chunk_id: "book-ca4fca8dd8-chunk-1369"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1369
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.8
Applications
833
of miles of simulated driving, which would be impossible in the real world. Then, when the
controller is transitioned to the real vehicle, it adapts quickly to the new environment.
Multitask learning is a form of transfer learning in which we simultaneously train a
Multitask learning
model on multiple objectives. For example, rather than training a natural language system on
part-of-speech tagging and then transferring the learned weights to a new task such as docu-
ment classiﬁcation, we train one system simultaneously on part-of-speech tagging, document
classiﬁcation, language detection, word prediction, sentence difﬁculty modeling, plagiarism
detection, sentence entailment, and question answering. The idea is that to solve any one of
these tasks, a model might be able to take advantage of superﬁcial features of the data. But to
solve all eight at once with a common representation layer, the model is more likely to create
a common representation that reﬂects real natural language usage and content.
22.8 Applications
Deep learning has been applied successfully to many important problem areas in AI. For in-
depth explanations, we refer the reader to the relevant chapters: Chapter 23 for the use of
deep learning in reinforcement learning systems, Chapter 25 for natural language processing,
Chapter 27 (particularly Section 27.4) for computer vision, and Chapter 26 for robotics.
22.8.1 Vision
We begin with computer vision, which is the application area that has arguably had the biggest
impact on deep learning, and vice versa. Although deep convolutional networks had been in
use since the 1990s for tasks such as handwriting recognition, and neural networks had begun
to surpass generative probability models for speech recognition by around 2010, it was the
success of the AlexNet deep learning system in the 2012 ImageNet competition that propelled
deep learning into the limelight.
The ImageNet competition was a supervised learning task with 1,200,000 images in 1,000
different categories, and systems were evaluated on the “top-5” score—how often the correct
category appears in the top ﬁve predictions. AlexNet achieved an error rate of 15.3%, whereas
the next best system had an error rate of more than 25%. AlexNet had ﬁve convolutional
layers interspersed with max-pooling layers, followed by three fully connected layers. It used
ReLU activation functions and took advantage of GPUs to speed up the process of training
60 million weights.
Since 2012, with improvements in network design, training methods, and computing
resources, the top-5 error rate has been reduced to less than 2%—well below the error rate of
a trained human (around 5%). CNNs have been applied to a wide range of vision tasks, from
self-driving cars to grading cucumbers.8 Driving, which is covered in Section 27.7.6 and in
several sections of Chapter 26, is among the most demanding of vision tasks: not only must
the algorithm detect, localize, track, and recognize pigeons, paper bags, and pedestrians, but
it has to do it in real time with near-perfect accuracy.
8
The widely known tale of the Japanese cucumber farmer who built his own cucumber-sorting robot using
TensorFlow is, it turns out, mostly mythical. The algorithm was developed by the farmer’s son, who worked
previously as a software engineer at Toyota, and its low accuracy—about 70%—meant that the cucumbers still
had to be sorted by hand (Zeeberg, 2017).
