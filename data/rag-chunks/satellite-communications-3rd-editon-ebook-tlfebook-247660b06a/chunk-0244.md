---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0244"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 244
confidence: "first-pass"
extraction_method: "structured-local"
---

tion. Figure 11.6 shows the general form for concatenated codes. The
input data are fed into the encoder designed for burst error correction.
This is the outer encoder. The output from the outer encoder is fed into
the encoder designed for random error correction. This is the inner
encoder. The signal is then modulated and passed on for transmission.
At the receiver, the signal is demodulated. The inner decoder matches
the inner encoder and follows the demodulator. The output from the
inner decoder is fed into the outer decoder, which matches the outer
encoder. The term outer refers to the outermost encoding/decoding
units in the equipment chain, and the term inner refers to the inner-
most encoding/decoding unit. In digital satellite television, the outer
code is a Reed-Solomon code, and the inner code is a convolutional code.
The inner decoder utilizes Viterbi decoding.
11.7
Link Parameters Affected by Coding
Where no error control coding is employed, the message will be referred
to as an uncoded message, and its parameters will be denoted by the
294
Chapter Eleven
Tx
Inner
encoder
Modulator
Rx
Outer
encoder
Rb
Inner
decoder
Demodulator
Outer
decoder
Rb
Figure 11.6
Concatenated coding (see Sec. 11.6).
TLFeBOOK

## Page 309

subscript U. Figure 11.7a shows the arrangement for an uncoded mes-
sage. Where error control coding is employed, the message will be
referred to as a coded message, and its parameters will be denoted by
the subscript C. Figure 11.7b shows the arrangement for a coded mes-
sage. For comparison purposes, the [C/No] value is assumed to be the
same for both situations. The input bit rate to the modulator for the
uncoded message is Rb and for the coded message is Rc. Since n code bits
must be transmitted for every k data bits, the bit rates are related as
 rc
(11.2)
Since rc is always less than unity, then Rc  Rb always. For constant
carrier power, the bit energy is inversely proportional to bit rate (see
Eq. 10.22), and therefore,
Rb

Rc
Error Control Coding
295
Tx
Modulator
Rb
Rx
Demodulator
Rb
Pe
[C/No]
Tx
Modulator
Encoder
Rb
Rc
Rx
Demodulator
Decoder
Rc
Rb
[C/No]
BER
(a)
(b)
Figure 11.7
Comparing links with and without FEC.
TLFeBOOK

## Page 310
