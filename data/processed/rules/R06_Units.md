---
id: R6
name: Units
type: rule
page: 64
target_scope: individual_statement
established_characteristics:
- C3
- C4
- C7
- C8
related_rules: []
---

## **4.1.6 R6 - /ACCURACY/UNITS**

**Use appropriate units when stating quantities.**

### Elaboration

All numbers should have units of measure explicitly stated in terms of the measurement system used or the thing the number refers. 

Within a project, a common measurement system must be used consistently.  For example, do not mix both US and metric units of measure within any of the project’s artifacts. 

There are three primary measurement systems: British imperial, US, Metric 

For temperatures, the following are used: Celsius, Fahrenheit, or Kelvin, etc. 

### Examples

**Unacceptable:** The Circuit_Board shall … a temperature less than 30 degrees. 

_[This is unacceptable because the units used are stated without indicating the specific measurement system used.]_ 

**Acceptable:** The Circuit_Board shall … a temperature of less than 30 degrees Celsius. 
**Unacceptable:** The system shall establish communications with at least 4 in less than or equal to 10 seconds. 

[This is unacceptable because the units used are incomplete.  “4” of what?] 

**Acceptable:** The system shall establish communications with at least 4 satellites in less than or equal to 10 seconds. 

[Note that the term “communications” is acceptable at the business level but would need further elaboration at lower levels so that the requirement is decomposed and verifiable.  E.g., frequency, type of communications (voice? data?), quality, bandwidth, etc.] 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C4 - Complete
- C7 - Verifiable
- C8 - Correct
