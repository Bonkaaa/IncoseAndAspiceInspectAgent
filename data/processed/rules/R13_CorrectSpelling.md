---
id: R13
name: CorrectSpelling
type: rule
page: 71
target_scope: individual_statement
established_characteristics:
- C3
- C7
- C8
related_rules: []
---

## **4.3.2 R13 - /NONAMBIGUITY/CORRECTSPELLING**

**Use correct spelling.**

### Elaboration

Incorrect spelling can lead to ambiguity and confusion.  Some words may sound the same but, depending on the spelling, will have entirely different meaning.  For example, “red” versus “read” or “ordinance” versus “ordnance.” In other cases, the word could be spelled the same, but have a different meaning or the meaning changes depending on the context of which it is used.  For example, "clear windscreen" and "clear the screen” which has the 2 different meanings for "clear". _In addition, the word “sound” could be ambiguous as it can be a noun, a verb, adverb, or adjective._ In these cases, a spell checker cannot distinguish the meaning nor context not finding these kinds of errors. 

A requirement that has spelling errors is not correct (C8) and may not be Verifiable (C7). 

In addition to misspelling, this rule also refers to the proper use of: 

- Capital letters in acronyms: avoid “SYRD” and “SyRD” in the same set of design input requirements. 

- Capital letters in other non-acronyms concepts: avoid “Requirements Working Group” and “Requirements working group” in the same set of design input requirements. 

- Proper use of hyphenation: “non-functional” versus “nonfunctional.” Often hyphenation is used when two related words are used as adjectives but is not used when used as a noun. 

### Examples

**Unacceptable:** The Weapon_Subsystem shall store the location of all _ordinance_ . 

[This is unacceptable because the word “ordinance” means regulation or law.  It is unlikely that the Weapon_Subsystem is interested in the location of ordinance (regulations).  In the context of a weapon system, what the authors meant to use is "ordnance" as in weapons and ammunition, not “ordinance”.] 

**Acceptable:** The Weapon_Subsystem shall store the Location of all Ordnance. 

[Note that “Location” and “Ordnance” must be defined in the glossary to be explicit about the types of weapons and ammunition.] 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C7 - Verifiable
- C8 - Correct
