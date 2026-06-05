---
chunk_id: "book-ca4fca8dd8-chunk-1621"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1621
confidence: "first-pass"
extraction_method: "structured-local"
---

984
Chapter 26
Robotics
humanoid robots, and some software simulations. Stone (2016) describes recent innovations
in RoboCup.
The DARPA Grand Challenge, organized by DARPA in 2004 and 2005, required au-
tonomous vehicles to travel more than 200 kilometers through the desert in less than ten
hours (Buehler et al., 2006). In the original event in 2004, no robot traveled more than eight
miles, leading many to believe the prize would never be claimed. In 2005, Stanford’s robot
Stanley won the competition in just under seven hours (Thrun, 2006). DARPA then orga-
nized the Urban Challenge, a competition in which robots had to navigate 60 miles in an
urban environment with other trafﬁc. Carnegie Mellon University’s robot BOSS took ﬁrst
place and claimed the $2 million prize (Urmson and Whittaker, 2008). Early pioneers in the
development of robotic cars included Dickmanns and Zapp (1987) and Pomerleau (1993).
The ﬁeld of robotic mapping has evolved from two distinct origins. The ﬁrst thread
began with work by Smith and Cheeseman (1986), who applied Kalman ﬁlters to the simulta-
neous localization and mapping (SLAM) problem. This algorithm was ﬁrst implemented by
Moutarlier and Chatila (1989) and later extended by Leonard and Durrant-Whyte (1992); see
Dissanayake et al. (2001) for an overview of early Kalman ﬁlter variations. The second thread
began with the development of the occupancy grid representation for probabilistic mapping,
Occupancy grid
which speciﬁes the probability that each (x,y) location is occupied by an obstacle (Moravec
and Elfes, 1985).
Kuipers and Levitt (1988) were among the ﬁrst to propose topological rather than metric
mapping, motivated by models of human spatial cognition. A seminal paper by Lu and Milios
(1997) recognized the sparseness of the simultaneous localization and mapping problem,
which gave rise to the development of nonlinear optimization techniques by Konolige (2004)
and Montemerlo and Thrun (2004), as well as hierarchical methods by Bosse et al. (2004).
Shatkay and Kaelbling (1997) and Thrun et al. (1998) introduced the EM algorithm into the
ﬁeld of robotic mapping for data association. An overview of probabilistic mapping methods
can be found in (Thrun et al., 2005).
Early mobile robot localization techniques are surveyed by Borenstein et al. (1996).
Although Kalman ﬁltering was well known as a localization method in control theory for
decades, the general probabilistic formulation of the localization problem did not appear in
the AI literature until much later, through the work of Tom Dean and colleagues (Dean et al.,
1990) and of Simmons and Koenig (1995). The latter work introduced the term Markov
localization. The ﬁrst real-world application of this technique was by Burgard et al. (1999),
Markov localization
through a series of robots that were deployed in museums. Monte Carlo localization based
on particle ﬁlters was developed by Fox et al. (1999) and is now widely used. The Rao-
Blackwellized particle ﬁlter combines particle ﬁltering for robot localization with exact
Rao-Blackwellized
particle ﬁlter
ﬁltering for map building (Murphy and Russell, 2001; Montemerlo et al., 2002).
A great deal of early work on motion planning focused on geometric algorithms for de-
terministic and fully observable motion planning problems. The PSPACE-hardness of robot
motion planning was shown in a seminal paper by Reif (1979). The conﬁguration space rep-
resentation is due to Lozano-Perez (1983). A series of papers by Schwartz and Sharir on what
they called piano movers problems (Schwartz et al., 1987) was highly inﬂuential.
Piano movers
Recursive cell decomposition for conﬁguration space planning was originated in the work
of Brooks and Lozano-Perez (1985) and improved signiﬁcantly by Zhu and Latombe (1991).
The earliest skeletonization algorithms were based on Voronoi diagrams (Rowat, 1979) and
