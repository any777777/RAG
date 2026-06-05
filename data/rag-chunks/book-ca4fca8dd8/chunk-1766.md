---
chunk_id: "book-ca4fca8dd8-chunk-1766"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1766
confidence: "first-pass"
extraction_method: "structured-local"
---

APPENDIX A
MATHEMATICAL BACKGROUND
A.1 Complexity Analysis and O() Notation
Computer scientists are often faced with the task of comparing algorithms to see how fast
they run or how much memory they require. There are two approaches to this task. The ﬁrst
is benchmarking—running the algorithms on a computer and measuring speed in seconds
Benchmarking
and memory consumption in bytes. Ultimately, this is what really matters, but a benchmark
can be unsatisfactory because it is so speciﬁc: it measures the performance of a particular
program written in a particular language, running on a particular computer, with a particular
compiler and particular input data. From the single result that the benchmark provides, it can
be difﬁcult to predict how well the algorithm would do on a different compiler, computer, or
data set. The second approach relies on a mathematical analysis of algorithms, independent
Analysis of
algorithms
of the particular implementation and input, as discussed below.
A.1.1 Asymptotic analysis
We will consider algorithm analysis through the following example, a program to compute
the sum of a sequence of numbers:
function SUMMATION(sequence) returns a number
sum←0
for i = 1 to LENGTH(sequence) do
sum←sum + sequence[i]
return sum
The ﬁrst step in the analysis is to abstract over the input, in order to ﬁnd some parameter or
parameters that characterize the size of the input. In this example, the input can be charac-
terized by the length of the sequence, which we will call n. The second step is to abstract
over the implementation, to ﬁnd some measure that reﬂects the running time of the algorithm
but is not tied to a particular compiler or computer. For the SUMMATION program, this could
be just the number of lines of code executed, or it could be more detailed, measuring the
number of additions, assignments, array references, and branches executed by the algorithm.
Either way gives us a characterization of the total number of steps taken by the algorithm as
a function of the size of the input. We will call this characterization T(n). If we count lines
of code, we have T(n)=2n+2 for our example.
If all programs were as simple as SUMMATION, the analysis of algorithms would be a
trivial ﬁeld. But two problems make it more complicated. First, it is rare to ﬁnd a parameter
like n that completely characterizes the number of steps taken by an algorithm. Instead,
the best we can usually do is compute the worst case Tworst(n) or the average case Tavg(n).
Computing an average means that the analyst must assume some distribution of inputs.
