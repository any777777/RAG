---
chunk_id: "book-ca4fca8dd8-chunk-1038"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1038
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 623

Section 17.4
Making Collective Decisions
623
I have a
problem... 
problem recognition
task 
announcement
bidding
awarding
Figure 17.8 The contract net task allocation protocol.
in isolation, or because a cooperative solution might in some way be better (faster, more
efﬁcient, more accurate).
The agent advertises the task to other agents in the net with a task announcement mes-
Task announcement
sage, and then acts as the manager of that task for its duration. The task announcement
Manager
message must include sufﬁcient information for recipients to judge whether or not they are
willing and able to bid for the task. The precise information included in a task announcement
will depend on the application area. It might be some code that needs to be executed; or it
might be a logical speciﬁcation of a goal to be achieved. The task announcement might also
include other information that might be required by recipients, such as deadlines, quality-of-
service requirements, and so on.
When an agent receives a task announcement, it must evaluate it with respect to its own
capabilities and preferences. In particular, each agent must determine, whether it has the
capability to carry out the task, and second, whether or not it desires to do so. On this basis, it
may then submit a bid for the task. A bid will typically indicate the capabilities of the bidder
Bid
that are relevant to the advertised task, and any terms and conditions under which the task
will be carried out.
In general, a manager may receive multiple bids in response to a single task announce-
ment. Based on the information in the bids, the manager selects the most appropriate agent
(or agents) to execute the task. Successful agents are notiﬁed through an award message, and
become contractors for the task, taking responsibility for the task until it is completed.
The main computational tasks required to implement the contract net protocol can be
summarized as follows:

## Page 624
