---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0428"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 428
confidence: "first-pass"
extraction_method: "structured-local"
---

a time marker is also required, which necessitates getting simultane-
ous measurements from four satellites.
The GPS system uses one-way transmissions, from satellites to
users, so that the user does not require a transmitter, only a GPS
receiver. The only quantity the receiver has to be able to measure is
time, from which propagation delay, and hence the range to each satel-
lite, can be determined. Each satellite broadcasts its ephemeris (which
is a table of the orbital elements as described in Chap. 2), from which
its position can be calculated. Knowing the range to three of the satel-
lites and their positions, it is possible to compute the position of the
observer (user). The geocentric-equatorial coordinate system (see Sec.
2.9.6) is used with the GPS system, where it is called the earth-cen-
tered, earth-fixed (ECEF) coordinate system.
As mentioned above, if the positions of three points relative to the
coordinate system are known and the distance from an observer to each
of the points can be measured, then the position of the observer relative
to the coordinate system can be calculated. In the GPS system, the
three points are provided by three satellites. Of course, the satellites
are moving, so their positions must be tracked accurately. The satellite
orbits can be predicted from the orbital parameters (as described in
Chap. 2). These parameters are continually updated by a master con-
trol station which transmits them up to the satellites, where they are
broadcast as part of the navigational message from each satellite.
Just as in a land-based system, better accuracy is obtained by using
reference points well separated in space. For example, the range mea-
surements made to three reference points clustered together will yield
nearly equal values. Position calculations involve range differences, and
where the ranges are nearly equal, any error is greatly magnified in the
difference. This effect, brought about as a result of the satellite geome-
try, is known as dilution of precision (DOP). This means that range
errors which occur from other causes, such as timing errors, are magni-
fied by the geometric effect. With the GPS system, dilution of position is
taken into account through a factor known as the position dilution of
precision (PDOP) factor. This is the factor by which the range errors are
multiplied to get the position error. The GPS system has been designed
to keep the PDOP factor less than 6 most of the time (Langley, 1991c).
The GPS constellation consists of 24 satellites in six near-circular
orbits, at an altitude of approximately 20,000 km (Daly, 1993). The
ascending nodes of the orbits are separated by 60°, and the inclination
of each orbit is 55°. The four satellites in each orbit are irregularly
spaced to keep the PDOP factor within the limits referred to above.
It was stated earlier that three satellites are needed to fix position. In
the GPS system, a minimum of four satellites must be observed, for rea-
sons which will be explained shortly. Where more than four satellites
496
Chapter Seventeen
TLFeBOOK
