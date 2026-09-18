---
id: R3
name: SubjectVerb
type: rule
page: 60
target_scope: individual_statement
established_characteristics:
- C2
- C3
- C7
- C10
- C14
related_rules: []
---

## **4.1.3 R3 - /ACCURACY/SUBJECTVERB**

**Ensure the subject and verb of the need or requirement statement are appropriate to the entity to which the need or requirement refers.**

### Elaboration

### **Subject** 

The subject of a need or requirement statement must be appropriate to the entity to which it _refers_ . 

Requirements referring to the business management level therefore have the form “The <business> shall …”; those referring to the business operations level have the form “The < operations> shall …”; those referring to the system level have the form "The <system> shall …"; requirements referring to the subsystem level have the form "The <subsystem> shall ..."; and requirements referring to the component level have the form "The <component> shall ...". 
As a general rule, sets of need and requirement statements for a specific entity should only contain needs or requirements for that entity—that is, a set of business management requirements would contain only business management needs or requirements, a set of business operations requirements would contain only business operations needs or requirements, a set system requirements would contain only needs or requirements that apply to the integrated system, a set subsystem requirements would contain only needs or requirements that apply to that subsystem, a set system element requirements would contain only needs or requirements that apply to that system element. 

In some cases, however, a higher-level entity may wish to be prescribe needs and requirements that apply to a lower-level entity.  For example, it may be important for a business to mandate that the new aircraft under development must use a particular engine (perhaps for support reasons) in which case they may make a statement at the business level that refers to an entity at the subsystem level.  Therefore, any set of entity needs, or requirements can state for that entity needs or requirements that refer to itself, as well a lower-level entity the need or requirement applies (should there be a good reason to do so).  When this is the case, the prescriptive allocated need or requirement is treated as a constraint on the lower-level entity.  In these cases, the lower-level entity will then include an entity specific child requirement and trace that child requirement to its parent or source. 

Consequently, regardless of the entity to which a need or requirement applies, the subject of a need or requirement statement must be appropriate to the entity to which it _refers_ .  To continue our aircraft example above, although many requirements at the business management level will begin with “The ACME Aircraft Company shall …”, the business may therefore wish to state at the business management level a requirement stating that all aircraft developed by the organization shall use an engine with specific characteristics.  For a specific aircraft, child requirements will be written for the appropriate entity that implements the intent of the business management generic requirement.  For the entity dealing with the engine specifically, the system level child requirement would begin “The Aircraft shall….”; and at the subsystem level the child requirement would begin “The Engine shall …” and trace back to the system level parent requirement, which, in turn, would trace back to the business management level constraint as the parent or source. 

### **Verb** 

Similarly, the verb of a need or requirement statement must be appropriate to the subject of the need or requirement for the entity it is stated.  For needs the verbs such as “support”, “process”, “handle”, “track”, “manage”, and “flag” may be appropriate.  However, they are too vague for requirement statements which therefore may not be Unambiguous (C3) nor Verifiable (C7) .  At the business management level, for example, the use of a verb such as “safe”, may be acceptable as long as it is unambiguous at that level, decomposed at the lower levels, and is verifiable at those levels. 

### Examples

#### Subject examples

Business management requirements have the form “The <business> shall …”—for example, “ACME_Transport shall …”. 

Business operations requirements on personnel roles have the form: “The <personnel role> shall …”—for example, “The Production_Manager shall …”; “The Marketing_Manager shall …”. System level needs have the form “The stakeholders need the system to ……” 

System requirements have the form "The <system> shall ..."—for example, “The Aircraft shall …” Subsystem level needs have the form “The stakeholders need the subsystem to ……” 
Subsystem requirements have the form "The <subsystem> shall ..." –for example, once the subsystems are defined: “The Engine shall …”; “The Landing_Gear shall …”. 

#### Verb examples

System level stakeholder need: “The stakeholders need the system to process data received from [other system] XYZ.” 

System level requirement: “The system shall [process] data having the characteristics defined in [Other system that supplies the data] Interface Definition XYZ.” 

Through analysis, the verb/function “process” could be decomposed into sub functions such as “receive”, “store”, “calculate”, “report”, and “display”.  Then a decision needs to be made regarding the level at which these sub functions are to be stated.  If more than one subsystem is involved in any one of the sub functions, that requirement should be communicated at the system level and allocated to the applicable subsystems.  If a sub function is to be implemented by a single subsystem, then the sub function requirement should be communicated at the subsystem level and traced back to the parent requirement from which it was decomposed. 

**Unacceptable system requirement:** “The User shall ……….” 

- [This is unacceptable because the requirement should be on the system, not the user or operator of the system.  This wording is often the result of writing requirements directly from user stories or resulting need statements, without doing the transformation of the use case or user need into a system requirement.  Ask, what does the system have to do so that the user need can be achieved?] 

**Acceptable:** “The <system> shall …….” 
### Characteristics that are established by this rule

- C2 - Appropriate
- C3 - Unambiguous
- C7 - Verifiable
- C10 - Complete
- C14 - Able to be Validated
