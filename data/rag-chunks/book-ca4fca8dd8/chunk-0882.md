---
chunk_id: "book-ca4fca8dd8-chunk-0882"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 882
confidence: "first-pass"
extraction_method: "structured-local"
---

534
Chapter 15
Making Simple Decisions
extremely natural way to describe an agent’s preferences and are valid in many real-world
situations. For n attributes, assessing an additive value function requires assessing n separate
one-dimensional value functions rather than one n-dimensional function; typically, this repre-
sents an exponential reduction in the number of preference experiments that are needed. Even
when MPI does not strictly hold, as might be the case at extreme values of the attributes, an
additive value function might still provide a good approximation to the agent’s preferences.
This is especially true when the violations of MPI occur in portions of the attribute ranges
that are unlikely to occur in practice.
To understand MPI better, it helps to look at cases where it doesn’t hold. Suppose you
are at a medieval market, considering the purchase of some hunting dogs, some chickens,
and some wicker cages for the chickens. The hunting dogs are very valuable, but if you
don’t have enough cages for the chickens, the dogs will eat the chickens; hence, the tradeoff
between dogs and chickens depends strongly on the number of cages, and MPI is violated.
The existence of these kinds of interactions among various attributes makes it much harder to
assess the overall value function.
Preferences with uncertainty
When uncertainty is present in the domain, we also need to consider the structure of prefer-
ences between lotteries and to understand the resulting properties of utility functions, rather
than just value functions. The mathematics of this problem can become quite complicated,
so we present just one of the main results to give a ﬂavor of what can be done.
The basic notion of utility independence extends preference independence to cover lot-
Utility independence
teries: a set of attributes X is utility independent of a set of attributes Y if preferences be-
tween lotteries on the attributes in X are independent of the particular values of the attributes
in Y. A set of attributes is mutually utility independent (MUI) if each of its subsets is
Mutually utility
independent
utility-independent of the remaining attributes. Again, it seems reasonable to propose that
the airport attributes are MUI.
MUI implies that the agent’s behavior can be described using a multiplicative utility
function (Keeney, 1974). The general form of a multiplicative utility function is best seen by
Multiplicative utility
function
looking at the case for three attributes. For conciseness, we use Ui to mean Ui(xi):
U = k1U1 +k2U2 +k3U3 +k1k2U1U2 +k2k3U2U3 +k3k1U3U1
+k1k2k3U1U2U3 .
Although this does not look very simple, it contains just three single-attribute utility functions
and three constants. In general, an n-attribute problem exhibiting MUI can be modeled using
n single-attribute utilities and n constants. Each of the single-attribute utility functions can
be developed independently of the other attributes, and this combination will be guaranteed
to generate the correct overall preferences. Additional assumptions are required to obtain a
purely additive utility function.
15.5 Decision Networks
In this section, we look at a general mechanism for making rational decisions. The notation
is often called an inﬂuence diagram (Howard and Matheson, 1984), but we will use the
Inﬂuence diagram
more descriptive term decision network. Decision networks combine Bayesian networks
Decision network
