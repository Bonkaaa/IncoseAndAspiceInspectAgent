---
id: C10
name: Complete
type: characteristic
target_scope: set_of_statements
supporting_rules:
- R3
- R29
- R40
- R41
page: 45
---

### Definition

The need or requirement set for a given SOI should stand alone such that it sufficiently describes the necessary capabilities, characteristics, functionality, performance, drivers, constraints, interactions, standards, regulations, and/or quality factors without requiring other sets of needs or requirements at the appropriate level of abstraction. 

### Rationale

If the formal derivation of needs from agreed-to lifecycle concepts results in individual needs that are necessary, the set of needs must be a sufficient representation of the lifecycle concepts and other sources from which they were derived—that is, all necessary needs have been included to implement the lifecycle concepts and other sources, and that all unnecessary needs have been excluded. 

If the formal transformation of needs, parent requirements, and other sources into requirements results in individual requirements that are necessary, the set of requirements must be a sufficient representation of the set of needs, parent requirements, and other sources for the entity from which it was transformed — that is, all necessary requirements have been included and all unnecessary requirements have been excluded. 

Necessity and sufficiency of the requirement set can only be determined with respect to the set of needs and other sources of requirements for the entity, and the set of parent requirements allocated to the entity. 

Complete must also address the possible conditions a system may experience, including anomalies.  Completeness therefore requires an additional analysis of all possible conditions to ensure that the required behavior for specific conditions is consistent with stakeholder needs. These are the kinds of requirements (“what if?”) that might not be addressed as part of initial analysis because the focus is on desired behavior under expected conditions.  These additional requirements derived from anomalous conditions may not arise until the system development is underway and represent risk in system development and difficulty in ensuring completeness. 
Unspecified anomalous conditions can be handled using an “else” statement in the requirements. However, the required behavior still needs to be validated by the stakeholders 

A set of needs or requirements is incomplete when there are needs or requirements missing. Missing needs or requirements can result in significant shortcomings in the delivered product pertaining to needed functionality/performance, robustness, quality, or conformance resulting in a failure to validate the SOI meets its intended use in the operational environment when operated by the intended users. 

A set of needs or requirements cannot be complete if any individual need or requirement is not complete (C4) or contains any unnecessary needs or requirements (C1). 

Unnecessary needs or requirements inappropriately constrain the available solution space and cause extra program expense for developing, managing, implementing, verifying the unnecessary requirements, and validating the unnecessary needs.  In the worst case, such unnecessary needs or requirements may over-constrain and compromise the overall SOI performance, leading to infeasible solutions which fail to satisfy necessary needs and resulting requirements.  Including unnecessary needs in the set may also result in a set of needs that is not Feasible (C12). 

### Guidance

The goal is to clearly communicate the needs for an SOI via a minimum set that are necessary and sufficient and no more and clearly communicate the design input requirements for an SOI via a minimum set that are necessary and sufficient and no more.  This applies no matter the level in the architecture the SOI exists. 

For each SOI, the integrated set of needs represents a complete definition of the stakeholder expectations, goals, objectives, lifecycle concepts, drivers, constraints, and risks to be mitigated whether explicitly stated or undocumented implicit expectations.  Addressing implicit stakeholder expectations is a key part of lifecycle concept and needs definition activities and transforming the resulting integrated set of needs into a set of design input requirements that when realized will result in a SOI that meets those needs, even if not originally stated. _Any implicit needs should be captured and included explicitly in the integrated set of needs.  It is the responsibility of those defining the integrated set of needs, to establish bi-directional traceability between each need and its source._ 

A complete requirements set represents a complete transformation of the needs for an SOI, both explicitly stated as needs and the implicit needs not documented (part of the transformation process).  Addressing implicit needs (and making them explicit) is a key part of requirements analysis defining the requirement set and deriving requirements that result in those needs being met, even if not originally stated as needs. _Note: This should not be an issue if the organization defined a complete integrated set of needs as described in the previous paragraph.  However, if this set of needs was not defined, then implicit needs could be an issue and will need to be considered when writing the requirement set.  It is the responsibility of those defining the set of requirements to establish bi-directional traceability between each design input requirement and the need or source the requirement is being transformed._ 

A complete requirements set also represents a complete transformation of higher-level requirements that were allocated to the SOI into a necessary and sufficient set of child requirements, that when implemented, will result in the intent of the allocated parent requirements being met.  It is the responsibility of owners of the allocated requirements to ensure these child requirements exist and the responsibility of the owners of the receiving SOI to 1) validate the allocations were correct, 2) develop the set of child requirements, 3) provide bi-directional 
traceability between the child requirements and their parent and 4) notify the owners of the higher-level SOI whenever a parent requirement is missing. 

As an example, a set of software requirements may not be complete because not all relevant child requirements may be considered by the software architect if hardware limitations (for example, bandwidth, reliability, latency) are ignored.  The hardware requirements and limitations may be missing or inconsistent with the assumed software architecture and software requirements.  Therefore, it is important to consider the macro system of which the software is a part and include hardware stakeholders that can be the source of these missing needs and requirements. 

Stakeholders are a primary source of requirements; leaving out a relevant stakeholder could result in missing or incorrect needs and the resulting requirements, resulting in expensive and time-consuming rework. 

With today’s increasingly complex, software-intensive systems it is almost impossible for a person or even a group of people to completely understand and manage every aspect of an SOI.  A key tool to help define and manage these complex systems is the use of diagrams and modeling to ensure what is needed is included and what is not needed is excluded. 

In the case of interactions across interface boundaries, the interface requirements need to refer to where the interaction between the SOI and other system is defined.  In the case of standards and regulations, reference should be made to the specific requirements that apply to the SOI, rather than the whole document. 

Completeness can be facilitated through traceability, allocation, and budgeting. 

Completeness of the sets of needs and requirements can be assessed during early system validation as well as during design validation activities discussed in the NRM and GtVV. 

Completeness of the sets of needs and requirements can also be facilitated through the use templates for organizing sets of needs and requirement.  Each organization will define types or categories in which a need or requirement fits, based on how they may wish to organize the requirements.  Organizing by type/category is useful because it allows the stakeholders to view the sets of needs and requirements from a variety of perspectives.  Each of these perspectives represents unique needs and requirements.  Completeness can be aided by addressing each perspective.   See R41 for examples of use of types/categories of needs and requirements such as functional/performance, fit (operational), form (physical attributes), quality (-ilities), and compliance (regulations and standards). 

Refer also to the NRM and GtNR for additional guidance concerning completeness of sets of needs and requirements. 
### Rules that help establish this characteristic

- R3 - /Accuracy/SubjectVerb
- R29 - /Uniqueness/Classify
- R40 - /Modularity/Related
- R41 - /Modularity/Structured

### Attributes that help establish this characteristic

(_ Refer to the NRM Section 15.) A2- Trace to Parent A4 - States and Modes A40 - Type/Category
### Activities and concepts associated with this characteristic

(Sections within the NRM)

3.2.2.1 – Analysis from Which Needs and Requirements are Derived; 3.2.2.2 – Completeness; Identify and Manage Interdependencies; 4.3.3 – Identify External and Internal Stakeholders; 4.4.3 – Get Stakeholder Agreement; 4.4.4 – Completeness; 4.5.3 – User of Diagrams and Models for Analysis; 4.5.7.1 – Model Development, Analysis, and Maturation; 4.6.2.3 – Organizing the Intergrade Set of Needs; 4.6.3.3 – Completeness of the Integrated Set of Needs; 4.8 – Baseline and Manage Lifecycle Concepts and Needs Definition Outputs; 5.1.2 – Perform Needs Verification; 5.2.2 – Perform Needs Validation; 6.2 – Perform Design Input Requirements Definition; 6.2.1 – Transforming Needs into Design Input Requirements; 6.2.1.1 – Organizing the Sets of Design Input Requirements; 6.2.1.2 – Considerations for Each Type of Requirement; 6.2.2 – Establish Traceability; 6.2.3.6 – Interface Requirements Audit; 6.2.6.2 – Completeness, Correctness, and Consistency; 6.3 – Baseline and Manage Design Input Requirements; 6.4.3 – Allocation – Flow Down of Requirements; 6.4.4 -  Defining Child Requirements that Meet the Intent of the Allocated Parents; 6.4.5 – Budgeting of Performance, Resource, and Quality Requirements; 6.4.7 – Use of Traceability and Allocation to Manage Requirements; 7.1.2 – Perform Design Input Requirements Verification; 7.2.2 – Perform Design Input Requirements Validation; 8.1 – Design Definition Process Overview, 8.2 – Early System Verification and System Validation; 8.5 – Design Validation, 14.2.1 – Baseline Needs, Requirements, and Specifications; 14.2.7 – Combine Allocation and Traceability to Manage Requirements; 14.2.8 – Managing Interfaces.
