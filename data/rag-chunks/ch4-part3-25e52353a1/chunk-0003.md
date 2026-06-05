---
chunk_id: "ch4-part3-25e52353a1-chunk-0003"
source_id: "ch4-part3-25e52353a1"
source_file: "New folder (3)/ch4_part3.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 3
confidence: "first-pass"
extraction_method: "structured-local"
---

• The maximum path length for a GEO satellite link is 
40,000 km, which gives a path loss of 196.5 dB at 4 
GHz (𝜆𝜆 = 0.075 m).  
• We must make an allowance in the link budget for 
some losses that will inevitably occur on the link. At C 
band, propagation losses are small, but the slant path 
through the atmosphere will suffer a typical 
attenuation of 0.2 dB in clear air. We will allow an 
additional 0.5-dB margin in the link design to account 
for 
miscellaneous 
losses, 
such 
as 
antenna 
mispointing, polarization mismatch, and antenna 
degradation, to ensure that the link budget is 
realistic. 
• The earth station receiver C/N ratio is first calculated 
for clear air conditions, with no rain in the slant path. 
The C/N ratio is then recalculated taking account of 
the effects of rain.  
• The minimum permitted overall C/N ratio for this link 
is 9.5 dB, corresponding to the FM threshold of an 
analog satellite TV receiver. Table 4.4a shows that we 
have a downlink C/N of 16.0 dB in clear air, giving a 
link margin of 6.5 dB. This link margin is available in 
clear air conditions, but will be reduced when there is 
rain in the slant path.

## Page 6

• Heavy rain in the slant path can cause up to 1 dB of 
attenuation at 4 GHz, which reduces the received 
power by 1 dB and increases the noise temperature 
of the receiving system. 
• The sky noise temperature resulting from a path 
attenuation Atotal dB is found from the output noise 
model using an assumed medium temperature of 273 
K for the rain 𝑇𝑇𝑠𝑠𝑠𝑠𝑠𝑠= 273(1 −10−𝐴𝐴/10). 
• Using a total path loss for clear air plus rain of 1.2 dB 
(ratio of 1.32), the sky noise temperature in rain is 
 
• In clear air the sky noise temperature is about 13 K, 
the result of 0.2 dB of clear air attenuation.  
• The noise temperature of the receiving system has 
therefore increased by (66 - 13) K = 53 K to 75 + 53 K 
= 128 K with 1 dB rain attenuation in the slant path, 
from a clear air value of 75 K. This is an increase in 
system noise temperature of 2.3 dB. 
• We can now adjust the link budget very easily to 
account for heavy rain in the slant path without 
having to recalculate the C/N ratio from the 
beginning. The received carrier power is reduced by 1 
dB because of the rain attenuation and the system

## Page 7
