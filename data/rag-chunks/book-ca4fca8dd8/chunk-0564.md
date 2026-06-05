---
chunk_id: "book-ca4fca8dd8-chunk-0564"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 564
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 10.3
Events
341
successor-state axiom can say that the tub is empty before the action and full when the action
is done, but it can’t talk about what happens during the action. It also can’t easily describe
two actions happening at the same time—such as brushing one’s teeth while waiting for the
tub to ﬁll. To handle such cases we introduce an approach known as event calculus.
Event calculus
The objects of event calculus are events, ﬂuents, and time points. At(Shankar,Berkeley)
is a ﬂuent: an object that refers to the fact of Shankar being in Berkeley. The event E1 of
Shankar ﬂying from San Francisco to Washington, D.C., is described as
E1 ∈Flyings∧Flyer(E1,Shankar)∧Origin(E1,SF)∧Destination(E1,DC).
where Flyings is the category of all ﬂying events. By reifying events we make it possible to
add any amount of arbitrary information about them. For example, we can say that Shankar’s
ﬂight was bumpy with Bumpy(E1). In an ontology where events are n-ary predicates, there
would be no way to add extra information like this; moving to an n+1-ary predicate isn’t a
scalable solution.
To assert that a ﬂuent is actually true starting at some point in time t1 and continuing
to time t2, we use the predicate T, as in T(At(Shankar,Berkeley),t1,t2). Similarly, we use
Happens(E1,t1,t2) to say that the event E1 actually happened, starting at time t1 and ending
at time t2. The complete set of predicates for one version of the event calculus4 is:
T(f,t1,t2)
Fluent f is true for all times between t1 and t2
Happens(e,t1,t2)
Event e starts at time t1 and ends at t2
Initiates(e, f,t)
Event e causes ﬂuent f to become true at time t
Terminates(e, f,t)
Event e causes ﬂuent f to cease to be true at time t
Initiated(f,t1,t2)
Fluent f become true at some point between t1 and t2
Terminated(f,t1,t2)
Fluent f cease to be true at some point between t1 and t2
t1 < t2
Time point t1 occurs before time t2
We can describe the effects of a ﬂying event:
E = Flyings(a,here,there)∧Happens(E,t1,t2) ⇒
Terminates(E,At(a,here),t1)∧Initiates(E,At(a,there),t2)
We assume a distinguished event, Start, that describes the initial state by saying which ﬂuents
are true (using Initiates) or false (using Terminated) at the start time. We can then describe
what ﬂuents are true at what points in time with a pair of axioms for T and ¬T that follow the
same general format as the successor-state axioms: Assume an event happens between time
t1 and t3, and at t2 somewhere in that time interval the event changes the value of ﬂuent f,
either initiating it (making it true) or terminating it (making it false). Then at time t4 in the
future, if no other intervening event has changed the ﬂuent (either terminated or initiated it,
respectively), then the ﬂuent will have maintained its value. Formally, the axioms are:
Happens(e,t1,t3)∧Initiates(e, f,t2)∧¬Terminated(f,t2,t4)∧t1 ≤t2 ≤t3 ≤t4 ⇒
T(f,t2,t4)
Happens(e,t1,t3)∧Terminates(e, f,t2)∧¬Initiated(f,t2,t4))∧t1 ≤t2 ≤t3 ≤t4 ⇒
¬T(f,t2,t4)
4
Our version is based on Shanahan (1999), but with some alterations.
