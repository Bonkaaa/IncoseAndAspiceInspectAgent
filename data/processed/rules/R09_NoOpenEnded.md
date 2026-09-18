---
id: R9
name: NoOpenEnded
type: rule
page: 67
target_scope: individual_statement
established_characteristics:
- C3
- C4
- C5
- C7
related_rules:
- R17
- R18
- R22
- R28
---

## **4.1.9 R9 - /ACCURACY/NOOPENENDED**

**Avoid open-ended clauses.**

### Elaboration

Open-ended clauses imply there is more required without stating exactly what.  Avoid nonspecific phrases such as “including but not limited to”, “etc.” and “and so on.” 

Open-ended clauses can lead to ambiguous, unverifiable needs and requirements that do not reflect accurately the stakeholder’s expectations and needs and can create ambiguity in the mind of the reader. 

Use of open-ended clauses also violates the one-thought rule (R18) that leads to the singular characteristic.  If more cases are required, then include additional needs and requirements that explicitly state those cases. 

Needs or requirements with open-ended clauses are not Complete (C4) 

Depending on the contract type (fixed price versus level of effort or cost plus) open-ended needs and requirement statements can lead to serious interpretation problems concerning what is in or out of scope of the contract; possibly resulting in expensive contract changes. 

### Examples

**Unacceptable:** The ATM shall display the Customer Account_Number, Account_Balance, and so on. 

[This is unacceptable because it contains an opened list of what is to be displayed.] 
**Acceptable:** _[Split into as many requirements as necessary to be complete.  Note that the types of customer information to be displayed needs to be defined in the glossary.]:_ 

The ATM shall display the Customer Account_Number. 

The ATM shall display the Customer Account_Balance. 

The ATM shall display the Customer Account_Type. 

The ATM shall display the Customer Account_Overdraft_Limit. 

[Note: Some may feel that a bulleted list or table is acceptable.  While, from a readability perspective, this may be true, from a requirement management perspective, each item in the bulleted list is still a requirement.  Because of this requirement statements as in the example above should be written as individual statements especially when allocation, traceability, verification, and validation activities are specific to the single item.  See also R17, R18, R22, and R28.] 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C4 - Complete
- C5 - Singular
- C7 - Verifiable
