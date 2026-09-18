---
id: R18
name: SingleSentence
type: rule
page: 76
target_scope: individual_statement
established_characteristics:
- C3
- C5
- C7
- C9
- C13
related_rules:
- R1
- R11
- R22
---

## **4.4.1 R18 - /SINGULARITY/SINGLESENTENCE**

**Write a single sentence that contains a single thought conditioned and qualified by relevant subclauses.**

### Elaboration

Based on the concepts of allocation, traceability, validation, and verification, need and requirement statements must contain a single thought allowing needs to be traced to their source and the single thought within a requirement statement to be allocated, the resulting single thought child requirements to trace to their allocated parent, requirements to trace to a single thought source, and allowing design and system validation and design and system verification against the single thought need or requirement. 

Sometimes a need or requirement statement is only applicable under a specific condition or multiple conditions.  See R1, R11, and R27. 

If multiple actions are needed for a single condition, each action should be repeated in the text of a separate need or requirement statement along with the triggering condition, rather than stating the condition and then listing the multiple actions to be taken.  Using this convention, the system can be verified to perform each action and each action be separately allocated to the entities at the next level of the architecture. 

Also avoid stating the condition or trigger for an action in a separate sentence.  Instead write a simple affirmative declarative sentence with a single subject, a single main action verb and a single object, framed and qualified by one or more sub-clauses. 

Compound sentences are to be avoided that contain more than subject/verb/object. 

Often when there are multiple sentences for one requirement, the writer is using the second sentence to communicate the conditions for use or rationale for the requirement for the first sentence.  This practice is not acceptable – rather include this information in the attribute A1 - _Rationale_ as part of the requirement expression as discussed in the NRM and include the condition of use within the need or requirement statement. 

See also R1, R11, R22. 

### Examples

**Unacceptable:** When in the Active_State, the Record_Subsystem shall display the Name of each Line_Item _and_ shall record the Location of each Line_Item, without obscuring the User_ID. 

[This is unacceptable because the sentence contains two requirements and the qualification only applies to the first requirement, not the second.] 

**Acceptable:** (Split into two separate requirements) 

When in the Active_State, the Record_Subsystem shall display the Name of each Line_Item, without obscuring the User_ID. 

When in the Active_ State, the Record_Subsystem shall record the Location of each Line_Item. [Note use of the glossary to define terms.] 
**Unacceptable:** The Control_Subsystem will close the Inlet_Valve until the temperature has reduced to 85 °C, when it will reopen it. 

[This is unacceptable because the sentence contains two event driven requirements. Additionally, the sentence contains two occurrences of the pronoun “it” ambiguously referring to different things (see R26), the term 'has reduced' is ambiguous, and the action verb must be 'shall', not 'will'.] 

**Acceptable:** (Split into two requirements) 

If the temperature of water in the Boiler is greater than 85 °C, the Control_Subsystem shall close the Inlet_Valve in less than 3 seconds 

When the temperature of water in the Boiler is reduced to less than or equal to 85 °C., the Control_Subsystem shall open the Inlet_Valve in less than 3 seconds. 

[Note use of the glossary to define terms.] 

**Unacceptable:** 

In the event of a fire detection: 

- Power to electromagnetic magnetic fire door catches shall be turned off. 

- Security entrances shall be set to Free_Access_Mode. 

- Fire escape doors shall be unlocked. 

[This is unacceptable because the condition “in the event of a fire detection” is stated following a list of actions to be taken; each of which the system must be verified against.  Also, note the actions are written in passive voice which violates R2.  Each action needs to be communicated in a separate requirement statement.  For multiple conditions for a single action see R28.] 

**Acceptable:** (Split into three requirements) 

In the event of a fire detection, the Security_System shall turn off power to electromagnetic magnetic fire door catches. 

In the event of a fire detection, the Security_System shall set security entrances to the Free_Access_Mode. 

In the event of a fire detection, the Security_System shall unlock fire escape doors. 

### Exceptions and relationships

Every requirement should have a main clause with a main verb (R1).  However, additional subclauses with auxiliary verbs or adverbs may be used to qualify the requirement with performance attributes. 

Such sub-clauses cannot be verified in isolation since they are incomprehensible without the main clause.  Sub-clauses that need to be verified separately from others should be expressed as separate requirements. 

For example, “The Ambulance_Control_System shall communicate Incident_Details to the Driver” is a complete, comprehensible statement with a single main verb.  An auxiliary clause may be added to provide a constraint “The Ambulance_Control_System shall communicate Incident_Details to the Driver _while simultaneously maintaining communication with the Caller.”_ 

Similarly, if the requirement is to extinguish and dispose of a match as a single combined action, the requirement must ensure that both are verified the same time and allocated the same. 
Note that, if performance attributes need to be verified separately, they should be expressed as sub-clauses in separate requirements. 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C5 - Singular
- C7 - Verifiable
- C9 - Conforming
- C13 - Comprehensible
