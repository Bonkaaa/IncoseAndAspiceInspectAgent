---
id: R35
name: TemporalIndefinite
type: rule
page: 95
target_scope: individual_statement
established_characteristics:
- C3
- C4
- C7
related_rules: []
---

## **4.12.2 R35 - /QUANTIFICATION/TEMPORALINDEFINITE**

**Define temporal dependencies explicitly instead of using indefinite temporal keywords.**

### Elaboration

Some words and phrases signal non-specific timing, such as “eventually”, “until”, “before”, “after”, “as”, “once”, “earliest”, “latest”, “instantaneous”, “simultaneous”, and “at last” are ambiguous and not verifiable.  Indefinite temporal keywords can cause confusion or unintended meaning.  These words should be replaced by specific timing constraints. 

### Examples

**Unacceptable:** Continual operation of the pump shall eventually result in the tank being empty. [This is unacceptable because “eventually” is ambiguous.  Also, this statement is not written in the proper form.  It is written on “operation” rather than on a requirement on the pump which violates R3.] 

**Acceptable:** The Pump shall remove greater than 99% of the Fluid from the Tank in less than 3 days of continuous operation. 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C4 - Complete
- C7 - Verifiable
