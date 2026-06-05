---
chunk_id: "reference-777408ef16-chunk-0054"
source_id: "reference-777408ef16"
source_file: "New folder (3)/Reference.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 54
confidence: "first-pass"
extraction_method: "structured-local"
---

 :  atan  
…Eq. (2.49)
The azimuth is determined by setting the quadrant conditions (see Table
2.4) as
Aza :  if [ (S  0  m)  (E  0  m) , , 0]
Azb :  if [ (S  0  m)  (E  0  m) , 180  deg  , 0]
Azc :  if [ (S  0  m)  (E  0  m) , 180  deg  , 0]
Azd :  if [ (S  0  m)  (E  0  m) , 360  deg  , 0]
Since all but one of these are zero, the azimuth is given by
Az :  Aza  Azb  Azc  Azd
Az  100.5  deg
      
Note that the range could also have been obtained from
I
2 
J
2 
K
2
  1810  km
2.9.9
The subsatellite point
The point on the earth vertically under the satellite is referred to as
the subsatellite point. The latitude and longitude of the subsatellite
point and the height of the satellite above the subsatellite point can be
determined from a knowledge of the radius vector r. Figure 2.13 shows
the meridian plane which cuts the subsatellite point. The height of the
terrain above the reference ellipsoid at the subsatellite point is denot-
ed by HSS, and the height of the satellite above this, by hSS. Thus the
total height of the satellite above the reference ellipsoid is
h  HSS  hSS
(2.50)
Now the components of the radius vector r in the IJK frame are giv-
en by Eq. (2.33). Figure 2.13 is seen to be similar to Fig. 2.11, with the
difference that r replaces R, the height to the point of interest is h
rather than H, and the subsatellite latitude SS is used. Thus Eqs.
(2.39) through (2.42) may be written for this situation as
N 
(2.51)
aE

1 eE
2 sin2
SS

E

S
Orbits and Launching Methods
57
TLFeBOOK

## Page 68

rI  (N  h) cos SS cos LST
(2.52)
rJ  (N  h) cos SS sin LST
(2.53)
rK  [N (1  eE
2)  h] sin SS
(2.54)
We now have three equations in three unknowns, LST, E, and h,
and these can be solved as shown in the following Mathcad example.
In addition, by analogy with the situation shown in Fig. 2.10, the east
longitude is obtained from Eq. (2.35) as
EL  LST  GST
(2.55)
where GST is the Greenwich sidereal time.
Example 2.21
Determine the subsatellite height, latitude, and LST for the
satellite in Example 2.16.
solution
From Example 2.16, the components of the radius vector are
rI
4685.3  km
rJ	 : 
5047.7  km 
rK
3289.1  km
58
Chapter Two
r
z
S
h
HSS
λSS
ψSS
hSS
Figure 2.13
Geometry for determining the subsatellite point.
TLFeBOOK

## Page 69
