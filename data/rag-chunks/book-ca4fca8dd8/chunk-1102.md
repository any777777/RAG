---
chunk_id: "book-ca4fca8dd8-chunk-1102"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1102
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 659

Section 18.3
Keeping Track of a Complex World
659
(a)
(b)
Figure 18.10 Images from (a) upstream and (b) downstream surveillance cameras roughly
two miles apart on Highway 99 in Sacramento, California. The boxed vehicle has been
identiﬁed at both cameras.
18.3.2 Example: Traﬃc monitoring
Figure 18.10 shows two images from widely separated cameras on a California freeway. In
this application, we are interested in two goals: estimating the time it takes, under current
trafﬁc conditions, to go from one place to another in the freeway system; and measuring
demand—that is, how many vehicles travel between any two points in the system at particular
times of the day and on particular days of the week. Both goals require solving the data
association problem over a wide area with many cameras and tens of thousands of vehicles
per hour.
With visual surveillance, false alarms are caused by moving shadows, articulated vehi-
cles, reﬂections in puddles, etc.; detection failures are caused by occlusion, fog, darkness, and
lack of visual contrast; and vehicles are constantly entering and leaving the freeway system
at points that may not be monitored. Furthermore, the appearance of any given vehicle can
change dramatically between cameras depending on lighting conditions and vehicle pose in
the image, and the transition model changes as trafﬁc jams come and go. Finally, in dense
trafﬁc with widely separated cameras, the prediction error in the transition model for a car
driving from one camera location to the next is far greater than the typical separation between
vehicles. Despite these problems, modern data association algorithms have been successful
in estimating trafﬁc parameters in real-world settings.
Data association is an essential foundation for keeping track of a complex world, be-
cause without it there is no way to combine multiple observations of any given object. When
objects in the world interact with each other in complex activities, understanding the world
requires combining data association with the relational and open-universe probability models
of Section 18.2. This is currently an active area of research.

## Page 660
