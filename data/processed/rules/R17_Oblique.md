---
id: R17
name: Oblique
type: rule
page: 75
target_scope: individual_statement
established_characteristics:
- C3
- C7
related_rules: []
---

## **4.3.6 R17 - /NONAMBIGUITY/OBLIQUE**

**Avoid the use of the oblique ("/") symbol.**

### Elaboration

The oblique symbol (“/”), or “slash”, has so many possible meanings that it should be avoided. The slash symbol (e.g., “user/operator”, “budget/schedule” or the construct “and/or” discussed in R15) can lead to ambiguous need and requirement statements that do not reflect accurately the true customer needs or lifecycle concepts from which the needs were derived. 

An exception to this rule is where the oblique symbol is used in SI units (for example “km/h”) or when communicating a symmetrical range of a value (for example +/- 5 degrees F.) Also see R19. 

### Examples

**Unacceptable:** The User_Management_System shall Open/Close the User_Account in less than 1 second. 

[This is unacceptable because it is unclear as to what is meant: open, close, or both?] **Acceptable:** (Split into two requirements) 

The User_Management_System shall Open the User_Account in less than 1 second. 

The User_Management_System shall Close the User_Account in less than 1 second. 

**Unacceptable:** The Engine_Management_System shall disengage the Speed_Control_Subsystem when the Clutch is disengaged and/or the Driver applies the Brake. 

[This is unacceptable because of the use of “and/or.” If “and” is meant, split the two thoughts into separate requirements.  If “or” is meant, write the requirement as an exclusive “or.”] 

**Acceptable:** (Split into two requirements) 

The Engine_Management_System shall disengage the Speed_Control_Subsystem when the Clutch is disengaged. 

The Engine_Management_System shall disengage the Speed_Control_Subsystem when the Driver is applying the Brake. 

**Acceptable:** (as one requirement if exclusive or is intended) 

The Engine_Management_System shall disengage the Speed_Control_Subsystem when [the Clutch is disengaged OR the Driver is applying the Brake]. 

### Characteristics that are established by this rule

- C3 - Unambiguous
- C7 - Verifiable
