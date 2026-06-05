---
chunk_id: "book-ca4fca8dd8-chunk-1667"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1667
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.7
Using Computer Vision
1017
Q. What is the cat wearing?
A. Hat
Q. What is the weather like?
A. Rainy
Q. What surface is this?
A. Clay
Q. What toppings are on the pizza?
A. Mushrooms
Q. How many holes are in the pizza?
A. 8
Q. What letter is on the racket?
A. w
Q. What color is the right front leg?
A. Brown
Q. Why is the sign bent?
A. It’s not
Figure 27.20 Visual question-answering systems produce answers (typically chosen from a
multiple-choice set) to natural-language questions about images. Top: the system is produc-
ing quite sensible answers to rather difﬁcult questions about the image. Bottom: less satis-
factory answers. For example, the system is guessing about the number of holes in a pizza,
because it doesn’t understand what counts as a hole, and it has real difﬁculty counting. Simi-
larly, the system selects brown for the cat’s leg because the background is brown and it can’t
localize the leg properly. Image credits: (Top) Tobyanna/Shutterstock; 679411/Shutterstock;
ESB Professional/Shutterstock; Africa Studio/Shutterstock; (Bottom) Stuart Russell; Max-
isport/Shutterstock; Chendongshan/Shutterstock; Scott Biales DitchTheMap/Shutterstock.
The images shown are similar but not identical to the original images to which the question-
answering system was applied. For the original images see Goyal et al. (2017).
The most accurate methods search through the sentences that the model can generate to ﬁnd
the best, and strong methods appear to require a slow search. Sentences are evaluated with
a set of scores that check whether the generated sentence (a) uses phrases common in the
ground truth annotations and (b) doesn’t use other phrases. These scores are hard to use
directly as a loss function, but reinforcement learning methods can be used to train networks
that get very good scores. Often there will be an image in the training set whose description
has the same set of words as an image in the test set; in that case a captioning system can just
retrieve a valid caption rather than having to generate a new one. Caption writing systems
produce a mix of excellent results and embarrassing errors (see Figure 27.19).
Captioning systems can hide their ignorance by omitting to mention details they can’t get
right or by using contextual cues to guess. For example, captioning systems tend to be poor at
identifying the gender of people in images, and often guess based on training data statistics.
That can lead to errors—men also like shopping and women also snowboard. One way to
establish whether a system has a good representation of what is happening in an image is to
force it to answer questions about the image. This is a visual question answering or VQA
Visual question
answering (VQA)
system. An alternative is a visual dialog system, which is given a picture, its caption, and a
Visual dialog
dialog. The system must then answer the last question in the dialog. As Figure 27.20 shows,
vision remains extremely hard and VQA systems often make errors.
