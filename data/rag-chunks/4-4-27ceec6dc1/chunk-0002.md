---
chunk_id: "4-4-27ceec6dc1-chunk-0002"
source_id: "4-4-27ceec6dc1"
source_file: "New folder (3)/4.4.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

Example: Coverage of the Continental United States
(CONUS)
Consider a satellite positioned at approximately 100◦W longitude in geostationary orbit.
• The continental United States subtends approximately:
– 3◦in the North–South direction
– 6◦in the East–West direction
To cover this region using a single satellite beam, the antenna must produce a
beamwidth of approximately 6◦× 3◦.
Satellite Antenna Characteristics
An aperture antenna producing this beam has:
• Dimensions: approximately 12.5λ × 25λ
• Maximum gain: approximately 33 dB (antenna efficiency: 50%)
• Edge-of-coverage gain: approximately 30 dB (3 dB edge of beam loss)
Link Budget Example for a Small Earth Station
Consider the following parameters:
• Transponder output power: 5 W at 4 GHz
• Path length to receiving station (typical): 38, 000 km
• Satellite antenna gain (edge of coverage): 30 dB
• Earth station antenna diameter: 3 m
• Earth station antenna efficiency: 63%
Received Carrier Power
The received carrier power is given by
Pr = 7.0 + 30.0 −196.5 + 40.0 = −119.5 dBW
2

## Page 3

Noise Power
For a receiver with:
• Noise bandwidth: 30 MHz
• System noise temperature: 100 K
the noise power is
N = kTsBn = −228.6 + 20.0 + 74.8 = −133.8 dBW
Carrier-to-Noise Ratio
C
N = Pr −N = 14.3 dB
This value exceeds the FM threshold of approximately 9.5 dB by 4.8 dB, providing
adequate operational margin.
Direct Broadcast Satellite Television (DBS-TV)
DBS-TV systems were first deployed in Europe in the 1980s using analog FM transmission
in the Ku band. In the 1990s, advances in digital modulation enabled large-scale DBS-TV
deployment, particularly in the United States.
DBS-TV Characteristics
• Operating frequency band: 12.2–12.7 GHz (BSS band)
• Typical transponder power: 100–200 W
• Typical flux density at Earth: up to −100 dBW/m2
• Number of transponders per satellite: up to 16
• Total RF power: approximately 2.6 kW
DBS-TV satellites are among the largest commercial GEO satellites, with launch
masses approaching 6800 kg.
3

## Page 4
