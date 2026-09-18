---
id: R26
name: AvoidAbsolutes
type: rule
page: 84
target_scope: individual_statement
established_characteristics:
- C6
- C7
- C8
related_rules: []
---

## **4.6.1 R26 - /REALISM/AVOIDABSOLUTES**

**Avoid using unachievable absolutes.**

### Elaboration

An absolute, such as “100% availability”, is not achievable.  Think ahead to design and system verification and design and system validation: how would you prove 100% availability?  Even if you could build such a system, could you afford to verify or validate it? 

Other examples to avoid are “all”, “every”, “always”, and “never” since such absolutes are impossible to verify without an infinite number of verification or validation activities. 

A need or requirement that contains absolutes is neither Feasible (C6), Verifiable (C7), nor Correct (C8). 

### Examples

**Unacceptable:** The system shall have 100% availability. 

[This is unacceptable because 100% is an absolute that is impossible to achieve and verify. Also, available over what time period?] 

**Acceptable:** The system shall have an Availability of greater than or equal to 98% during Operating_Hours. 

[Note use of the glossary to define Operating_Hours.] 
### Characteristics that are established by this rule

- C6 - Feasible
- C7 - Verifiable
- C8 - Correct
