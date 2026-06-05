---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0403"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 403
confidence: "first-pass"
extraction_method: "structured-local"
---

quantizer following the DCT transform block, the discrete values of G(u,
v) are quantized to predetermined levels. This reduces the number of
levels to be transmitted and therefore provides compression. The com-
ponents of G(u, v) at the higher spatial frequencies represent finer spa-
tial resolution. The human eye is less sensitive to resolution at these
high spatial frequencies; therefore, they can be quantized in much
coarser steps. This results in further compression. (This step is analo-
gous to the nonlinear quantization discussed in Sec. 10.3.)
Compression is also achieved through motion estimation. Frames in
MPEG-2 are designated I, P, and B frames, and motion prediction is
achieved by comparing certain frames with other frames. The I frame 
is an independent frame, meaning that it can be reconstructed without
reference to any other frames. A P (for previous) frame is compared with
the previous I frame, and only those parts which differ as a result of move-
ment need to be encoded. The comparison is carried out in sections called
macroblocks for the frames. A B (for bidirectional) frame is compared with
the previous I or P frame and with the next P frame. This obviously
means that frames must be stored in order for the forward comparison to
take place. Only the changes resulting from motion are encoded, which
provides further compression. Taking the 200 Mb/s deduced in Sec. 16.6
as the uncompressed rate, and taking 5 Mb/s as typical of that for a TV
channel, the compression needed is on the order 200/5  40:1. The 5 Mb/s
would include audio and data, but these should not take more than about
200 kb/s. Audio compression is considered later in this section.
The whole encoding process relies on digital decision-making cir-
cuitry and is computationally intensive and expensive. The decoding
process is much simpler because the rules for decoding are part of the
syntax of the bit stream. Decoding is carried out in the integrated
receiver decoder (IRD) unit. This is described in Sec. 16.8.
In DBS systems, MPEG-1 is used for audio compression, and as dis-
cussed earlier, MPEG-2 is used for video compression. Both of these
MPEG standards cover audio and video, but MPEG-1 video is not
designed for DBS transmissions. MPEG-1 audio supports mono and
two-channel stereo only, which is considered adequate for DBS sys-
tems currently in use. MPEG-2 audio supports multichannel audio in
addition to mono and stereo. It is fully compatible with MPEG-1 audio,
so the integrated receiver decoders (IRDs), which carry MPEG-2
decoders, will have little trouble in being upgraded to work with DBS
systems transmitting multichannel audio.
The need for audio compression can be seen by considering the bit
rate required for high-quality audio. The bit rate is equal to the num-
ber of samples per second (the sampling frequency fs) multiplied by the
number of bits per sample n:
Rb  fs  n
(16.3)
468
Chapter Sixteen
TLFeBOOK
