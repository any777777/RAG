---
chunk_id: "reference-777408ef16-chunk-0050"
source_id: "reference-777408ef16"
source_file: "New folder (3)/Reference.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 50
confidence: "first-pass"
extraction_method: "structured-local"
---

Example 2.18
Find the LST for Thunder Bay, longitude 89.26°W for 13 h
UT on December 18, 2000.
solution
Expressing the longitude in degrees west:
WL :  89.26  deg
In degrees east this is
EL :  2  	  WL
EL  270.74  deg
GST is obtained from Example 2.17, and Eq. (2.35) gives
LST :  GST  EL
LST  9.655  rad
Taking mod 2	 and expressing the result in degrees:
LST :  mod (LST, 2  	) 
LST  193.189  deg
        
Knowing the LST enables the position vector R of the earth station
to be located with reference to the IJK frame as shown in Fig. 2.10.
However, when R is resolved into its rectangular components, account
must be taken of the oblateness of the earth. The earth may be mod-
eled as an oblate spheroid, in which the equatorial plane is circular,
and any meridional plane (i.e., any plane containing the earth’s polar
axis) is elliptical, as illustrated in Fig. 2.11. For one particular model,
known as a reference ellipsoid, the semimajor axis of the ellipse is
equal to the equatorial radius, the semiminor axis is equal to the polar
radius, and the surface of the ellipsoid represents the mean sea level.
Denoting the semimajor axis by aE and the semiminor axis by bE and
using the known values for the earth’s radii gives
aE  6378.1414 km
(2.36)
bE  6356.755 km
(2.37)
From these values, the eccentricity of the earth is seen to be
eE 
 0.08182
(2.38)
In Figs. 2.10 and 2.11, what is known as the geocentric latitude is
shown as E. This differs from what is normally referred to as latitude.
An imaginary plumb line dropped from the earth station makes an
angle E with the equatorial plane, as shown in Fig. 2.11. This is
known as the geodetic latitude, and for all practical purposes here, this
can be taken as the geographic latitude of the earth station.
aE
2 
bE
2


aE
Orbits and Launching Methods
51
TLFeBOOK

## Page 62
