---
chunk_id: "book-ca4fca8dd8-chunk-0135"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 135
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
79
concept of a controller in control theory is identical to that of an agent in AI. Perhaps sur-
Controller
prisingly, AI has concentrated for most of its history on isolated components of agents—
question-answering systems, theorem-provers, vision systems, and so on—rather than on
whole agents. The discussion of agents in the text by Genesereth and Nilsson (1987) was an
inﬂuential exception. The whole-agent view is now widely accepted and is a central theme in
recent texts (Padgham and Winikoff, 2004; Jones, 2007; Poole and Mackworth, 2017).
Chapter 1 traced the roots of the concept of rationality in philosophy and economics. In
AI, the concept was of peripheral interest until the mid-1980s, when it began to suffuse many
discussions about the proper technical foundations of the ﬁeld. A paper by Jon Doyle (1983)
predicted that rational agent design would come to be seen as the core mission of AI, while
other popular topics would spin off to form new disciplines.
Careful attention to the properties of the environment and their consequences for ra-
tional agent design is most apparent in the control theory tradition—for example, classical
control systems (Dorf and Bishop, 2004; Kirk, 2004) handle fully observable, deterministic
environments; stochastic optimal control (Kumar and Varaiya, 1986; Bertsekas and Shreve,
2007) handles partially observable, stochastic environments; and hybrid control (Henzinger
and Sastry, 1998; Cassandras and Lygeros, 2006) deals with environments containing both
discrete and continuous elements. The distinction between fully and partially observable en-
vironments is also central in the dynamic programming literature developed in the ﬁeld of
operations research (Puterman, 1994), which we discuss in Chapter 16.
Although simple reﬂex agents were central to behaviorist psychology (see Chapter 1),
most AI researchers view them as too simple to provide much leverage. (Rosenschein (1985)
and Brooks (1986) questioned this assumption; see Chapter 26.)
A great deal of work
has gone into ﬁnding efﬁcient algorithms for keeping track of complex environments (Bar-
Shalom et al., 2001; Choset et al., 2005; Simon, 2006), most of it in the probabilistic setting.
Goal-based agents are presupposed in everything from Aristotle’s view of practical rea-
soning to McCarthy’s early papers on logical AI. Shakey the Robot (Fikes and Nilsson,
1971; Nilsson, 1984) was the ﬁrst robotic embodiment of a logical, goal-based agent. A
full logical analysis of goal-based agents appeared in Genesereth and Nilsson (1987), and a
goal-based programming methodology called agent-oriented programming was developed by
Shoham (1993). The agent-based approach is now extremely popular in software engineer-
ing (Ciancarini and Wooldridge, 2001). It has also inﬁltrated the area of operating systems,
where autonomic computing refers to computer systems and networks that monitor and con-
Autonomic
computing
trol themselves with a perceive–act loop and machine learning methods (Kephart and Chess,
2003). Noting that a collection of agent programs designed to work well together in a true
multiagent environment necessarily exhibits modularity—the programs share no internal state
and communicate with each other only through the environment—it is common within the
ﬁeld of multiagent systems to design the agent program of a single agent as a collection of
autonomous sub-agents. In some cases, one can even prove that the resulting system gives
the same optimal solutions as a monolithic design.
The goal-based view of agents also dominates the cognitive psychology tradition in the
area of problem solving, beginning with the enormously inﬂuential Human Problem Solv-
ing (Newell and Simon, 1972) and running through all of Newell’s later work (Newell, 1990).
Goals, further analyzed as desires (general) and intentions (currently pursued), are central to
the inﬂuential theory of agents developed by Michael Bratman (1987).
