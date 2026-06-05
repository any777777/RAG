---
chunk_id: "4-3-1013b0cabc-chunk-0004"
source_id: "4-3-1013b0cabc"
source_file: "New folder (3)/4.3.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 4
confidence: "first-pass"
extraction_method: "structured-local"
---

transmitter feeds a satellite, and the resulting signals are received by thousands or mil-
lions of inexpensive receive-only terminals. In this architecture, the uplink transmitter
cost is amortized across the entire network.
Backoff Requirements in Bent-Pipe Transponders
Typical bent-pipe satellite transponders operate as quasi-linear amplifiers. The received
uplink carrier level directly controls the downlink output level. When the output high-
power amplifier (HPA) is a traveling-wave tube amplifier (TWTA), and frequency-division
multiple access (FDMA) is used, output backoff is required to suppress intermodulation
(IM) distortion products.
For multi-carrier operation, the required output backoff is generally:
OBO ≈1–3 dB
More heavily loaded FDMA systems—such as certain VSAT networks with many small
earth stations accessing a single transponder—may require:
OBO ≈5–7 dB
to maintain IM products at acceptable levels [?].
Even single-carrier operation typi-
cally requires some backoff to avoid the PM–AM conversion that occurs in nonlinear RF
amplifiers [?].
Accurate control of uplink carrier power is therefore essential. This is easily achieved
in fixed earth-station networks but more difficult in networks with many small or mobile
terminals.
Flux Density and Required Uplink EIRP
Earth station transmit power is often determined by specifying the flux density that must
arrive at the satellite or by specifying the required power at the input to the transponder.
Early INTELSAT C-band satellites required very high flux densities, on the order of
−73.7 to −67.5 dBW/m2,
to drive their transponders to saturation [?]. This required large antennas and transmit-
ters up to 3 kW. Modern domestic GEO satellites typically require lower flux densities;
at C-band a 5–9 m uplink antenna with a 100 W HPA produces a peak flux density of
7

## Page 8
