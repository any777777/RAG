---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0404"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 404
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 479

For a stereo CD recording, the sampling frequency is 44.1 kHz, and the
number of bits per sample is 16:
Rb  44.1  103  16  2
 1411.2 kb/s
The factor 2 appears on the right-hand side because of the two chan-
nels in stereo. This bit rate, approximately 1.4 Mb/s, represents too
high a fraction of the total bit rate allowance per channel, and hence
the need for audio compression. Audio compression in MPEG exploits
certain perceptual phenomena in the human auditory system. In par-
ticular, it is known that a loud sound at one particular frequency will
mask a less intense sound at a nearby frequency. For example, consider
a test conducted using two tones, one at 1000 Hz, which will be called
the masking tone, and the other at 1100 Hz, the test tone. Starting with
both tones at the same level, say, 60 dB above the threshold of hear-
ing, if now the level of the 1000-Hz tone is held constant while reduc-
ing the level of the 1100-Hz tone, a point will be reached where the
1100-Hz tone becomes inaudible. The 1100-Hz tone is said to be
masked by the 1000-Hz tone. Assume for purposes of illustration that
the test tone becomes inaudible when it is 18 dB below the level of the
masking tone. This 18 dB is the masking threshold. It follows that any
noise below the masking threshold also will be masked.
For the moment, assuming that only these two tones are present,
then it can be said that the noise floor is 18 dB below the masking tone.
If the test-tone level is set at, say, 6 dB below the masking tone, then
of course it is 12 dB above the noise floor. This means that the signal-
to-noise ratio for the test tone need be no better than 12 dB. Now in a
pulse-code modulated (PCM) system the main source of noise is that
arising from the quantization process (see Sec. 10.3). It can be shown
(see, for example, Roddy and Coolen, 1995) that the signal-to-quanti-
zation noise ratio is given by
 q
 22n
(16.4)
where n is the number of bits per sample. In decibels this is
 	q
 10 log 22n

6n dB
(16.5)
This shows that increasing n by 1 bit increases the signal-to-quanti-
zation noise ratio by 6 dB. Another way of looking at this is to say that
S

N
S

N
Direct Broadcast Satellite Services
469
TLFeBOOK

## Page 480
