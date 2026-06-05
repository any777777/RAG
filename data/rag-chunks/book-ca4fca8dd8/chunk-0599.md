---
chunk_id: "book-ca4fca8dd8-chunk-0599"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 599
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 11.1
Deﬁnition of Classical Planning
363
and “ground atomic” means there is a single predicate, and if there are any arguments, they
must be constants. For example, Poor∧Unknown might represent the state of a hapless agent,
and At(Truck1,Melbourne)∧At(Truck2,Sydney) could represent a state in a package delivery
problem. PDDL uses database semantics: the closed-world assumption means that any
ﬂuents that are not mentioned are false, and the unique names assumption means that Truck1
and Truck2 are distinct.
The following ﬂuents are not allowed in a state: At(x,y) (because it has variables), ¬Poor
(because it is a negation), and At(Spouse(Ali),Sydney) (because it uses a function symbol,
Spouse). When convenient, we can think of the conjunction of ﬂuents as a set of ﬂuents.
An action schema represents a family of ground actions. For example, here is an action
Action schema
schema for ﬂying a plane from one location to another:
Action(Fly(p,from,to),
PRECOND:At(p,from)∧Plane(p)∧Airport(from)∧Airport(to)
EFFECT:¬At(p,from)∧At(p,to))
The schema consists of the action name, a list of all the variables used in the schema, a
precondition and an effect. The precondition and the effect are each conjunctions of literals
Precondition
Eﬀect
(positive or negated atomic sentences). We can choose constants to instantiate the variables,
yielding a ground (variable-free) action:
Action(Fly(P1,SFO,JFK),
PRECOND:At(P1,SFO)∧Plane(P1)∧Airport(SFO)∧Airport(JFK)
EFFECT:¬At(P1,SFO)∧At(P1,JFK))
A ground action a is applicable in state s if s entails the precondition of a; that is, if every
positive literal in the precondition is in s and every negated literal is not.
The result of executing applicable action a in state s is deﬁned as a state s′ which is
represented by the set of ﬂuents formed by starting with s, removing the ﬂuents that appear as
negative literals in the action’s effects (what we call the delete list or DEL(a)), and adding the
Delete list
ﬂuents that are positive literals in the action’s effects (what we call the add list or ADD(a)):
Add list
RESULT(s,a) = (s−DEL(a))∪ADD(a).
(11.1)
For example, with the action Fly(P1,SFO,JFK), we would remove the ﬂuent At(P1,SFO)
and add the ﬂuent At(P1,JFK).
A set of action schemas serves as a deﬁnition of a planning domain. A speciﬁc problem
within the domain is deﬁned with the addition of an initial state and a goal. The initial
state is a conjunction of ground ﬂuents (introduced with the keyword Init in Figure 11.1).
As with all states, the closed-world assumption is used, which means that any atoms that
are not mentioned are false. The goal (introduced with Goal) is just like a precondition: a
conjunction of literals (positive or negative) that may contain variables. For example, the goal
At(C1,SFO)∧¬At(C2,SFO)∧At(p,SFO), refers to any state in which cargo C1 is at SFO but
C2 is not, and in which there is a plane at SFO.
11.1.1 Example domain: Air cargo transport
Figure 11.1 shows an air cargo transport problem involving loading and unloading cargo and
ﬂying it from place to place. The problem can be deﬁned with three actions: Load, Unload,
and Fly. The actions affect two predicates: In(c, p) means that cargo c is inside plane p,
and At(x,a) means that object x (either plane or cargo) is at airport a. Note that some care
