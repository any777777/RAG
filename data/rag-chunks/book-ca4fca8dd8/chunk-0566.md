---
chunk_id: "book-ca4fca8dd8-chunk-0566"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 566
confidence: "first-pass"
extraction_method: "structured-local"
---

342
Chapter 10
Knowledge Representation
where Terminated and Initiated are deﬁned by:
Terminated(f,t1,t5) ⇔
∃e,t2,t3,t4 Happens(e,t2,t4)∧Terminates(e, f,t3)∧t1 ≤t2 ≤t3 ≤t4 ≤t5
Initiated(f,t1,t5) ⇔
∃e,t2,t3,t4 Happens(e,t2,t4)∧Initiates(e, f,t3)∧t1 ≤t2 ≤t3 ≤t4 ≤t5
We can extend event calculus to represent simultaneous events (such as two people being nec-
essary to ride a seesaw), exogenous events (such as the wind moving an object), continuous
events (such as the rising of the tide), nondeterministic events (such as ﬂipping a coin and
having it come up heads or tails), and other complications.
10.3.1 Time
Event calculus opens us up to the possibility of talking about time points and time intervals.
We will consider two kinds of time intervals: moments and extended intervals. The distinc-
tion is that only moments have zero duration:
Partition({Moments,ExtendedIntervals},Intervals)
i∈Moments ⇔Duration(i)=Seconds(0).
Next we invent a time scale and associate points on that scale with moments, giving us abso-
lute times. The time scale is arbitrary; we will measure it in seconds and say that the moment
at midnight (GMT) on January 1, 1900, has time 0. The functions Begin and End pick out
the earliest and latest moments in an interval, and the function Time delivers the point on the
time scale for a moment. The function Duration gives the difference between the end time
and the start time.
Interval(i) ⇒Duration(i)=(Time(End(i))−Time(Begin(i))).
Time(Begin(AD1900))=Seconds(0).
Time(Begin(AD2001))=Seconds(3187324800).
Time(End(AD2001))=Seconds(3218860800).
Duration(AD2001)=Seconds(31536000).
To make these numbers easier to read, we also introduce a function Date, which takes six
arguments (hours, minutes, seconds, day, month, and year) and returns a time point:
Time(Begin(AD2001))=Date(0,0,0,1,Jan,2001)
Date(0,20,21,24,1,1995)=Seconds(3000000000).
Two intervals Meet if the end time of the ﬁrst equals the start time of the second. The complete
set of interval relations (Allen, 1983) is shown below and in Figure 10.2:
Meet(i, j)
⇔
End(i)=Begin(j)
Before(i, j)
⇔
End(i) < Begin(j)
After(j,i)
⇔
Before(i, j)
During(i, j)
⇔
Begin(j) < Begin(i) < End(i) < End(j)
Overlap(i, j)
⇔
Begin(i) < Begin(j) < End(i) < End(j)
Starts(i, j)
⇔
Begin(i) = Begin(j)
Finishes(i, j)
⇔
End(i) = End(j)
Equals(i, j)
⇔
Begin(i) = Begin(j)∧End(i) = End(j)
These all have their intuitive meaning, with the exception of Overlap: we tend to think of
overlap as symmetric (if i overlaps j then j overlaps i), but in this deﬁnition, Overlap(i, j)
only is true if i begins before j. Experience has shown that this deﬁnition is more useful for
