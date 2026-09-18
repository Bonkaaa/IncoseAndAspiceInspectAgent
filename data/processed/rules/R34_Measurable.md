---
id: R34
name: Measurable
type: rule
page: 94
target_scope: individual_statement
established_characteristics:
- C3
- C4
- C7
- C12
related_rules: []
---

## **4.12.1 R34 - /QUANTIFICATION/MEASURABLE**

**Provide specific measurable performance targets appropriate to the entity to which the need or requirement is stated and against which the entity will be verified to meet.**

### Elaboration

Some words signal unmeasured quantification, such as “prompt”, ”fast”, ”routine”, ”maximum”, ”minimum”, ”optimum”, ”nominal”, ”easy to use”, ”close quickly”, ”high speed”, ”medium-sized”, ”best practices”, and ”user-friendly.” These are ambiguous and need to be replaced by specific quantities within feasible ranges that can be measured. 
### Examples

**Unacceptable:** The system shall use minimum power. 

[This is unacceptable because “minimum” is ambiguous.] 

**Acceptable:** The system shall use less than or equal to 50W of main power. 

[This both considers the underlying goal - to minimize power consumption - and provides a measurable target.] 

**Unacceptable:** The engine shall achieve an emissions level that is at least 5% less than the competition’s emission levels 2 years from now. 

[This is an actual requirement from marketing to an engineering department.  The statement sets a completely unmeasurable end state.] 

_Acceptable:_ The Engine shall achieve an emissions level that is at least xxx. 

[where xxx represents the required threshold value.] 

### Exceptions and relationships

Some quantification such as “minimum”, “maximum”, “optimal” is almost always ambiguous. Other terms may be ambiguous at lower levels but sufficient at the higher levels and as need statements.  For example, it may be appropriate that the business state that “The Aircraft shall provide class-leading comfort.”—while such a requirement is not quantifiable and therefore not measurable, it may be sufficient for the business to communicate its intentions as a need statement to developers who can then turn comfort into such measurable quantities such as seat dimensions and leg length. 

This exception also applies to needs stated at the system or system element levels. 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C4 - Complete
- C7 - Verifiable
- C12 - Feasible
