---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0159"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 159
confidence: "first-pass"
extraction_method: "structured-local"
---

hard limiter before being amplified in the TWT. The hard limiter is a
circuit which clips the carrier amplitude close to the zero baseline to
remove any amplitude modulation. The frequency modulation is pre-
served in the zero crossover points and is not affected by the limiting.
A TWT also may be called on to amplify two or more carriers simul-
taneously, this being referred to as multicarrier operation. The AM/PM
conversion is then a complicated function of carrier amplitudes, but in
addition, the nonlinear transfer characteristic introduces a more seri-
ous form of distortion known as intermodulation distortion. The non-
linear transfer characteristic may be expressed as a Taylor series
expansion which relates input and output voltages:
eo  aei  bei
2  cei
3  . . .
(7.1)
Here, a, b, c, etc. are coefficients which depend on the transfer char-
acteristic, eo is the output voltage, and ei is the input voltage, which
consists of the sum of the individual carriers. The third-order term is
cei3. This and higher-order odd-power terms give rise to intermodula-
tion products, but usually only the third-order contribution is signifi-
cant. Suppose multiple carriers are present, separated from one
another by "f, as shown in Fig. 7.20. Considering specifically the car-
riers at frequencies f1 and f2, these will give rise to frequencies 2f2 
f1 and 2f1  f2 as a result of the third-order term. (This is demon-
strated in App. E.)
Because f2  f1  "f, these two intermodulation products can be
written as f2  "f and f1  "f, respectively. Thus the intermodulation
products fall on the neighboring carrier frequencies as shown in Fig.
7.20. Similar intermodulation products will arise from other carrier
pairs, and when the carriers are modulated the intermodulation dis-
tortion appears as noise across the transponder frequency band. This
intermodulation noise is considered further in Sec. 12.10.
192
Chapter Seven 
Figure 7.19
Phase characteristics for a TWT.  is the input-to-output
phase shift, and S is the value at saturation. The AM/PM curve is
derived from the slope of the phase shift curve.
TLFeBOOK

## Page 207
