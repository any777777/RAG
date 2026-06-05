---
chunk_id: "book-ca4fca8dd8-chunk-0004"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 4
confidence: "first-pass"
extraction_method: "structured-local"
---

Preface
Artiﬁcial Intelligence (AI) is a big ﬁeld, and this is a big book. We have tried to explore
the full breadth of the ﬁeld, which encompasses logic, probability, and continuous mathemat-
ics; perception, reasoning, learning, and action; fairness, trust, social good, and safety; and
applications that range from microelectronic devices to robotic planetary explorers to online
services with billions of users.
The subtitle of this book is “A Modern Approach.” That means we have chosen to tell
the story from a current perspective. We synthesize what is now known into a common
framework, recasting early work using the ideas and terminology that are prevalent today.
We apologize to those whose subﬁelds are, as a result, less recognizable.
New to this edition
This edition reﬂects the changes in AI since the last edition in 2010:
• We focus more on machine learning rather than hand-crafted knowledge engineering,
due to the increased availability of data, computing resources, and new algorithms.
• Deep learning, probabilistic programming, and multiagent systems receive expanded
coverage, each with their own chapter.
• The coverage of natural language understanding, robotics, and computer vision has
been revised to reﬂect the impact of deep learning.
• The robotics chapter now includes robots that interact with humans and the application
of reinforcement learning to robotics.
• Previously we deﬁned the goal of AI as creating systems that try to maximize expected
utility, where the speciﬁc utility information—the objective—is supplied by the human
designers of the system. Now we no longer assume that the objective is ﬁxed and known
by the AI system; instead, the system may be uncertain about the true objectives of the
humans on whose behalf it operates. It must learn what to maximize and must function
appropriately even while uncertain about the objective.
• We increase coverage of the impact of AI on society, including the vital issues of ethics,
fairness, trust, and safety.
• We have moved the exercises from the end of each chapter to an online site. This
allows us to continuously add to, update, and improve the exercises, to meet the needs
of instructors and to reﬂect advances in the ﬁeld and in AI-related software tools.
• Overall, about 25% of the material in the book is brand new. The remaining 75% has
been largely rewritten to present a more uniﬁed picture of the ﬁeld. 22% of the citations
in this edition are to works published after 2010.
Overview of the book
The main unifying theme is the idea of an intelligent agent. We deﬁne AI as the study of
agents that receive percepts from the environment and perform actions. Each such agent
implements a function that maps percept sequences to actions, and we cover different ways
to represent these functions, such as reactive agents, real-time planners, decision-theoretic
7
