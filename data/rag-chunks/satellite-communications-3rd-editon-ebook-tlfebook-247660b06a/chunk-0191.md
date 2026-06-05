---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0191"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 191
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 249

dating 12 transponders as described in Sec. 7.7. The individual
transponder bandwidth is typically 36 MHz. In contrast, the baseband
bandwidth for a telephony channel is typically 3.1 kHz.
In theory, the spectrum of a frequency-modulated carrier extends to
infinity. In a practical satellite system, the bandwidth of the transmit-
ted FM signal is limited by the intermediate-frequency amplifiers. The
IF bandwidth, denoted by BIF, must be wide enough to pass all the sig-
nificant components in the FM signal spectrum that is generated. The
required bandwidth is usually estimated by Carson’s rule as
BIF  2 (F  FM)
(9.1)
where F is the peak carrier deviation produced by the modulating
baseband signal, and FM is the highest frequency component in the
baseband signal. These maximum values, F and FM, are specified in
the regulations governing the type of service. For example, for com-
mercial FM sound broadcasting in North America, F  75 kHz and
FM  15 kHz.
The deviation ratio D is defined as the ratio
D 
(9.2)
Example 9.1
A video signal of bandwidth 4.2 MHz is used to frequency
modulate a carrier, the deviation ratio being 2.56. Calculate the peak devi-
ation and the signal bandwidth.
solution
F  2.56  4.2  10.752 MHz
BIF  2 (10.752  4.2)  29.9 MHz
A similar ratio, known as the modulation index, is defined for sinu-
soidal modulation. This is usually denoted by ß in the literature.
Letting f represent the peak deviation for sinusoidal modulation and
fm the sinusoidal modulating frequency gives
ß 
(9.3)
The difference between ß and D is that D applies for an arbitrary
modulating signal and is the ratio of the maximum permitted values
of deviation and baseband frequency, whereas ß applies only for sinu-
soidal modulation (or what is often termed tone modulation). Very
often the analysis of an FM system will be carried out for tone 
f

fm
F

FM
Analog Signals
235
TLFeBOOK

## Page 250
