---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0254"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 254
confidence: "first-pass"
extraction_method: "structured-local"
---

Other losses can only be estimated from statistical data, and some of
these are dependent on weather conditions, especially on rainfall.
The first step in the calculations is to determine the losses for clear-
weather, or clear-sky, conditions. These calculations take into account
the losses, including those calculated on a statistical basis, which do
not vary significantly with time. Losses which are weather-related,
and other losses which fluctuate with time, are then allowed for by
introducing appropriate fade margins into the transmission equation.
12.3.1
Free-space transmission
As a first step in the loss calculations, the power loss resulting from the
spreading of the signal in space must be determined. This calculation is
similar for the uplink and the downlink of a satellite circuit. Using Eqs.
(12.1) and (12.2) gives the power flux density at the receiving antenna as
M 
(12.6)
The power delivered to a matched receiver is this power flux densi-
ty multiplied by the effective aperture of the receiving antenna, given
by Eq. (6.15). The received power is therefore
PR  MAeff

(12.7)
 (EIRP) (GR) 

2
Recall that r is the distance, or range, between the transmit and
receive antennas and GR is the isotropic power gain of the receiving
antenna. The subscript R is used to identify the receiving antenna.
The right-hand side of Eq. (12.7) is separated into three terms asso-
ciated with the transmitter, receiver, and free space, respectively. In
decibel notation, the equation becomes
[PR]  [EIRP]  [GR]  10 log 

2
(12.8)
The received power in dBW is therefore given as the sum of the
transmitted EIRP in dBW plus the receiver antenna gain in dB minus
a third term which represents the free-space loss in decibels. The free-
space loss component in decibels is given by
4	r




4	r
2GR

EIRP

4	r 2
EIRP

4	r2
The Space Link
307
TLFeBOOK

## Page 322
