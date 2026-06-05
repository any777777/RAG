---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0325"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 325
confidence: "first-pass"
extraction_method: "structured-local"
---

In certain phase detection systems, the phase detector must be
allowed time to recover from one burst before the next burst is received
by it. This is termed decoder quenching, and a time slot, referred to as a
postamble, is allowed for this function. The postamble is shown as Q in
Fig. 14.13. Many systems are designed to operate without a postamble.
14.7.3
Carrier recovery
A factor which must be taken into account with TDMA is that the var-
ious bursts in a frame lack coherence so that carrier recovery must be
repeated for each burst. This applies to the traffic as well as the refer-
ence bursts. Where the carrier recovery circuit employs a phase-locked
loop such as shown in Fig. 10.20, a problem known as hangup can
occur. This arises when the loop moves to an unstable region of its
operating characteristic. The loop operation is such that it eventually
returns to a stable operating point, but the time required to do this
may be unacceptably long for burst-type signals.
One alternative method utilizes a narrowband tuned circuit filter to
recover the carrier. An example of such a circuit for quadrature phase-
shift keying (QPSK), taken from Miya (1981), is shown in Fig. 14.15. The
QPSK signal, which has been downconverted to a standard IF of 140
MHz, is quadrupled in frequency to remove the modulation, as described
in Sec. 10.7. The input frequency must be maintained at the resonant
frequency of the tuned circuit, which requires some form of automatic
frequency control. Because of the difficulties inherent in working with
high frequencies, the output frequency of the quadrupler is downcon-
verted from 560 to 40 MHz, and the AFC is applied to the voltage-
controlled oscillator (VCO) used to make the frequency conversion. The
AFC circuit is a form of phase-locked loop (PLL) in which the phase dif-
ference between input and output of the single-tuned circuit is held at
zero, which ensures that the 40-MHz input remains at the center of the
tuned circuit response curve. Any deviation of the phase difference from
zero generates a control voltage which is applied to the VCO in such a
way as to bring the frequency back to the required value.
Interburst interference may be a problem with the tuned-circuit
method because of the energy stored in the tuned circuit for any given
burst. Avoidance of interburst interference requires careful design of
the tuned circuit (Miya, 1981) and possibly the use of a postamble, as
mentioned in the previous section.
Other methods of carrier recovery are discussed in Gagliardi (1991).
14.7.4
Network synchronization
Network synchronization is required to ensure that all bursts arrive at
the satellite in their correct time slots. As mentioned previously, tim-
390
Chapter Fourteen
TLFeBOOK
