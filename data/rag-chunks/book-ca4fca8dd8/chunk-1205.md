---
chunk_id: "book-ca4fca8dd8-chunk-1205"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1205
confidence: "first-pass"
extraction_method: "structured-local"
---

726
Chapter 19
Learning from Examples
You can also introduce new attributes based on your domain knowledge. For example,
given a data set of customer purchases where each entry has a date attribute, you might want
to augment the data with new attributes saying whether the date is a weekend or holiday.
As another example, consider the task of estimating the true value of houses that are for
sale. In Figure 19.13 we showed a toy version of this problem, doing linear regression of
house size to asking price. But we really want to estimate the selling price of a house, not
the asking price. To solve this task we’ll need data on actual sales. But that doesn’t mean we
should throw away the data about asking price—we can use it as one of the input features.
Besides the size of the house, we’ll need more information: the number of rooms, bedrooms,
and bathrooms; whether the kitchen and bathrooms have been recently remodeled; the age of
the house and perhaps its state of repair; whether it has central heating and air conditioning;
the size of the yard and the state of the landscaping.
We’ll also need information about the lot and the neighborhood. But how do we deﬁne
neighborhood? By zip code? What if a zip code straddles a desirable and an undesirable
neighborhood? What about the school district? Should the name of the school district be
a feature, or the average test scores? The ability to do a good job of feature engineering
is critical to success. As Pedro Domingos (2012) says, “At the end of the day, some ma-
chine learning projects succeed and some fail. What makes the difference? Easily the most
important factor is the features used.”
Exploratory data analysis and visualization
John Tukey (1977) coined the term exploratory data analysis (EDA) for the process of
exploring data in order to gain an understanding of it, not to make predictions or test hy-
potheses. This is done mostly with visualizations, but also with summary statistics. Looking
at a few histograms or scatter plots can often help determine if data are missing or erroneous;
whether your data are normally distributed or heavy-tailed; and what learning model might
be appropriate.
It can be helpful to cluster your data and then visualize a prototype data point at the
center of each cluster. For example, in the data set of images, I can identify that here is a
cluster of cat faces; nearby is a cluster of sleeping cats; other clusters depict other objects.
Expect to iterate several times between visualizing and modeling—to create clusters you need
a distance function to tell you which items are near each other, but to choose a good distance
function you need some feel for the data.
It is also helpful to detect outliers that are far from the prototypes; these can be considered
critics of the prototype model, and can give you a feel for what type of errors your system
might make. An example would be a cat wearing a lion costume.
Our computer display devices (screens or paper) are two-dimensional, which means that
it is easy to visualize two-dimensional data. And our eyes are experienced at understanding
three-dimensional data that has been projected down to two dimensions. But many data sets
have dozens or even millions of dimensions. In order to visualize them we can do dimension-
ality reduction, projecting the data down to a map in two dimensions (or sometimes to three
dimensions, which can then be explored interactively).17
17 Geoffrey Hinton provides the helpful advice “To deal with a 14-dimensional space, visualize a 3D space and
say ‘fourteen’ to yourself very loudly.”
