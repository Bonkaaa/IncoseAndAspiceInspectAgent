---
id: R23
name: Context
type: rule
page: 82
target_scope: individual_statement
established_characteristics:
- C4
related_rules: []
---

## **4.4.6 R23 - /SINGULARITY/CONTEXT**

**When a need or requirement is related to complex behavior, refer to the supporting diagram or model.**

### Elaboration

Sometimes it can be difficult to express a complicated need or requirement in words, and it is better simply to refer to a diagram or model. 

An example is a requirement on voltage at turn on which involves a magnitude, rise time, overshoot, and dampening time along with tolerances.  Stating all these values in the same requirement could be seen to violate our combiner and multiple thought rules.  Having a requirement that states: “Upon turn on, the system shall supply the initial voltage with the characteristics shown in drawing xxxxx.” It is much simpler for the drawing to show the magnitude, rise time, allowable overshoot, and dampening time.  Stating each as a separate requirement is not applicable because all four conditions are part of the one action. 

### Examples

**Unacceptable:** The control system shall close Valves A and B within 5 seconds of the temperature exceeding 95 °C and within 2 seconds of each other. 

[This is unacceptable because of the confusing set of conditions.  In this case what is meant will be clear if expressed in the form of a diagram.] 

**Acceptable:** When the Product temperature exceeds 95 °C, the Control_System shall close Input_Valves as specified in timing diagram 6. 

- [Note that this assumes, of course, that the timing diagram itself is not ambiguous.  If it is not possible to remove the ambiguity by using a diagram, it may be better to split the requirement into two.] 

[Note: for the above example, if this complex behavior is the result of a design decision, then the requirement needs to be communicated below the line as a design output.  The design input requirement should focus on why this behavior is needed.] 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C4 - Complete
- C5 - Singular
