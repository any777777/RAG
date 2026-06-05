---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0294"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 294
confidence: "first-pass"
extraction_method: "structured-local"
---

The second situation, illustrated in Fig. 13.5b, is where multiple
interfering carriers are present within the wanted passband, such as
with single carrier per channel (SCPC) operation discussed in Sec.
14.5. Here, Q represents the sum of the interfering carrier powers
within the passband, and [Q]  0 dB.
In the FCC report FCC/OST R83–2 (Sharp, 1983), Q values are com-
puted for a wide range of interfering and wanted carrier combinations.
Typical [Q] values obtained from the FCC report are as follows: with
the wanted carrier a TV/FM signal and the interfering carrier a simi-
lar TV/FM signal, [Q]  0 dB; with SCPC/PSK interfering carriers, [Q]
 27.92 dB; and with the interfering carrier a wideband digital-type
signal, [Q]  3.36 dB.
The passband [C/I] ratio is calculated using
 	pb   	ant  [Q]
(13.7)
The positions of these ratios in the receiver chain are illustrated in
Fig. 13.6, where it will be seen that both [C/I]ant and [C/I]pb are prede-
tection ratios, measured at rf or IF. Interference also can be measured
in terms of the postdetector output, shown as [S/I] in Fig. 13.6, and
this is discussed in the next section.
13.2.6
Receiver transfer characteristic
In some situations a measure of the interference in the postdetection
baseband, rather than in the IF or rf passband, is required. Baseband
interference is measured in terms of baseband signal-to-interference
ratio [S/I]. To relate [S/I] to [C/I]ant, a receiver transfer characteristic is
introduced which takes into account the modulation characteristics of
the wanted and interfering signals and the carrier frequency separa-
tion. Denoting the receiver transfer characteristic in decibels by
[RTC], the relationship can be written as
 	   	ant  [RTC]
(13.8)
It will be seen that [RTC] is analogous to the receiver processing gain
[GP] introduced in Sec. 9.6.3. Note that it is the [C/I] at the antenna
C
I
S
I
C
I
C
I
354
Chapter Thirteen
Figure 13.6
Carrier-to-interference ratios and signal-to-interference ratio.
TLFeBOOK

## Page 365
