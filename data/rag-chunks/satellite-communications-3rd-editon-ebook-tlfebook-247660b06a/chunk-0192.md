---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0192"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 192
confidence: "first-pass"
extraction_method: "structured-local"
---

modulation rather than for an arbitrary signal because the mathe-
matics are easier and the results usually give a good indication of what
to expect with an arbitrary signal.
Example 9.2
A test tone of frequency 800 Hz is used to frequency modu-
late a carrier, the peak deviation being 200 kHz. Calculate the modulation
index and the bandwidth.
solution
ß 
 250
B  2 (200  0.8)  401.6 kHz
Carson’s rule is widely used in practice, even though it tends to give
an underestimate of the bandwidth required for deviation ratios in the
range 2  D  10, which is the range most often encountered in prac-
tice. For this range, a better estimate of bandwidth is given by
BIF  2 ("F  2FM)
(9.4)
Example 9.3
Recalculate the bandwidths for Examples 8.1 and 8.2.
solution
For the video signal,
BIF  2 (10.75  8.4)  38.3 MHz
For the 800 Hz tone: BIF  2 (200  1.6)  403.2 kHz
In Examples 9.1 through 9.3 it will be seen that when the deviation
ratio (or modulation index) is large, the bandwidth is determined
mainly by the peak deviation and is given by either Eq. (9.1) or Eq.
(9.4). However, for the video signal, for which the deviation ratio is rel-
atively low, the two estimates of bandwidth are 29.9 and 38.3 MHz. In
practice, the standard bandwidth of a satellite transponder required to
handle this signal is 36 MHz.
The peak frequency deviation of an FM signal is proportional to the
peak amplitude of the baseband signal. Increasing the peak amplitude
results in increased signal power and hence a larger signal-to-noise
ratio. At the same time, "F, and hence the FM signal bandwidth, will
increase as shown previously. Although the noise power at the demod-
ulator input is proportional to the IF filter bandwidth, the noise pow-
er output after the demodulator is determined by the bandwidth of the
baseband filters, and therefore, an increase in IF filter band-width
does not increase output noise. Thus an improvement in signal-
to-noise ratio is possible but at the expense of an increase in the IF 
200

0.8
236
Chapter Nine
TLFeBOOK

## Page 251
