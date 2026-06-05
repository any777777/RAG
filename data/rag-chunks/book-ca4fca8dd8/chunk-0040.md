---
chunk_id: "book-ca4fca8dd8-chunk-0040"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 40
confidence: "first-pass"
extraction_method: "structured-local"
---

28
Chapter 1
Introduction
The science of economics originated in 1776, when Adam Smith (1723–1790) published An
Inquiry into the Nature and Causes of the Wealth of Nations. Smith proposed to analyze
economies as consisting of many individual agents attending to their own interests. Smith
was not, however, advocating ﬁnancial greed as a moral position: his earlier (1759) book The
Theory of Moral Sentiments begins by pointing out that concern for the well-being of others
is an essential component of the interests of every individual.
Most people think of economics as being about money, and indeed the ﬁrst mathemati-
cal analysis of decisions under uncertainty, the maximum-expected-value formula of Arnauld
(1662), dealt with the monetary value of bets. Daniel Bernoulli (1738) noticed that this for-
mula didn’t seem to work well for larger amounts of money, such as investments in maritime
trading expeditions. He proposed instead a principle based on maximization of expected
utility, and explained human investment choices by proposing that the marginal utility of an
additional quantity of money diminished as one acquired more money.
L´eon Walras (pronounced “Valrasse”) (1834–1910) gave utility theory a more general
foundation in terms of preferences between gambles on any outcomes (not just monetary
outcomes). The theory was improved by Ramsey (1931) and later by John von Neumann
and Oskar Morgenstern in their book The Theory of Games and Economic Behavior (1944).
Economics is no longer the study of money; rather it is the study of desires and preferences.
Decision theory, which combines probability theory with utility theory, provides a for-
Decision theory
mal and complete framework for individual decisions (economic or otherwise) made under
uncertainty—that is, in cases where probabilistic descriptions appropriately capture the de-
cision maker’s environment. This is suitable for “large” economies where each agent need
pay no attention to the actions of other agents as individuals. For “small” economies, the
situation is much more like a game: the actions of one player can signiﬁcantly affect the
utility of another (either positively or negatively). Von Neumann and Morgenstern’s develop-
ment of game theory (see also Luce and Raiffa, 1957) included the surprising result that, for
some games, a rational agent should adopt policies that are (or least appear to be) random-
ized. Unlike decision theory, game theory does not offer an unambiguous prescription for
selecting actions. In AI, decisions involving multiple agents are studied under the heading of
multiagent systems (Chapter 17).
Economists, with some exceptions, did not address the third question listed above: how to
make rational decisions when payoffs from actions are not immediate but instead result from
several actions taken in sequence. This topic was pursued in the ﬁeld of operations research,
Operations research
which emerged in World War II from efforts in Britain to optimize radar installations, and later
found innumerable civilian applications. The work of Richard Bellman (1957) formalized a
class of sequential decision problems called Markov decision processes, which we study in
Chapter 16 and, under the heading of reinforcement learning, in Chapter 23.
Work in economics and operations research has contributed much to our notion of rational
agents, yet for many years AI research developed along entirely separate paths. One reason
was the apparent complexity of making rational decisions. The pioneering AI researcher
Herbert Simon (1916–2001) won the Nobel Prize in economics in 1978 for his early work
showing that models based on satisﬁcing—making decisions that are “good enough,” rather
Satisﬁcing
than laboriously calculating an optimal decision—gave a better description of actual human
behavior (Simon, 1947). Since the 1990s, there has been a resurgence of interest in decision-
theoretic techniques for AI.
