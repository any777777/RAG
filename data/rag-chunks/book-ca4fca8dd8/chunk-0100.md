---
chunk_id: "book-ca4fca8dd8-chunk-0100"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 100
confidence: "first-pass"
extraction_method: "structured-local"
---

60
Chapter 2
Intelligent Agents
To the extent that an agent relies on the prior knowledge of its designer rather than on its
own percepts and learning processes, we say that the agent lacks autonomy. A rational agent
Autonomy
should be autonomous—it should learn what it can to compensate for partial or incorrect
prior knowledge. For example, a vacuum-cleaning agent that learns to predict where and
when additional dirt will appear will do better than one that does not.
As a practical matter, one seldom requires complete autonomy from the start: when the
agent has had little or no experience, it would have to act randomly unless the designer gave
some assistance. Just as evolution provides animals with enough built-in reﬂexes to survive
long enough to learn for themselves, it would be reasonable to provide an artiﬁcial intelligent
agent with some initial knowledge as well as an ability to learn. After sufﬁcient experience
of its environment, the behavior of a rational agent can become effectively independent of its
prior knowledge. Hence, the incorporation of learning allows one to design a single rational
agent that will succeed in a vast variety of environments.
2.3 The Nature of Environments
Now that we have a deﬁnition of rationality, we are almost ready to think about building
rational agents. First, however, we must think about task environments, which are essen-
Task environment
tially the “problems” to which rational agents are the “solutions.” We begin by showing how
to specify a task environment, illustrating the process with a number of examples. We then
show that task environments come in a variety of ﬂavors. The nature of the task environment
directly affects the appropriate design for the agent program.
2.3.1 Specifying the task environment
In our discussion of the rationality of the simple vacuum-cleaner agent, we had to specify
the performance measure, the environment, and the agent’s actuators and sensors. We group
all these under the heading of the task environment. For the acronymically minded, we call
this the PEAS (Performance, Environment, Actuators, Sensors) description. In designing an
PEAS
agent, the ﬁrst step must always be to specify the task environment as fully as possible.
The vacuum world was a simple example; let us consider a more complex problem:
an automated taxi driver. Figure 2.4 summarizes the PEAS description for the taxi’s task
environment. We discuss each element in more detail in the following paragraphs.
First, what is the performance measure to which we would like our automated driver
to aspire? Desirable qualities include getting to the correct destination; minimizing fuel con-
sumption and wear and tear; minimizing the trip time or cost; minimizing violations of trafﬁc
laws and disturbances to other drivers; maximizing safety and passenger comfort; maximiz-
ing proﬁts. Obviously, some of these goals conﬂict, so tradeoffs will be required.
Next, what is the driving environment that the taxi will face? Any taxi driver must deal
with a variety of roads, ranging from rural lanes and urban alleys to 12-lane freeways. The
roads contain other trafﬁc, pedestrians, stray animals, road works, police cars, puddles, and
potholes. The taxi must also interact with potential and actual passengers. There are also
some optional choices. The taxi might need to operate in Southern California, where snow
is seldom a problem, or in Alaska, where it seldom is not. It could always be driving on the
right, or we might want it to be ﬂexible enough to drive on the left when in Britain or Japan.
Obviously, the more restricted the environment, the easier the design problem.
