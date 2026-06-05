---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0360"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 360
confidence: "first-pass"
extraction_method: "structured-local"
---

Hence the bit energy to noise density ratio is

(14.48)
The noise bandwidth at the BPSK detector will be approximately equal
to the IF bandwidth as given by Eq. (10.15), but using the chip rate
BN  BIF
 (1  ) Rch
(14.49)
where  is the rolloff factor of the filter. Hence the bit energy to noise
density ratio becomes

(14.50)
As pointed out in Chap. 10, the probability of bit error is usually a
specified objective, and this determines the Eb/No ratio, for example,
through Fig.10.17. The number of channels is therefore
K  1  (1  ) 
(14.51)
The processing gain Gp is basically the ratio of power density in the
unspread signal to that in the spread signal. Since the power density
is inversely proportional to bandwidth, an approximate expression for
the processing gain is
Gp 
(14.52)
Hence
K  1  (1  ) GP
(14.53)
Example 14.8
The code waveform in a CDMA system spreads the carriers
over the full 36 MHz bandwidth of the channel, and the rolloff factor for the
filtering is 0.4. The information bit rate is 64 kb/s, and the system uses
BPSK. Calculate the processing gain in decibels. Given that the bit error
rate must not exceed 105, give an estimate of the maximum number of
channels that can access the system.
solution
Rch 
BIF

(1  )
No

Eb
Rch

Rb
No

Eb
Rch

Rb
(1  ) Rch

(K  1) Rb
Eb

No
BN

(K  1) Rb
Eb

No
Satellite Access
429
TLFeBOOK

## Page 440


 25.7  106 chips/s
Hence the processing gain is
Gp 
 401.56
[Gp]  10 log (401.56)
 26 dB
From Fig. 10.18 for Pe  105, [Eb/No]  9.6 dB approximately. This is a pow-
er ratio of 9.12, and from Eq. (14.53),
K  1

62 (rounded down)
The throughput efficiency is defined as the ratio of the total number
of bits per unit time that can be transmitted with CDMA to the total
number of bits per unit time that could be transmitted with single
access and no spreading. For K accesses as determined above, each at
bit rate Rb, the total bits per unit time is KRb. A single access could uti-
lize the full bandwidth, and hence its transmission rate as determined
by Eq. (10.15) as
RT 
(14.54)
This is the same as the chip rate, and hence the throughput is
 


(14.55)
Using the values obtained in Example 14.8 gives a throughput of 0.15,
or 15 percent. This should be compared with the frame efficiency for
K

Gp
KRb

Rch
KRb

RT
BIF

(1  )
1.4  401.56

9.12
25.7  106

64  103
36  106

1.4
430
Chapter Fourteen
TLFeBOOK

## Page 441
