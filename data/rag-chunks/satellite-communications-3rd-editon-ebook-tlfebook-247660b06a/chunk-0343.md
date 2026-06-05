---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0343"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 343
confidence: "first-pass"
extraction_method: "structured-local"
---

Because the TDMA earth stations have to transmit at a higher bit
rate compared with FDMA, a higher [EIRP] is required, as can be
deduced from Eq. (10.24). Equation (10.24) states that

	  
	  [R]
where [R] is equal to [Rb] for an FDMA uplink and [RTDMA] for a TDMA
uplink.
For a given bit error rate (BER) the [Eb/N0] ratio is fixed as shown
by Fig. 10.17. Hence, assuming that [Eb/N0] is the same for the TDMA
Eb

N0
C

N0
Satellite Access
409
Figure 14.24
(a) FDMA network; (b) TDMA network.
TLFeBOOK

## Page 420

and the FDMA uplinks, an increase in [R] requires a corresponding
increase in [C/N0]. Assuming that the TDMA and FDMA uplinks oper-
ate with the same [LOSSES] and satellite [G/T], Eq. (12.39) shows
that the increase in [C/N0] can be achieved only through an increase in
the earth station [EIRP], and therefore
[EIRP]TDMA  [EIRP]FDMA  [RTDMA]  [Rb]
(14.31)
For the same earth station antenna gain in each case, the decibel
increase in earth station transmit power for TDMA compared with
FDMA is
[P] TDMA  [P]FDMA  [RTDMA]  [Rb]
(14.32)
Example 14.7
A 14-GHz uplink operates with transmission losses and
margins totaling 212 dB and a satellite [G/T]  10 dB/K. The required
uplink [Eb/N0] is 12 dB. (a) Assuming FDMA operation and an earth station
uplink antenna gain of 46 dB, calculate the earth station transmitter pow-
er needed for transmission of a T1 baseband signal. (b) If the downlink
transmission rate is fixed at 74 dBb/s, calculate the uplink power increase
required for TDMA operation.
solution
(a) From Sec. 10.4 the T1 bit rate is 1.544 Mb/s or [R]  62 dBb/s.
Using the [Eb/N0]  12-dB value specified, Eq. (10.24) gives

	  12  62  74 dBHz
From Eq. (12.39),
[EIRP]  
	   	  [LOSSES]  228.6
 74  10  212  228.6
 47.4 dBW
Hence the transmitter power required is
[P]  47.4  46  1.4 dBW
or
1.38 W
(b) With TDMA operation the rate increase is 74  62  12 dB. All other fac-
tors being equal, the earth station [EIRP] must be increased by this amount,
and hence
[P]  1.4  12  13.4 dBW
or
21.9 W
G

T
C

N0
C

N0
410
Chapter Fourteen
TLFeBOOK

## Page 421
