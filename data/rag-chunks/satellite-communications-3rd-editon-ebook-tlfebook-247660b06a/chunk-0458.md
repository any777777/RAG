---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0458"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 458
confidence: "first-pass"
extraction_method: "structured-local"
---

553
Mathcad
1 Notation
Mathcad is a mathematical software package used in problem solving
throughout this book. Equations written in Mathcad appear on the
screen more or less the way one would write them by hand, which
makes them easy to interpret. There are some differences in notation,
however, which need to be explained. Values are assigned to variables
by means of a colon.
Typing the statement
x:5
appears on the screen as
x:  5
This is an assignment statement. To find the value of x, one types
x 
and the screen shows
x  5
Suppose a second variable y is typed in as
y:x2
This appears on the screen as
y:  x2
AppendixH
1Mathcad is a registered trademark of Mathsoft, Inc.
Copyright 2001 The McGraw-Hill Companies   Click Here for Terms of Use
TLFeBOOK

## Page 563

Typing in
y 
results in the screen displaying
y  25
There are various ways in which a range of values can be assigned
to a variable. The statement
x:0;9
appears on the screen as
x:  0 .. 9
meaning that x takes on all integer values from 0 to 9. Thus a colon
appearing in front of an equal sign means the value or values to the
right are being assigned to the variable on the left. The normal equal
sign gives the value that the variable has, which of course may have
changed from the assigned value through computation.
Mathcad has built-in units, the default set being SI units. These are
best illustrated by means of a simple example. To set a current equal
to 3 amperes, one types
I:3*amp
and this appears on the screen as
I:  3  amp
Likewise,
R:10*ohm
appears as
R:  10  ohm
The statement
V:I*R
appears as
V:  I  R
554
Appendix H
TLFeBOOK

## Page 564

Typing
V 
appears as
V  30  kg  m2  sec2  coul1 I
This gives the voltage in terms of fundamental units. A units
placeholder 
I appears at the end. Placing the cursor on this and typ-
ing in the desired units changes these automatically. Thus, setting
the cursor on the 
I and typing volt gives
V  30  volt
The units will change values automatically. Thus, in Example 2.1 of
the text, the mean motion n is defined as
n: 
This sets n equal to 2	 radians per day. Typing
n 
results in
n  7.272  105  sec1 I
Typing rad/sec at the units placeholder results in
n  7.272  105 
Typing in rad/day results in
n  6.283 
(These values have been rounded off.)
rad

day
rad

sec
2  	

1  day
Mathcad Notation
555
TLFeBOOK

## Page 565

This page intentionally left blank.
TLFeBOOK

## Page 566
