---
chunk_id: "book-ca4fca8dd8-chunk-1706"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1706
confidence: "first-pass"
extraction_method: "structured-local"
---

1042
Chapter 28
Philosophy, Ethics, and Safety of AI
Balanced against the individual’s right to privacy is the value that society gains from
sharing data. We want to be able to stop terrorists without oppressing peaceful dissent, and
we want to cure diseases without compromising any individual’s right to keep their health
history private. One key practice is de-identiﬁcation: eliminating personally identifying in-
De-identiﬁcation
formation (such as name and social security number) so that medical researchers can use the
data to advance the common good. The problem is that the shared de-identiﬁed data may
be subject to re-identiﬁcation. For example, if the data strips out the name, social security
number, and street address, but includes date of birth, gender, and zip code, then, as shown by
Latanya Sweeney (2000), 87% of the U.S. population can be uniquely re-identiﬁed. Sweeney
emphasized this point by re-identifying the health record for the governor of her state when
he was admitted to the hospital. In the Netﬂix Prize competition, de-identiﬁed records of in-
Netﬂix Prize
dividual movie ratings were released, and competitors were asked to come up with a machine
learning algorithm that could accurately predict which movies an individual would like. But
researchers were able to re-identify individual users by matching the date of a rating in the
Netﬂix database with the date of a similar ranking in the Internet Movie Database (IMDB),
where users sometimes use their actual names (Narayanan and Shmatikov, 2006).
This risk can be mitigated somewhat by generalizing ﬁelds: for example, replacing the
exact birth date with just the year of birth, or a broader range like “20-30 years old.” Deleting
a ﬁeld altogether can be seen as a form of generalizing to “any.” But generalization alone
does not guarantee that records are safe from re-identiﬁcation; it may be that there is only
one person in zip code 94720 who is 90–100 years old. A useful property is k-anonymity:
K-anonymity
a database is k-anonymized if every record in the database is indistinguishable from at least
k −1 other records. If there are records that are more unique than this, they would have to be
further generalized.
An alternative to sharing de-identiﬁed records is to keep all records private, but allow
aggregate querying. An API for queries against the database is provided, and valid queries
Aggregate querying
receive a response that summarizes the data with a count or average. But no response is
given if it would violate certain guarantees of privacy. For example, we could allow an
epidemiologist to ask, for each zip code, the percentage of people with cancer. For zip codes
with at least n people a percentage would be given (with a small amount of random noise),
but no response would be given for zip codes with fewer than n people..
Care must be taken to protect against de-identiﬁcation using multiple queries. For exam-
ple, if the query “average salary and number of employees of XYZ company age 30-40” gives
the response [$81,234, 12] and the query “average salary and number of employees of XYZ
company age 30-41” gives the response [$81,199, 13], and if we use LinkedIn to ﬁnd the one
41-year-old at XYZ company, then we have successfully identiﬁed them, and can compute
their exact salary, even though all the responses involved 12 or more people. The system must
be carefully designed to protect against this, with a combination of limits on the queries that
can be asked (perhaps only a predeﬁned set of non-overlapping age ranges can be queried)
and the precision of the results (perhaps both queries give the answer “about $81,000”).
A stronger guarantee is differential privacy, which assures that an attacker cannot use
Diﬀerential privacy
queries to re-identify any individual in the database, even if the attacker can make multiple
queries and has access to separate linking databases. The query response employs a random-
ized algorithm that adds a small amount of noise to the result. Given a database D, any record
in the database r, any query Q, and a possible response y to the query, we say that the database
