---
id: R27
name: Explicit
type: rule
page: 85
target_scope: individual_statement
established_characteristics:
- C4
- C7
- C8
related_rules:
- R1
- R11
- R18
---

## **4.7.1 R27 - /CONDITIONS/EXPLICIT**

**State applicability conditions explicitly.**

### Elaboration

State applicability conditions explicitly instead of leaving applicability to be inferred from the context. 

Sometimes need or requirement statements are only applicable under certain conditions.  If so, the condition should be repeated in the text of each need or requirement statement, rather than stating the condition and then listing the actions to be taken. 

There are several agreed to types of condition: 

Event-driven requirements: 

When <optional preconditions/trigger> the <system name> shall <system response>. 

In the event of <specific event> the <system name> shall <system response>. 

Behavior driven requirements: 

If <optional preconditions/trigger>, then the <system name> shall <system response>. 

State-driven requirements : 

While <entering, exiting or in a specific state (or mode)> the <system name> shall <system response>. 

If a condition that applies to a need or requirement is not stated explicitly within the need or requirement statement, the need or requirement statement is not Complete (C4), Verifiable (C7), nor Correct (C8) unless the condition clause is included. 

See also R1, R11, R18. 

### Examples

**Unacceptable:** 

In the event of a fire detection: 

- Power to electromagnetic magnetic fire door catches shall be turned off. 

- Security entrances shall be set to Free_Access_Mode. 

- Fire escape doors shall be unlocked. 

[This is unacceptable because the condition “in the event of a fire detection” is stated following a list of actions to be taken.  Also, note the actions are written in passive voice which violates R2.] 

**Acceptable:** (Split into three separate requirements.) 

In the event of a fire detection, the Security_System shall turn off power to electromagnetic magnetic fire door catches. 

In the event of a fire detection, the Security_System shall set security entrances to the Free_Access_Mode. 

In the event of a fire detection, the Security_System shall unlock fire escape doors. 
### Characteristics that are established by this rule

- C4 - Complete
- C7 - Verifiable
- C8 - Correct
