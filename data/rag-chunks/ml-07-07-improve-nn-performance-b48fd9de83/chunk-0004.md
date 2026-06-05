---
chunk_id: "ml-07-07-improve-nn-performance-b48fd9de83-chunk-0004"
source_id: "ml-07-07-improve-nn-performance-b48fd9de83"
source_file: "_ML_07_07_Improve NN performance.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 4
confidence: "first-pass"
extraction_method: "structured-local"
---

Stopping Training Early
•
Neural networks are often set up with more than enough parameters for over-
fitting to occur, and so other procedures have to be employed to prevent it.
•
For the iterative gradient descent based network training procedures we have
considered the training set error will naturally decrease with increasing numbers
of epochs of training.
•
The error on the unseen validation and testing data sets, however, will start off
decreasing as the under-fitting is reduced, but then it will eventually begin to
increase again as over-fitting occurs.
•
The natural solution to get the best generalization, i.e. the lowest error on the test
set, is to use the procedure of early stopping.
–
One simply trains the network on the training set until the error on the validation set starts
rising again, and then stops.
–
That is the point at which we expect the generalization error to start rising as well.
