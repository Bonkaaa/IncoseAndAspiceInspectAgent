---
id: R25
name: UseOfHeadings
type: rule
page: 83
target_scope: individual_statement
established_characteristics:
- C4
related_rules: []
---

## **4.5.2 R25 - /COMPLETENESS/USEOFHEADINGS**

**Avoid relying on headings to support explanation or understanding of the requirement.**

### Elaboration

It is a common mistake in document-centric documentation of needs and requirements to use the heading for a specific topic or subject under which the requirement applies to contribute to the explanation of the need or requirement statement.  The need or requirement statement should be complete in and of itself and not require the heading for the intent of the need or requirement to be clearly understood. 

Use of a heading can be avoided when using a data-centric approach to SE where sets of needs and requirements are developed and managed using a modern requirements management tool (RMT) or other SE tool rather than a legacy tool that is document-centric which organizes needs and requirements within sections and paragraphs of a document. 
### Examples

Example heading:” 4.0  Alert Buzzer Requirements” 

**Unacceptable:** _4.1_ The system shall sound it for greater than 20 minutes. 

[This is unacceptable because the requirement uses the pronoun “it” (R24), which requires the heading to understand what “it” means.  In addition, the word “sound” could be ambiguous as it can be a noun, a verb, adverb, or adjective.  We do not know whether Alert_Buzzer is a subsystem that controls the noise or the thing that makes the noise] 

**Acceptable:** The system shall activate the Alert_Buzzer for greater than 20 minutes. 

### Exceptions and relationships

The use of headings is acceptable when producing an output of a RMT, grouping like types or categories of needs or requirements.  See R40 and R41. 
### Characteristics that are established by this rule

- C4 - Complete
