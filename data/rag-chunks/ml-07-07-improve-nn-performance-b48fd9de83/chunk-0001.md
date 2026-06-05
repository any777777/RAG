---
chunk_id: "ml-07-07-improve-nn-performance-b48fd9de83-chunk-0001"
source_id: "ml-07-07-improve-nn-performance-b48fd9de83"
source_file: "_ML_07_07_Improve NN performance.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 1
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1

Practical Considerations for Back-
Propagation Learning
•
Randomize input sequence
•
Maximize information content
– Distribution
– Outlier
•
Activation function choice
•
Do we need to pre-process the training data? If so, how?
•
How do we choose the initial weights from which the training is started?
•
How do we choose an appropriate learning rate η?
•
Should we change the weights after each training pattern, or after the
whole set?
•
How can we avoid flat spots in the error function?
•
How can we avoid local minima in the error function?
•
How do we know when we should stop the training?
•
How many hidden units do we need?
•
Should we have different learning rates for the different layers?

## Page 2

How Many Hidden Units?
•
The best number of hidden units depends in a complex way on many factors, including:
1. The number of training patterns
2. The numbers of input and output units
3. The amount of noise in the training data
4. The complexity of the function or classification to be learned
5. The type of hidden unit activation function
6. The training algorithm
•
Too few hidden units:
–
will generally leave high training and generalization errors due to under-fitting.
•
Too many hidden units:
–
will result in low training errors,
–
but will make the training unnecessarily slow,
–
and will often result in poor generalization unless some other technique (such as regularization) is used to
prevent over-fitting.
•
Virtually all “rules of thumb” you might hear about are actually nonsense. The sensible strategy is
to try a range of numbers of hidden units and see which works best.

## Page 3
