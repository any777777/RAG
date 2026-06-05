---
chunk_id: "ml-07-07-improve-nn-performance-b48fd9de83-chunk-0002"
source_id: "ml-07-07-improve-nn-performance-b48fd9de83"
source_file: "_ML_07_07_Improve NN performance.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

Different Learning Rates for Different 
Layers?
•
A network as a whole will usually learn most efficiently if all its neurons are
learning at roughly the same speed.
–
So maybe different parts of the network should have different learning rates η.
•
There are a number of factors that may affect the choices:
1. The later network layers (nearer the outputs) will tend to have larger local
gradients (deltas) than the earlier layers (nearer the inputs).
2. The activations of units with many connections feeding into or out of them tend
to change faster than units with fewer connections.
3. There is empirical evidence that it helps to have different learning rates η for the
thresholds/biases compared with the real connection weights.
•
In practice, it is often quicker to just use the same rates η for all the weights and
thresholds, rather than spending time trying to work out appropriate differences.
•
A very powerful approach is to use some strategies to determine good learning
rates.

## Page 4

Preventing Under-fitting and Over-
fitting (Improving Generalization)
• To prevent under-fitting we need to make sure that:
1. The network has enough hidden units to represent the required
mappings.
2. We train the network for long enough so that the error/cost
function (e.g., MSE) is sufficiently minimized.
• To prevent over-fitting we can:
1.
Restrict the number of adjustable parameters the network has
by reducing the number of hidden units.
2. Stop the training early – before it has had time to learn the
training data too well.
3. Add some form of regularization term to the error/cost function
to encourage smoother network mappings.
4. Add noise to the training patterns to smear out the data points.

## Page 5
