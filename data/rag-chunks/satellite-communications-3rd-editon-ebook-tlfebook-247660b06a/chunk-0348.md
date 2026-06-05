---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0348"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 348
confidence: "first-pass"
extraction_method: "structured-local"
---

along the same beam, enabling intercommunications between stations
within a beam. Of course, the uplink and downlink microwave fre-
quencies are different.
Because of beam isolation, one frequency can be used for all uplinks,
and a different frequency for all downlinks (e.g., 14 and 12 GHz in the
Ku band). To simplify the satellite switch design, the switching is car-
ried out at the intermediate frequency that is common to uplinks and
downlinks. The basic block schematic for the 3  3 system is shown in
Fig. 14.28.
A mode pattern is a repetitive sequence of satellite switch modes,
also referred to as SS/TDMA frames. Successive SS/TDMA frames
need not be identical, since there is some redundancy between modes.
For example, in Fig. 14.27b, beam A interconnects with beam B in
modes 3 and 5, and thus not all modes need be transmitted during
each SS/TDMA frame. However, for full interconnectivity, the mode
pattern must contain all modes.
All stations within a beam receive all the TDM frames transmitted
in the downlink beam. Each frame is a normal TDMA frame consist-
ing of bursts, addressed to different stations in general. As mentioned,
successive frames may originate from different transmitting stations
and therefore have different burst formats. The receiving station in a
beam recovers the bursts addressed to it in each frame.
The two basic types of switch matrix are the crossbar matrix and the
rearrangeable network. The crossbar matrix is easily configured for the
broadcast mode, in which one station transmits to all stations. The
broadcast mode with the rearrangeable network-type switch is more
complex, and this can be a deciding factor in favor of the crossbar
matrix (Watt, 1986). The schematic for a 3  3 crossbar matrix is
shown in Fig. 14.29, which also shows input beam B connected in the
broadcast mode.
The switching elements may be ferrites, diodes, or transistors. The
dual-gate FET appears to offer significant advantages over the other
416
Chapter Fourteen
Figure 14.28
Switch matrix in the R.F. link.
TLFeBOOK

## Page 427
