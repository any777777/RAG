---
chunk_id: "book-ca4fca8dd8-chunk-0602"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 602
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 365

Section 11.1
Deﬁnition of Classical Planning
365
Init(Tire(Flat) ∧Tire(Spare) ∧At(Flat,Axle) ∧At(Spare,Trunk))
Goal(At(Spare,Axle))
Action(Remove(obj,loc),
PRECOND: At(obj,loc)
EFFECT: ¬ At(obj,loc) ∧At(obj,Ground))
Action(PutOn(t, Axle),
PRECOND: Tire(t) ∧At(t,Ground) ∧¬ At(Flat,Axle) ∧¬ At(Spare,Axle)
EFFECT: ¬ At(t,Ground) ∧At(t,Axle))
Action(LeaveOvernight,
PRECOND:
EFFECT: ¬ At(Spare,Ground) ∧¬ At(Spare,Axle) ∧¬ At(Spare,Trunk)
∧¬ At(Flat,Ground) ∧¬ At(Flat,Axle) ∧¬ At(Flat, Trunk))
Figure 11.2 The simple spare tire problem.
Start State
Goal State
B
A
C
A
B
C
Figure 11.3 Diagram of the blocks-world problem in Figure 11.4.
Init(On(A,Table) ∧On(B,Table) ∧On(C,A)
∧Block(A) ∧Block(B) ∧Block(C) ∧Clear(B) ∧Clear(C) ∧Clear(Table))
Goal(On(A,B) ∧On(B,C))
Action(Move(b,x,y),
PRECOND: On(b,x) ∧Clear(b) ∧Clear(y) ∧Block(b) ∧Block(y) ∧
(b̸=x) ∧(b̸=y) ∧(x̸=y),
EFFECT: On(b,y) ∧Clear(x) ∧¬On(b,x) ∧¬Clear(y))
Action(MoveToTable(b,x),
PRECOND: On(b,x) ∧Clear(b) ∧Block(b) ∧Block(x),
EFFECT: On(b,Table) ∧Clear(x) ∧¬On(b,x))
Figure 11.4 A planning problem in the blocks world: building a three-block tower. One
solution is the sequence [MoveToTable(C,A),Move(B,Table,C),Move(A,Table,B)].

## Page 366
