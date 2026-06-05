---
chunk_id: "reference-777408ef16-chunk-0068"
source_id: "reference-777408ef16"
source_file: "New folder (3)/Reference.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 68
confidence: "first-pass"
extraction_method: "structured-local"
---

the look angles need not be determined with great precision but are
calculated to give the expected values for a satellite whose longitude is
close to the earth station longitude. In some cases, especially with
direct broadcast satellites (DBS), the home antenna is aligned to one
particular cluster of satellites, as described in Chap. 16, and no further
adjustments are necessary.
3.3
The Polar Mount Antenna
Where the home antenna has to be steerable, expense usually pre-
cludes the use of separate azimuth and elevation actuators. Instead,
a single actuator is used which moves the antenna in a circular arc.
This is known as a polar mount antenna. The antenna pointing can
only be accurate for one satellite, and some pointing error must be
accepted for satellites on either side of this. With the polar mount
antenna, the dish is mounted on an axis termed the polar axis such
that the antenna boresight is normal to this axis, as shown in Fig.
3.5a. The polar mount is aligned along a true north line, as shown in
Fig. 3.5, with the boresight pointing due south. The angle between the
polar mount and the local horizontal plane is set equal to the earth
station latitude E; simple geometry shows that this makes the bore-
sight lie parallel to the equatorial plane. Next, the dish is tilted at an
angle  relative to the polar mount until the boresight is pointing at
a satellite position due south of the earth station. Note that there does
not need to be an actual satellite at this position. (The angle of tilt is
often referred to as the declination, which must not be confused with
the magnetic declination used in correcting compass readings. The
term angle of tilt will be used for  in this text.)
The required angle of tilt is found as follows: From the geometry of
Fig. 3.5b,
  90°  El0  E
(3.13)
where El0 is the angle of elevation required for the satellite position
due south of the earth station. But for the due south situation, angle
B in Eq. (3.8) is equal to zero; hence, from Eq. (3.9), b  E. Hence,
from Eq. (3.12), or Fig 3.5c.
cos El0 
sin E
(3.14)
Combining Eqs. (3.13) and (3.14) gives the required angle of tilt as
  90°  arccos 
sin E  E
(3.15)
aGSO

d
aGSO

d
The Geostationary Orbit
75
TLFeBOOK

## Page 86

76
Chapter Three
N
λE N
R
R
d
aGSO
S
90°
λE
N
90° + δ
Local horizontal
plane
S
Boresight
Equatorial
plane
E  o
aGSO
d
(b)
(a)
(c)
R
90° + E  o
λE
Figure 3.5
The polar mount antenna.
TLFeBOOK

## Page 87
