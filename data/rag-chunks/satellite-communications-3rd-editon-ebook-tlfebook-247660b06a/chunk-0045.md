---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0045"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 45
confidence: "first-pass"
extraction_method: "structured-local"
---

solution
Enter the 4-digit year:
y :  2000
Enter the month number:
mon :  12
Enter the day number of the month:
dy :  18  day
Enter the time of day:
hours :  13  hr
minutes :  0  min
seconds :  0  sec
d :  dy  hours  minutes  seconds
y :  if (mon  2, y  1, y)
mon :  if (mon  2, mon  12, mon)
A :  floor 

B :  2  A  floor  
C:  floor (365  25 y)
D:  floor (30.6001  (mon  1) )
JD :  B  day  C  day  D  day  d  1720994.5  day
JD :  2451897.0417  day
          
In Sec. 2.9.7, certain calculations require a time interval measured
in Julian centuries, where a Julian century consists of 36,525 mean
solar days. The time interval is reckoned from a reference time of
January 0.5, 1900, which corresponds to 2,415,020 Julian days.
Denoting the reference time as JDref, the Julian century by JC, and the
time in question by JD, then the interval in Julian centuries from the
reference time to the time in question is given by
T 
(2.20)
This is illustrated in the following example.
JD  JDref 

JC
A
4
y

100
40
Chapter Two
TLFeBOOK

## Page 56

Example 2.11
Find the time in Julian centuries from the reference time
January 0.5, 1900 to 13 h UT on 18 December 2000.
solution
JDref:  2415020  day
JC:  36525  day
From Example 2.10:
JD :  2451897.0417  day
Equation (2.20) gives
T : 
T  1.00963838
      
Note that the time units are days and T is dimensionless.
2.9.4
Sidereal time
Sidereal time is time measured relative to the fixed stars (Fig. 2.7). It
will be seen that one complete rotation of the earth relative to the fixed
JD  JDref

JC
Orbits and Launching Methods
41
Figure 2.7
A sidereal day, or one rotation of the earth relative to
fixed stars, is shorter than a solar day.
TLFeBOOK

## Page 57
