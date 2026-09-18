---
id: R30
name: ExpressOnce
type: rule
page: 88
target_scope: individual_statement
established_characteristics:
- C1
- C9
- C11
related_rules: []
---

## **4.8.2 R30 - /UNIQUENESS/EXPRESSONCE**

**Express each need and requirement once and only once.**

### Elaboration

Avoid including the same or equivalent need and requirement more than once, either as a duplicate or in similar form.  Exact duplicates are relatively straightforward to identify; finding similar need or requirement statements with slightly different wording is much more difficult but is aided by the consistent use of defined terms (R4) and by classification (R29). 
### Examples

Exact duplicates can be found by matching of text strings.  The main problem is to identify similarities with different expressions, but which are equivalent.  For example: "The system shall generate a report of financial transactions containing the information defined in <some standard or contract deliverable listing>" and "The system shall generate a financial report." are overlapping in that the first is a subset of the second. 

Avoidance of duplication can be aided by classification (R29) so a subset of needs or requirements can be compared. 
### Characteristics that are established by this rule

- C1 - Necessary
- C9 - Conforming
- C11 - Consistent
