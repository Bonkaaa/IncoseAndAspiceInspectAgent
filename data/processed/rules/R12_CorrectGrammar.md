---
id: R12
name: CorrectGrammar
type: rule
page: 70
target_scope: individual_statement
established_characteristics:
- C3
- C7
- C8
- C9
related_rules:
- R4
---

## **4.3.1 R12 - /NONAMBIGUITY/CORRECTGRAMMAR**

**Use correct grammar.**

### Elaboration

We interpret language based on the rules of grammar.  Incorrect grammar leads to ambiguity and clouds understanding.  This is especially true when the recipient of the need or requirement statement is working in a second language relying on specific rules of grammar.  If these rules are not followed, that person may misinterpret the meaning of the need or requirement statement. 

Incorrect use of grammar may make the true intent unclear resulting in an incorrect requirement and thus make it difficult to verify the SOI meets the intent of the requirement. 

Care must be taken when translating needs and requirements from one language to another and when sentence structure differs depending on the language in which the original need or requirement statement was written.  Punctuation varies from language to language and even between dialects of a given language. 

Be cautious when need and requirement statements must be translated.  An interesting exercise is to translate a requirement from one language to another and translate the result back to the original language. 

See also R4 – Define terms. 
### Examples

**Unacceptable:** The Weapon_Subsystem shall _storing_ the location of all ordnance. 

[This is unacceptable because the grammatical error leads to uncertainty about the meaning.] **Acceptable:** The Weapon_Subsystem shall store the location of all Ordnance. 

[Note that “Ordnance” must be defined in the glossary to be explicit about the types of weapons and ammunition.] 
**Unacceptable:** When in the Active_State, the Record_Subsystem shall display each of the Names of the Line_Items, without obscuring the User_ID. 

[This is unacceptable because the grammatical error involving the inappropriate placement of “each of”—it is most likely that a Line_Item has only one name.] 

**Acceptable:** When in the Active_State, the Record_Subsystem shall display the Name of each Line_Item, without obscuring the User_ID. 

### Characteristics that are established by this rule

- C3 - Unambiguous
- C7 - Verifiable
- C8 - Correct
- C9 - Conforming
