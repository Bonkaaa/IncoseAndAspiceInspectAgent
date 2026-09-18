---
id: R20
name: AvoidPurpose
type: rule
page: 79
target_scope: individual_statement
established_characteristics:
- C1
- C5
related_rules: []
---

## **4.4.3 R20 - /SINGULARITY/AVOIDPURPOSE**

**Avoid phrases that indicate the purpose of or reason for the need or requirement statement.**

### Elaboration

Needs and requirement statements should be as concise as possible and be complete (C4).  To avoid ambiguity or communicate why the need or requirement is necessary (C1), some writers feel the need to include additional information to make the intent and reason clearer by including additional text within the need or requirement statement.  The text of a need or requirement statement does not and should not have to carry around this extra text. 

Expressions of purpose are often indicated by the presence of phrases such as “……to”, “in order to”, “so that”, and “thus allowing.” 

This extra information should be included separately in the need or requirement expression using the rationale attribute (A1) as discussed in the NRM. 

### Examples

**Unacceptable:** The Record_Subsystem shall display the Name of each Line_Item so that the Operator can confirm that it is the correct Item. 

[This is unacceptable because the text “so that the Operator can confirm that it is the correct Item” is rationale.] 

**Acceptable:** The Record_Subsystem shall display the Name of each Line_Item. 

[The text “so that the Operator can confirm that it is the correct Item” should be included in the rationale attribute.] 

**Unacceptable:** The Operation_Logger shall record each Warning_Message produced by the system. 

[This is unacceptable because of the superfluous words “produced by the system”.] 

**Acceptable:** The Operation_Logger shall record each Warning_Message. 

### Characteristics that are established by this rule

- C1 - Necessary
- C5 - Singular
