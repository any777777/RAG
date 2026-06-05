---
chunk_id: "book-ca4fca8dd8-chunk-1710"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1710
confidence: "first-pass"
extraction_method: "structured-local"
---

1044
Chapter 28
Philosophy, Ethics, and Safety of AI
• Group fairness: A requirement that two classes are treated similarly, as measured by
some summary statistic.
• Fairness through unawareness: If we delete the race and gender attributes from the
data set, then it might seem that the system cannot discriminate on those attributes.
Unfortunately, we know that machine learning models can predict latent variables (such
as race and gender) given other correlated variables (such as zip code and occupation).
Furthermore, deleting those attributes makes it impossible to verify equal opportunity
or equal outcomes. Still, some countries (e.g., Germany) have chosen this approach for
their demographic statistics (whether or not machine learning models are involved).
• Equal outcome: The idea that each demographic class gets the same results; they have
demographic parity. For example, suppose we have to decide whether we should
Demographic parity
approve loan applications; the goal is to approve those applicants who will pay back
the loan and not those who will default on the loan. Demographic parity says that
both males and females should have the same percentage of loans approved. Note that
this is a group fairness criterion that does nothing to ensure individual fairness; a well-
qualiﬁed applicant might be denied and a poorly-qualiﬁed applicant might be approved,
as long as the overall percentages are equal. Also, this approach favors redress of past
biases over accuracy of prediction. If a man and a woman are equal in every way, except
the woman receives a lower salary for the same job, should she be approved because she
would be equal if not for historical biases, or should she be denied because the lower
salary does in fact make her more likely to default?
• Equal opportunity: The idea that the people who truly have the ability to pay back
the loan should have an equal chance of being correctly classiﬁed as such, regardless of
their sex. This approach is also called “balance.” It can lead to unequal outcomes and
ignores the effect of bias in the societal processes that produced the training data.
• Equal impact: People with similar likelihood to pay back the loan should have the
same expected utility, regardless of the class they belong to. This goes beyond equal
opportunity in that it considers both the beneﬁts of a true prediction and the costs of a
false prediction.
Let us examine how these issues play out in a particular context. COMPAS is a com-
mercial system for recidivism (re-offense) scoring. It assigns to a defendant in a criminal
case a risk score, which is then used by a judge to help make decisions: Is it safe to release
the defendant before trial, or should they be held in jail? If convicted, how long should the
sentence be? Should parole be granted? Given the signiﬁcance of these decisions, the system
has been the subject of intense scrutiny (Dressel and Farid, 2018).
COMPAS is designed to be well calibrated: all the individuals who are given the same
Well calibrated
score by the algorithm should have approximately the same probability of re-offending, re-
gardless of race. For example, among all people that the model assigns a risk score of 7 out
of 10, 60% of whites and 61% of blacks re-offend. The designers thus claim that it meets the
desired fairness goal.
On the other hand, COMPAS does not achieve equal opportunity: the proportion of
those who did not re-offend but were falsely rated as high-risk was 45% for blacks and 23%
for whites. In the case State v. Loomis, where a judge relied on COMPAS to determine the
sentence of the defendant, Loomis argued that the secretive inner workings of the algorithm
