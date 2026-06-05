---
chunk_id: "book-ca4fca8dd8-chunk-1546"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1546
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 26
ROBOTICS
In which agents are endowed with sensors and physical effectors with which to move about
and make mischief in the real world.
26.1 Robots
Robots are physical agents that perform tasks by manipulating the physical world. To do
Robot
so, they are equipped with effectors such as legs, wheels, joints, and grippers. Effectors are
Eﬀector
designed to assert physical forces on the environment. When they do this, a few things may
happen: the robot’s state might change (e.g., a car spins its wheels and makes progress on the
road as a result), the state of the environment might change (e.g., a robot arm uses its gripper
to push a mug across the counter), and even the state of the people around the robot might
change (e.g., an exoskeleton moves and that changes the conﬁguration of a person’s leg; or
a mobile robot makes progress toward the elevator doors, and a person notices and is nice
enough to move out of the way, or even push the button for the robot).
Robots are also equipped with sensors, which enable them to perceive their environment.
Sensor
Present-day robotics employs a diverse set of sensors, including cameras, radars, lasers, and
microphones to measure the state of the environment and of the people around it; and gyro-
scopes, strain and torque sensors, and accelerometers to measure the robot’s own state.
Maximizing expected utility for a robot means choosing how to actuate its effectors to
assert the right physical forces—the ones that will lead to changes in state that accumulate as
much expected reward as possible. Ultimately, robots are trying to accomplish some task in
the physical world.
Robots operate in environments that are partially observable and stochastic: cameras
cannot see around corners, and gears can slip. Moreover, the people acting in that same
environment are unpredictable, so the robot needs to make predictions about them.
Robots usually model their environment with a continuous state space (the robot’s po-
sition has continuous coordinates) and a continuous action space (the amount of current a
robot sends to its motor is also measured in continuous units). Some robots operate in high-
dimensional spaces: cars need to know the position, orientation, and velocity of themselves
and the nearby agents; robot arms have six or seven joints that can each be independently
moved; and robots that mimic the human body have hundreds of joints.
Robotic learning is constrained because the real world stubbornly refuses to operate faster
than real time. In a simulated environment, it is possible to use learning algorithms (such as
the Q-learning algorithm described in Chapter 23) to learn in a few hours from millions of
trials. In a real environment, it might take years to run these trials, and the robot cannot risk
(and thus cannot learn from) a trial that might cause harm. Thus, transferring what has been
