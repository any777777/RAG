---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0330"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 330
confidence: "first-pass"
extraction_method: "structured-local"
---

types of “packet satellite networks,” for example, the basic Aloha sys-
tem (Rosner, 1982), which are closely related to TDMA, in which syn-
chronization is not used.
14.7.5
Unique word detection
The unique word (UW) or burst code word (BCW) is used to establish
burst timing in TDMA. Figure 14.18 shows the basic arrangement for
detecting the UW. The received bit stream is passed through a shift
register which forms part of a correlator. As the bit stream moves
through the register, the sequence is continuously compared with a
stored version of the UW. When correlation is achieved, indicated by a
high output from the threshold detector, the last bit of the UW pro-
vides the reference point for timing purposes. It is important therefore
to know the probability of error in detecting the UW. Two possibilities
have to be considered. One, termed the miss probability, is the proba-
bility of the correlation detector failing to detect the UW even though
it is present in the bit stream. The other, termed the probability of
false alarm, is the probability that the correlation detector misreads a
sequence as the UW. Both of these will be examined in turn.
Miss probability.
Let E represent the maximum number of errors
allowed in the UW of length N bits, and let I represent the actual
number of errors in the UW as received. The following conditions
apply:
When I  E, the detected sequence is declared to be the UW.
When I  E, the detected sequence N is declared not to be the UW;
that is, the unique word is missed.
Let p represent the average probability of error in transmission (the
BER). The probability of receiving a sequence N containing I errors in
any one particular arrangement is
pI  pI (1  p)N  I
(14.18)
The number of combinations of N things taken I at a time, usually
written as NCI, is given by
NCI 
(14.19)
The probability of receiving a sequence of N bits containing I errors is
therefore
PI  NCIpI
(14.20)
N!

I! (N  I)!
Satellite Access
395
TLFeBOOK

## Page 406
