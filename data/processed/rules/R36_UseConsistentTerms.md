---
id: R36
name: UseConsistentTerms
type: rule
page: 95
target_scope: individual_statement
established_characteristics:
- C3
- C8
- C9
- C11
- C13
- C14
related_rules: []
---

## **4.13.1 R36 - /UNIFORMLANGUAGE/USECONSISTENTTERMS**

**Use each term and units of measure consistently throughout need and requirement sets.**

### Elaboration

R4 requires the definition of terms in each requirement and R6 requires units of measure to be included with numbers.  In addition to those rules, terms and units of measure must be used consistently throughout not only the sets of needs and requirements, but all artifacts developed across all lifecycle stages.  A common ontology therefore needs to be defined for each project defining terms and units of measure across all artifacts, including the sets of needs and requirements as well as all design output artifacts.  Synonyms are not acceptable. 

A glossary or data dictionary is extremely useful to define words precisely.  Terms defined within the glossary or data dictionary terms are capitalized to signify that the word or term being used has a specific meaning in the context of the set of statements. 

For a numeric value for a given variable that may appear in multiple needs or requirements, to help ensure consistency, it is a best practice to define the variable and its numeric value and units of measure in a glossary or data dictionary.   An example would be the maximum and minimum environment temperatures specified in multiple places.  For example, Maximum_Temperature_Value.  This also resolves the units problem as this is also defined at the same time in the glossary entry.  Although it could be argued that the loss of the value in the text 
makes the requirement harder to understand, however the ability to maintain consistency is higher priority 

Ideally, the glossary or data dictionary used for the sets of needs and requirements is the same the project glossary or data dictionary. 
### Examples

**Unacceptable:** It would not be acceptable for one requirement to refer to an entity using one term and another to refer to the same entity using another term. 

For example, in a subsystem set of design input requirements, the following three requirement statements: 

The radio shall .... The receiver shall .... The terminal shall .... _Or:_ The bleed valve shall .... The high-pressure bleed valve shall .... The HPBV shall .... 

If each term refers to the same subject, the statements need to be modified to use the same word (or, if they are meant to be different, the words must be defined to be so). 

**Acceptable:** Settle on only one term, define it in the glossary or data dictionary, and then use it consistently in each need, requirement, and design output artifact. 

**Unacceptable:** When the Input_Valve is connected to the Water_Source, the Control_Subsystem shall open the Inlet_Valve. 

[Two terms are used for the same thing “Input_Valve” and “Inlet_Valve”.] 

**Acceptable:** When the Inlet_Valve is connected to the Water_Source, the Control_Subsystem shall open the Inlet_Valve. 

**Unacceptable:** It would not be acceptable for one requirement to use one unit of measure (e.g., US - feet) and another requirement to use another unit of measure (e.g., Metric - meter). 

**Acceptable:** Settle on which units of measure will be used and use that unit of measure consistency across all SE artifacts including needs, design input requirements and design output specifications. 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C8 - Correct
- C9 - Conforming
- C11 - Consistent
- C13 - Comprehensible
- C14 - Able to be Validated
