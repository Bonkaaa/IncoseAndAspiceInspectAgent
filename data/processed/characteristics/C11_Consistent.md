---
id: C11
name: Consistent
type: characteristic
target_scope: set_of_statements
supporting_rules:
- R4
- R29
- R30
- R36
- R37
- R38
- R39
- R40
- R41
page: 48
---

### Definition

The set of needs contains individual needs that are unique, do not conflict with or overlap with other needs in the set, and the units and measurement systems they use are homogeneous.  The language used within the set of needs is consistent (i.e., the same words are used throughout the set to mean the same thing). 

The set of requirements contains individual requirements that are unique, do not conflict with or overlap with other requirements in the set, and the units and measurement systems they use are homogeneous.  The language used within the set of requirements is consistent (i.e., the same words are used throughout the set to mean the same thing) 

All terms used within the need and requirement statements are consistent with the architectural model, project glossary, and project data dictionary. 

### Rationale

Conflicting needs and requirements lead to an incomplete solution space, and, if not identified early in the development process, can lead to expensive rework. 

For the transformation to be formal, the resultant set of individual needs and requirements must not conflict and must be consistent with each other. 

Frequently, customer and other relevant stakeholder expectations or design constraints conflict with one another and need to be reconciled.  Additionally, even if individual needs or requirements are unambiguous, the inconsistent use of terms, abbreviations, units, and measurement systems in different requirements results in ambiguity in the requirement set. 
Needs and requirements that are inconsistent and conflicting with other requirements are not Correct (C8). 

Needs and requirements that are inconsistent and conflicting with other requirements also result in a set of needs or requirements that are not Feasible (C12), are not Comprehensible (C13), and that are not Able to be Validated (C14). 

Consistency in needs and requirements wording is greatly assisted using a centralized domain ontology, glossary, and data dictionary that is shared among all stakeholders. 

### Guidance

It is a challenge spotting conflicts between needs and requirements when the set of needs and requirements is large, as is often the case in today’s increasingly complex, software intensive systems. 

As discussed in the NRL and GtNR, it is important to identify needs and requirements that have relationships with other requirements, either directly or indirectly.  This is especially an issue when one need or requirement is changed without making a corresponding change to the other dependent need(s) or requirement(s). 

Concepts to help prevent this type of inconsistency is allocation, budgeting, and linking (trace) dependent requirements to each other.  When allocating and budgeting functionality, performance, or quality requirements to lower-level entities of the architecture, in many cases the resulting child requirements are dependent.  To ensure consistency throughout the development lifecycle, these dependent requirements need to be linked together to ensure consistency is maintained when changes occur. 

It can be difficult to identify conflicts merely through the language used to express individual need and requirement statements, but it can be made easier by classifying and grouping like needs and requirements together.  This can be facilitated through the use templates for organizing sets of needs and requirement.  Buy grouping like needs and requirements together, it will be easier to identify inconsistencies. 

See R41 for examples of use of types/categories of needs and requirements such as functional/performance, fit (operational), form (physical attributes), quality (-ilities), and compliance (regulations and standards). 

Another strategy is to have the need or requirement statement within a common type or category to follow the defined pattern defined for that type or category as discussed in Appendix C.  Using the pattern specific for a given type or category of need or requirement will aid in consistency. 

Another key tool is the use of diagrams and other models that show the relationships and dependencies within sets of needs and requirements as well as between needs and the resulting requirements.  Using a software tool, e.g., diagraming and modeling, to manage relationships and dependencies can help in identifying conflicts and manage these relationships and dependencies. 

Define an ontology for the project and use a glossary or data dictionary to ensure consistent use of terms and abbreviations throughout the need and requirement sets. 

Use an NLP/AI supplication to evaluate need and requirement statements within a set using the defied ontology, glossary, data dictionary, patterns, and templates to help establish consistency. Some applications of this type can be used as a digital assistant during the formulation of a need or requirement statement to both ensure the proper pattern or template for a given need or requirement type is used as well as help ensure consistent user of terminology. 
Pay special attention to interface requirements to make sure they are consistent with the interface requirements for other systems your SOI interacts with.  Ideally, both systems are managed within the same tool allowing interface requirements to be linked in applicable pairs, and traced to a common definition concerning the specific interaction addressed within the pair of interface requirements, e.g., ICD or data dictionary, 

Consistency within and between the sets of needs and requirements can be assessed during early system validation as well as during design validation activities discussed in the NRM and GtVV. 

### Rules that help establish this characteristic

- R4 - /Accuracy/UseDefinedTerms
- R29 - /Uniqueness/Classify
- R30 - /Uniqueness/ExpressOnce
- R36 - /UniformLanguage/UseConsistentTerms
- R37 - /UniformLanguage/DefineAcronyms
- R38 - /UniformLanguage/AvoidAbbreviations
- R39 - /UniformLanguage/StyleGuide
- R40 - /Modularity/RelatedRequirements
- R41 - /Modularity/Structured

### Attributes that help establish this characteristic

( Refer to the NRM Section 15.)

A32 - Trace to Interface Definition A33 - Trace to Dependent Peer Requirements 

### Activities and concepts associated with this characteristic

(Sections within the NRM)

3.2.2.1 – Analysis from Which Needs and Requirements are Derived; 3.2.2.3 – Consistency; 3.2.2.4 – Identify and Manage Interdependencies; 4.4.3 – Get Stakeholder Agreement; 4.5 – Lifecycle Concepts Analysis and Maturity; 4.5.3 – User of Diagrams and Models for Analysis; 4.5.7.1 – Model Development, Analysis, and Maturation; 4.8 – Baseline and Manage Lifecycle Concepts and Needs Definition Outputs; 5.1.2 – Perform Needs Verification; 6.2 – Perform Design Input Requirements Definition; 6.2.2 – Establish Traceability; 6.2.2.1 – Establishing Traceability Between Dependent Peer Requirements; 6.2.3.6 – Interface Requirements Audit; 6.2.6.2 – Completeness, Correctness, and Consistency; 6.3 – Baseline and Manage Design Input Requirements; 6.4.3 – Allocation – Flow Down of Requirements; 6.4.5 – Budgeting of Performance, Resource, and Quality Requirements; 6.4.7 - User of Traceability and Allocation to Manage Requirements; 7.1.2 – Perform Design Input Requirement Verification; 7.2.2 -Perform Design Input Requirements Validation; 8.1 – Design Definition Process Overview, 8.2 – Early System Verification and System Validation; 8.4 – Design Verification; 8.5 – Design Validation; 14.2.1 – Baseline Needs, Requirements, and Specifications; 14.2.4 - Managing Unknowns; 14.2.8 – Managing Interfaces
