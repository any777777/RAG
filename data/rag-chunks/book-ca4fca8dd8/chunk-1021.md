---
chunk_id: "book-ca4fca8dd8-chunk-1021"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1021
confidence: "first-pass"
extraction_method: "structured-local"
---

614
Chapter 17
Multiagent Decision Making
H
R
R
R
[2,0]
[1,1]
[0,2]
[90,0]
[50,50]
[0,90]
$0.90
$1.00
$1.10
Figure 17.6 The paperclip game. Each branch is labeled [p,s] denoting the number of pa-
perclips and staples manufactured on that branch. Harriet the human can choose to make two
paperclips, two staples, or one of each. (The values in green italics are the values for Harriet
if the game ended there, assuming θ=0.45.) Robbie the robot then has a choice to make 90
paperclips, 90 staples, or 50 of each.
strategies in general assistance games include actions on Harriet’s part that we would describe
as teaching, rewarding, commanding, correcting, demonstrating, or explaining, as well as ac-
tions on Robbie’s part that we would describe as asking permission, learning from demon-
strations, preference elicitation, and so on. The key point is that these behaviors need not be
scripted: by solving the game, Harriet and Robbie work out for themselves how to convey
preference information from Harriet to Robbie, so that Robbie can be more useful to Harriet.
We need not stipulate in advance that Harriet is to “give rewards” or that Robbie is to “follow
instructions,” although these may be reasonable interpretations of how they end up behaving.
To illustrate assistance games, we’ll use the paperclip game. It’s a very simple game in
Paperclip game
which Harriet the human has an incentive to “signal” to Robbie the robot some information
about her preferences. Robbie is able to interpret that signal because he can solve the game
and therefore he can understand what would have to be true about Harriet’s preferences in
order for her to signal in that way.
The steps of the game are depicted in Figure 17.6. It involves making paperclips and
staples. Harriet’s preferences are expressed by a payoff function that depends on the number
of paperclips and the number of staples produced, with a certain “exchange rate” between the
two. Harriet’s preference parameter θ denotes the relative value (in dollars) of a paperclip;
for example, she might value paperclips at θ=0.45 dollars, which means staples are worth
1 −θ=0.55 dollars. So, if p paperclips and s staples are produced, Harriet’s payoff will be
pθ + s(1 −θ) dollars in all. Robbie’s prior is P(θ) = Uniform(θ;0,1). In the game itself,
Harriet goes ﬁrst, and can choose to make two paperclips, two staples, or one of each. Then
Robbie can choose to make 90 paperclips, 90 staples, or 50 of each.
Notice that if she were doing this by herself, Harriet would just make two staples, with a
value of $1.10. (See the annotations at the ﬁrst level of the tree in Figure 17.6.) But Robbie
is watching, and he learns from her choice. What exactly does he learn? Well, that depends
on how Harriet makes her choice. How does Harriet make her choice? That depends on how
Robbie is going to interpret it. We can resolve this circularity by ﬁnding a Nash equilibrium.
In this case, it is unique and can be found by applying myopic best response: pick any strategy
for Harriet; pick the best strategy for Robbie, given Harriet’s strategy; pick the best strategy
