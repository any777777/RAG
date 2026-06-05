---
chunk_id: "book-ca4fca8dd8-chunk-0734"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 734
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 443

Section 13.2
The Semantics of Bayesian Networks
443
Figure 13.9 A Bayesian network for evaluating car insurance applications.
causal structure of the domain and gives an accurate, well-calibrated distribution over the
output variables given the evidence available from the application form.3 The Bayes net will
include hidden variables that are neither input nor output variables, but are essential for
Hidden variable
structuring the network so that it is reasonably sparse with a manageable number of parame-
ters. The hidden variables are shaded brown in Figure 13.9.
The claims to be paid out—shaded lavender in Figure 13.9—are of three kinds: the
MedicalCost for any injuries sustained by the applicant; the LiabilityCost for lawsuits ﬁled by
other parties against the applicant and the company; and the PropertyCost for vehicle damage
to either party and vehicle loss by theft. The application form asks for the following input
information (the light blue nodes in Figure 13.9):
• About the applicant: Age; YearsLicensed—how long since a driving license was ﬁrst
obtained; DrivingRecord—some summary, perhaps based on “points,” of recent acci-
dents and trafﬁc violations; and (for students) a GoodStudent indicator for a grade-point
average of 3.0 (B) on a 4-point scale.
• About the vehicle: the MakeModel and VehicleYear; whether it has an Airbag; and some
summary of SafetyFeatures such as anti-lock braking and collision warning.
• About the driving situation: the annual Mileage driven and how securely the vehicle is
Garaged, if at all.
3
The network shown in Figure 13.9 is not in actual use, but its structure has been vetted with insurance experts.
In practice, the information requested on application forms varies by company and jurisdiction—for example,
some ask for Gender—and the model could certainly be made more detailed and sophisticated.

## Page 444
