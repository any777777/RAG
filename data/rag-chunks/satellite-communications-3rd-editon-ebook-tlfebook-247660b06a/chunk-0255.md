---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0255"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 255
confidence: "first-pass"
extraction_method: "structured-local"
---

[FSL]  10 log 

2
(12.9)
Normally, the frequency rather than wavelength will be known, and
the substitution   c/f can be made, where c  108 m/s. With fre-
quency in megahertz and distance in kilometers, it is left as an exer-
cise for the student to show that the free-space loss is given by
[FSL]  32.4  20 log r  20 log f
(12.10)
Equation (12.8) can then be written as
[PR]  [EIRP]  [GR]  [FSL]
(12.11)
The received power [PR] will be in dBW when the [EIRP] is in dBW
and [FSL] in dB. Equation (12.9) is applicable to both the uplink and
the downlink of a satellite circuit, as will be shown in more detail
shortly.
Example 12.3
The range between a ground station and a satellite is 42,000
km. Calculate the free-space loss at a frequency of 6 GHz.
solution
[FSL]  (32.4  20 log 42,000  20 log 6000)  200.4 dB
This is a very large loss. Suppose that the [EIRP] is 56 dBW (as cal-
culated in Example 12.1 for a radiated power of 6 W) and the receive
antenna gain is 50 dB. The receive power would be 56  50  200.4 
94.4 dBW. This is 355 pW. It also may be expressed as 64.4 dBm,
which is 64.4 dB below the 1-mW reference level.
Equation (12.11) shows that the received power is increased by
increasing antenna gain as expected, and Eq. (6.32) shows that anten-
na gain is inversely proportional to the square of the wavelength.
Hence it might be thought that increasing the frequency of operation
(and therefore decreasing wavelength) would increase the received
power. However, Eq. (12.9) shows that the free-space loss is also
inversely proportional to the square of the wavelength, so these two
effects cancel. It follows, therefore, that for a constant EIRP, the
received power is independent of frequency of operation.
If the transmit power is a specified constant, rather than the EIRP,
then the received power will increase with increasing frequency for
given antenna dish sizes at the transmitter and receiver. It is left 
as an exercise for the student to show that under these conditions 
the received power is directly proportional to the square of the 
frequency.
4	r


308
Chapter Twelve
TLFeBOOK

## Page 323
