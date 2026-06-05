---
chunk_id: "book-ca4fca8dd8-chunk-1756"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1756
confidence: "first-pass"
extraction_method: "structured-local"
---

1068
Chapter 29
The Future of AI
be automatically optimized through gradient descent. Our computer models will learn from
conversations with human experts as well as by using all the available data.
Yann LeCun, Geoffrey Hinton, and others have suggested that the current emphasis on
supervised learning (and to a lesser extent reinforcement learning) is not sustainable—that
computer models will have to rely on weakly supervised learning, in which some supervi-
sion is given with a small number of labeled examples and/or a small number of rewards, but
most of the learning is unsupervised, because unannotated data are so much more plentiful.
LeCun uses the term predictive learning for an unsupervised learning system that can
Predictive learning
model the world and learn to predict aspects of future states of the world—not just predict
labels for inputs that are independent and identically distributed with respect to past data, and
not just predict a value function over states. He suggests that GANs (generative adversarial
networks) can be used to learn to minimize the difference between predictions and reality.
Geoffrey Hinton stated in 2017 that “My view is throw it all away and start again,” mean-
ing that the overall idea of learning by adjusting parameters in a network is enduring, but the
speciﬁcs of the architecture of the networks and the technique of back-propagation need to be
rethought. Smolensky (1988) had a prescription for how to think about connectionist models;
his thoughts remain relevant today.
Resources
Machine learning research and development has been accelerated by the increasing availabil-
ity of data, storage, processing power, software, trained experts, and the investments needed to
support them. Since the 1970s, there has been a 100,000-fold speedup in general-purpose pro-
cessors and an additional 1,000-fold speedup due to specialized machine learning hardware.
The Web has served as a rich source of images, videos, speech, text, and semi-structured data,
currently adding over 1018 bytes every day.
Hundreds of high-quality data sets are available for a range of tasks in computer vision,
speech recognition, and natural language processing. If the data you need is not already
available, you can often assemble it from other sources, or engage humans to label data for
you through a crowdsourcing platform. Validating the data obtained in this way becomes an
important part of the overall workﬂow (Hirth et al., 2013).
An important recent development is the shift from shared data to shared models. The
Shared model
major cloud service providers (e.g., Amazon, Microsoft, Google, Alibaba, IBM, Salesforce)
have begun competing to offer machine learning APIs with pre-built models for speciﬁc tasks
such as visual object recognition, speech recognition, and machine translation. These models
can be used as is, or can serve as a baseline to be customized with your particular data for
your particular application.
We expect that these models will improve over time, and that it will become unusual to
start a machine learning project from scratch, just as it is now unusual to do a Web develop-
ment project from scratch, with no libraries. It is possible that a big jump in model quality
will occur when it becomes economical to process all the video on the Web; for example, the
YouTube platform alone adds 300 hours of video every minute.
Moore’s law has made it more cost effective to process data; a megabyte of storage cost $1
million in 1969 and less then $0.02 in 2019, and supercomputer throughput has increased by a
factor of more than 1010 in that time. Specialized hardware components for machine learning
such as graphics processing units (GPUs), tensor cores, tensor processing units (TPUs), and
