---
chunk_id: "book-ca4fca8dd8-chunk-0675"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 675
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 12.1
Acting under Uncertainty
405
One confusing point is that at the time of our diagnosis, there is no uncertainty in the
actual world: the patient either has a cavity or doesn’t. So what does it mean to say the
probability of a cavity is 0.8? Shouldn’t it be either 0 or 1? The answer is that probability
statements are made with respect to a knowledge state, not with respect to the real world. We
say “The probability that the patient has a cavity, given that she has a toothache, is 0.8.” If we
later learn that the patient has a history of gum disease, we can make a different statement:
“The probability that the patient has a cavity, given that she has a toothache and a history of
gum disease, is 0.4.” If we gather further conclusive evidence against a cavity, we can say
“The probability that the patient has a cavity, given all we now know, is almost 0.” Note that
these statements do not contradict each other; each is a separate assertion about a different
knowledge state.
12.1.2 Uncertainty and rational decisions
Consider again the A90 plan for getting to the airport. Suppose it gives us a 97% chance
of catching our ﬂight. Does this mean it is a rational choice? Not necessarily: there might
be other plans, such as A180, with higher probabilities. If it is vital not to miss the ﬂight,
then it is worth risking the longer wait at the airport. What about A1440, a plan that involves
leaving home 24 hours in advance? In most circumstances, this is not a good choice, because
although it almost guarantees getting there on time, it involves an intolerable wait—not to
mention a possibly unpleasant diet of airport food.
To make such choices, an agent must ﬁrst have preferences among the different possible
Preference
outcomes of the various plans. An outcome is a completely speciﬁed state, including such
Outcome
factors as whether the agent arrives on time and the length of the wait at the airport. We
use utility theory to represent preferences and reason quantitatively with them. (The term
Utility theory
utility is used here in the sense of “the quality of being useful,” not in the sense of the electric
company or water works.) Utility theory says that every state (or state sequence) has a degree
of usefulness, or utility, to an agent and that the agent will prefer states with higher utility.
The utility of a state is relative to an agent. For example, the utility of a state in which
White has checkmated Black in a game of chess is obviously high for the agent playing
White, but low for the agent playing Black. But we can’t go strictly by the scores of 1, 1/2,
and 0 that are dictated by the rules of tournament chess—some players (including the authors)
might be thrilled with a draw against the world champion, whereas other players (including
the former world champion) might not. There is no accounting for taste or preferences: you
might think that an agent who prefers jalape˜no bubble-gum ice cream to chocolate chip is
odd, but you could not say the agent is irrational. A utility function can account for any set of
preferences—quirky or typical, noble or perverse. Note that utilities can account for altruism,
simply by including the welfare of others as one of the factors.
Preferences, as expressed by utilities, are combined with probabilities in the general the-
ory of rational decisions called decision theory:
Decision theory
Decision theory = probability theory+utility theory.
The fundamental idea of decision theory is that an agent is rational if and only if it chooses ◀
the action that yields the highest expected utility, averaged over all the possible outcomes
of the action. This is called the principle of maximum expected utility (MEU). Here, “ex-
Maximum expected
utility (MEU)
pected” means the “average,” or “statistical mean” of the outcome utilities, weighted by the
probability of the outcome. We saw this principle in action in Chapter 6 when we touched
