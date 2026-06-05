---
chunk_id: "chapter6-reduced-1-e8f2336f2b-chunk-0004"
source_id: "chapter6-reduced-1-e8f2336f2b"
source_file: "Chapter6_reduced-1.pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 4
confidence: "first-pass"
extraction_method: "structured-local"
---

24

## Slide 25

Idea: Keep track of remaining legal values for unassigned variables Terminate search when any variable has no legal values

WA

NT

Q

NSW

V

SA

T

Forward Checking

25

## Slide 26

Idea: Keep track of remaining legal values for unassigned variables Terminate search when any variable has no legal values

WA

NT

Q

NSW

V

SA

T

Forward Checking

26

## Slide 27

Idea: Keep track of remaining legal values for unassigned variables Terminate search when any variable has no legal values

WA

NT

Q

NSW

V

SA

T

Forward Checking

27

It does not check for constraints  for variables that have not been assigned yet. It check constraints after assigning values!!!

## Slide 28

Forward checking propagates information from assigned to unassigned vari- ables, but doesn’t provide early detection for all failures:

WA

NT

Q

NSW

V

SA

T

|  |  |  |  |  |

|  |  |  |  |  |

|  |  |  |  |  |

NT and SA cannot both be blue!
Constraint propagation repeatedly enforces constraints locally

Constraint propagation

A CSP algorithm can do a specific type of inference called constraint  propagation:  using the constraints to reduce the number of legal values for a variable,

28

## Slide 29

Simplest form of constraint propagation makes each arc consistent
X → Y	is consistent iff
for every value x of X there is some allowed y

WA

NT

Q

NSW

V

SA

T

|  |  |  |  |  |

Arc consistency

An arc X→Y is arc consistent if:
For every value x in the domain of X, there exists at least one value y in the domain of Ythat satisfies the constraint between X and Y.
If some x has no corresponding y, then x is removed from X’s domain.

29

## Slide 30

Simplest form of propagation makes each arc consistent
X → Y	is consistent iff
for every value x of X there is some allowed y

WA

NT

Q

NSW

V

SA

T

|  |  |  |  |  |

Arc consistency

30

## Slide 31

Simplest form of propagation makes each arc consistent
X → Y	is consistent iff
for every value x of X there is some allowed y

WA

NT

Q

NSW

V

SA

T

|  |  |  |  |  |

If X loses a value, neighbors of X need to be rechecked

Arc consistency

31

## Slide 32

Simplest form of propagation makes each arc consistent
X → Y	is consistent iff
for every value x of X there is some allowed y

WA

NT

Q

NSW

V

SA

T

|  |  |  |  |  |

If X loses a value, neighbors of X need to be rechecked
Arc consistency detects failure earlier than forward checking Can be run as a preprocessor or after each assignment

Arc consistency

32

## Slide 33
