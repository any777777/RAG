---
chunk_id: "book-ca4fca8dd8-chunk-1099"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1099
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 18.3
Keeping Track of a Complex World
657
#Aircraft(EntryTime =t) ∼Poisson(λa)
Exits(a,t) ∼if InFlight(a,t) then Boolean(αe)
InFlight(a,t) = (t=EntryTime(a)) ∨(InFlight(a,t −1) ∧¬ Exits(a,t −1))
X(a,t) ∼if t = EntryTime(a) then InitX()
else if InFlight(a,t) then N(FX(a,t −1),Σx)
#Blip(Source=a, Time=t) ∼if InFlight(a,t) then Bernoulli(DetectionProb(X(a,t)))
#Blip(Time=t) ∼Poisson(λ f )
Z(b) ∼if Source(b)=null then UniformZ(R) else N(HX(Source(b),Time(b)),Σz)
Figure 18.9 An OUPM for radar tracking of multiple targets with false alarms, detection
failure, and entry and exit of aircraft. The rate at which new aircraft enter the scene is λa,
while the probability per time step that an aircraft exits the scene is αe. False alarm blips (i.e.,
ones not produced by an aircraft) appear uniformly in space at a rate of λ f per time step. The
probability that an aircraft is detected (i.e., produces a blip) depends on its current position.
the blip has as its origins an aircraft and a time step. So, omitting the prior for now, the model
looks like this:
guaranteed Aircraft A1, A2
X(a,t) ∼if t = 0 then InitX() else N(F X(a,t −1), Σx)
#Blip(Source=a, Time=t) = 1
Z(b) ∼N(H X(Source(b),Time(b)), Σz)
where F and Σx are matrices describing the linear transition model and transition noise co-
variance, and H and Σz are the corresponding matrices for the sensor model. (See page 501.)
The key difference between this model and a standard Kalman ﬁlter is that there are
two objects producing sensor readings (blips). This means there is uncertainty at any given
time step about which object produced which sensor reading. Each possible world in this
model includes an association—deﬁned by values of all the Source(b) variables for all the
time steps—between aircraft and blips. Two possible association hypotheses are shown in
Figure 18.8(b–c). In general, for n objects and T time steps, there are (n!)T ways of assigning
blips to aircraft—an awfully large number.
The scenario described so far involved n known objects generating n observations at
each time step. Real applications of data association are typically much more complicated.
Often, the reported observations include false alarms (also known as clutter), which are not
False alarm
Clutter
caused by real objects. Detection failures can occur, meaning that no observation is reported
Detection failure
for a real object. Finally, new objects arrive and old ones disappear. These phenomena,
which create even more possible worlds to worry about, are illustrated in Figure 18.8(d). The
corresponding OUPM is given in Figure 18.9.
Because of its practical importance for both civilian and military applications, tens of
thousands of papers have been written on the problem of multitarget tracking and data as-
sociation. Many of them simply try to work out the complex mathematical details of the
probability calculations for the model in Figure 18.9, or for simpler versions of it. In one
sense, this is unnecessary once the model is expressed in a probabilistic programming lan-
guage, because the general-purpose inference engine does all of the mathematics correctly for
any model—including this one. Furthermore, elaborations of the scenario (formation ﬂying,
