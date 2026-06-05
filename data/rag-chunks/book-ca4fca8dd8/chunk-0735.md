---
chunk_id: "book-ca4fca8dd8-chunk-0735"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 735
confidence: "first-pass"
extraction_method: "structured-local"
---

444
Chapter 13
Probabilistic Reasoning
Now we need to think about how to arrange these into a causal structure. The key hidden
variables are whether or not a Theft or Accident will occur in the next time period. Obviously,
one cannot ask the applicant to predict these; they have to be inferred from the available
information and the insurer’s previous experience.
What are the causal factors leading to Theft? The MakeModel is certainly important—
some models are stolen much more often than others because there is an efﬁcient resale
market for vehicles and parts; the CarValue also matters, because an old, beat-up, or high-
mileage vehicle has lower resale value. Moreover, a vehicle that is Garaged and has an
AntiTheft device is harder to steal. The hidden variable CarValue depends in turn on the
MakeModel, VehicleYear, and Mileage. CarValue also dictates the loss amount when a Theft
occurs, so that is one of the contributors to OwnCarCost (the other being accidents, which
we will get to shortly).
It is common in models of this type to introduce another hidden variable, SocioEcon,
the socioeconomic category of the applicant. This is thought to inﬂuence a wide range of
behaviors and characteristics. In our model, there is no direct evidence in the form of observed
income and occupation variables;4 but SocioEcon inﬂuences MakeModel and VehicleYear; it
also affects ExtraCar and GoodStudent, and depends somewhat on Age.
For any insurance company, perhaps the most important hidden variable is RiskAversion:
people who are risk-averse are good insurance risks! Age and SocioEcon affect RiskAversion,
and its “symptoms” include the applicant’s choice of whether the vehicle is Garaged and has
AntiTheft devices and SafetyFeatures.
In predicting future accidents, the key is the applicant’s future DrivingBehavior, which
is inﬂuenced by both RiskAversion and DrivingSkill; the latter in turn depends on Age and
YearsLicensed. The applicant’s past driving behavior is reﬂected in the DrivingRecord, which
also depends on RiskAversion and DrivingSkill as well as on YearsLicensed (because some-
one who started driving only recently may not have had time to accumulate a litany of acci-
dents and violations). In this way, DrivingRecord provides evidence about RiskAversion and
DrivingSkill, which in turn help to predict future DrivingBehavior.
We can think of DrivingBehavior as a per-mile tendency to drive in an accident-prone
way; whether an Accident actually occurs in a ﬁxed time period depends also on the annual
Mileage and on the SafetyFeatures of the vehicle. If an Accident occurs, there are three
kinds of costs: the MedicalCost for the applicant depends on Age and Cushioning, which
depends in turn on the Ruggedness of the car and whether it has an Airbag; the LiabilityCost
(medical, pain and suffering, loss of income, etc.) for the other driver; and the PropertyCost
for the applicant and the other driver, both of which depend (in different ways) on the car’s
Ruggedness and on the applicant’s CarValue.
We have illustrated the kind of reasoning that goes into developing the topology and
hidden variables in a Bayes net. We also need to specify the ranges and the conditional distri-
butions for each variable. For the ranges, the primary decision is often whether to make the
variable discrete or continuous. For example, the Ruggedness of the vehicle could be a con-
tinuous variable between 0 and 1, or a discrete variable with range {TinCan,Normal,Tank}.
4
Some insurance companies also acquire the applicant’s credit history to help in assessing risk; this provides
considerably more information about socioeconomic category. Whenever using hidden variables of this kind, one
must be careful that they do not inadvertently become proxies for variables such as race that may not be used in
insurance decisions. Techniques for avoiding biases of this kind are described in Chapter 19.
