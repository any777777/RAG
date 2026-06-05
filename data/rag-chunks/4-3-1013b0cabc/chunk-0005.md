---
chunk_id: "4-3-1013b0cabc-chunk-0005"
source_id: "4-3-1013b0cabc"
source_file: "New folder (3)/4.3.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 5
confidence: "first-pass"
extraction_method: "structured-local"
---

about
−100 dBW/m2.
Although flux density is useful for system specification, uplink CNR calculations
must be based on the power delivered to the transponder input. Thus, the
standard link equation is used to compute the uplink receive power.
Uplink Noise Power at the Transponder Input
Repeating Eq. (4.13) from Section 4.2, the noise power at the input of the satellite receiver
is
Nxp = k + Txp + Bn
(dBW),
(4.36)
where
• k is Boltzmann’s constant in dBW/K/Hz (−228.6 dBW/K/Hz),
• Txp is the system noise temperature of the transponder (in dBK),
• Bn is the receiver noise bandwidth (in dBHz).
Received Power at the Transponder Input
The power received at the satellite transponder input is
Prxp = Pt + Gt + Gr −Lp −Lup
(dBW),
(4.37)
where
• Pt is the earth station transmitter output power (dBW),
• Gt is the uplink antenna gain (dB),
• Gr is the satellite receive antenna gain in the direction of the earth station (dB),
• Lp is the free-space path loss (dB),
• Lup includes miscellaneous uplink losses such as atmospheric attenuation and po-
larization mismatch.
Uplink CNR at the Satellite Receiver Input
The uplink carrier-to-noise ratio is
(CNR)up = Prxp −Nxp
(dB).
(4.38)
8

## Page 9

Equivalently, in linear units:
(CNR)up = 10 log10

Prxp
kTxpBn

.
The required transmitter power is therefore computed from the desired transponder
CNR. Because
Prxp = Nxp + (CNR)up,
(4.39)
uplink power allocation is straightforward.
Calculating Earth Station Transmitter Power from Transponder
Output
Alternatively, if the transponder is a bent-pipe repeater and its output power is specified,
then
Prxp = Psat −BOo −Gxp
(dBW),
(4.40)
where
• Psat is the saturated output power of the transponder (dBW),
• BOo is the output backoff (dB),
• Gxp is the gain of the transponder (dB).
This method is used when the satellite operator specifies output levels rather than
required uplink CNR.
9

## Page 10
