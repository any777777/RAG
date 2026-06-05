---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0133"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 133
confidence: "first-pass"
extraction_method: "structured-local"
---

6.17
Arrays
Beam shaping can be achieved by using an array of basic elements.
The elements are arranged so that their radiation patterns provide
mutual reinforcement in certain directions and cancellation in others.
Although most arrays used in satellite communications are two-
dimensional horn arrays, the principle is most easily explained with
reference to an in-line array of dipoles (Fig. 6.26a and b). As shown
previously (Fig. 6.8), the radiation pattern for a single dipole in the xy
plane is circular, and it is this aspect of the radiation pattern that is
altered by the array configuration. Two factors contribute to this: the
difference in distance from each element to some point in the far field
and the difference in the current feed to each element. For the coordi-
nate system shown in Fig. 6.26b, the xy plane, the difference in dis-
tance is given by s cos . Although this distance is small compared with
the range between the array and point P, it plays a crucial role in
determining the phase relationships between the radiation from each
element. It should be kept in mind that at any point in the far field the
array appears as a point source, the situation being as sketched in Fig.
6.26c. For this analysis, the point P is taken to lie in the xy plane.
Since a distance of one wavelength corresponds to a phase difference
of 2	, the phase lead of element n relative to n  1 resulting from the
difference in distance is (2	/)s cos . To illustrate the array princi-
ples, it will be assumed that each element is fed by currents of equal
magnitude but differing in phase progressively by some angle .
Positive values of  mean a phase lead and negative values a phase
lag. The total phase lead of element n relative to n  1 is therefore
   
s cos 
(6.36)
The Argand diagram for the phasors is shown in Fig. 6.27. The mag-
nitude of the resultant phasor can be found by first resolving the indi-
vidual phasors into horizontal (real axis) and vertical (imaginary axis)
components, adding these, and finding the resultant. Mathematically,
this is stated as
ER  E  E cos   jE sin   E cos 2  jE sin 2    
 
N  1
n  0
E cos n  jE sin n
 E 
N  1
n  0
ejn
(6.37)
2	


Antennas
157
TLFeBOOK

## Page 172

158
Chapter Six
x
φ
s
P
x
y
x
P
(c)
(b)
(a)
Array
y
s cos φ
y
z
Figure 6.26
An in-line array of
dipoles.
TLFeBOOK

## Page 173
