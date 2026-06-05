---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0408"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 408
confidence: "first-pass"
extraction_method: "structured-local"
---

100.8°W longitude; and DBS-3, launched June 3, 1994, is at 100.8°W
longitude. There is a spread of plus or minus 0.2° about the nominal
101°W position. The 3-dB beamwidth is given as approximately
70/D, as shown by Eq. (6.33). A 60-cm dish at 12 GHz would have a
3-dB beamwidth of approximately 70  2.5/60  2.9°, which is ade-
quate for the cluster.
16.10
The Home Receiver Indoor Unit (IDU)
The block schematic for the indoor unit (IDU) is shown in Fig. 16.7. The
transponder frequency bands shown in Fig. 16.2 are downconverted to
be in the range 950 to 1450 MHz, but of course, each transponder
retains its 24-MHz bandwidth. The IDU must be able to receive any of
the 32 transponders, although only 16 of these will be available for a sin-
gle polarization. The tuner selects the desired transponder. It should be
recalled that the carrier at the center frequency of the transponder is
QPSK modulated by the bit stream, which itself may consist of four to
eight TV programs time-division multiplexed. Following the tuner, the
carrier is demodulated, the QPSK modulation being converted to a bit
stream. Error correction is carried out in the decoder block labeled
FEC1. The demultiplexer following the FEC1 block separates out the
individual programs, which are then stored in buffer memories for fur-
ther processing (not shown in the diagram). This further processing
would include such things as conditional access, viewing history of pay-
per-view (PPV) usage, and connection through a modem to the service
provider (for PPV billing purposes). A detailed description of the IRD
will be found in Mead (2000).
16.11
Downlink Analysis
The main factor governing performance of a DBS system will be the
[Eb/No] of the downlink. The downlink performance for clear-sky condi-
tions can be determined using the method described in Sec. 12.8 and illus-
trated in Example 12.2 that follows. The effects of rain can be calculated
using the procedure given in Sec. 12.9.2 and illustrated in Example 12.3
that follows. These examples are worked in Mathcad (see Appendix H). In
calculating the effects of rain, use is made of Fig.16.8, which shows the
regions (indicated by letters) tabulated along with rainfall in Table 16.2.
Example 16.1
A ground station located at 45°N and 90°W is receiving the
transmission from a DBS at 101°W. The [EIRP] is 55 dBW, and the downlink
frequency may be taken as 12.5 GHz for calculations. An 18-in-diameter
antenna is used, and an efficiency of 0.55 may be assumed. Miscellaneous
transmission losses of 2 dB also may be assumed. For the IRD, the equivalent
474
Chapter Sixteen
TLFeBOOK
