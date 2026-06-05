---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0341"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 341
confidence: "first-pass"
extraction_method: "structured-local"
---

By removing the redundant speech samples and silent periods from
the transmission link, a doubling in channel capacity is achieved. As
shown in Fig. 14.23, the transmission is at 2.048 Mb/s for an input-out-
put rate of 4.096 Mb/s.
An advantage of the SPEC method over the DSI method is that
freeze-out does not occur during overload conditions. During overload,
sample values which should change may not. This effectively leads to
a coarser quantization and therefore an increase in quantization noise.
This is subjectively more tolerable than freeze-out.
14.7.11
Downlink analysis for digital trans-
mission
As mentioned in Sec. 14.6, the transponder power output and band-
width both impose limits on the system transmission capacity. With
TDMA, TWT backoff is not generally required, which allows the
transponder to operate at saturation. One drawback arising from this
is that the uplink station must be capable of saturating the transpon-
der, which means that even a low-traffic-capacity station requires com-
paratively large power output compared with what would be required
for FDMA. This point is considered further in Sec. 14.7.12.
As with the FDM/FDMA system analysis, it will be assumed that
the overall carrier-to-noise ratio is essentially equal to the downlink
carrier-to-noise ratio. With a power-limited system this C/N ratio is
one of the factors that determines the maximum digital rate, as shown
by Eq. (10.24). Equation (10.24) can be rewritten as
[Rb]  
	  
	
(14.29)
The [Eb/N0] ratio is determined by the required bit-error rate, as
shown in Fig. 10.17 and described in Sec. 10.6.4. For example, for a
BER of 105 an [Eb/N0] of 9.6 dB is required. If the rate Rb is specified,
then the [C/N0] ratio is determined, as shown by Eq. (14.29), and this
value is used in the link budget calculations as required by Eq. (12.53).
Alternatively, if the [C/N0] ratio is fixed by the link budget parameters
as given by Eq. (12.53), the bit rate is then determined by Eq. (14.29).
The bit rate is also constrained by the IF bandwidth. As shown in
Sec. 10.6.3, the ratio of bit rate to IF bandwidth is given by

where m  1 for BPSK and m  2 for QPSK and  is the rolloff factor.
The value of 0.2 is commonly used for the rolloff factor, and therefore,
the bit rate for a given bandwidth becomes
m

1  
Rb

BIF
Eb

N0
C

N0
Satellite Access
407
TLFeBOOK

## Page 418
