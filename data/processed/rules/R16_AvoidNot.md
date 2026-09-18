---
id: R16
name: AvoidNot
type: rule
page: 74
target_scope: individual_statement
established_characteristics:
- C3
- C7
- C8
related_rules: []
---

## **4.3.5 R16 - /NONAMBIGUITY/AVOIDNOT**

**Avoid the use of “not.”**

### Elaboration

The presence of “not” in a need or requirement statement implies “not ever”, which is impossible to verify in a finite time. 

In cases like this, the need or requirement statement is not correct (C8). 

Rewriting the need or requirement statement to avoid the use of “not” results in a need or requirement statement that is clearer and is verifiable or able to be validated. 

### Examples

Unacceptable: The <system> shall not fail. 

[This is unacceptable because verification of the requirement would require infinite time.] _**Acceptable:**_ The <system> shall have an Availability of greater than or equal to 95%.  Or The <system> shall have a Mean Time Between Failures (MTBF) of 6 months. 

Unacceptable: The <system> shall not contain mercury. 

[This is unacceptable because verification of the requirement would require the ability to measure the amount of mercury with infinite accuracy and precision.  In addition, the real requirement may not be stated, for example, the real concern may be the use of toxic materials, not just mercury.  If that is the case, it may be best to reference a standard from a governmental agency concerning allowable exposures to a list of common toxic materials.] 

_**Acceptable:**_ The <system> shall limit metallic mercury exposures to workers to less than or equal 0.025 mg/m<sup>3</sup> over an 8-hour workday. 

### Exceptions and relationships

It may be reasonable to include “not” in a requirement when the logical “NOT” is implied—for example when using not [X or Y].  In that case, however, in accordance with Rule 15, it may be better to capitalize the “NOT” to make the logical condition explicit: NOT [X or Y].  There may be other cases such as “The <system> shall not be red in color.” Which is stating a constraint and is verifiable, as long as the range of shades of red is stated (RBG rr,bb,gg range or a “name” of red in some standard). 

### Characteristics that are established by this rule

- C3 - Unambiguous
- C7 - Verifiable
- C8 - Correct
