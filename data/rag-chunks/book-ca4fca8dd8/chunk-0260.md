---
chunk_id: "book-ca4fca8dd8-chunk-0260"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 260
confidence: "first-pass"
extraction_method: "structured-local"
---

160
Chapter 4
Search in Complex Environments
Bibliographical and Historical Notes
Local search techniques have a long history in mathematics and computer science. Indeed,
the Newton–Raphson method (Newton, 1671; Raphson, 1690) can be seen as a very efﬁ-
cient local search method for continuous spaces in which gradient information is available.
Brent (1973) is a classic reference for optimization algorithms that do not require such in-
formation. Beam search, which we have presented as a local search algorithm, originated
as a bounded-width variant of dynamic programming for speech recognition in the HARPY
system (Lowerre, 1976). A related algorithm is analyzed in depth by Pearl (1984, Ch. 5).
The topic of local search was reinvigorated in the early 1990s by surprisingly good results
for large constraint-satisfaction problems such as n-queens (Minton et al., 1992) and Boolean
satisﬁability (Selman et al., 1992) and by the incorporation of randomness, multiple simul-
taneous searches, and other improvements. This renaissance of what Christos Papadimitriou
has called “New Age” algorithms also sparked increased interest among theoretical computer
scientists (Koutsoupias and Papadimitriou, 1992; Aldous and Vazirani, 1994).
In the ﬁeld of operations research, a variant of hill climbing called tabu search has gained
Tabu search
popularity (Glover and Laguna, 1997). This algorithm maintains a tabu list of k previously
visited states that cannot be revisited; as well as improving efﬁciency when searching graphs,
this list can allow the algorithm to escape from some local minima.
Another useful improvement on hill climbing is the STAGE algorithm (Boyan and Moore,
1998). The idea is to use the local maxima found by random-restart hill climbing to get an
idea of the overall shape of the landscape. The algorithm ﬁts a smooth quadratic surface to
the set of local maxima and then calculates the global maximum of that surface analytically.
This becomes the new restart point. Gomes et al. (1998) showed that the run times of system-
atic backtracking algorithms often have a heavy-tailed distribution, which means that the
Heavy-tailed
distribution
probability of a very long run time is more than would be predicted if the run times were ex-
ponentially distributed. When the run time distribution is heavy-tailed, random restarts ﬁnd a
solution faster, on average, than a single run to completion. Hoos and St¨utzle (2004) provide
a book-length coverage of the topic.
Simulated annealing was ﬁrst described by Kirkpatrick et al. (1983), who borrowed
directly from the Metropolis algorithm (which is used to simulate complex systems in
physics (Metropolis et al., 1953) and was supposedly invented at a Los Alamos dinner party).
Simulated annealing is now a ﬁeld in itself, with hundreds of papers published every year.
Finding optimal solutions in continuous spaces is the subject matter of several ﬁelds,
including optimization theory, optimal control theory, and the calculus of variations.
The basic techniques are explained well by Bishop (1995); Press et al. (2007) cover a wide
range of algorithms and provide working software.
Researchers have taken inspiration for search and optimization algorithms from a wide
variety of ﬁelds of study: metallurgy (simulated annealing); biology (genetic algorithms);
neuroscience (neural networks); mountaineering (hill climbing); economics (market-based
algorithms (Dias et al., 2006)); physics (particle swarms (Li and Yao, 2012) and spin glasses
(M´ezard et al., 1987)); animal behavior (reinforcement learning, grey wolf optimizers (Mir-
jalili and Lewis, 2014)); ornithology (Cuckoo search (Yang and Deb, 2014)); entomology
(ant colony (Dorigo et al., 2008), bee colony (Karaboga and Basturk, 2007), ﬁreﬂy (Yang,
2009) and glowworm (Krishnanand and Ghose, 2009) optimization); and others.
