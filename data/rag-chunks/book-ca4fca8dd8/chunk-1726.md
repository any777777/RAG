---
chunk_id: "book-ca4fca8dd8-chunk-1726"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1726
confidence: "first-pass"
extraction_method: "structured-local"
---

1052
Chapter 28
Philosophy, Ethics, and Safety of AI
If robots have rights, then they should not be enslaved, and there is a question of whether
reprogramming them would be a kind of enslavement. Another ethical issue involves voting
rights: a rich person could buy thousands of robots and program them to cast thousands
of votes—should those votes count? If a robot clones itself, can they both vote? What is
the boundary between ballot stufﬁng and exercising free will, and when does robotic voting
violate the “one person, one vote” principle?
Ernie Davis argues for avoiding the dilemmas of robot consciousness by never building
robots that could possibly be considered conscious. This argument was previously made by
Joseph Weizenbaum in his book Computer Power and Human Reason (1976), and before that
by Julien de La Mettrie in L’Homme Machine (1748). Robots are tools that we create, to do
the tasks we direct them to do, and if we grant them personhood, we are just declining to take
responsibility for the actions of our own property: “I’m not at fault for my self-driving car
crash—the car did it itself.”
This issue takes a different turn if we develop human–robot hybrids. Of course we already
have humans enhanced by technology such as contact lenses, pacemakers, and artiﬁcial hips.
But adding computational protheses may blur the lines between human and machine.
28.3.7 AI Safety
Almost any technology has the potential to cause harm in the wrong hands, but with AI
and robotics, the hands might be operating on their own. Countless science ﬁction stories
have warned about robots or cyborgs running amok. Early examples include Mary Shelley’s
Frankenstein, or the Modern Prometheus (1818) and Karel ˇCapek’s play R.U.R. (1920), in
which robots conquer the world. In movies, we have The Terminator (1984) and The Matrix
(1999), which both feature robots trying to eliminate humans—the robopocalypse (Wilson,
Robopocalypse
2011). Perhaps robots are so often the villains because they represent the unknown, just like
the witches and ghosts of tales from earlier eras. We can hope that a robot that is smart
enough to ﬁgure out how to terminate the human race is also smart enough to ﬁgure out that
that was not the intended utility function; but in building intelligent systems, we want to rely
not just on hope, but on a design process with guarantees of safety.
It would be unethical to distribute an unsafe AI agent. We require our agents to avoid
accidents, to be resistant to adversarial attacks and malicious abuse, and in general to cause
beneﬁts, not harms. That is especially true as AI agents are deployed in safety-critical appli-
cations, such as driving cars, controlling robots in dangerous factory or construction settings,
and making life-or-death medical decisions.
There is a long history of safety engineering in traditional engineering ﬁelds. We know
Safety engineering
how to build bridges, airplanes, spacecraft, and power plants that are designed up front to
behave safely even when components of the system fail. The ﬁrst technique is failure modes
and effect analysis (FMEA): analysts consider each component of the system, and imagine
Failure modes and
eﬀect analysis
(FMEA)
every possible way the component could go wrong (for example, what if this bolt were to
snap?), drawing on past experience and on calculations based on the physical properties of
the component. Then the analysts work forward to see what would result from the failure.
If the result is severe (a section of the bridge could fall down) then the analysts alter the
design to mitigate the failure. (With this additional cross-member, the bridge can survive the
failure of any 5 bolts; with this backup server, the online service can survive a tsunami taking
out the primary server.) The technique of fault tree analysis (FTA) is used to make these
Fault tree analysis
(FTA)
