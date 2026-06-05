---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0322"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 322
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 396

system timing is derived from the high-stability clock in the master pri-
mary, which is accurate to 1 part in 1011 (Lewis, 1982). A clock on the
satellite is locked to the master primary, and this acts as the clock for
the other participating earth stations. The satellite clock will provide a
constant frame time, but the participating earth stations must make
386
Chapter Fourteen
Figure 14.12
Some of the basic equipment blocks in a TDMA system.
TLFeBOOK

## Page 397

corrections for variations in the satellite range, since the transmitted
bursts from all the participating earth stations must reach the satellite
in synchronism. Details of the timing requirements will be found in
Spilker (1977).
In the INTELSAT system, two reference bursts are transmitted in
each frame. The first reference burst, which marks the beginning of a
frame, is transmitted by a master primary (or a primary) reference
station and contains the timing information needed for the acquisition
and synchronization of bursts. The second reference burst, which is
transmitted by a secondary reference station, provides synchroniza-
tion but not acquisition information. The secondary reference burst is
ignored by the receiving earth stations unless the primary or master
primary station fails.
14.7.1
Reference burst
The reference burst that marks the beginning of a frame is subdivid-
ed into time slots or channels used for various functions. These will
differ in detail for different networks, but Fig. 14.13 shows some of
the basic channels that are usually provided. These can be summa-
rized as follows:
Guard time (G). A guard time is necessary between bursts to prevent
the bursts from overlapping. The guard time will vary from burst to
burst depending on the accuracy with which the various bursts can
be positioned within each frame.
Satellite Access
387
Figure 14.13
Frame and burst formats for a TDMA system.
TLFeBOOK

## Page 398
