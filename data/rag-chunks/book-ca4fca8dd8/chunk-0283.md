---
chunk_id: "book-ca4fca8dd8-chunk-0283"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 283
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 174

174
Chapter 5
Constraint Satisfaction Problems
3
2
6
9
3
5
1
1 8
6 4
8 1
2 9
7
8
6 7
8 2
2 6
9 5
8
2
3
9
5
1
3
3
2
6
9
3
5
1
1 8
6 4
8 1
2 9
7
8
6 7
8 2
2 6
9 5
8
2
3
9
5
1
3
4 8
9
1
5 7
6 7
4
8 2
2 5
7
9 3
5 4
3
7 6
2 9 5 6 4 1 3
1 3
9
4 5
3 7
8
1 4
1 4
5
7 6
6 9
4
7
8 2
1
2
3
4
5
6
7
8
9
A
B
C
D
E
F
G
H
I
A
B
C
D
E
F
G
H
 I
1
2
3
4
5
6
7
8
9
(a)
(b)
Figure 5.4 (a) A Sudoku puzzle and (b) its solution.
The Sudoku puzzles that appear in newspapers and puzzle books have the property that
there is exactly one solution. Although some can be tricky to solve by hand, taking tens of
minutes, a CSP solver can handle thousands of puzzles per second.
A Sudoku puzzle can be considered a CSP with 81 variables, one for each square. We
use the variable names A1 through A9 for the top row (left to right), down to I1 through I9 for
the bottom row. The empty squares have the domain {1,2,3,4,5,6,7,8,9} and the pre-ﬁlled
squares have a domain consisting of a single value. In addition, there are 27 different Alldiff
constraints, one for each unit (row, column, and box of 9 squares):
Alldiff(A1,A2,A3,A4,A5,A6,A7,A8,A9)
Alldiff(B1,B2,B3,B4,B5,B6,B7,B8,B9)
···
Alldiff(A1,B1,C1,D1,E1,F1,G1,H1,I1)
Alldiff(A2,B2,C2,D2,E2,F2,G2,H2,I2)
···
Alldiff(A1,A2,A3,B1,B2,B3,C1,C2,C3)
Alldiff(A4,A5,A6,B4,B5,B6,C4,C5,C6)
···
Let us see how far arc consistency can take us. Assume that the Alldiff constraints have been
expanded into binary constraints (such as A1 ̸= A2) so that we can apply the AC-3 algorithm
directly. Consider variable E6 from Figure 5.4(a)—the empty square between the 2 and the 8
in the middle box. From the constraints in the box, we can remove 1, 2, 7, and 8 from E6’s
domain. From the constraints in its column, we can eliminate 5, 6, 2, 8, 9, and 3 (although
2 and 8 were already removed). That leaves E6 with a domain of {4}; in other words, we
know the answer for E6. Now consider variable I6—the square in the bottom middle box
surrounded by 1, 3, and 3. Applying arc consistency in its column, we eliminate 5, 6, 2, 4
(since we now know E6 must be 4), 8, 9, and 3. We eliminate 1 by arc consistency with I5,

## Page 175
