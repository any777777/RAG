---
chunk_id: "reference-777408ef16-chunk-0053"
source_id: "reference-777408ef16"
source_file: "New folder (3)/Reference.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 53
confidence: "first-pass"
extraction_method: "structured-local"
---

The coordinates l and z given in Eqs. (2.40) and (2.42) are known in
terms of the earth station height and latitude, and hence the range
vector is known in terms of these quantities and the LST. As a point of
interest, for zero height, the angle E is known as the geocentric lati-
tude and is given by
tan E (H  0)  (1  eE
2) tan E
(2.46)
Here, eE is the earth’s eccentricity, equal to 0.08182. The difference
between the geodetic and geocentric latitudes reaches a maximum at
a geocentric latitude of 45°, when the geodetic latitude is 45.192°.
Finally, the magnitude of the range and the antenna look angles are
obtained from
  S
2 
E
2 
Z
2

(2.47)
El  arcsin  
(2.48)
We define an angle  as
  arctan 
(2.49)
Then the azimuth depends on which quadrant  is in and is given by
Table 2.2.
Example 2.20
The IJK range vector components for a certain satellite, at GST
 240 degrees, are as given below. Calculate the corresponding range and the
look angles for an earth station the coordinates for which are, latitude 48.42
degrees N, longitude 89.26 degrees W, height above mean sea level 200 m.
solution
Given data:
I :  1280  km
J :  1278  km
K :  66  km
GST :  240  deg
E :  48.42  deg
E :  89.26  deg
H :  200  m
|E|

|S|
Z


Orbits and Launching Methods
55
TABLE 2.2
Azimuth angles
S
E
Azimuth degrees





180  


180  


360  
TLFeBOOK

## Page 66

The required earth constants are
aE :  6378.1414  km
eE :  .08182
l : 
 H  cos (E) …Eq. (2.40)
z : 
 H	  sin (E) …Eq. (2.41)
The values for check purposes are
l  4241  km
z  4748.2  km
E :  atan  
Eq. (2.45) 
E  48.2  deg
LST :  240  deg  E
…Eq. (2.35)
(sin (E)  cos (LST) )
(sin (E)  sin (LST) )
 cos (E)
D : 
(sin (LST) )
(cos (LST) )
0      	
(cos (E)  cos (LST) )
(cos (E)  sin (LST) )
(sin (E) )
0.651
0.365
 0.666
D : 0.489
 0.872
0      
...The D-values are given for 
0.581
0.326
0.746
check purposes.
S
I
 E	:  D  J	
…Eq. (2.44)
Z
K
S
323
 E	:   1740.6 km
...The values are given for check purposes
Z
377
In Mathcad the magnitude is given simply by
||  1810  km
      
El :  asin  
…Eq. (2.48)
El  12  deg
     
Z


z
l
aE  (1  eE
2) 

1  eE
2  sin
 (E)2

aE

1  eE
2  sin
 (E)2

56
Chapter Two
TLFeBOOK

## Page 67
