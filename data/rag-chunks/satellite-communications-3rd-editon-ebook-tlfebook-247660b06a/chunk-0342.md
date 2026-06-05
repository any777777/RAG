---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0342"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 342
confidence: "first-pass"
extraction_method: "structured-local"
---

Rb 
(14.30)
Example 14.6
Using Eq. (12.53), a downlink [C/N0] of 87.3 dBHz is calcu-
lated for a TDMA circuit that uses QPSK modulation. A BER of 105 is
required. Calculate the maximum transmission rate. Calculate also the IF
bandwidth required assuming a rolloff factor of 0.2.
solution
Figure 10.17 is applicable for QPSK and BPSK. From this figure,
[Eb/N0]  9.5 dB for a BER of 105. Hence
[Rb]  87.3  9.5  77.8 dBb/s
This is equal to 60.25 Mb/s.
For QPSK m  2 and using Eq. (14.30), we have
BIF  60.25 
 36.15 MHz
From Example 14.6 it will be seen that if the satellite transpon-
der has a bandwidth of 36 MHz, and an EIRP that results in a
[C/N0] of 87.3 dBHz at the receiving ground station, the system is
optimum in that the power and the bandwidth limits are reached
together.
14.7.12
Comparison of uplink power
requirements for FDMA and TDMA
With frequency-division multiple access, the modulated carriers at the
input to the satellite are retransmitted from the satellite as a com-
bined frequency-division-multiplexed signal. Each carrier retains its
modulation, which may be analog or digital. For this comparison, dig-
ital modulation will be assumed. The modulation bit rate for each car-
rier is equal to the input bit rate [adjusted as necessary for forward
error correction (FEC)]. The situation is illustrated in Fig. 14.24a,
where for simplicity, the input bit rate Rb is assumed to be the same
for each earth station. The [EIRP] is also assumed to be the same for
each earth station.
With time-division multiple access, the uplink bursts which are
displaced in time from one another are retransmitted from the satel-
lite as a combined time-division-multiplexed signal. The uplink bit
rate is equal to the downlink bit rate in this case, as illustrated in
Fig. 14.24b. As described in Sec. 14.7, compression buffers are need-
ed in order to convert the input bit rate Rb to the transmitted bit
rate RTDMA.
1.2

2
mBIF

1.2
408
Chapter Fourteen
TLFeBOOK

## Page 419
