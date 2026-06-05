---
chunk_id: "book-ca4fca8dd8-chunk-0102"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 102
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 2.3
The Nature of Environments
61
Agent Type
Performance
Measure
Environment
Actuators
Sensors
Taxi driver
Safe, fast,
legal,
comfortable
trip, maximize
proﬁts,
minimize
impact on
other road
users
Roads, other
trafﬁc, police,
pedestrians,
customers,
weather
Steering,
accelerator,
brake, signal,
horn, display,
speech
Cameras, radar,
speedometer, GPS, engine
sensors, accelerometer,
microphones, touchscreen
Figure 2.4 PEAS description of the task environment for an automated taxi driver.
The actuators for an automated taxi include those available to a human driver: control
over the engine through the accelerator and control over steering and braking. In addition, it
will need output to a display screen or voice synthesizer to talk back to the passengers, and
perhaps some way to communicate with other vehicles, politely or otherwise.
The basic sensors for the taxi will include one or more video cameras so that it can see, as
well as lidar and ultrasound sensors to detect distances to other cars and obstacles. To avoid
speeding tickets, the taxi should have a speedometer, and to control the vehicle properly,
especially on curves, it should have an accelerometer. To determine the mechanical state of
the vehicle, it will need the usual array of engine, fuel, and electrical system sensors. Like
many human drivers, it might want to access GPS signals so that it doesn’t get lost. Finally,
it will need touchscreen or voice input for the passenger to request a destination.
In Figure 2.5, we have sketched the basic PEAS elements for a number of additional
agent types. Further examples appear in Exercise 2.PEAS. The examples include physical
as well as virtual environments. Note that virtual task environments can be just as complex
as the “real” world: for example, a software agent (or software robot or softbot) that trades
Software agent
Softbot
on auction and reselling Web sites deals with millions of other users and billions of objects,
many with real images.
2.3.2 Properties of task environments
The range of task environments that might arise in AI is obviously vast. We can, however,
identify a fairly small number of dimensions along which task environments can be catego-
rized. These dimensions determine, to a large extent, the appropriate agent design and the
applicability of each of the principal families of techniques for agent implementation. First
we list the dimensions, then we analyze several task environments to illustrate the ideas. The
deﬁnitions here are informal; later chapters provide more precise statements and examples of
each kind of environment.
Fully observable vs. partially observable: If an agent’s sensors give it access to the
Fully observable
Partially observable
complete state of the environment at each point in time, then we say that the task environ-
ment is fully observable. A task environment is effectively fully observable if the sensors
detect all aspects that are relevant to the choice of action; relevance, in turn, depends on the
