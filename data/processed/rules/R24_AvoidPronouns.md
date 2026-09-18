---
id: R24
name: AvoidPronouns
type: rule
page: 82
target_scope: individual_statement
established_characteristics:
- C3
- C4
- C7
related_rules:
- R32
- R36
---

## **4.5.1 R24 - /COMPLETENESS/AVOIDPRONOUNS**

**Avoid the use of pronouns and indefinite pronouns.**

### Elaboration

Repeat nouns in full instead of using pronouns to refer to nouns in other need or requirement statements. 

Pronouns are words such as “it”, “this”, “that”, “he”, “she”, “they”, and “them.” 
When writing stories, pronouns are a useful device for avoiding the repetition of nouns; but when writing need and requirement statements, pronouns are effectively cross-references to nouns in other need or requirement statements and, as such, are ambiguous and should be avoided. 

When originally written, the noun that defines the pronoun may have preceded the pronoun in the previous need or requirement statement, however, as the set of requirements mature, individual requirements may be added, deleted, reordered, or regrouped, and the defining requirement is no longer nearby.  This is especially true when requirements are stored in a requirement management tool where they exist as single statements in a database that may not be in order. To avoid these problems, repeat the proper nouns rather than using a pronoun. 

Indefinite pronouns are words such as “all”, “another”, “any”, “anybody”, “anything”, “both”, “each”, “either”, “every”, “everybody”, “everyone”, “everything”, “few”, “many”, “most”, “much”, “neither”, “no one”, “nobody”, “none”, “one”, “several”, “some”, “somebody”, “someone”, “something”, and “such.” Indefinite pronouns stand in for unnamed people or things, which makes their meaning subject to interpretation, ambiguous, and unverifiable. 

See also R32 and R36. 

### Examples

**Unacceptable:** The controller shall send the driver his itinerary for the day. It shall be delivered at least 8 hours prior to his Shift. 

[This is unacceptable because the requirement is expressed as two sentences and the second sentence uses the pronouns “it” and “his.”] 

**Acceptable:** The Controller shall send the Driver_Itinerary for the day to the Driver at least 8 hours prior to the Driver_Shift. 

[Note use of the glossary to define terms and to be explicit about the relationship between the driver, shift, and the itinerary for that particular driver.] 

### Characteristics that are established by this rule

- C3 - Unambiguous
- C4 - Complete
- C7 - Verifiable
