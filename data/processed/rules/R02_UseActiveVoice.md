---
id: R2
name: UseActiveVoice
type: rule
page: 59
target_scope: individual_statement
established_characteristics:
- C2
- C3
- C4
- C7
related_rules: []
---

## **4.1.2 R2 - /ACCURACY/USEACTIVEVOICE**

**Use the active voice in the main sentence structure of the need or requirement statement with the responsible entity clearly identified as the subject of the sentence.**

### Elaboration

The active voice requires that the entity performing the action is the subject of the sentence.  This is important in writing needs and requirements since the onus for satisfying the requirement is on the subject, not the object of the statement.  If the entity responsible for the action is not identified explicitly, it is unclear who or what should perform the action making it difficult to verify the SOI meets the requirement.  Including the entity in the subject also helps ensure the requirement 
refers to the appropriate level consistent with the entity name (see R3).  If the entity name is not clearly identified as the subject of the sentence, the need or requirement is not Completed (C4). 

Often when the phrase “shall be” is used, the statement is in the passive voice. 

### Examples

**Unacceptable:** The Identity of the Customer shall be confirmed. 

[This is unacceptable because it does not identify the entity that is responsible/accountable for confirming the identity.] 

**Acceptable:** The Accounting_System shall confirm the Customer_Identity. 

[Note that” Accounting_System”, “confirm”, and “Customer_Identity” must be defined in the glossary since there are a number of possible interpretations of these terms.] 

_**Unacceptable:**_ The Audio shall be recorded by the System. 

[This is unacceptable because the entity that is responsible/accountable for recording the audio is at the end of the sentence rather than the beginning.] 

**Unacceptable:** The Audio shall be recorded. 

[This is unacceptable because the entity that is responsible/accountable for recording the audio is not stated.] 

**Acceptable:** The System shall record the Audio_Feed. 

[Note that “Audio_Feed” must be defined in the glossary and required performance and conditional clauses added for the requirement to be complete.] 
### Characteristics that are established by this rule

- C2 - Appropriate
- C3 - Unambiguous
- C4 - Complete
- C7 - Verifiable
