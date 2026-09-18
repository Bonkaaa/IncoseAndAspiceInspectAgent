---
id: R31
name: SolutionFree
type: rule
page: 88
target_scope: individual_statement
established_characteristics:
- C2
related_rules: []
---

## **4.9.1 R31 - /ABSTRACTION/SOLUTIONFREE**

**When defining design inputs avoid stating a solution unless there is rationale for constraining the design.**

### Elaboration

Refer to Section 1.7 concerning the differences between needs and requirements. 

As design inputs, every system endeavor should have a level of needs and requirements for an entity that captures the problem to be solved (design inputs) without including solutions (design 
outputs).  System level needs and requirements should provide a system-level requirement for the overall problem to be addressed by design.  The first level of architecture may be laid out, but subsystems are considered as black boxes to be elaborated as the project team moves down levels of the architecture.  See the NRM concerning levels and moving between levels. 

When reviewing a requirement that states a solution, ask “for what purpose?  The answer will reveal the real requirement.  (Notice that this question is subtly different from simply asking "Why?” and encourages a teleological rather than causal response.) Understanding the concepts of design inputs versus design outputs allows you to ask the question: “Is this requirement addressing what the system needs to do versus how the system needs to do it”?  The answer to these questions has the potential to help do three things: 

1. Rephrase the requirement in terms of the problem being solved. 

2. Determine if the requirement is at the right level. 

3. Identify which design input requirement(s) or need(s) the design output requirement is addressing or whether the design input requirement is missing. 

Often when rationale is provided with requirements that state a solution (design output), the rationale often answers the “for what purpose?” question, and thus the real (and often missing) design input requirement may be extracted from the rationale. 

### Examples

General: For a medical diagnostic system 

- Stakeholders need statement: “The stakeholders need the diagnostic system to measure [something] with an accuracy as good as or better than similar devices in the market.” [This is an appropriate level of abstraction for a stakeholder need statement, clearly stating the expectation the stakeholders have concerning accuracy, however this would not be a good design input requirement.] 

- Requirement transformed from the stakeholder need statement: “The diagnostic system shall measure [something] with an accuracy of [xxxxx].” 

- [The developers have explored various concepts for meeting the need for accuracy, have examined candidate technologies, have accessed their maturity (technology readiness level (TRL), and have decided that the value [xxxxxxx] is feasible with acceptable risk for this lifecycle stage.  As stated, this is an appropriate level of detail for a design input requirement.] 

This system level design input accuracy requirement is then allocated to the key parts of the system that have a role in meeting the overall system accuracy requirement.  For a medical diagnostic system this could include allocations to the hardware (instrument), assay (biological sample), and software.  These allocations could then be further sub-allocated within the hardware, assay, and software lower-level entities. 

As long as the requirements are written on the accuracy allocation and not how that accuracy will be obtained by one of the architectural entities, the requirements are design input requirements.  As soon as specific hardware components are named (laser, LEDs emitting light at a specific wavelength, optical system components, specific magnifications, algorithms, formulations, etc.,) then the requirements are reflecting design outputs and need to be communicated within deign output artifacts (specifications). 
**Unacceptable:** Traffic lights shall be used to control pedestrian traffic at the intersection. [This is unacceptable because “Traffic lights” are a solution (design output).  Why are traffic lights needed? This requirement is also written in passive voice – see R2] 

**Acceptable:** (several requirements): 

The Traffic_Control_System shall signal “Walk” when the Pedestrian is permitted to cross the road at the Intersection. 

The Traffic_Control_System shall limit the Wait_Time of Vehicles traversing the Intersection to less than Maximum_Daylight_Wait_Time_Value during Normal_Daytime traffic conditions. [Note that glossary definitions should be used for Traffic_Control_System, Maximum_Daylight_Wait_Time_Value, Normal_Daytime , Vehicles, and Intersection.] 

**Unacceptable:** By pressing a button on the traffic-light pillar, the pedestrian signals his presence, and the light turns red for the traffic to stop. 

- [This is unacceptable because this requirement contains solution-biased detail – design output. In addition, the requirement is unacceptable because the subject is the user over which we have no control—that is, we cannot tell the user what to do in a requirement statement for the system being developed.] 

**Acceptable:** The Traffic_Control_System shall allow the Pedestrian to signal intent to cross the road at the Intersection. 

[This requirement allows freedom in determining the best solution (design input), which may be a means of automatic detection rather than button pushing.] 

- [Note that glossary definitions should be used for “Pedestrian”, “Traffic_Control_System”, and Intersection.] 

### Exceptions and relationships

Sometimes solutions have to be described in requirements, even if it is very detailed for a given level, for example if the airworthiness authorities require the use of a specific template for a certain report; or if a naval customer requires that the new naval vessel be equipped with a specific weapon system from a specific supplier; or, if all vehicles in a fleet are required to use the same fuel or the next model make use of a particular engine. In these cases, it is not a premature solution, but a real stakeholder or customer need concerning a constraint.  As such this is acceptable as a design input. 

However, as a rule, if a detailed, specific design solution is expressed as a design input without proper justification, it may be a premature solution and should be communicated as a design output and an appropriate set of design input needs and associated requirements developed that communicate “For what purpose?” which the design output requirements can be traced to. 
### Examples

of issues concerning design outputs expressed as design inputs include:

1. The project is developing an upgrade to an existing system (brownfield SE).  Rather than documenting design input “what” requirements, the project team focuses on known solutions and implementations and documenting design output level requirements as design inputs. This is problematic in that the real “for what purpose?” question is not being addressed and the real design input requirements are not communicated. 

2. A similar case exists when procuring a commercial off the shelf (COTS) solution and communicating the requirements for that solution as design input requirements rather than in a design output specification.  Again, this is problematic in that the real “for what 
purpose?” question is not being addressed and the real design input requirements are not communicated. 

3. A common issue is when an existing system or COTS exists, yet the project develops and documents as design inputs a detailed design output level set of requirements (design output specification) for the system rather than a set of design input set of “what” requirements that would guide the selection of an appropriate COTS.  This can result in a redundant set of requirements that are not necessary, will have to be verified – adding additional cost to the project, yet not addressing the “for what purpose?” design input requirement set that should drive the selection of the specific COTS.  Refer to the NRM for a detailed discussion the use of OTC and COTS entities. 

4. As part of the lifecycle concept analysis and maturation activities a prototype was developed to access feasibility.  The resulting needs and resulting requirements are based on the prototype and an associated trade study that resulted a specific solution that meets the needs of the stakeholders.  Rather than communicating the design input requirements, the design output requirements for the prototype are included in the design input set of requirements while not addressing the “for what purpose?” design input requirement set that would drive the design for the prototype. 

### Characteristics that are established by this rule

- C2 - Appropriate
