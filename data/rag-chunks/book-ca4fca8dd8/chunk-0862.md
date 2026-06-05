---
chunk_id: "book-ca4fca8dd8-chunk-0862"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 862
confidence: "first-pass"
extraction_method: "structured-local"
---

522
Chapter 15
Making Simple Decisions
• Expected Utility of a Lottery: The utility of a lottery is the sum of the probability of
each outcome times the utility of that outcome.
U([p1,S1;...; pn,Sn]) = ∑
i
piU(Si).
In other words, once the probabilities and utilities of the possible outcome states are speciﬁed,
the utility of a compound lottery involving those states is completely determined. Because the
outcome of a nondeterministic action is a lottery, it follows that an agent can act rationally—
that is, consistently with its preferences—only by choosing an action that maximizes expected
utility according to Equation (15.1).
The preceding theorems establish that (assuming the constraints on rational preferences)
a utility function exists for any rational agent. The theorems do not establish that the utility
function is unique. It is easy to see, in fact, that an agent’s behavior would not change if its
utility function U(S) were transformed according to
U′(S) = aU(S)+b,
(15.2)
where a and b are constants and a > 0; a positive afﬁne transformation.3 This fact was noted
in Chapter 6 (page 213) for two-player games of chance; here, we see that it applies to all
kinds of decision scenarios.
As in game-playing, in a deterministic environment an agent needs only a preference
ranking on states—the numbers don’t matter. This is called a value function or ordinal
Value function
utility function.
Ordinal utility
function
It is important to remember that the existence of a utility function that describes an agent’s
preference behavior does not necessarily mean that the agent is explicitly maximizing that
utility function in its own deliberations. As we showed in Chapter 2, rational behavior can be
generated in any number of ways. A rational agent might be implemented with a table lookup
(if the number of possible states is small enough).
By observing a rational agent’s behavior, an observer can learn about the utility function
that represents what the agent is actually trying to achieve (even if the agent doesn’t know it).
We return to this point in Section 15.7.
15.3 Utility Functions
Utility functions map from lotteries to real numbers. We know they must obey the axioms
of orderability, transitivity, continuity, substitutability, monotonicity, and decomposability. Is
that all we can say about utility functions? Strictly speaking, that is it: an agent can have any
preferences it likes. For example, an agent might prefer to have a prime number of dollars in
its bank account; in which case, if it had $16 it would give away $3. This might be unusual,
but we can’t call it irrational. An agent might prefer a dented 1973 Ford Pinto to a shiny new
Mercedes. The agent might prefer prime numbers of dollars only when it owns the Pinto, but
when it owns the Mercedes, it might prefer more dollars to fewer. Fortunately, the preferences
of real agents are usually more systematic and thus easier to deal with.
3
In this sense, utilities resemble temperatures: a temperature in Fahrenheit is 1.8 times the Celsius temperature
plus 32, but converting from one to the other doesn’t make you hotter or colder.
