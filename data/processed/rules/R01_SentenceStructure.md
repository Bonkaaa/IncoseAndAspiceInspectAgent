---
id: R1
name: SentenceStructure
type: rule
page: 57
target_scope: individual_statement
established_characteristics:
- C3
- C4
- C7
- C8
- C9
related_rules:
- R2
- R3
- R11
- R18
- R27
---

## **4.1.1 R1 - /ACCURACY/SENTENCESTRUCTURE**

**Use a structured, complete sentence.**

### Elaboration

The structure of needs and requirements statements must be in the form of a complete sentence, the simplest form of which is: 

<subject> <verb> <object>. 

The subject is essential because it is the entity undertaking the action; the verb is essential because it is the action being performed; and the object is essential because it must be clear as to which entity is being acted upon. 

The subject and objects are therefore normally entities and for a requirement statement the verb is “shall” as described in Section 1.  Use of “shall” makes it clear that what is being communicated is formal, the statement is a requirement, the statement is legally binding, and the SOI will be verified against the requirement.  Currently, no other form, other than textual “shall” requirement statements, have been shown to meet these characteristics.  Some organizations may use other verbs such as “must”, “will”, “should”, or “may”—regardless, whichever verb is used, the 
mandatory, contractually binding nature of the action must be defined somewhere in the terms and conditions of the contract to made clear the statement is a requirement. 

Expanding on the <subject> <verb> <object> form, requirements have a general form of 

The <entity> shall <entity response> <qualifying statement> which can be further expanded to The <entity> shall <action verb> <object> <measurable outcome> <qualifying statement>. 

In terms of a function/performance requirement, the <action verb> <object> pair is communicated as a function/object pair (heat coffee) and the <measurable outcome> is a specific performance outcome of performing that function (to a temperature of 120deg F.) The <qualifying statement> is additional information needed to clearly communicate the intent of the requirement as discussed below. 

For a requirement involving an interaction between two entities (interface requirement) the <action verb> indicates the type of interaction, the <object> is what is involved in the interaction, and the <measurable outcome> is a pointer where the specific interaction is defined (e.g., Interface Control Document). 

Need statements have a similar form: 

The <stakeholders> need the <entity><entity response>.  or 

The <stakeholders> need the <entity><action verb> <object> <outcome>. 

For need statements the outcome may be at a higher level of abstraction and not as specific as <measurable outcome> for a requirement statement as discussed in Section 2 and R3. 

If a <qualifying statement> is needed to clearly communicate the intent of the action verb on the object is not stated explicitly within the need or requirement statement, the need or requirement statement is not Complete (C4) ), Verifiable (C7), nor Correct (C8)  unless the qualifying statement is included, .e.g., performance associated with the action verb or for an interface requirement where a pointer to where the specific interaction is defined (i.e., and ICD). 

ISO/IEC 29148 states that a more-complete, typical sentence form for a functional requirement is: When <condition clause>, the <subject clause> shall <action verb clause> <object clause> <optional qualifying clause>. 

There are several agreed types of condition clauses: 

_Event-driven requirements:_ 

When <optional preconditions/trigger>, the <system name> shall <system response>. 

In the event of <specific event>, the <system name> shall <system response>. 

_Behavior driven requirements:_ 

If <optional preconditions/trigger>, then the <system name> shall <system response>. _State-driven requirements_ **_:_** 

While <entering, exiting or in a specific state (or mode)>, the <system name> shall <system response>. 

See Appendix C for additional example patterns using clauses. 

If a condition that applies to a need or requirement is not stated explicitly within the need or requirement statement, the need or requirement statement is not Complete (C4), Verifiable (C7), nor Correct (C8) unless the condition clause is included. 
Note: While IEEE/ISO/IEC 29148 shows the conditional phrase at the beginning of the sentence, some organizations prefer to put the conditional phrase at the end of the sentence. 

Organizations need to define the desired form in their standards, guides, and processes and then be consistent in the form being used.  As long as the result is clear and unambiguous, either form is acceptable. 

See also R2, R3, R11, R18, R27, and Appendix C. 

### Examples

**Condition examples:** 

Event-driven requirements: 

When Continuous_Ignition is commanded by the Aircraft, the Control_System shall switch on Continuous_Ignition. 

In the event of a fire detection, the Security_System shall Unlock the Fire_Escape_Doors _._ Behavior driven requirements: 

If the Computed_Airspeed Fault_Flag is set, [then] the Control_System shall use Modelled_Airspeed. 

State-driven requirements **:** 

While the Aircraft is In-flight, the Control_System shall Maintain Engine_Fuel_Flow at greater than XX lbs/sec. 

Qualification examples: 

When in the ‘ON’ state, the System shall display the Time, without obscuring the Work_Space. 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C4 - Complete
- C7 - Verifiable
- C8 - Correct
- C9 - Conforming
