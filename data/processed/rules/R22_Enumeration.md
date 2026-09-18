---
id: R22
name: Enumeration
type: rule
page: 80
target_scope: individual_statement
established_characteristics:
- C3
- C5
related_rules:
- R18
---

## **4.4.5 R22 - /SINGULARITY/ENUMERATION**

**Enumerate sets explicitly instead of using a group noun to name the set.**

### Elaboration

If a number of functions are implied, a need or requirement statement should be written for each. 

The use of a group noun to combine functions or entities is often ambiguous because it leaves membership of that group in doubt. 

Other issues include allocation, traceability, verification, and validation.  As with the singularity characteristic C5, each member of the set could be allocated differently, have different child requirements, each of which must be individually verified and validated. 
It is almost always best to list all the members of the set as separate needs or requirements. See exceptions and relationship discussion below. 

See also R18. 

### Examples

**Unacceptable:** The thermal control system shall manage temperature-related functions. 

[This is unacceptable because there is ambiguity regarding which functions are to be managed. The specific functions should be enumerated explicitly in separate requirement statements.] 

**Acceptable:** (three separate requirements _):_ 

The Thermal_Control_System shall update the display of Current_System_Temperature every 10 +/- 1 seconds. 

The Thermal_Control_System shall maintain the Current_System_Temperature between 95°C and 98°C. 

The Thermal_Control_System shall store the history of Current_System_Temperature. [Note use of the glossary to define terms.] 

### Exceptions and relationships

It is almost always better to enumerate members in a set, but the rule may be softened at the higher levels of abstraction if the resulting requirement is sufficiently unambiguous.  For example, at the business management level the business may state “ACME Consulting shall manage HR functions centrally.” or a system level need statement may state: “The stakeholders need the system to manage HR functions centrally.” 

Although this raises the question of which HR functions are being referred to, it is not useful to include a long list at these levels of abstractions and it is often not necessary since the statement is sufficiently clear at the level at which it is stated.  The detailed enumeration of functions will be undertaken at the business operations level, and the business management stakeholders should be comfortable that no function will be omitted as a result of not listing it at the business management level. 

At the system level, the during the transformation of the need statement into design input requirements, the project team would decompose the need into individual functional/performance requirements as well as define requirements concerning the word “centrally” and would then validate with the stakeholders that the resulting design input requirements, when realized, would meet the intent of the need statement. 

### Characteristics that are established by this rule

- C3 - Unambiguous
- C5 - Singular
