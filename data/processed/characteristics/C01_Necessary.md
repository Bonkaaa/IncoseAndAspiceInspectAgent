---
id: C1
name: Necessary
type: characteristic
target_scope: individual_statement
supporting_rules:
- R20
- R30
page: 26
---

### Definition

The need or requirement statement defines an essential capability, characteristic, constraint, or quality factor needed to satisfy a lifecycle concept, need, source, or parent requirement.  If it is not included in the set of needs and requirements, a deficiency in capability or characteristic will exist which cannot be fulfilled by implementing other needs or requirements in the set. 

### Rationale

The formal transformation of a need from a lifecycle concept must result in a need addressing a specific aspect of the lifecycle concept that is necessary in order to meet the goals, objectives, stakeholder expectations, drivers, constraints, risks that are included in the lifecycle concepts. 

Each need, individually or in combination with other needs in the set, must be sufficient to satisfy the intent of a specific aspect of the of the lifecycle concept or other source from which it was derived.  “Sufficient” both encompasses the characteristic “Correct” (C8) and enhances it to 
ensure it is not only an “accurate representation of the specific aspect of the of the lifecycle concept or other source but is sufficient to ensure the specific aspect of the of the lifecycle concept or other source will be satisfied when the SOI realizes the needs. 

The transformation of a need into a one or more requirements must result in a set of requirements that where each is necessary, and the set is sufficient in order to meet a need or set of needs for the entity from which it was transformed. 

Each requirement, individually or in combination with other requirements in the set, must be sufficient to satisfy a specific stakeholder need, source, or parent requirement. 

A requirement is considered sufficient if it, along with any siblings (common children of a single parent requirement), satisfies its parent requirement with acceptable margin (as determined by the program/project).  For example, if the parent is a functional/performance requirement, compliance with the required functionality and performance level described by the set of sibling requirements should ensure conformance to the parent requirement by the integrated product. Sufficient both encompasses the characteristic “Correct” (C8) and enhances it to ensure it is not only an “accurate representation of the entity need but is sufficient to ensure the need is satisfied by the child requirement when the SOI fulfills the requirements. 

The development of child requirements via either decomposition or derivation must result in a set of child requirements that are necessary and sufficient in order to meet the intent of the need or source from which it is transformed or the allocated parent requirement the child is being developed in response to.  Members of the set of child requirements can exist in different system element sets of requirements which the parent requirement was allocated to.  In many cases these child requirements have a dependency, where a change in one could require a change in one or more of the others.  This is true when the child requirements are in response to a budgeted quantity (performance or quality characteristic) as well as interface requirements.  It is important to link these dependent child requirements together.  Refer to the NRM Section 6 concerning allocation/budgeting and interface requirements. 

Realization of every need and requirement requires resources, effort, and cost in the form of development, review, management, implementation, design verification, design validation, system verification, system validation, and maintenance.  Unnecessary needs and requirements can lead to non-value-added work, additional cost, and unnecessary risk.  Only necessary needs and the resulting requirements should therefore be included in the need and requirement sets.  Once each need and requirement is proven to be necessary, the set of needs must then be a sufficient solution for the agreed-to lifecycle concepts and requirements must then be a sufficient solution to the set of needs.  Together, the sets of needs and requirements form the design inputs to which the design outputs will be verified and validated against. 

### Guidance

There is no such thing as a “self-derived” need or requirement!  A need must be traced to a lifecycle concept, driver or constraint, system need, or mission statement, goal, objective, risk, trade study or stakeholder expectation defined during lifecycle concept and needs definition activities discussed in the NRM and GtNR. 

A requirement must be traced to a need, parent, or source which could be one or more need(s) or higher-level allocated parent requirement(s)), lifecycle concept, driver, constraint, or risk. 

A need or requirement is not necessary (not needed in the set of needs or requirements) if: 

- the need or requirement can be removed, and the remaining set will still result in the entity lifecycle concept or needs being satisfied; 
- the intent of the need or requirement will be met by the implementation of other needs or requirements; 

- the need or requirement cannot be traced back to a source, need, or parent requirement; or 

- the author cannot communicate a valid reason (rationale) for the need or requirement. 

One approach used by some organizations to limit the number of design input requirements is to take a “zero based” or “minimum viable product (MVP)” approach.  Start by only including needs and requirements that are high priority and are critical or essential for an MVP.  Then only add additional requirements that add value by reviewing each proposed need and requirement against the mission, goals, and objectives as well as drivers, constraints, risks, lifecycle concepts, and scenarios defined for the entity.  If the need or requirement cannot be traced to one or more needs, parent requirement, or one of these sources, it is not necessary.  The inclusion of rationale and other attributes defined in the NRM, Section 15, such as trace to source or parent, for each need and requirement also aids in communicating the necessity and intent of the need or requirement. 

Caution: When developing child requirements in response to a need or an allocated parent or source, the set of child requirement must be limited to only those that can be proven to be necessary and sufficient to meet the intent of the need, parent, or source to which they are traced and not include any unnecessary requirements.  Avoid gold plating and needs and requirements creep.   Refer to the NRM, Sections 4.6.3.4 and 6.2.6.3 for advice on avoiding gold plating and Section 14.2.51 on managing needs and requirements creep. 

For market focused product development, many companies will aim to elicit as much information as possible from stakeholders to help define the product being built.  A process of needs and requirements analysis is used where they are considered based on their prevalence, urgency, and the value realized by satisfying that need or requirement.  Through the process of product management, a market can be defined consisting of stakeholders with similar product needs.  At this point, a decision can be made on which needs and requirements to include as necessary to satisfy the market needs. 
### Rules that help establish this characteristic

- R20 - /Singularity/AvoidPurpose
- R30 - /Uniqueness/ExpressOnce

### Attributes that help establish this characteristic

(Refer to the NRM Section 15.)

A1 - Rationale 

A2 - Trace to Parent 

A3 - Trace to Source 

A32 – Trace to Interface Definition 

A33 - Trace to Dependent Peer Requirements 

A34 – Priority 

A35 – Criticality or Essentiality 
### Activities and concepts associated with this characteristic

(Sections within the NRM)

3.2.1.5 – Attributes; 3.2.1.6 – Attributes; 3.2.2.1 – Analysis From Which Needs and Requirements Are Derived; 4.4.3 – Get Stakeholder Agreement; 4.5 – Lifecycle Concepts Analysis and Maturation; 4.5.3 – User of Diagrams and Models for Analysis; 4.5.7.1 – Model Development, Analysis, and Maturation; 4.6.3.4 – Needs Feasibility and Risk; 4.8 – Baseline and Manage 
Lifecycle Concepts and Needs Definition Outputs; 5.1.2 – Perform Needs Verification; 6.2 – Perform Design Input Requirements Definition; 6.2.1 – Transforming Needs into Design Input Requirements; 6.2.2 – Establish Traceability; 6.2.3.6 – Interface Requirements Audit;  6.2.6.3 – Requirements Feasibility And Risk; 6.3 – Baseline and Manage Design Input Requirements; 6.4.7 – Use of Traceability and Allocation to Manage Requirements; 7.1.2 – Perform Design Input Requirement Verification; 7.2.2 – Perform  Design Inputs Requirement Validation; 14.2.1 – Baseline Needs, Requirements, and Specifications; 14.2.7 – Combine Allocation and Traceability to Manage Requirements;
