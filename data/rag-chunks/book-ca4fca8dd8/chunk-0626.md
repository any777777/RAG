---
chunk_id: "book-ca4fca8dd8-chunk-0626"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 626
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 379

Section 11.4
Hierarchical Planning
379
(a)
(b)
Figure 11.9 Schematic examples of reachable sets. The set of goal states is shaded in purple.
Black and red arrows indicate possible implementations of h1 and h2, respectively. (a) The
reachable set of an HLA h1 in a state s. (b) The reachable set for the sequence [h1,h2].
Because this intersects the goal set, the sequence achieves the goal.
It treats the HLA’s multiple outcomes exactly as if the HLA were a nondeterministic action,
as in Section 4.3. For our case, the agent itself will choose the implementation.
The programming languages community has coined the term demonic nondeterminism
Demonic
nondeterminism
for the case where an adversary makes the choices, contrasting this with angelic nondeter-
minism, where the agent itself makes the choices. We borrow this term to deﬁne angelic
Angelic
nondeterminism
semantics for HLA descriptions. The basic concept required for understanding angelic se-
Angelic semantics
mantics is the reachable set of an HLA: given a state s, the reachable set for an HLA h,
Reachable set
written as REACH(s,h), is the set of states reachable by any of the HLA’s implementations.
The key idea is that the agent can choose which element of the reachable set it ends up in
when it executes the HLA; thus, an HLA with multiple reﬁnements is more “powerful” than
the same HLA with fewer reﬁnements. We can also deﬁne the reachable set of a sequence of
HLAs. For example, the reachable set of a sequence [h1,h2] is the union of all the reachable
sets obtained by applying h2 in each state in the reachable set of h1:
REACH(s,[h1,h2]) =
[
s′∈REACH(s, h1)
REACH(s′,h2).
Given these deﬁnitions, a high-level plan—a sequence of HLAs—achieves the goal if its
reachable set intersects the set of goal states. (Compare this to the much stronger condition
for demonic semantics, where every member of the reachable set has to be a goal state.)
Conversely, if the reachable set doesn’t intersect the goal, then the plan deﬁnitely doesn’t
work. Figure 11.9 illustrates these ideas.
The notion of reachable sets yields a straightforward algorithm: search among high-
level plans, looking for one whose reachable set intersects the goal; once that happens, the
algorithm can commit to that abstract plan, knowing that it works, and focus on reﬁning the
plan further. We will return to the algorithmic issues later; for now consider how the effects

## Page 380
