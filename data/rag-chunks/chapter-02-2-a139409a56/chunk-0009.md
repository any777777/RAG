---
chunk_id: "chapter-02-2-a139409a56-chunk-0009"
source_id: "chapter-02-2-a139409a56"
source_file: "Chapter 02 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 9
confidence: "first-pass"
extraction_method: "structured-local"
---

2.4.3 Model-based reflex agents: Ex
• For the braking problem:
•
previous frame from the camera, allowing the agent to detect when two red lights at the edge of the vehicle go on or off simultaneously. 
• For other driving tasks such as changing lanes, the agent needs to keep track of where the other cars are if 
it can’t see them all at once.
• Updating this internal state information as time goes by requires two kinds of knowledge to be encoded in 
the agent program in some form( mentioned in previous slide): 
• First, information about how the world changes over time, which can be divided roughly into two parts: 
•
the effects of the agent’s actions and 
•
how the world evolves independently of the agent. 
•
For example, when the agent turns the steering wheel clockwise, the car turns to the right, and when it’s raining the car’s cameras 
can get wet.
• Second, information about how the state of the world is reflected in the agent’s percepts. 
•
For example, when the car in front initiates braking, one or more illuminated red regions appear in the forward-facing camera image, 
and, when the camera gets wet, droplet-shaped objects appear in the image partially confusing the road. 
47

## Page 48

48
… Model-based reflex agents
“best guess”
Uncertainty about the current
state may be unavoidable, 
but the agent still has to 
make a decision.

## Page 49

49
… Model-based reflex agents

## Page 50

2.4.4 Goal-based agents
• As well as a current state description, the agent needs some sort of 
goal information that describes situations that are desirable.
• The agent program can combine this with the model to choose actions that 
achieve the goal.
• Distinction:
• The reflex agent brakes when it sees brake lights, period. It has no idea why. 
• A goal-based agent brakes when it sees brake lights because that’s the only 
action that it predicts will achieve its goal of not hitting other cars.
• Search (Chapters 3 to 5) and planning (Chapter 11) are the subfields 
of AI devoted to finding action sequences that achieve the agent’s 
goals.
50

## Page 51

51
… Goal-based agents

## Page 52
