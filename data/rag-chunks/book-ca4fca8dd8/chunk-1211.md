---
chunk_id: "book-ca4fca8dd8-chunk-1211"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1211
confidence: "first-pass"
extraction_method: "structured-local"
---

730
Chapter 19
Learning from Examples
But a separate explanation module might be able to examine the neural network model and
come up with the explanation “it has four legs, fur, a tail, ﬂoppy ears, and a long snout; it
is smaller than a wolf, and it is lying on a dog bed, so I think it is a dog.” Explanations
are one way to build trust, and some regulations such as the European GDPR (General Data
Protection Regulation) require systems to provide explanations.
As an example of a separate explanation module, the local interpretable model-agnostic
explanations (LIME) system works like this: no matter what model class you use, LIME
builds an interpretable model—often a decision tree or linear model—that is an approxima-
tion of your model, and then interprets the linear model to create explanations that say how
important each feature is. LIME accomplishes this by treating the machine-learned model as
a black box, and probing it with different random input values to create a data set from which
the interpretable model can be built. This approach is appropriate for structured data, but not
for things like images, where each pixel is a feature, and no one pixel is “important” by itself.
Sometimes we choose a model class because of its explainability—we might choose
decision trees over neural networks not because they have higher accuracy but because the
explainability gives us more trust in them.
However, a simple explanation can lead to a false sense of security. After all, we typically
choose to use a machine learning model (rather than a hand-written traditional program)
because the problem we are trying to solve is inherently complex, and we don’t know how to
write a traditional program. In that case, we shouldn’t expect that there will necessarily be a
simple explanation for every prediction.
If you are building a machine learning model primarily for the purpose of understanding
the domain, then interpretability and explainability will help you arrive at that understanding.
But if you just want the best-performing piece of software then testing may give you more
conﬁdence and trust than explanations. Which would you trust: an experimental aircraft that
has never ﬂown before but has a detailed explanation of why it is safe, or an aircraft that
safely completed 100 previous ﬂights and has been carefully maintained, but comes with no
guaranted explanation?
19.9.5 Operation, monitoring, and maintenance
Once you are happy with your model’s performance, you can deploy it to your users. You’ll
face additional challenges. First, there is the problem of the long tail of user inputs. You
Long tail
may have tested your system on a large test set, but if your system is popular, you will soon
see inputs that were never tested before. You need to know whether your model generalizes
well for them, which means you need to monitor your performance on live data—tracking
Monitoring
statistics, displaying a dashboard, and sending alerts when key metrics fall below a threshold.
In addition to automatically updating statistics on user interactions, you may need to hire and
train human raters to look at your system and grade how well it is doing.
Second, there is the problem of nonstationarity—the world changes over time. Suppose
Nonstationarity
your system classiﬁes email as spam or non-spam. As soon as you successfully classify a
batch of spam messages, the spammers will see what you have done and change their tactics,
sending a new type of message you haven’t seen before. Non-spam also evolves, as users
change the mix of email versus messaging or desktop versus mobile services that they use.
You will continually face the question of what is better: a model that has been well tested
but was built from older data, versus a model that is built from the latest data but has not
