---
id: R7
name: AvoidVagueTerms
type: rule
page: 65
target_scope: individual_statement
established_characteristics:
- C3
- C4
- C7
related_rules: []
---

## **4.1.7 R7 - /ACCURACY/AVOIDVAGUETERMS**

**Avoid the use of vague terms.**

### Elaboration

Avoid words that provide vague quantification, such as “some”, “any”, “allowable”, “several”, “many”, “a lot of”, “a few”, “almost always”, “very nearly”, “nearly”, “about”, “close to”, “almost”, and “approximate”, 

Avoid vague adjectives such as “ancillary”, "relevant”, “routine”, “common”, “generic”, “significant”, “flexible”, “expandable”, “typical”, “sufficient”, “adequate”, “appropriate”, “efficient”, “effective”, “proficient”, “reasonable” and “customary.” 

Vague adjectives can lead to ambiguous, unverifiable requirements that do not reflect accurately the stakeholder expectations. 

Adverbs qualify actions in some way and are particularly troublesome.  Avoid vague adverbs, such as “usually”, “approximately”, “sufficiently”, and “typically”. 

Vague adverbs can lead to ambiguous, unverifiable requirements that do not reflect accurately the stakeholder expectations. 

Because the true intent is not being communicated, the need or requirement is not complete (C4). As a general rule, words that end in “-ly” often result in ambiguity. 
### Examples

**Unacceptable:** The Flight_Information_System shall usually be online. 

[This is unacceptable because “usually” is ambiguous - is availability what is meant?] 

**Acceptable:** The Flight_Information_System shall have an Availability of greater than xx% over a period of greater than yyyy hours. 

[Note that “Availability” must be defined in the glossary since there are a number of possible ways of calculating that measure.] 
**Unacceptable:** The Flight_Information_System shall display the Tracking_Information for relevant aircraft. 

[This is unacceptable because it does not make explicit which aircraft are relevant.  Additionally, the statement allows the developer to decide what is relevant; such decisions are in the province of the customer, who should make the requirement explicit.] 

**Acceptable:** The Flight_Information_System shall display the Tracking_Information of each Aircraft located less than or equal to 20 kilometers from the Airfield. 

[Now it is clear for which aircraft the information needs to be displayed.  Note that “Aircraft”, “Tracking_Information”, and “Airfield” must be defined in the glossary.] 

### Exceptions and relationships

R3 points out that the use of a verb such as “safe”, may be acceptable at the business management or operations level as long as it is unambiguous at that level, decomposed at the lower levels, and is verifiable at the level stated.  Similarly, some vague adjectives may be allowable at the business management or operations level, providing they are not ambiguous at that level. 

### Characteristics that are established by this rule

- C3 - Unambiguous
- C4 - Complete
- C7 - Verifiable
