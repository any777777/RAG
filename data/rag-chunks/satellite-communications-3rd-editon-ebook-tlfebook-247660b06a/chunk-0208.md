---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0208"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 208
confidence: "first-pass"
extraction_method: "structured-local"
---

forms. This is so because the waveform does not return to the zero
baseline at any point during the bit period.
Figure 10.2c shows an example of a polar return-to-zero (RZ) wave-
form. Here, the waveform does return to the zero baseline in the mid-
dle of the bit period, so transitions will always occur even within a long
string of like symbols, and bit timing can be extracted. However, dc
drift still occurs with long strings of like symbols.
In the split-phase or Manchester encoding shown in Fig. 10.2d, a
transition between positive and negative levels occurs in the middle of
each bit. This ensures that transitions will always be present so that
bit timing can be extracted, and because each bit is divided equally
between positive and negative levels, there is no dc component.
A comparison of the frequency bandwidths required for digital wave-
forms can be obtained by considering the waveforms which alternate at
the highest rate between the two extreme levels. These will appear as
squarewaves. For the basic polar NRZ waveform of Fig. 10.2b, this hap-
pens when the sequence is…101010.…The periodic time of such a
squarewave is 2Tb, and the fundamental frequency component is f 
1/2Tb. For the split-phase encoding, the squarewave with the highest
repetition frequency occurs with a long sequence of like symbols such
as…1111111…, as shown in Fig. 10.2d. The periodic time of this square-
wave is Tb, and hence the fundamental frequency component is twice
that of the basic polar NRZ. Thus the split-phase encoding requires twice
the bandwidth compared with that for the basic polar NRZ, while the bit
rate remains unchanged. The utilization of bandwidth, measured in bits
per second per hertz, is therefore less efficient.
An alternate mark inversion (AMI) code is shown in Fig. 10.2e. Here,
the binary 0s are at the zero baseline level, and the binary 1s alternate
in polarity. In this way, the dc level is removed, while bit timing can be
extracted easily, except when a long string of zeros occurs. Special tech-
niques are available to counter this last problem. The highest pulse-rep-
etition frequency occurs with a long string of…111111…, the periodic
time of which is 2Tb, the same as the waveform of Fig. 10.2b. The AMI
waveform is also referred to as a bipolar waveform in North America.
Bandwidth requirements may be reduced by utilizing multilevel dig-
ital waveforms. Figure 10.3a shows a polar NRZ signal for the
sequence 11010010. By arranging the bits in groups of two, four levels
can be used. For example, these may be
11
3A
10
A
01
A
00
3A
254
Chapter Ten
TLFeBOOK
