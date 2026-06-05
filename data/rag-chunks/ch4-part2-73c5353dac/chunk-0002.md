---
chunk_id: "ch4-part2-73c5353dac-chunk-0002"
source_id: "ch4-part2-73c5353dac"
source_file: "New folder (3)/ch4_part2.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

Calculation of System Noise Temperature 
 
 
 
• This is the form used for all radio receivers, with 
few exceptions, known as the superhet (short for 
superheterodyne). The superhet receiver has 
three main subsystems: a front end (RF amplifier, 
mixer and local oscillator) an IF amplifier (IF 
amplifiers and filters), and a demodulator and 
baseband section. 
 
• The RF amplifier in a satellite communications 
receiver must generate as little noise as possible, 
so it is called a low noise amplifier or LNA. The 
mixer and local oscillator form a frequency 
conversion stage that down converts the RF signal 
to a fixed intermediate frequency (IF), where the 
signal can be amplified and filtered accurately.

## Page 5

• Many earth station receivers use the double 
superhet configuration shown in Figure 4.6 which 
has two stages of frequency conversion.

## Page 6

• The noisy devices in the receiver are replaced by 
equivalent noiseless blocks with the same gain 
and noise generators at the input to each block 
such that the block produces the same noise at its 
output as the device it replaces. 
 
 
• The total noise power at the output of the IF 
amplifier of the receiver in Figure 4.7a is given by 
 
 
where GRF, Gm, and GIF are the gains of the RF 
amplifier, mixer, and IF amplifier, and TRF, Tm, and

## Page 7

TIF are their equivalent noise temperatures. Tin is 
the noise temperature of the antenna, measured at 
its output port. 
 
• Equation (4.15) can be rewritten as 
 
• The single source of noise shown in Figure 4.7b 
with noise temperature T, generates the same 
noise power Pn at its output if 
 
• The noise power at the output of the noise model 
in Figure 4.7b will be the same as the noise power 
at the output of the noise model in Figure 4.7a if 
 
• Hence the equivalent noise source in Figure 4.7b 
has a system noise temperature T, where 
 
 
• Succeeding stages of the receiver contribute less 
and less noise to the total system noise 
temperature. Frequently, when the RF amplifier in 
the receiver front end has a high gain, the noise 
contributed by the IF amplifier and later stages 
can be ignored and the system noise temperature 
is simply the sum of the antenna noise

## Page 8
