---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0248"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 248
confidence: "first-pass"
extraction_method: "structured-local"
---

decision decoding is more complex to implement than hard decision
decoding and is only used where the improvement it provides must
be had.
11.10
Automatic Repeat Request (ARQ)
Error detection without correction is more efficient than forward error
correction in terms of code utilization. It is less complicated to imple-
ment, and more errors can be detected than corrected. Of course, it
then becomes necessary for the receiver to request a retransmission
when an error has been detected. This is an automatic procedure,
termed automatic repeat request (ARQ). The request for retransmission
must be made over a low-bit-rate channel where the probability of bit
error can be kept negligibly small. Because of the long round-trip delay
time, on the order of half a second or more, encountered with geosta-
tionary satellites, ARQ is only suitable for transmission that is not sen-
sitive to long delays. ARQ is normally used with block encoding.
An estimate of the probability of an error remaining undetected can
be made. With an (n, k) block code, the number of datawords is 2k, and
the total number of codewords is 2n. When a given dataword is trans-
mitted, an undetected error results when the transmission errors con-
vert the received codeword into one that contains a permissible
dataword but not the one that was transmitted. The number of such
datawords is 2k  1. An upper bound on the probability of an error get-
ting through can be made by assuming that all codewords are
equiprobable. The ratio of number of possible error words to total num-
ber of codewords then gives the average probability of error. In practice,
of course, all the codewords will not be equiprobable, those containing
datawords being more probable than those which do not. The ratio,
therefore, gives an upper bound on the probability of error:
BER 
 2 (n  k)
(11.9)
 2r
where r is the number of redundant bits in a codeword. For example, a
(15, 11) code has an upper bound of approximately 0.06, while a (64, 32)
code has an upper bound of approximately 2.3 	 1010.
It will be assumed, therefore, that the data are sent in coded blocks
(referred to simply as blocks in the following). The receiver acknowledges
receipt of each block by sending back a positive acknowledgment or ACK
signal if no errors are detected in the block and a negative acknowledg-
ment or NAK signal if errors are detected. In what is termed stop and
2k  1

2n
300
Chapter Eleven
TLFeBOOK

## Page 315
