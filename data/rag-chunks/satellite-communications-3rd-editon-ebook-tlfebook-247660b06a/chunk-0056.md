---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0056"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 56
confidence: "first-pass"
extraction_method: "structured-local"
---

z : 
 H	  sin (E) …Eq. (2.41)
For check purposes, the values are
l  4241  km
z  4748.2  km
l  cos (LST)
R : l  sin (LST)
…This gives the R components in matrix form.
z
The values are
4140.1
R  919.7   km
4748.2
The magnitude of the R vector is
| R |  6366.4  km
At this point, both the satellite radius vector r and the earth station
radius vector R are known in the IJK frame for any position of satel-
lite and earth. From the vector diagram shown in Fig. 2.12a, the range
vector  is obtained as
  r  R
(2.43)
This gives  in the IJK frame. It then remains to transform  to the
observer’s frame, known as the topocentric-horizon frame, shown in
Fig. 2.12b.
2.9.8
The topocentric-horizon coordinate
system
The position of the satellite, as measured from the earth station, is usu-
ally given in terms of the azimuth and elevation angles and the range .
These are measured in the topocentric-horizon coordinate system illus-
trated in Fig. 2.12b. In this coordinate system, the fundamental plane is
the observer’s horizon plane. In the notation given in Bate et al. (1971),
the positive x axis is taken as south, the unit vector being denoted by S.
The positive y axis points east, the unit vector being E. The positive z
axis is “up,” pointing to the observer’s zenith, the unit vector being Z.
(Note: This is not the same z as that used in Sec. 2.9.7.) The frame is
referred to as the SEZ frame, which of course rotates with the earth.
As shown in the previous section, the range vector  is known in the
IJK frame, and it is now necessary to transform this to the SEZ frame.
aE  (1  eE
2

1  eE
2  sin
 (E)2)

Orbits and Launching Methods
53
TLFeBOOK

## Page 69

Again, this is a standard transformation procedure. See Bate et al.,
1971.
S
sin E cos LST
sin E sin LST
 cos E
I
E	 
sin LST
cos LST
0    	 J	
(2.44)
Z
cos E cos LST
cos E sin LST
sin E
K
From Fig. 2.11, the geocentric angle E is seen to be given by
E  arctan 
(2.45)
zl
54
Chapter Two
Figure 2.12
Topocentric-horizon coordinate system (SEZ frame):
(a) overall view; (b) detailed view.
TLFeBOOK

## Page 70
