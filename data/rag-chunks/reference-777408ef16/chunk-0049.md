---
chunk_id: "reference-777408ef16-chunk-0049"
source_id: "reference-777408ef16"
source_file: "New folder (3)/Reference.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 49
confidence: "first-pass"
extraction_method: "structured-local"
---

earth station will be denoted as EL. Recall that previously longitude
was expressed in positive degrees east and negative degrees west. For
east longitudes, EL  E, while for west longitudes, EL  360°  E.
For example, for an earth station at east longitude 40°, EL  40°. For
an earth station at west longitude 40°, EL  360  (40)  320°. Thus
the local sidereal time in degrees is given by
LST  GST  EL
(2.35)
The procedure is illustrated in the following examples
Example 2.17
Find the GST for 13 h UT on 18 December 2000.
solution
From Example 2.11:
T :  1.009638376
The first three terms of Eq. (2.34) add up to
GST :  99.6910  deg  36000.7689  T  deg  .0004  T2  deg
Note that Mathcad stores this result in radians even though the terms are
in degrees:
GST  636.128  rad
The universal time is
UT :  13  h
Converting this to a fraction of earth rotation:
UT : 
 UT
This gives UT in radians:
UT  3.403  rad
Hence GST in radians is
GST :  GST  UT
GST :  mod (GST, 2  	)
Using the mod function, multiple revolutions are removed, and Mathcad
allows this to be expressed in degrees as
GST  282.449  deg
        
2  	

day
50
Chapter Two
TLFeBOOK

## Page 61
