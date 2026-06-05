---
chunk_id: "chapter-02-2-a139409a56-chunk-0010"
source_id: "chapter-02-2-a139409a56"
source_file: "Chapter 02 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 10
confidence: "first-pass"
extraction_method: "structured-local"
---

2.4.5 Utility-based agents
• Goals alone are not enough to generate high-quality behavior in most environments.
• For example, many action sequences will get the taxi to its destination (thereby achieving the 
goal), but some are quicker, safer, more reliable, or cheaper than others.
• Goals just provide a simple binary distinction between “happy” and “unhappy” states.
• Because “happy” does not sound very scientific, economists and computer scientists use
the term utility instead.
• “utility” here refers to “the quality of being useful,” 
• A performance measure assigns a score to any given sequence of environment states: 
(google map).
• An agent’s utility function is essentially an internalization of the performance measure,
• an agent that chooses actions to maximize its utility will be rational according to the external 
performance measure.
• Like goal-based agents, a utility-based agent has many advantages in terms of flexibility 
and learning.
52
•Example: An autonomous vehicle selecting a route that optimizes safety, speed, and fuel 
efficiency, balancing competing factors.

## Page 53

53
Utility Based Agent
•Mechanism:
•Assigns numerical utility values to states to represent preference levels.
•Selects actions that maximize expected utility allowing trade-offs between 
conflicting goals.
•Advantages:
•Supports complex decision making under uncertainty.
•Facilitates handling of conflicting objectives via quantitative evaluation.

## Page 54

• In two kinds of cases, goals are inadequate (insufficient for a 
purpose), but a utility-based agent can still make rational decisions:
• First, when there are conflicting goals, only some of which can be achieved 
• (for example, speed and safety), the utility function specifies the appropriate tradeoff. 
• Second, when there are several goals that the agent can aim for, none of 
which can be achieved with certainty, 
• utility agent provides a way in which the likelihood of success can be weighed against 
the importance of the goals.
• A rational utility-based agent chooses the action that maximizes the 
expected utility of the action outcomes—
• that is, the utility the agent expects to derive, on average, given the 
probabilities and utilities of each outcome.
54
… Utility-based agents

## Page 55
