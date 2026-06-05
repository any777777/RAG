---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0430"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 430
confidence: "first-pass"
extraction_method: "structured-local"
---

are in view, the additional data are used to minimize errors by using the
method of least squares.
Each satellite broadcasts its ephemeris, which contains the orbital
elements needed to calculate its position, and as previously men-
tioned, the ephemerides are updated and corrected continuously from
an earth control station. It should be mentioned that the GPS system
is first and foremost intended for military use. However, civilian appli-
cations have now become quite extensive and are an accepted part of
the GPS program.
Time enters into the position determination in two ways. First, the
ephemerides must be associated with a particular time or epoch (as
described in Chap. 2). The standard timekeeper is an atomic standard,
maintained at the U.S. Naval Observatory, and the resulting time is
known as GPS time. Each satellite carries its own atomic clock. The
time broadcasts from the satellites are monitored by the control station
which transmits back to the satellites any errors detected in timing rel-
ative to GPS time. No attempt is made to correct the clocks aboard the
satellites; rather, the error information is rebroadcast to the user sta-
tions, where corrections can be implemented in the calculations.
Second, time markers are needed to show when transmissions leave
the satellites so that, by measuring propagation times and knowing
the speed of propagation, the ranges can be calculated. Therein lies a
problem, since the user stations have no direct way of telling when a
transmission from a satellite commenced. The problem is overcome by
having the satellite transmit a continuous-wave carrier which is mod-
ulated by a clocking signal, both the carrier and the clocking signal
being derived from the atomic clock aboard the satellite. At a user sta-
tion, the receiver generates a replica of the modulated signal from its
own atomic clock. The satellite signal and its replica are compared in
a correlator at the receiver, and the replica is shifted in time until
exact correlation is achieved. If the receiver clock kept exactly the
same time as the satellite clock, the time shift as measured by the cor-
relator would give the propagation delay. However, the receiver clock
in general will be offset from the satellite clock (which is synchronized
to GPS time) by an unknown amount. This offset will be the same for
the signals received from the four satellites, and hence by obtaining
four range measurements, four equations can be set up in terms of the
x,y,z position vectors for the user and the time offset. The four equa-
tions can then be solved for these four unknowns. All this requires
quite sophisticated microprocessing in the receiver. Also, the composi-
tion of the GPS signal is much more complex than indicated here, uti-
lizing spread-spectrum techniques. The reader is referred to the
following for details: Langley (1990a, 1991b, 1991c), Kleusberg and
Langley (1990), and Mattos (1992, 1993a, 1993b, 1993c, 1993d, 1993e).
Satellite Services
497
TLFeBOOK
