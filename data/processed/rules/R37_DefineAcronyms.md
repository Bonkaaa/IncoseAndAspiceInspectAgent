---
id: R37
name: DefineAcronyms
type: rule
page: 97
target_scope: individual_statement
established_characteristics:
- C3
- C9
- C11
- C13
- C14
related_rules: []
---

## **4.13.2 R37 - /UNIFORMLANGUAGE/DEFINEACRONYMS**

**If acronyms are used in need and requirement statements, c.**

### Elaboration

The same acronym must be used in each need and requirement; various versions of the acronym are not acceptable. The use of different acronyms implies that the two items being referred to are different.  Inconsistency in the use of acronyms can lead to ambiguity. 

In a document-based practice of SE, a common rule is to use the full term and the abbreviation or acronym (in brackets) the first time and then use just the abbreviation or acronym from then on within a document (as is done in this Guide). 

In a data-centric practice of SE, in need and requirement sets that are generated and managed within an RMT, there is no guarantee that the set will be extracted in any particular order, so the old practice is not useful.  Because of this, the use of acronyms should be avoided. 

However, if used, acronyms must be used consistently throughout not only the sets of needs and requirements, but all artifacts developed across all lifecycle stages.  To address this issue, make sure acronyms are defined in a project wide acronym list or glossary. 

Acronyms must be written in a consistent way in terms of capitalization and periods.  For example, always “CMDP” and not “C.M.D.P.” nor “CmdP”. 

### Examples

**Unacceptable:** It would not be acceptable for one requirement to use the acronym “CP” for command post and another acronym “CMDP” to also refer to the “command post.” The use of two different acronyms implies that the two system elements being referred to are different. 

**Acceptable:** Settle on only one acronym, define it in the list of acronyms, and then use it consistently throughout the requirement set. 

**Unacceptable:** It would not be acceptable for one requirement to refer to the “Global Positioning System” and the remaining requirements refer just to “GPS.” 

**Acceptable:** Use the full term every time or, perhaps more usefully, define the acronym in the project acronym list or glossary and use it every time. 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C9 - Conforming
- C11 - Consistent
- C13 - Comprehensible
- C14 - Able to be Validated
