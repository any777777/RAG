---
chunk_id: "book-ca4fca8dd8-chunk-1079"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1079
confidence: "first-pass"
extraction_method: "structured-local"
---

646
Chapter 18
Probabilistic Programming
Recommendation(C1, B1)
Honest(C1)
Kindness(C1)
Quality(B1)
Recommendation(C1, B2)
Quality(B2)
Fan(C1, A1)
Fan(C1, A2)
Author(B2)
Figure 18.3 Fragment of the equivalent Bayes net for the book recommendation RPM when
Author(B2) is unknown.
authors, A1 and A2. Then Author(B2) is a random variable with two possible values, A1 and
A2, and it is a parent of Recommendation(C1,B2). The variables Fan(C1,A1) and Fan(C1,A2)
are parents too. The conditional distribution for Recommendation(C1,B2) is then essentially a
multiplexer in which the Author(B2) parent acts as a selector to choose which of Fan(C1,A1)
Multiplexer
and Fan(C1,A2) actually gets to inﬂuence the recommendation. A fragment of the equivalent
Bayes net is shown in Figure 18.3. Uncertainty in the value of Author(B2), which affects the
dependency structure of the network, is an instance of relational uncertainty.
Relational
uncertainty
In case you are wondering how the system can possibly work out who the author of B2 is:
consider the possibility that three other customers are fans of A1 (and have no other favorite
authors in common) and all three have given B2 a 5, even though most other customers ﬁnd
it quite dismal. In that case, it is extremely likely that A1 is the author of B2. The emergence
of sophisticated reasoning like this from an RPM model of just a few lines is an intriguing
example of how probabilistic inﬂuences spread through the web of interconnections among
objects in the model. As more dependencies and more objects are added, the picture conveyed
by the posterior distribution often becomes clearer and clearer.
18.1.2 Example: Rating player skill levels
Many competitive games have a numerical measure of players’ skill levels, sometimes called
a rating. Perhaps the best-known is the Elo rating for chess players, which rates a typical be-
Rating
ginner at around 800 and the world champion usually somewhere above 2800. Although Elo
ratings have a statistical basis, they have some ad hoc elements. We can develop a Bayesian
rating scheme as follows: each player i has an underlying skill level Skill(i); in each game g,
i’s actual performance is Performance(i,g), which may vary from the underlying skill level;
and the winner of g is the player whose performance in g is better. As an RPM, the model
looks like this:
Skill(i) ∼N(µ,σ2)
Performance(i,g) ∼N(Skill(i),β2)
Win(i,j,g) = if Game(g,i, j) then (Performance(i,g) > Performance(j,g))
where β2 is the variance of a player’s actual performance in any speciﬁc game relative to the
player’s underlying skill level. Given a set of players and games, as well as outcomes for
some of the games, an RPM inference engine can compute a posterior distribution over the
skill of each player and the probable outcome of any additional game that might be played.
