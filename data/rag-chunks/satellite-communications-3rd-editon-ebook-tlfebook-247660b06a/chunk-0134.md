---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0134"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 134
confidence: "first-pass"
extraction_method: "structured-local"
---

Here, N is the total number of elements in the array. A single element
would have resulted in a field E, and the array is seen to modify this
by the summation factor. The magnitude of summation factor is
termed the array factor (AF):
AF  
N  1
n  0 e jn
(6.38)
The array factor has a maximum value of N when   0. Note that this
just means that ERmax  NE. By recalling that  as given by Eq. (6.36) is
a function of the current phase angle  and the angular coordinate , it is
possible to choose the current phase to make array factor show a peak in
some desired direction 0. The required relationship is, from Eq. (6.36),
  
s cos 0
(6.39)
This is illustrated in the following example.
Example 6.2
A dipole array has 5 elements equispaced at 0.25 wavelength.
The array factor is required to have a maximum along the positive axis of
the array. Plot the magnitude of the array factor as a function of .
solution
Given data are
N:  5
s:  .25
0:  0  deg
Set the current phase to
:  2  	  s  cos (0)
2	


Antennas
159
j
E
E
E
ER
0
ψ
ψ
(Real)
(Imaginary)
Figure 6.27
Phasor diagram for
the in-line array of dipoles.
TLFeBOOK

## Page 174

Set up the variable:
:  180  deg, 175  deg..180  deg
The total phase angle is
 () :    2  	  s  cos ()
The array factor, as plotted on the previous page, is
AF () :  
N  1
n  0
ej  n   ()
As the example shows, the array factor has a main peak at   0
and some sidelobes. For this particular example, the values were pur-
posely chosen to illustrate what is termed an end-fire array, where the
main beam is directed along the positive axis of the array. Keep in
mind that a single dipole would have had a circular pattern.
The current phasing can be altered to make the main lobe appear at
  90°, giving rise to a broadside array. The symmetry of the dipole
array means that two broadside lobes occur, one on each side of the
array axis. This is illustrated in the next example.
Example 6.3
Repeat the previous example for   90 degrees.
solution
Given data are
N:  5
s:  .25
0:  90  deg
Set the current phase to
:  2  	  s  cos (0)
160
Chapter Six
180
0
150
120
60
5
4
3
2
240
300
90
270
φ
30
210
330
1
AF(φ)
TLFeBOOK

## Page 175
