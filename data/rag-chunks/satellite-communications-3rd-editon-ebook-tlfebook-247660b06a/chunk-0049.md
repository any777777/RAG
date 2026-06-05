---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0049"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 49
confidence: "first-pass"
extraction_method: "structured-local"
---

The perifocal system is very convenient for describing the motion of
the satellite. If the earth were uniformly spherical, the perifocal coor-
dinates would be fixed in space, i.e., inertial. However, the equatorial
bulge causes rotations of the perifocal coordinate system, as described
in Sec. 2.8.1. These rotations are taken into account when the satellite
position is transferred from perifocal coordinates to geocentric-equato-
rial coordinates, described in the next section.
Example 2.15
Using the values r  7257 km and   204.81° obtained in
the previous example, express r in vector form in the perifocal coordinate
system.
solution
rP  7257  cos 204.81  6587.6 km
rQ  7257  sin 204.81  3045.3 km
Hence
r  6587.6P  3045.3Q km
2.9.6
The geocentric-equatorial coordinate
system
The geocentric-equatorial coordinate system is an inertial system of
axes, the reference line being fixed by the fixed stars. The reference
line is the line of Aries described in Sec. 2.5. (The phenomenon known
as the precession of the equinoxes is ignored here. This is a very slow
rotation of this reference frame, amounting to approximately
1.396971° per Julian century, where a Julian century consists of
36,525 mean solar days.) The fundamental plane is the earth’s equa-
torial plane. Figure 2.9 shows the part of the ellipse above the equato-
rial plane and the orbital angles , 
, and i. It should be kept in mind
that  and 
 may be slowly varying with time, as shown by Eqs. (2.12)
and (2.13).
The unit vectors in this system are labeled I, J, and K, and the coor-
dinate system is referred to as the IJK frame, with positive I pointing
along the line of Aries. The transformation of vector r from the PQW
frame to the IJK frame is most easily expressed in matrix form, the
components being indicated by the appropriate subscripts:
rIrJ	  R˜ rP	
(2.33a)
rK
rQ
46
Chapter Two
TLFeBOOK

## Page 62
