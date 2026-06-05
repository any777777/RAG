---
chunk_id: "book-ca4fca8dd8-chunk-1665"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1665
confidence: "first-pass"
extraction_method: "structured-local"
---

1016
Chapter 27
Computer Vision
A baby eating a piece
of food in his mouth
A young boy eating
a piece of cake
A small bird is perched
on a branch
A small brown bear is
sitting in the grass
Figure 27.19 Automated image captioning systems produce some good results and some
failures. The two captions at left describe the respective images well, although “eating ...in
his mouth” is a disﬂuency that is fairly typical of the recurrent neural network language mod-
els used by early captioning systems. For the two captions on the right, the captioning system
seems not to know about squirrels, and so guesses the animal from context; it also fails to
recognize that the two squirrels are eating. Image credits: geraine/Shutterstock; ESB Pro-
fessional/Shutterstock; BushAlex/Shutterstock; Maria.Tem/Shutterstock. The images shown
are similar but not identical to the original images from which the captions were generated.
For the original images see Aneja et al. (2018).
people do so many things in so many contexts. For example, suppose we have a pedestrian
detector that performs well on a large data set. There will be rare phenomena (for example,
people mounting unicycles) that do not appear in the training set, so we can’t say for sure
how the detector will work in such cases. The challenge is to prove that the detector is safe
whatever pedestrians do, which is difﬁcult for current theories of learning.
27.7.2 Linking pictures and words
Many people create and share pictures and videos on the Internet. The difﬁculty is ﬁnding
what you want. Typically, people want to search using words (rather than, say, example
sketches). Because most pictures don’t come with words attached, it is natural to try and
build tagging systems that tag images with relevant words. The underlying machinery is
Tagging system
straightforward—we apply image classiﬁcation and object detection methods and tag the im-
age with the output words. But tags aren’t a comprehensive description of what is happening
in an image. It matters who is doing what, and tags don’t capture this. For example, tagging
a picture of a cat in the street with the object categories “cat”, “street”, “trash can” and “ﬁsh
bones” leaves out the information that the cat is pulling the ﬁsh bones out of an open trash
can on the street.
As an alternative to tagging, we might build captioning systems—systems that write a
Captioning systems
caption of one or more sentences describing the image. The underlying machinery is again
straightforward—couple a convolutional network (to represent the image) to a recurrent neu-
ral network or transformer network (to generate sentences), and train the result with a data set
of captioned images. There are many images with captions available on the Internet; curated
data sets use human labor to augment each image with additional captions to capture the vari-
ation in natural language. For example, the COCO (Common Objects in Context) data set is
a comprehensive collection of over 200,000 images labeled with ﬁve captions per image.
Current methods for captioning use detectors to ﬁnd a set of words that describe the
image, and provide those words to a sequence model that is trained to generate a sentence.
