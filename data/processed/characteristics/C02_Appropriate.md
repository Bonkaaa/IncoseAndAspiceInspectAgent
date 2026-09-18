---
id: C2
name: Appropriate
type: characteristic
target_scope: individual_statement
supporting_rules:
- R2
- R3
- R31
page: 29
---

### Definition

The specific intent and amount of detail of the need or requirement statement is appropriate to the level (the level of abstraction, organization, or system architecture) of the entity to which it refers. 

### Rationale

Level of abstraction refers to the level of detail and specificity of the information being communicated within a need or requirement statement. 

The wording of needs is often stated at a higher level of abstraction than is appropriate for a requirement. _See the example under R31, Abstraction/SolutionFree_ . 

Levels can also refer to levels within an organization or levels within an architecture – system, subsystems, or system elements.  Needs and requirements may be defined at any level of the organization or system architecture; however, as a rule, a need or requirement should be expressed at the level of the entity to which it refers.  Design input, design-to “what” requirements should state what needs to be stated for that level of the entity, not “how” the requirement should be met via design.  However, design output, build-to/code-to “how” requirements purpose is to communicate to the builders/coders the agreed-to design, so they will reflect implementation. 

To avoid confusion, many organizations refer to design output requirements as “specifications” that often include parts lists, drawings, wiring diagrams, plumbing diagrams, labeling diagrams and requirements, logic diagrams, algorithms, Computer-aided Design (CAD) files, or STL files (for 3D printing). **_For the purposes of this Guide, the focus is on design input needs and requirements as shown in Figure 4_** . 

A need or requirement stated at the wrong level for an entity is either not correct or may not be verifiable nor able to be validated at that level. 

Refer to the NRM for an in-depth discussion on levels. 

### Guidance

Refer to Section 1.6 for a discussion concerning needs and requirements and the entity to which they apply.  Refer to Section 1.7 concerning the differences between needs and requirements. 

Design input requirements must not be any more detailed or specific than is necessary for the level of the entity at which they are stated.  In particular, the entity for which the requirement applies needs to be appropriate to the level of organization or architecture in which the entity lives.  Unless there is a good reason, a requirement subject/noun should refer to the entity at the level the requirement is being expressed (not higher or lower). 
The design input requirements avoid placing unnecessary constraints on the design at the given level.  The goal for design input requirements is to be implementation independent.  There may be cases where there is good rationale for stating implementation.  When this happens, the rationale must be included to make it clear why the specific implementation needs to be stated as a constraint to the design. 

A useful question to ask of a requirement is “for what purpose?” or “why?” If the requirement is expressed in implementation terms (design output), the answer to this question may be the real requirement (design input). 

Needs and requirements should be stated for an entity at the level of integration at which system verification and system validation will be performed to verify the entity meets that requirement. 

Requirements for lower-level entities stated within the requirements set for a higher-level entity may seem like implementation.  I n this case, the real higher-level entity requirement may not be stated and thus not properly allocated to the next lower-level entities.  When this is the case, the requirement should be moved down to the appropriate level entity set of requirements and the missing parent requirement added to the higher-level entity’s set of requirements.  Conversely, higher level entity requirements stated improperly within a lower-level entity’s set of requirements can be problematic because they may not have been allocated properly to the other entities at the next level of the architecture, resulting in missing requirements for those entities. 

If the requirement is valid but stated at a lower or higher-level entity, determine what the appropriate level entity is and document the requirement for that level entity. 

It is good practice, once the next level entity requirements are written, for the project team to do a “leveling” exercise, where they look at each requirement for the entity and determine whether or not it is at the appropriate level or should be moved down to a lower-level entity’s set of requirements or moved up to a higher-level entity’s set of requirements. 

### Rules that help establish this characteristic

- R2 - /Accuracy/UseActiveVoice
- R3 - /Accuracy/SubjectVerb
- R31 - /Abstraction/SolutionFree

### Activities and concepts associated with this characteristic

(Sections within the NRM)

4.5.4 – Levels of Detail and Abstraction; 4.6.3.2 – Appropriate to Level; 4.6.3.4 – Needs Feasibility and Risk; 6.2 – Perform Design Input Requirements Definition; 6.2.1 – Transforming Needs into Design Input Requirements; 6.2.1.4 – Appropriate to Level; 6.2.6.3 – Requirements Feasibility and Risk; 6.4.3 – Allocation – Flow Down of Requirements.
