---
id: R21
name: AvoidParentheses
type: rule
page: 80
target_scope: individual_statement
established_characteristics:
- C5
related_rules: []
---

## **4.4.4 R21 - /SINGULARITY/AVOIDPARENTHESES**

**Avoid parentheses and brackets containing subordinate text.**

### Elaboration

If the text of a need or requirement statement contains parentheses or brackets, it usually indicates the presence of superfluous information that can simply be removed or communicated in the rationale.  Other times, brackets introduce ambiguity. 

If the information in the parentheses or brackets aids in the understanding of the intent of the requirement, then that information should be included in the rationale Attribute (A1) defined in the NRM. 

Conventions for the use of parentheses or brackets may be agreed upon for specific purposes, but such conventions should be documented at the start of the needs or requirements document. 

### Examples

**Unacceptable:** The Control_Unit shall disconnect power from the Boiler when the water temperature exceeds 85 °C (usually towards the end of the boiling cycle.) 

[This is unacceptable because of the parenthetical phrase as well as the ambiguous word “usually”.] 

**Acceptable:** The Control_Unit shall disconnect power from the Boiler when the water temperature is greater than 85 °C. 

[Note: for the above example, if this behavior is the result of a design decision, then the requirement needs to be communicated as a design output.  The design input requirement should focus on why this behavior is needed – for example, prevent the boiler from over pressurizing and exploding.] 

### Exceptions and relationships

While this rule states brackets are to be avoided, R15 indicates that brackets may be used as part of a convention for eliminating ambiguous conditions such as logical expressions. 
### Characteristics that are established by this rule

- C5 - Singular
