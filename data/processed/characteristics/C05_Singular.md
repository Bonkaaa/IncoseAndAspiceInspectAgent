---
id: C5
name: Singular
type: characteristic
target_scope: individual_statement
supporting_rules:
- R9
- R18
- R19
- R20
- R21
- R22
- R23
- R39
page: 35
---

### Definition

The stakeholder need or requirement statement should state a single capability, characteristic, constraint, or quality factor. 

### Rationale

The formal transformation from a lifecycle concept to a need can be a many-to-one, one-to-one or a one-to-many transformation, however, the resultant need statement(s) must each represent a single thought, aspect or expectation. 

Similarly, the formal transformation from a need, source, or allocated parent requirement to a requirement can be a many-to-one, one-to-one, or a one-to-many transformation so the resultant requirement statement(s) must each represent a single thought, aspect or expectation. 

The effectiveness of several process activities associated with needs and requirements definition, such as decomposition, derivation, allocation, traceability, verification, and validation, depends on being able to identify singular statements.  For instance, the system verification information defined for a requirement can be far more precise when that requirement addresses a single capability, characteristic, constraint, or quality factor.  A need or requirement with multiple thoughts is difficult to allocate and to trace to a parent or source. 

A nonsingular need or requirement is neither Verifiable (C7) nor Correct (C8). 

Requirements patterns are useful ways to ensure singularity (see Appendix C). 

### Guidance

Keep the need or requirement statement limited to one quality, characteristic, capability, function, or constraint.  Understand how the statements fit into the allocation and traceability philosophy for the project. 

Use the project standard patterns for writing needs and requirements. 

Although a single need or requirement should consist of a single function, quality or constraint, it may have multiple conditions under which the requirement is to be met. 

Avoid the use of the word “and”, R19, when it ties together multiple thoughts (phrases in the sentence), each of which may be allocated and verified differently.  The presence of the conjunction “and” in a need or requirement statement should always prompt the writer to consider whether or not the statement is singular. 

There are exceptions to the use of “and”.  Some organizations allow the use of “and” to join two actions that will always be allocated, traced, and verified together.  For example, there may be a 
requirement for a lit match to be extinguished and disposed into a container.  Given that these two actions need to always be performed together (you would never do one action without the other), organizations may allow both actions to be communicated within a single requirement.  In that case, however, it would be best to combine the two actions with a logical “AND”—see R15. 

### Rules that help establish this characteristic

- R9 - /Accuracy/NoOpenEnded
- R18 - /Singularity/SingleSentence
- R19 - /Singularity/AvoidCombinators
- R20 - /Singularity/AvoidPurpose
- R21 - /Singularity/AvoidParentheses
- R22 - /Singularity/Enumeration
- R23 - /Singularity/Context
- R39 - /UniformLanguage/StyleGuide
