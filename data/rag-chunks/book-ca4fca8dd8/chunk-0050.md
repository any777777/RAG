---
chunk_id: "book-ca4fca8dd8-chunk-0050"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 50
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 1.2
The Foundations of Artiﬁcial Intelligence
33
to start multiplying the number of CPU cores rather than the clock speed. Current expecta-
tions are that future increases in functionality will come from massive parallelism—a curious
convergence with the properties of the brain. We also see new hardware designs based on
the idea that in dealing with an uncertain world, we don’t need 64 bits of precision in our
numbers; just 16 bits (as in the bfloat16 format) or even 8 bits will be enough, and will
enable faster processing.
We are just beginning to see hardware tuned for AI applications, such as the graphics
processing unit (GPU), tensor processing unit (TPU), and wafer scale engine (WSE). From
the 1960s to about 2012, the amount of computing power used to train top machine learn-
ing applications followed Moore’s law. Beginning in 2012, things changed: from 2012 to
2018 there was a 300,000-fold increase, which works out to a doubling every 100 days or
so (Amodei and Hernandez, 2018). A machine learning model that took a full day to train
in 2014 takes only two minutes in 2018 (Ying et al., 2018). Although it is not yet practical,
quantum computing holds out the promise of far greater accelerations for some important
Quantum computing
subclasses of AI algorithms.
Of course, there were calculating devices before the electronic computer. The earliest
automated machines, dating from the 17th century, were discussed on page 24. The ﬁrst
programmable machine was a loom, devised in 1805 by Joseph Marie Jacquard (1752–1834),
that used punched cards to store instructions for the pattern to be woven.
In the mid-19th century, Charles Babbage (1792–1871) designed two computing ma-
chines, neither of which he completed. The Difference Engine was intended to compute
mathematical tables for engineering and scientiﬁc projects. It was ﬁnally built and shown
to work in 1991 (Swade, 2000). Babbage’s Analytical Engine was far more ambitious: it
included addressable memory, stored programs based on Jacquard’s punched cards, and con-
ditional jumps. It was the ﬁrst machine capable of universal computation.
Babbage’s colleague Ada Lovelace, daughter of the poet Lord Byron, understood its
potential, describing it as “a thinking or . . . a reasoning machine,” one capable of reasoning
about “all subjects in the universe” (Lovelace, 1843). She also anticipated AI’s hype cycles,
writing, “It is desirable to guard against the possibility of exaggerated ideas that might arise as
to the powers of the Analytical Engine.” Unfortunately, Babbage’s machines and Lovelace’s
ideas were largely forgotten.
AI also owes a debt to the software side of computer science, which has supplied the
operating systems, programming languages, and tools needed to write modern programs (and
papers about them). But this is one area where the debt has been repaid: work in AI has pio-
neered many ideas that have made their way back to mainstream computer science, including
time sharing, interactive interpreters, personal computers with windows and mice, rapid de-
velopment environments, the linked-list data type, automatic storage management, and key
concepts of symbolic, functional, declarative, and object-oriented programming.
1.2.7 Control theory and cybernetics
• How can artifacts operate under their own control?
Ktesibios of Alexandria (c. 250 BCE) built the ﬁrst self-controlling machine: a water clock
with a regulator that maintained a constant ﬂow rate. This invention changed the deﬁnition
of what an artifact could do. Previously, only living things could modify their behavior in
response to changes in the environment. Other examples of self-regulating feedback control
