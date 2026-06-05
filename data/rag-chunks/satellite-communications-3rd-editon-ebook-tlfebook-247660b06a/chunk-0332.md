---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0332"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 332
confidence: "first-pass"
extraction_method: "structured-local"
---

False detection probability.
Consider now a sequence of N which is not
the UW but which would be interpreted as the UW even if it differs
from it in some number of bit positions E, and let I represent the num-
ber of bit positions by which the random sequence actually does differ
from the UW. Thus E represents the number of acceptable “bit errors”
considered from the point of view of the UW, although they may not
be errors in the message they represent. Likewise, I represents the
actual number of “bit errors” considered from the point of view of the
UW, although they may not be errors in the message they represent.
As before, the number of combinations of N things taken I at a time
is given by Eq. (14.19), and hence the number of words acceptable as
the UW is
W  
E
I  0
NCI
(14.23)
The number of words which can be formed from a random sequence
of N bits is 2N, and on the assumption that all such words are
equiprobable, the probability of receiving any one particular word is
2N. Hence the probability of a false detection is
PF  2NW
(14.24)
Written out in full, this is
PF  2N 
E
I  0
(14.25)
Again it will be noticed that because this is an average probability,
it is not necessary to know a specific value of I. Also, in this case, the
BER does not enter into the calculation. A Mathcad calculation is giv-
en in Example 14.3.
Example 14.3
Determine the probability of false detection for the follow-
ing values:
N:  40
E:  5
solution
PF:  2N 	 
E
I  0
PF  6.9 	 107

From Examples 14.2 and 14.3 it is seen that the probability of a
false detection is much higher than the probability of a miss, and this
N!

I! 	 (N  I)!
N!

I! (N  I)!
Satellite Access
397
TLFeBOOK

## Page 408
