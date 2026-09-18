---
id: C14
name: AbleToBeValidated
type: characteristic
target_scope: set_of_statements
supporting_rules:
- R3
- R4
- R36
- R37
- R38
- R39
- R41
page: 54
---

### Definition

It must be able to be validated that the integrated set of needs will lead to the achievement of the product goals and objectives, stakeholder expectations, risks, and lifecycle concepts within the constraints (such as cost, schedule, technical, legal and regulatory compliance) with acceptable risk. 

It must be able to be validated that the set of requirements will lead to the achievement of the integrated set of needs and higher-level requirements within the constraints (such as cost, schedule, technical, and regulatory compliance) with acceptable risk. 

### Rationale

Referring to Figure 5, the transformation of lifecycle concepts into the integrated set of needs and transformation of the integrated set of needs into the sets of design input requirements must be formal and able to be validated, not just for individual needs and requirements, but also for the sets of needs and requirements.  It must be able to be shown at any lifecycle stage that achievement of the set of needs will result in the lifecycle concepts from which they were transformed and the achievement of the set of requirements will result in meeting the set of needs from which they were transformed. 
For a set of needs or requirements to be able to be validated, the set must be Complete (C10), Consistent (C11), Feasible (C12), and Comprehensible (C13).  Refer to the NRM and GtVV for more details on validating sets of needs and sets of requirements. 

Design validation is making sure the transformation of the design input requirements into the design and resulting design output specifications will result in a system that meets its intended purpose/use in its operational environment as defined by the integrated set of needs.  Thus, design validation goes back to the needs to make sure they have been met—as a set. 

System validation is making sure the built and verified system meets its intended purpose/use in its operational environment when operated by its intended users and does not enable unintended users to use the system in an unintended way.  Thus, system validation goes back to the integrated set of needs to make sure they have been met—as a set.  Refer to the NRM and GtVV for more details on design and system validation. 

### Guidance

The system lifecycle operational scenarios, concepts, and use cases—from which the needs were transformed, and the requirements were transformed—can be used as test cases to validate the sets of needs, sets of requirements, the design, and built or coded SOI. 

In other words, the needs can be validated to meet the lifecycle concepts from which they were derived, and the requirements can be validated to meet the needs by running tests based on the use cases or operational scenarios developed during lifecycle concept and needs definition activities discussed in the NRM and GtNR.  Doing so will result in evidence that the intended use, goals, objectives and stakeholder expectations have been met within the agreed-to drivers and constraints with acceptable risk. 

For the set of needs, ask the questions: “Do the needs and set of needs clearly and correctly communicate the agreed-to lifecycle concepts, drivers, constraints, risks, and stakeholder expectations?” or “Have we correctly and completely captured the needs the system must address?  For the set of requirements ask the questions: “Will the entity developed by this set of requirements satisfy the needs?” “Are we building the right thing?” 

These questions concerning the sets of needs and requirements are a major focus during early system validation as well as during design validation activities discussed in the NRM and GtVV. 
### Rules that help establish this characteristic

- R3 - /Accuracy/SubjectVerb
- R4 - /Accuracy/UseDefinedTerms
- R36 - /UniformLanguage/UseConsistentTerms
- R37 - /UniformLanguage/DefineAcronyms
- R38 - /UniformLanguage/AvoidAbbreviations
- R39 - /UniformLanguage/StyleGuide
- R41 - /Modularity/Structured

### Activities and concepts associated with this characteristic

(Sections within the NRM) 3.2.1.1 – Communication; 3.2.1.2 – Power of Expression; 3.2.1.6 – Formal, Binding Agreement; 3.2.1.7 – System Verification and System Validation; 3.2.2.1 – Analysis from Which Needs and Requirements ae Derived; 3.2.2.2 – Completeness; 3.2.2.3 – Consistency; 3.2.2.4 – Identity and Manage Interdependencies; 3.2.2.5 – Support Simulations; 3.2.2.6 – Key to Understanding; 4.4.3
– Get Stakeholder Agreement; 4.7 – Plan for System Validation; 4.8 – Baseline and Manage Lifecycle Concepts and Needs Definition Outputs; 5.1.2 – Perform Needs Verification; 5.2 – Needs Validation; 5.2.2 – Perform Needs Validation; 6.2 – Perform Design Input requirements Definition; 6.2.3.6 – Interface Requirements Audit; 6.3 – Baseline and Manage Design Input Requirements; 6.4.7 – Use of Traceability and Allocation to Manage Requirements; 7.1.2 – Perform Design Input Requirements Verification; 7.2 – Design Input Requirements Validation; 7.2.2 – Perform Design Input Requirements Validation; 8.1 – Design Definition Process Overview, 8.2 – Early System Verification and System Validation; 8.5 – Design Validation, 14.2.1 – Baseline Needs, Requirements, and Specifications; 14.2.7 – Combine Allocation and Traceability to Manage Requirements; 14.2.8 – Manage Interfaces, 14.2.9 – Managing System Verification and System Validation.
