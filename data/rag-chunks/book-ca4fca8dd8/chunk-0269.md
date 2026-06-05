---
chunk_id: "book-ca4fca8dd8-chunk-0269"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 269
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 166

166
Chapter 5
Constraint Satisfaction Problems
Western
Australia
Northern
Territory
South
Australia
Queensland
New
South
Wales
Victoria
Tasmania
Q
NT
WA
SA
V
NSW
T
(a)
(b)
Figure 5.1 (a) The principal states and territories of Australia. Coloring this map can be
viewed as a constraint satisfaction problem (CSP). The goal is to assign colors to each re-
gion so that no neighboring regions have the same color. (b) The map-coloring problem
represented as a constraint graph.
5.1.2 Example problem: Job-shop scheduling
Factories have the problem of scheduling a day’s worth of jobs, subject to various constraints.
In practice, many of these problems are solved with CSP techniques. Consider the problem of
scheduling the assembly of a car. The whole job is composed of tasks, and we can model each
task as a variable, where the value of each variable is the time that the task starts, expressed
as an integer number of minutes. Constraints can assert that one task must occur before
another—for example, a wheel must be installed before the hubcap is put on—and that only
so many tasks can go on at once. Constraints can also specify that a task takes a certain
amount of time to complete.
We consider a small part of the car assembly, consisting of 15 tasks: install axles (front
and back), afﬁx all four wheels (right and left, front and back), tighten nuts for each wheel,
afﬁx hubcaps, and inspect the ﬁnal assembly. We can represent the tasks with 15 variables:
X = {AxleF,AxleB,WheelRF,WheelLF,WheelRB,WheelLB,NutsRF,
NutsLF,NutsRB,NutsLB,CapRF,CapLF,CapRB,CapLB,Inspect}.
Next, we represent precedence constraints between individual tasks. Whenever a task T1
Precedence
constraint
must occur before task T2, and task T1 takes duration d1 to complete, we add an arithmetic
constraint of the form
T1 +d1 ≤T2 .
In our example, the axles have to be in place before the wheels are put on, and it takes 10
minutes to install an axle, so we write
AxleF +10 ≤WheelRF;
AxleF +10 ≤WheelLF;
AxleB +10 ≤WheelRB;
AxleB +10 ≤WheelLB .

## Page 167
