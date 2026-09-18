---
id: R4
name: UseDefinedTerms
type: rule
page: 62
target_scope: individual_statement
established_characteristics:
- C3
- C7
- C11
- C13
- C14
related_rules: []
---

## **4.1.4 R4 - /ACCURACY/USEDEFINEDTERMS**

**Define terms.**

### Elaboration

Most languages are rich with words having several synonyms, each with a subtly different meaning based on context.  In need and requirement statements, shades of meaning will most likely lead to ambiguity and to difficulty during verification and validation activities across the lifecycle.  Define terms in some form of ontology, including a glossary, data dictionary, or similar artifact that allows the reader of a need or requirement statement to know exactly what the writer meant when the word was chosen.  The meaning of a term should be the same every time the word is used no matter the work product, SE tool, or artifact being developed across all lifecycle stages. 

A standard should be agreed upon to make the use of glossary terms identifiable in the need and requirements text statements; for example, glossary items may be capitalized and multiple words 
in single terms joined by an underscore (e.g., “Current_Time”).  This is essential for consistency to avoid using the word with its general meaning without context.  This is the convention used in the examples in this section.  This standard should be implemented and enforced within all SE tools used by the project to help ensure consistency. 

Definitions of terms used within needs and requirement statements must be agreed to, documented, and used consistently throughout the project and all SE artifacts developed during all lifecycle activities. 

For cases where needs and requirements will be translated into a different language, it is helpful to develop a “translation matrix” where terms in the originating language are listed along with the acceptable term to be used in the target language such that the original intent is communicated. The use of this matrix will help ensure consistency in the translations when multiple people are involved in the translations over time. 

### Examples

**Unacceptable:** The system shall display the current time. 

[This is unacceptable because it is ambiguous--what is “current”, in which time zone, to what degree of accuracy, in what format?] 

**Acceptable:** The system shall display the Current_Time in "DD/MM/YYYY" format. 

[Note that “Current_Time” must then be defined in the glossary in terms of accuracy, format, time zone, and units.] 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C7 - Verifiable
- C11 - Consistent
- C13 - Comprehensible
- C14 - Able to be Validated
