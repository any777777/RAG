---
chunk_id: "book-ca4fca8dd8-chunk-0522"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 522
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 9.5
Resolution
319
binary resolution rule by itself does not yield a complete inference procedure. The full reso-
lution rule resolves subsets of literals in each clause that are uniﬁable. An alternative approach
is to extend factoring—the removal of redundant literals—to the ﬁrst-order case. Proposi-
tional factoring reduces two literals to one if they are identical; ﬁrst-order factoring reduces
two literals to one if they are uniﬁable. The uniﬁer must be applied to the entire clause. The
combination of binary resolution and factoring is complete.
9.5.3 Example proofs
Resolution proves that KB |= α by proving that KB ∧¬α unsatisﬁable—that is, by deriving
the empty clause. The algorithmic approach is identical to the propositional case, described
in Figure 7.13, so we need not repeat it here. Instead, we give two example proofs. The ﬁrst
is the crime example from Section 9.3. The sentences in CNF are
¬American(x)∨¬Weapon(y)∨¬Sells(x,y,z)∨¬Hostile(z)∨Criminal(x)
¬Missile(x)∨¬Owns(Nono,x)∨Sells(West,x,Nono)
¬Enemy(x,America)∨Hostile(x)
¬Missile(x)∨Weapon(x)
Owns(Nono,M1)
Missile(M1)
American(West)
Enemy(Nono,America).
We also include the negated goal ¬Criminal(West). The resolution proof is shown in Fig-
ure 9.10. Notice the structure: single “spine” beginning with the goal clause, resolving against
clauses from the knowledge base until the empty clause is generated. This is characteristic
of resolution on Horn clause knowledge bases. In fact, the clauses along the main spine
correspond exactly to the consecutive values of the goals variable in the backward-chaining
algorithm of Figure 9.6. This is because we always choose to resolve with a clause whose
positive literal uniﬁes with the leftmost literal of the “current” clause on the spine; this is
¬American(x) 
¬Weapon(y) 
¬Sells(x,y,z) ¬Hostile(z) Criminal(x)
¬Criminal(West)
¬Enemy(Nono,America)
Enemy(Nono,America)
¬Missile(x) Weapon(x)
¬Weapon(y)
¬Sells(West,y,z) ¬Hostile(z)
Missile(M1)
¬Missile(y)
¬Sells(West,y,z) ¬Hostile(z)
¬Missile(x) ¬Owns(Nono,x) 
Sells(West,x,Nono)
¬Sells(West,M1,z)
¬Hostile(z)
¬American(West) ¬Weapon(y) ¬Sells(West,y,z) ¬Hostile(z)
American(West)
¬Missile(M1) ¬Owns(Nono,M1) ¬Hostile(Nono)
Missile(M1)
¬Owns(Nono,M1) ¬Hostile(Nono)
Owns(Nono,M1)
¬Enemy(x,America) Hostile(x)
¬Hostile(Nono)
^
^
^
^
^
^
^
^
^
^
^
^
^
^
^
^
^
^
^
Figure 9.10 A resolution proof that West is a criminal. At each resolution step, the literals
that unify are in bold and the clause with the positive literal is shaded blue.
