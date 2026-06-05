---
chunk_id: "book-ca4fca8dd8-chunk-0108"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 108
confidence: "first-pass"
extraction_method: "structured-local"
---

64
Chapter 2
Intelligent Agents
that counts as deciding to do nothing. If the environment itself does not change with the
passage of time but the agent’s performance score does, then we say the environment is
semidynamic. Taxi driving is clearly dynamic: the other cars and the taxi itself keep moving
Semidynamic
while the driving algorithm dithers about what to do next. Chess, when played with a clock,
is semidynamic. Crossword puzzles are static.
Discrete vs. continuous: The discrete/continuous distinction applies to the state of the
Discrete
Continuous
environment, to the way time is handled, and to the percepts and actions of the agent. For
example, the chess environment has a ﬁnite number of distinct states (excluding the clock).
Chess also has a discrete set of percepts and actions. Taxi driving is a continuous-state and
continuous-time problem: the speed and location of the taxi and of the other vehicles sweep
through a range of continuous values and do so smoothly over time. Taxi-driving actions are
also continuous (steering angles, etc.). Input from digital cameras is discrete, strictly speak-
ing, but is typically treated as representing continuously varying intensities and locations.
Known vs. unknown: Strictly speaking, this distinction refers not to the environment
Known
Unknown
itself but to the agent’s (or designer’s) state of knowledge about the “laws of physics” of
the environment. In a known environment, the outcomes (or outcome probabilities if the
environment is nondeterministic) for all actions are given. Obviously, if the environment is
unknown, the agent will have to learn how it works in order to make good decisions.
The distinction between known and unknown environments is not the same as the one
between fully and partially observable environments. It is quite possible for a known environ-
ment to be partially observable—for example, in solitaire card games, I know the rules but
am still unable to see the cards that have not yet been turned over. Conversely, an unknown
environment can be fully observable—in a new video game, the screen may show the entire
game state but I still don’t know what the buttons do until I try them.
As noted on page 57, the performance measure itself may be unknown, either because
the designer is not sure how to write it down correctly or because the ultimate user—whose
preferences matter—is not known. For example, a taxi driver usually won’t know whether a
new passenger prefers a leisurely or speedy journey, a cautious or aggressive driving style.
A virtual personal assistant starts out knowing nothing about the personal preferences of its
new owner. In such cases, the agent may learn more about the performance measure based on
further interactions with the designer or user. This, in turn, suggests that the task environment
is necessarily viewed as a multiagent environment.
The hardest case is partially observable, multiagent, nondeterministic, sequential, dy-
namic, continuous, and unknown. Taxi driving is hard in all these senses, except that the
driver’s environment is mostly known. Driving a rented car in a new country with unfamiliar
geography, different trafﬁc laws, and nervous passengers is a lot more exciting.
Figure 2.6 lists the properties of a number of familiar environments. Note that the prop-
erties are not always cut and dried. For example, we have listed the medical-diagnosis task
as single-agent because the disease process in a patient is not proﬁtably modeled as an agent;
but a medical-diagnosis system might also have to deal with recalcitrant patients and skepti-
cal staff, so the environment could have a multiagent aspect. Furthermore, medical diagnosis
is episodic if one conceives of the task as selecting a diagnosis given a list of symptoms; the
problem is sequential if the task can include proposing a series of tests, evaluating progress
over the course of treatment, handling multiple patients, and so on.
