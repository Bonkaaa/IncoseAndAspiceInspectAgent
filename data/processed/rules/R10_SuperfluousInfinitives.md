---
id: R10
name: SuperfluousInfinitives
type: rule
page: 68
target_scope: individual_statement
established_characteristics:
- C3
- C7
related_rules:
- R1
- R11
---

## **4.2.1 R10 - /CONCISION/SUPERFLUOUSINFINITIVES**

**Avoid superfluous infinitives.**

### Elaboration

We sometimes see a need or requirement that contains more verbs than necessary to describe a basic action, such as “The system shall be designed to be able to ...” or “The system shall be designed to be capable of ...” rather than simply “The system shall ...” Think ahead to design verification and system verification.  If the system “is able to”, or “is capable of”, doing something one time but fails 99 times, the system has not met the requirement. 

Note that at the enterprise and business levels, requirements for an entity to “provide a capability” are acceptable.  Where capability is made up of people, processes, and products; these requirements will be decomposed to address the people aspects (skill set, training, roles, etc.), processes (procedures, work instructions, etc.); and products (hardware and software systems). The enterprise and business level parent requirements will be allocated appropriately to the people, processes, and products (SOI), as appropriate. 

When the resulting requirement sets are implemented for all three areas, the capability will exist to meet the need. 

This is also true for needs at the system or system element levels.  The stakeholders may have a need for the system to “be able to” or “have the capability to” do something.  For example: “The stakeholders need the system to provide the capability for users to [do something] ...”.  As part of the transformation process from need to requirement, the requirement writer will determine what the system needs to do to provide that capability.  The resulting well-formed requirement(s) will then define what the system needs to do to supply that capability in unambiguous and verifiable language. 
If the intent of using “be able to” or “be capable of” type wording is to communicate the system will only need to do the required action based on some condition, trigger, or state, then it is best to state the condition, trigger, or state as part of the requirements.  When this is the case, refer to R1 and R11. 

### Examples

**Unacceptable:** The Weapon_Subsystem shall _be able to_ store the location of each Ordnance. 

[This is unacceptable because it contains the superfluous infinitive “be able to”.  However, this is acceptable for the stakeholder need: “The stakeholders need the Weapon_Subsystem to be able to store the location of each Ordnance.”] 

**Acceptable:** The Weapon_Subsystem shall store the Location of each Ordnance. 

[Note that the terms “Weapon_Subsystem”, “Location”, and “Ordnance” must be defined in the glossary or data dictionary.] 

### Characteristics that are established by this rule

- C3 - Unambiguous
- C7 - Verifiable
