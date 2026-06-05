---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0401"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 401
confidence: "first-pass"
extraction_method: "structured-local"
---

A single DBS transponder has to carry somewhere between four and
eight TV programs to be commercially viable (Mead, 2000). The pro-
grams may originate from a variety of sources, film, analog TV, and
videocassette, for example. Before transmission, these must all be con-
verted to digital, compressed, and then time-division multiplexed
(TDM). This TDM baseband signal is applied as QPSK modulation to
the uplink carrier reaching a given transponder.
The compressed bit rate, and hence the number of channels that are
carried, depends on the type of program material. Talk shows where
there is little movement require the lowest bit rate, while sports chan-
nels with lots of movement require comparatively large bit rates.
Typical values are in the range of 4 Mb/s for a movie channel, 5 Mb/s
for a variety channel, and 6 Mb/s for a sports channel (Fogg, 1995).
Compression is carried out to MPEG standards.
16.7
MPEG Compression Standards
MPEG stands for Moving Pictures Expert Group, a group within the
International Standards Organization and the International
Electrochemical Commission (ISO/IEC) that undertook the job of
defining standards for the transmission and storage of moving pic-
tures and sound. The standards are concerned only with the bit-
stream syntax and the decoding process, not with how encoding and
decoding might be implemented. Syntax covers such matters as bit
rate, picture resolution, time frames for audio, and the packet details
for transmission. The design of hardware for the encoding and decod-
ing processes is left up to the equipment manufacturer. Com-
prehensive descriptions of the MPEG can be found at the Web site
http://www.mpeg.org and in Sweet (1997) and Bhatt et al. (1997). The
MPEG standards currently available are MPEG-1, MPEG-2, MPEG-
4, and MPEG-7. For a brief explanation of the “missing numbers,” see
Koenen (1999).
In DBS systems, MPEG-2 is used for video compression. As a first
or preprocessing step, the analog outputs from the red (R), green (G),
and blue (B) color cameras are converted to a luminance component
(Y) and two chrominance components (Cr) and (Cb). This is similar to
the analog NTSC arrangement shown in Fig. 9.7, except that the
coefficients of the matrix M are different. In matrix notation, the
equation relating the three primary colors to the Y, Cr, and Cb com-
ponents is
Y
0.299
0.587
0.114
R
[
Cr]
 [
0.169
0.331
0.500 ] [
G]
Cb
0.500
0.419
0.081
B
(16.2)
466
Chapter Sixteen
TLFeBOOK

## Page 477
