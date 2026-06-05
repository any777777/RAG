---
chunk_id: "book-ca4fca8dd8-chunk-0311"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 311
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
191
Drawing on this work and on results from database theory, Gottlob et al. (1999a, 1999b)
developed a notion, hypertree width, that is based on the characterization of the CSP as a
hypergraph. In addition to showing that any CSP with hypertree width w can be solved in
time O(nw+1 logn), they also showed that hypertree width subsumes all previously deﬁned
measures of “width” in the sense that there are cases where the hypertree width is bounded
and the other measures are unbounded.
The RELSAT algorithm of Bayardo and Schrag (1997) combined constraint learning and
backjumping and was shown to outperform many other algorithms of the time. This led to
AND-OR search algorithms applicable to both CSPs and probabilistic reasoning (Dechter
and Mateescu, 2007). Brown et al. (1988) introduce the idea of symmetry breaking in CSPs,
and Gent et al. (2006) give a survey.
The ﬁeld of distributed constraint satisfaction looks at solving CSPs when there is a
collection of agents, each of which controls a subset of the constraint variables. There have
been annual workshops on this problem since 2000, and good coverage elsewhere (Collin
et al., 1999; Pearce et al., 2008).
Comparing CSP algorithms is mostly an empirical science: few theoretical results show
that one algorithm dominates another on all problems; instead, we need to run experiments
to see which algorithms perform better on typical instances of problems. As Hooker (1995)
points out, we need to be careful to distinguish between competitive testing—as occurs in
competitions among algorithms based on run time—and scientiﬁc testing, whose goal is to
identify the properties of an algorithm that determine its efﬁcacy on a class of problems.
The textbooks by Apt (2003), Dechter (2003), Tsang (1993), and Lecoutre (2009), and
the collection by Rossi et al. (2006), are excellent resources on constraint processing. There
are several good survey articles, including those by Dechter and Frost (2002), and Bart´ak
et al. (2010). Carbonnel and Cooper (2016) survey tractable classes of CSPs. Kondrak and
van Beek (1997) give an analytical survey of backtracking search algorithms, and Bacchus
and van Run (1995) give a more empirical survey. Constraint programming is covered in the
books by Apt (2003) and Fruhwirth and Abdennadher (2003). Papers on constraint satisfac-
tion appear regularly in Artiﬁcial Intelligence and in the specialist journal Constraints; the
latest SAT solvers are described in the annual International SAT Competition. The primary
conference venue is the International Conference on Principles and Practice of Constraint
Programming, often called CP.
