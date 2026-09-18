---
id: R15
name: LogicalCondition
type: rule
page: 72
target_scope: individual_statement
established_characteristics:
- C3
- C7
related_rules: []
---

## **4.3.4 R15 - /NONAMBIGUITY/LOGICALCONDITION**

**Use a defined convention to express logical expressions.**

### Elaboration

Define a convention for logical expressions such as “[X AND Y]”, “[X OR Y]”, [X XOR Y]”, “NOT [X OR Y]”. 

As with the other rules and characteristics, we want to keep requirement statements as one thought with singular statements.  Thus, we avoid using “and” when it involves tying two thoughts together.  However, it is acceptable to use “AND”, “OR”, “XOR”, and “NOT” in a logical sense 
when talking about conditions to which the verb applies.  All logical expressions decompose to either “true” or “false”, resulting in a singular statement. 
### Examples

of conventions:

1. Place conjunctions in italics or in all capitals (AND, OR, XOR, NOT) to indicate that the author intends the conjunction to play a role in a condition. 

2. Place conditions within square brackets, also using the brackets to control their scope. For example, “[X AND Y].” 

Further, use of “and/or” is non-specific and therefore ambiguous.  The most common interpretation of the expression “and/or” is as an inclusive OR: either X OR Y OR both.  If an inclusive OR is intended, that should be written as “at least one of <the two or more requirements>”.  If an Exclusive OR is intended, that should be written as “Either <Requirement 1> OR <Requirement 2> but NOT both”, or similar wording. 

Note that caution should be used when including logical expressions in design input requirements.  In many cases the use of logical expressions is more appropriate to design output specifications/requirements.  Input requirements should focus on why the logical actions are needed – prevent something bad from happening, for example, 

The use of logical expressions within design input requirements is appropriate when stating “under what conditions” apply to a need or requirement.  For example, an action that must take place based on whether at logical condition is true or false. 

Also see R19 and R20. 

### Examples

**Unacceptable:** The Engine_Management_System shall disengage the Speed_Control_Subsystem when the Cruise_Control is engaged and the Driver applies the Accelerator. 

[This is unacceptable because of the ambiguity of “and” could be confused with combining two separate thoughts.  Instead use the form of a logical expression [X AND Y].] 

**Acceptable:** The Engine_Management_System shall disengage the Speed_Control_Subsystem, when [the Cruise_Control is engaged AND the Driver applies the Accelerator]. 

### Exceptions and relationships

While R21: /Singularity/AvoidParentheses states that parentheses or brackets are to be avoided within general sentence structure, this rule suggests that brackets may be used as part of a convention to avoid ambiguity when expressing a logical expression. 

### Characteristics that are established by this rule

- C3 - Unambiguous
- C7 - Verifiable
