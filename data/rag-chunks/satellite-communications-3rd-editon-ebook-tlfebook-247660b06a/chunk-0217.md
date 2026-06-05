---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0217"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 217
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 277

shaping cannot be achieved, so some ISI occurs, but it can be reduced
to negligible proportions.
The pulse shaping is carried out by controlling the spectrum of
the received pulse as given by Eq. (10.8). One theoretical model for
the spectrum is known as the raised cosine response, which is
shown in Fig. 10.10. Although a theoretical model, it can be
approached closely with practical designs. The raised cosine spec-
trum is described by
1
f  f1
V(f) 0.5 1  cos 

f1  f  B
(10.9)
0
B  f
The frequencies f1 and B are determined by the symbol rate and a
design parameter known as the rolloff factor, denoted here by the sym-
bol . The rolloff factor is a specified parameter in the range
0    1
(10.10)
	 (f  f1)

B  f1
Digital Signals
263
t
t
A
A
(b)
(a)
Sampling
instant
Figure 10.9
(a) Pulse ringing. (b) Sampling to avoid ISI.
TLFeBOOK

## Page 278

In terms of 	 and the symbol rate, the bandwidth B is given by
B 
Rsym
(10.11)
and
f1 
Rsym
(10.12)
For binary transmission, the symbol rate simply becomes the bit
rate. Thus, for the T1 signal, the required baseband bandwidth is
B 
 1.544  106  0.772 (1  	) MHz
(10.13)
For a rolloff factor of unity, the bandwidth for the T1 system becomes
1.544 MHz.
Although a satellite link requires the use of a modulated carrier
wave, the same overall baseband response is needed for the avoidance
of ISI. Fortunately, the channel for a satellite link does not introduce
frequency distortion, so the pulse shaping can take place in the trans-
mit and receive filters. The modulation of the baseband signal onto a
carrier is discussed in the next section.
10.6
Digital Carrier Systems
For transmission to and from a satellite, the baseband digital signal
must be modulated onto a microwave carrier. In general, the digital
baseband signals may be multilevel (M-ary), requiring multilevel
modulation methods. The main binary modulation methods are illus-
trated in Fig. 10.11. They are defined as follows:
1  	

2
(1  	) 

2
(1  	) 

2
264
Chapter Ten
f
A
1.0
0.5
f1
Rsym
B
2
Figure 10.10
The raised cosine response.
TLFeBOOK

## Page 279
