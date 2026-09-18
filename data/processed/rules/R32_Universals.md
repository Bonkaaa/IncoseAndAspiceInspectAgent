---
id: R32
name: Universals
type: rule
page: 91
target_scope: individual_statement
established_characteristics:
- C3
- C7
- C8
related_rules: []
---

## **4.10.1 R32 - /QUANTIFIERS/UNIVERSALS**

**Use “each” instead of “all”, “any”, or “both” when universal quantification is intended.**

### Elaboration

The use of “all”, “both”, or “any” is confusing because it is hard to distinguish whether the action happens to the whole set or to each element of the set.  “All” can also be hard to verify unless “all” can be clearly defined as a closed set.  In many cases, the word “all” is unnecessary and can be removed, resulting in a less ambiguous need or requirement statement. 

### Examples

**Unacceptable:** The Operation_Logger shall record any _(or all)_ warning messages. 

[This is unacceptable because of the use of the word “any”, which is then made worse by the addition of “(or all)”.] 

**Acceptable:** The Operation_Logger shall record each Warning_Message. 

[Note that Warning_Message must be defined so that it is clear that the system only will record each defined Warning Message.] 

**Unacceptable:** The Record_Subsystem shall display the Names of both of the Line_Items. [This is unacceptable because of the use of the word “both”.] 

**Acceptable:** The Record_Subsystem shall display the Name of each Line_Item. _**Acceptable:**_ : The Record_Subsystem shall display each Line_Item_Name. 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C7 - Verifiable
- C8 - Correct
