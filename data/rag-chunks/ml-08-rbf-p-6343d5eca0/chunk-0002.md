---
chunk_id: "ml-08-rbf-p-6343d5eca0-chunk-0002"
source_id: "ml-08-rbf-p-6343d5eca0"
source_file: "_ML_08_RBF_P.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

11
Too Many Receptive Fields?
•
In order to reduce the artificial complexity of  the RBF, we need 
to use fewer number of receptive fields.
•
• Approach 2: Fixed centers selected at random.
• Use M < N data points as the receptive field centers.
• Fast but may require excessive centers
•
• Approach 3: Centers are obtained from unsupervised 
learning (clustering). 
• Centers no longer has to coincide with data points
• This is the most commonly used procedure, providing good results.

## Page 12

Selecting the value of the Spread

## Page 13

Comparison of RBF Networks with MLPs
•
They are both non-linear feed-forward networks.
•
An RBF network has a single hidden layer, whereas MLPs can have any 
number of hidden layers.
•
RBF networks are usually fully connected, whereas it is common for MLPs to 
be only partially connected.
•
In RBF networks, the argument of each hidden unit activation function is the 
distance between the input and the “weights” (RBF centres), whereas in MLPs 
it is the inner product of the input and the weights.
•
Although, for approximating non-linear input-output mappings, the RBF 
networks can be trained much faster, MLPs may require a smaller number of 
parameters.
