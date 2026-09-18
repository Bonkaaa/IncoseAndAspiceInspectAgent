---
id: R33
name: ValueRange
type: rule
page: 92
target_scope: individual_statement
established_characteristics:
- C3
- C4
- C6
- C7
- C8
- C12
related_rules:
- R6
---

## **4.11.1 R33 - /TOLERANCE/VALUERANGE**

**Define quantities with a range of values appropriate to the entity to which the apply and to which the entity will be verified or validated against.**

### Elaboration

When it comes to defining performance, single-point values are seldom sufficient and are difficult to test.  Ask the question: “if the performance was a little less (or more) than this, would I still buy it?” If the answer is yes, then change the need or requirement statement to reflect an acceptable range of values. 

It also helps to consider the underlying goal: are you trying to minimize, maximize or optimize something?  The answer to this question will help determine whether there is an upper bound, lower bound, or both. 

State the quantities contained in a need or requirement statement with ranges or limits with a degree of accuracy that is appropriate to the entity to which the need or requirement applies and against which the entity will be verified against. 

Care should be taken to avoid unspecified value ranges and ensure the quantities are expressed with tolerances or limits.  There are two reasons for this: 

- 1) Several requirements may have to be traded against each other, and providing tolerances or limits is a way of describing the trade-space.  Seldom is a quantity absolute.  A range of values is usually acceptable, providing different performance levels. 

- 2) Verification against a single absolute value is usually not feasible or at best very expensive and time consuming, whereas verification against a defined range of values with upper and lower limits makes verification more manageable. 

Care should also be taken to ensure the tolerances are no tighter than needed.  Tighter tolerances can drive costs both in system design and manufacturing as well as the costs in verifying the system can perform within the tighter tolerances. 

### Examples

**Unacceptable:** The Pumping_Station shall maintain the flow of water at 120 liters per second for 30 minutes. 

[This is unacceptable because we do not know whether a solution that addresses more or less than the specified quantities is acceptable.] 

**Acceptable:** The Pumping_Station shall maintain a flow of water at 120 ±10 liters per second for at least 30 minutes. 

[Now the range of acceptable flow performance is clear and that the 30 minutes is a minimum acceptable performance.] 
**Unacceptable:** The Flight_Information_System shall display the current altitude to approximately 1 meter resolution. 

[This is unacceptable because it is imprecise.  What is “approximately” in the context of a distance of 1 meter?  Who has the option of deciding what is “approximately”?  How will “approximately” be verified?  What is the acceptable tolerance?  Further, altitude is more commonly described in units of feet, not meters, so is +3 feet an acceptable equivalent to 1 meter since 3 feet is less than 1 meter? ] 

[Note that care must be taken to confirm both units and transformation from one set of units to another set to ensure accuracy, acceptability and consistency.  See also R6.] 

**Acceptable:** The Flight_Information_System shall display Current_Altitude with an accuracy of ±3 feet. 

[Note that “Current_Altitude” must be defined in the glossary since there are a number of possible interpretations of the term.] 

**Unacceptable:** The System shall limit arsenic contamination in the drinking water to allowable levels.  Rationale: Arsenic contamination in drinking water can cause health problems. 

[While “allowable” is acceptable in a need statement, it is unacceptable in a requirement statement because allowable is ambiguous - allowable by whom?  What specific concentration is allowable?  In what market?] 

**Unacceptable:** The System shall limit arsenic contamination in the drinking water to 1 part per trillion.  Rationale: Arsenic contamination in drinking water can cause health problems. 

[This is unacceptable because the EPA contamination limit in drinking water is 10 parts per billion.  Requiring a tighter limit may be beyond the ability of current technology to measure or if measuring concentrations of 1 part per trillion are possible, the cost to do so may be unacceptably high.  Also, no range is specified.  Using less than is probably the real intent.] 

**Acceptable:** The System shall limit arsenic contamination in the drinking water to less than10 parts per billion.  Rationale: EPA set the arsenic standard for drinking water at 10 ppb (or 0.010 parts per million).  The EPA has determined that concentrations of this level or less will protect consumers from the effects of long-term, chronic exposure to arsenic. 

### Characteristics that are established by this rule

- C3 - Unambiguous
- C4 - Complete
- C6 - Feasible
- C7 - Verifiable
- C8 - Correct
- C12 - Feasible
