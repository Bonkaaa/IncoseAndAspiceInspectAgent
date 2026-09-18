---
id: R11
name: SeparateClauses
type: rule
page: 69
target_scope: individual_statement
established_characteristics:
- C3
- C4
- C7
- C8
related_rules:
- R1
- R18
- R27
---

## **4.2.2 R11 - /CONCISION/SEPARATECLAUSES**

**Use a separate clause for each condition or qualification.**

### Elaboration

Each need or requirement should have a main verb describing a basic function or need.  If appropriate, the main sentence may then be supplemented by clauses that provide conditions or qualifications (performance values or constraints).  A single, clearly identifiable clause should be used for each condition or qualification expressed. 

If a condition that applies to a need or requirement is not stated explicitly within the need or requirement statement, the need or requirement statement is not Complete (C4), Verifiable (C7), nor Correct (C8) unless the condition clause is included. 

If a qualifying statement that is needed to clearly communicate the intent of the action verb on the object is not stated explicitly within the need or requirement statement, the need or requirement statement is not Complete (C4) ), Verifiable (C7), nor Correct (C8)  unless the qualifying clause is included, .e.g., performance associated with the action verb or for an interface requirement where a pointer to where the specific interaction is defined (i.e., and ICD). 

When using clauses, make sure the clause does not separate the object of the sentence from the verb.  See also R1, R18, R27 and Appendix C, Patterns. 

### Examples

**Unacceptable:** The Navigation_Beacon shall provide Augmentation_Data at an accuracy of less than or equal to 20 meters to each Maritime_User during Harbor_Harbor_Approach_Maneuvering (HHAM). 

- [This is unacceptable because it inserts a phrase in such a way that the object of the sentence is separated from the verb.] 
**Acceptable:** The Navigation_Beacon shall provide Augmentation_Data to each Maritime_User engaged in Harbor_Harbor_Approach_Maneuvering (HHAM), at an accuracy of less than or equal to 20 meters. 

[This rewrite places the basic function in an unbroken clause followed by the sub-clause describing performance.] 

[Note that: “Navigation_Beacon”, “Maritime_User”, and 

“Harbor_Harbor_Approach_Maneuvering (HHAM)” must be defined in the glossary.] 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C4 - Complete
- C7 - Verifiable
- C8 - Correct
