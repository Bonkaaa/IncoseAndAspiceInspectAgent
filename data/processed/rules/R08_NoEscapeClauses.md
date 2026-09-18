---
id: R8
name: NoEscapeClauses
type: rule
page: 66
target_scope: individual_statement
established_characteristics:
- C3
- C7
related_rules: []
---

## **4.1.8 R8 - /ACCURACY/NOESCAPECLAUSES**

**Avoid escape clauses.**

### Elaboration

Escape clauses give an excuse to the developer of the system at lower levels not to implement a need or requirement.  From a contracting standpoint, needs or requirements with these phrases could therefore be interpreted as being optional even if communicated in a “shall” requirement statement. 

Such clauses provide vague conditions or possibilities, using phrases such as “so far as is possible”, “as little as possible”, “where possible”, “as much as possible”, “if it should prove necessary”, “if necessary”, “to the extent necessary”, “as appropriate”, “as required”, “to the extent practical”, and “if practicable.” 

Escape clauses can lead to ambiguous needs that the SOI cannot be validated to meet and are open to interpretation and that do not reflect accurately lifecycle concepts from which they were transformed. 

Escape clauses can lead to ambiguous, unverifiable requirements that are open to interpretation and that do not reflect accurately the needs from which they were transformed. 

### Examples

**Unacceptable:** The GPS shall, _where there is sufficient space_ , display the User_Location. 

[This is unacceptable because whether there is sufficient space is vague, ambiguous, and unverifiable.  The requirement is clearer without the escape clause.] 
**Acceptable:** The GPS shall display the User_Location. 

[Note that “GPS” and “User_Location” must be defined in the glossary.  Specific performance requirements need to be defined as well such as within what time, format, and accuracy.] 

**Unacceptable:** The Television shall, _to the extent necessary_ , conform to the requirements in Section a.1 of Standard XYZ. 

[This is unacceptable because it is unclear who is to determine the meaning of ‘necessary’.  The requirement is clearer without the escape clause.] 

**Acceptable:** The Television shall conform to the requirements in Section a.1 of Standard XYZ. 

[Note that this form of requirement means that each requirement of Standard XYZ is to be met—if only a subset of a standard or regulation is required, that subset must be either listed explicitly or implementing requirements derived that meet the intent of the specific requirements in the standard and regulation, with a trace to the source or parent requirement.]  Refer to the NRM and GtNR for a more detailed discussion concerning compliance with requirements within standards and regulations. 

### Characteristics that are established by this rule

- C3 - Unambiguous
- C7 - Verifiable
