---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0405"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 405
confidence: "first-pass"
extraction_method: "structured-local"
---

a 1-bit decrease in n increases the quantization noise by 6 dB. In the
example above where 12 dB is an adequate signal-to-noise ratio, Eq.
(16.5) shows that only 2 bits are needed to encode the 1100-Hz tone
(i.e., the levels would be quantized in steps represented by 00, 01, 10,
11). By way of contrast, the CD samples taken at a sampling frequen-
cy of 44.1 kHz are quantized using 16 bits to give a signal-to-quanti-
zation noise ratio of 96 dB.
Returning to the example of two tones, in reality, the audio signal
will not consist of two single tones but will be a complex signal cover-
ing a wide spectrum of frequencies. In MPEG-1, two processes take
place in parallel, as illustrated in Fig. 16.4. The filter bank divides the
spectrum of the incoming signal into subbands. In parallel with this
the spectrum is analyzed to permit identification of the masking lev-
els. The masking information is passed to the quantizer, which then
quantizes the subbands according to the noise floor.
The masking discussed so far is referred to as frequency masking for
the reasons given above. It is also an observed phenomenen that the
masking effect lasts for a short period after the masking signal is
removed. This is termed temporal masking, and it allows further com-
pression in that it extends the time for which the reduction is quanti-
zation applies. There are many more technical details to MPEG-1 than
can be covered here, and the reader is referred to Mead (2000), which
contains a detailed analysis of MPEG-1. The MPEG Web page at
http://www.mpeg.org/MPEG/audio.html also provides a number of
articles on the subject. The compressed bit rate for MPEG-1 audio
used in DBS systems is 192 kb/s.
16.8
Forward Error Correction
Because of the highly compressed nature of the DBS signal, there is
little redundancy in the information being transmitted, and bit errors
470
Chapter Sixteen
Filter bank/FFT
Quantize –
determined
by masking
Bit-stream
output
Audio
input
Compute
masking
Sub-bands
Figure 16.4
MPEG-1 block schematic.
TLFeBOOK

## Page 481
