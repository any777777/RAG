---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0044"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 44
confidence: "first-pass"
extraction_method: "structured-local"
---

sal time” systems, all interrelated (see Wertz, 1984) and all with the
mean solar day as the fundamental unit. For present purposes, the
distinction between these systems is not critical, and the term univer-
sal time, abbreviation UT, will be used from now on.
For computations, UT will be required in two forms: as a fraction of
a day and in degrees. Given UT in the normal form of hours, minutes,
and seconds, it is converted to fractional days as
UTday 
(hours 

)
(2.18)
In turn, this may be converted to degrees as
UT°  360  UTday
(2.19)
2.9.3
Julian dates1
Calendar times are expressed in UT, and although the time interval
between any two events may be measured as the difference in their
calendar times, the calendar time notation is not suited to computa-
tions where the timing of many events has to be computed. What is
required is a reference time to which all events can be related in deci-
mal days. Such a reference time is provided by the Julian zero time
reference, which is 12 noon (12:00 UT) on January 1 in the year 4713
B.C.! Of course, this date would not have existed as such at the time; it
is a hypothetical starting point which can be established by counting
backward according to a certain formula. For details of this intriguing
time reference, see Wertz (1984). The important point is that ordinary
calendar times are easily converted to Julian dates, measured on a
continuous time scale of Julian days. To do this, first determine the
day of the year, keeping in mind that day zero, denoted as Jan 0, is
December 31. For example, noon on December 31 is denoted as Jan
0.5, and noon on January 1 is denoted as Jan 1.5. It may seem strange
that the last day of December should be denoted as “day zero in
January,” but it will be seen that this makes the day count correspond
to the actual calendar day.
A general method for calculating the Julian day for any date and
time is given in Duffett-Smith (1986, p. 9). The Mathcad routine based
on this is illustrated in the following example.
Example 2.10
Find the Julian day for 13 h UT on 18 December 2000.
seconds

3600
minutes

60
1

24
Orbits and Launching Methods
39
1It should be noted that the Julian date is not associated with the Julian calendar
introduced by Julius Caesar
TLFeBOOK

## Page 55
