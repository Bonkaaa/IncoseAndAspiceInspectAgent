---
id: R28
name: ExplicitLists
type: rule
page: 86
target_scope: individual_statement
established_characteristics:
- C3
- C7
related_rules: []
---

## **4.7.2 R28 - /CONDITIONS/EXPLICITLISTS**

**Express the propositional nature of a condition explicitly for a single action instead of giving lists of actions for a specific condition.**

### Elaboration

When a list of conditions is given for a single action in a single need or requirement statement, it may not be clear whether all the conditions must hold (a conjunction) or any one of them (a disjunction) for the action to take place.  The wording of the need or requirement should make this clear. 

When the combination of conditions and actions that trigger another action is complex, consideration should be given to the use of a diagram or table (see R23). 

### Examples

**Unacceptable:** 

The Audit _Clerk shall be able to change the status of the action item when: 

- the Audit _Clerk originated the item; 

- the Audit _Clerk is the actionee; and 

- the Audit _Clerk is the reviewer. 

[This is unacceptable because it is not clear whether all the conditions must hold (a conjunction) or any one of them (a disjunction).  Also, the requirement contains the phrase “be able to” which violates R11.] 

**Acceptable if interpreted as a disjunction:** 

The Audit_System shall allow the Audit_Clerk to change the status of the action item when one or more of the following conditions are true: 

- the Audit_Clerk originated the item; 

- the Audit_Clerk is the actionee; 

- the Audit_Clerk is the reviewer. 

Alternately _,_ this could be stated as three distinct requirements as this makes each atomic and overall has the same meaning.  From an allocation, traceability, and verifiability perspective this form is preferable. 

- The Audit_System shall allow the Audit_Clerk to change the status of the action item when the Audit_Clerk originated the item. 

- The Audit_System shall allow the Audit_Clerk to change the status of the action item when the Audit_Clerk is the actionee. 

- The Audit_System shall allow the Audit_Clerk to change the status of the action item when the Audit_Clerk is the reviewer. 
**Acceptable if interpreted as a conjunction:** 

The Audit_System shall allow the Audit_Clerk to change the status of the action item when the following conditions are true: 

- the Audit_Clerk originated the item AND 

- the Audit_Clerk is the actionee AND 

- the Audit_Clerk is the reviewer. 

[In this form, the three conditions are expressed as a logical condition such that all three must be true for the logical condition to be true.] 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C7 - Verifiable
