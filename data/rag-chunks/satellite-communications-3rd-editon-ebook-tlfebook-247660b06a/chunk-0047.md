---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0047"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 47
confidence: "first-pass"
extraction_method: "structured-local"
---

The time of perigee passage T can be eliminated from Eq. (2.24) if one
is working from the elements specified by NASA. For the NASA elements,
M0  n (t0  T)
Therefore,
T  t0 
(2.25)
Hence, substituting this in Eq. (2.24) gives
M  M0  n (t  t0)
(2.26)
Consistent units must be used throughout. For example, with n in
degrees/day, time (t  t0) must be in days and M0 in degrees, and M
will then be in degrees.
Example 2.12
Calculate the time of perigee passage for the NASA ele-
ments given in Table 2.1.
solution
The specified values at epoch are mean motion n  14.23304826
rev/day, mean anomaly M0  246.6853°, and t0  223.79688452 days. In this
instance it is only necessary to convert the mean motion to degrees/day,
which is 360n. Applying Eq. (2.25) gives
T  223.79688452 
 223.79604425 days
       
246.6853

14.23304826  360
M0

n
Orbits and Launching Methods
43
Figure 2.8
Perifocal coordinate system (PQW frame).
TLFeBOOK

## Page 59

Once the mean anomaly M is known, the next step is to solve an
equation known as Kepler’s equation. Kepler’s equation is formulated
in terms of an intermediate variable E, known as the eccentric anom-
aly, and is usually stated as
M  E  e sin E
(2.27)
This rather innocent looking equation requires an iterative solution,
preferably by computer. The following example in Mathcad shows how
to solve for E as the root of the equation
M  (E  e sin E)  0
(2.28)
Example 2.13
Given that the mean anomaly is 205 degrees and the eccen-
tricity 0.0025, calculate the eccentric anomaly.
solution
M :  205  deg
e :  0.0025
E :  	
…This is the initial guess value for E.
E :  root (M  E  e  sin (E) , E)
…This is the root equation 
which Mathcad solves for E.
E  204.938  deg
       
Once E is found,  can be found from an equation known as Gauss’
equation, which is
tan 
 tan 
(2.29)
It may be noted that r, the magnitude of the radius vector, also can
be obtained as a function of E and is
r  a (1  e cos E)
(2.30)
For near-circular orbits where the eccentricity is small, an approxi-
mation for  directly in terms of M is

M  2e sin M 
e2 sin 2M
(2.31)
Note that the first M term on the right-hand side must be in radians,
and  will be in radians.
54
E
2
1  e

1  e
2
44
Chapter Two
TLFeBOOK

## Page 60
