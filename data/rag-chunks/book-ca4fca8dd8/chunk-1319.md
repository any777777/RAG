---
chunk_id: "book-ca4fca8dd8-chunk-1319"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1319
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.2
Computation Graphs for Deep Learning
807
happen to put unit j in the ﬂat operating region. If the derivative g′
j is small or zero, that
means that changing the weights leading into unit j will have a negligible effect on its output.
As a result, deep networks with many layers may suffer from a vanishing gradient—the
Vanishing gradient
error signals are extinguished altogether as they are propagated back through the network.
Section 22.3.3 provides one solution to this problem.
We have shown that gradients in our tiny example network are simple expressions that
can be computed by passing information back through the network from the output units.
It turns out that this property holds more generally. In fact, as we show in Section 22.4.1,
the gradient computations for any feedforward computation graph have the same structure as
the underlying computation graph. This property follows straightforwardly from the rules of
differentiation.
We have shown the gory details of a gradient calculation, but worry not: there is no need
to redo the derivations in Equations (22.4) and (22.5) for each new network structure! All such
gradients can be computed by the method of automatic differentiation, which applies the
Automatic
diﬀerentiation
rules of calculus in a systematic way to calculate gradients for any numeric program.1 In fact,
the method of back-propagation in deep learning is simply an application of reverse mode
Reverse mode
differentiation, which applies the chain rule “from the outside in” and gains the efﬁciency
advantages of dynamic programming when the network in question has many inputs and
relatively few outputs.
All of the major packages for deep learning provide automatic differentiation, so that
users can experiment freely with different network structures, activation functions, loss func-
tions, and forms of composition without having to do lots of calculus to derive a new learning
algorithm for each experiment. This has encouraged an approach called end-to-end learn-
ing, in which a complex computational system for a task such as machine translation can be
End-to-end learning
composed from several trainable subsystems; the entire system is then trained in an end-to-
end fashion from input/output pairs. With this approach, the designer need have only a vague
idea about how the overall system should be structured; there is no need to know in advance
exactly what each subsystem should do or how to label its inputs and outputs.
22.2 Computation Graphs for Deep Learning
We have established the basic ideas of deep learning: represent hypotheses as computation
graphs with tunable weights and compute the gradient of the loss function with respect to
those weights in order to ﬁt the training data. Now we look at how to put together computation
graphs. We begin with the input layer, which is where the training or test example x is
encoded as values of the input nodes. Then we consider the output layer, where the outputs ˆy
are compared with the true values y to derive a learning signal for tuning the weights. Finally,
we look at the hidden layers of the network.
22.2.1 Input encoding
The input and output nodes of a computational graph are the ones that connect directly to the
input data x and the output data y. The encoding of input data is usually straightforward, at
least for the case of factored data where each training example contains values for n input
1
Automatic differentiation methods were originally developed in the 1960s and 1970s for optimizing the pa-
rameters of systems deﬁned by large, complex Fortran programs.
