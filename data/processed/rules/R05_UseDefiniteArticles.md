---
id: R5
name: UseDefiniteArticles
type: rule
page: 63
target_scope: individual_statement
established_characteristics:
- C3
- C7
related_rules: []
---

## **4.1.5 R5 - /ACCURACY/USEDEFINITEARTICLES**

**Use definite article “the” rather than the indefinite article “a.”**

### Elaboration

The definite article is “ _the_ ”; the indefinite article is “ _a_ .” When referring to entities, use of the indefinite article can lead to ambiguity.  For example, if the need or requirement refers to “a user” it is unclear whether it means any user or one of the defined users for which the system has been designed.  This causes further confusion during verification and validation activities across the lifecycle—for example, babies are arguably users of baby food, but the system would fail if the test agency sought to verify or validate that a baby could order, receive, open, and serve (or even independently consume) baby food.  On the other hand, if the requirement refers to “the User”, the reference is explicitly to the nature of the user defined in the glossary—in the baby food example, the “User” is presumably the adult responsible for feeding the baby. 

### Examples

**Unacceptable:** The system shall provide a time display. 
[This is unacceptable for a requirement because it is ambiguous--will any time display do?  Is a one-off display of the time satisfactory?  The writer's intention was most likely that they wanted the system to display continuously the current time, yet if the developer provided a constant display of “10:00 am” (or even a one-off display of any time), they could argue (albeit unreasonably) that they have met the requirement; yet they would have clearly failed to meet the customer's need and intent. 

As a stakeholder need statement: “The stakeholders need the system to provide a time display.” The statement is acceptable.  As part of the transformation process the requirement writers will remove the ambiguity resulting in the following requirement statement.] 

**Acceptable:** The system shall display the Current_Time. 

[Note that “Current_Time” must be defined in the glossary since there are a number of possible meanings and formats of the more-general term “current time.” There may also be other requirements addressing where time needs to be displayed, accuracy, etc. if not addressed in the glossary or data dictionary.] 

### Exceptions and relationships

The purpose of this rule is to avoid the ambiguity that arises because “a” or “an” is tantamount to saying, “any one of”.  In some cases, however, the use of an indefinite article is not misleading. For instance, “… with an accuracy of less than 1 second” allows the phrase to read more naturally and there is no ambiguity because of the accuracy quoted. 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C7 - Verifiable
