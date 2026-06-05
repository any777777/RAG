---
chunk_id: "book-ca4fca8dd8-chunk-1095"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1095
confidence: "first-pass"
extraction_method: "structured-local"
---

654
Chapter 18
Probabilistic Programming
#SeismicEvents ∼Poisson(T ∗λe)
Time(e) ∼UniformReal(0,T)
EarthQuake(e) ∼Boolean(0.999)
Location(e) ∼if Earthquake(e) then SpatialPrior() else UniformEarth()
Depth(e) ∼
if Earthquake(e) then UniformReal(0,700) else Exactly(0)
Magnitude(e) ∼Exponential(log(10))
Detected(e, p,s) ∼Logistic(weights(s, p),Magnitude(e), Depth(e), Dist(e,s))
#Detections(site = s) ∼Poisson(T ∗λ f (s))
#Detections(event=e, phase=p, station=s) = if Detected(e, p,s) then 1 else 0
OnsetTime(a,s) if (event(a) = null) then ∼UniformReal(0,T)
else = Time(event(a)) + GeoTT(Dist(event(a),s),Depth(event(a)),phase(a))
+ Laplace(µt(s),σt(s))
Amplitude(a,s) if (event(a) = null) then ∼NoiseAmpModel(s)
else = AmpModel(Magnitude(event(a)),Dist(event(a),s),Depth(event(a)),phase(a))
Azimuth(a,s) if (event(a) = null) then ∼UniformReal(0, 360)
else = GeoAzimuth(Location(event(a)),Depth(event(a)),phase(a),Site(s))
+ Laplace(0,σa(s))
Slowness(a,s) if (event(a) = null) then ∼UniformReal(0,20)
else = GeoSlowness(Location(event(a)),Depth(event(a)),phase(a),Site(s))
+ Laplace(0,σs(s))
ObservedPhase(a,s) ∼CategoricalPhaseModel(phase(a))
Figure 18.6 A simpliﬁed version of the NET-VISA model (see text).
naturally occurring) as well as over their time, magnitude, depth, and location. The locations
of natural events are distributed according to a spatial prior that is trained (like other parts
of the model) from historical data; man-made events are, by the treaty rules, assumed to oc-
cur uniformly over the surface of the Earth. At every station s, each phase (seismic wave
type) p from an event e produces either 0 or 1 detections (above-threshold signals); the detec-
tion probability depends on the event magnitude and depth and its distance from the station.
“False alarm” detections also occur according to a station-speciﬁc rate parameter. The mea-
sured arrival time, amplitude, and other properties of a detection d from a real event depend
on the properties of the originating event and its distance from the station.
Once trained, the model runs continuously. The evidence consists of detections (90% of
which are false alarms) extracted from raw IMS waveform data, and the query typically asks
for the most likely event history, or bulletin, given the data. Results so far are encouraging;
for example, in 2009 the UN’s SEL3 automated bulletin missed 27.4% of the 27294 events
in the magnitude range 3–4 while NET-VISA missed 11.1%. Moreover, comparisons with
dense regional networks show that NET-VISA ﬁnds up to 50% more real events than the
ﬁnal bulletins produced by the UN’s expert seismic analysts. NET-VISA also tends to as-
sociate more detections with a given event, leading to more accurate location estimates (see
Figure 18.7). As of January 1, 2018, NET-VISA has been deployed as part of the CTBTO
monitoring pipeline.
Despite superﬁcial differences, the two examples are structurally similar: there are un-
known objects (papers, earthquakes) that generate percepts according to some physical pro-
