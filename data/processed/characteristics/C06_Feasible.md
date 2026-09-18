---
id: C6
name: Feasible
type: characteristic
target_scope: individual_statement
supporting_rules:
- R26
- R33
page: 36
---

### Definition

The need or requirement can be realized within entity constraints (for example: cost, schedule, technical, legal, ethical, safety) with acceptable risk. 

### Rationale

There is little point in agreeing to an obligation for a need or requirement that is not feasible. Agreeing to a need or requirement that cannot be realized with acceptable risk within constraints often results in project cost overruns and schedule slips.  Inherently unachievable needs and requirements, such as 100% reliability, are at best a waste of time, and at worst lead to needlessly expensive solutions. 

An infeasible need or requirement cannot be satisfied because 

- a. it breaks the laws of physics, 

- b. it violates laws or regulations in an applicable jurisdiction, 

- c. it conflicts with another requirement and cannot be concurrently satisfied, or 

- d. it leads to excessive program risk because of technical immaturity or inadequate margin with respect to program cost and schedule as a function of lifecycle phase. 

An infeasible need or requirement is neither verifiable (C7) nor correct (C8). 

### Guidance

The need or requirement is considered feasible if, when considered along with other needs or requirements for a single system element (i.e., a set of entity needs or requirements), it does not cause an unacceptable cost, schedule or risk impact during the entity’s lifecycle 

Feasible implies the existence of a possible feasible solution to satisfying a requirement.  As stated in the definitions for needs and requirements, requirements are transformed from needs. With this in mind, if the organization has not defined a feasible set of lifecycle concepts and assessed the maturity of the critical technologies, then the needs derived from those concepts may not be feasible nor will be the requirements transformed from those needs. 
Therefore, in most cases determining whether the need or requirement is feasible is difficult without an underlying assessment and analysis of the proposed lifecycle concepts from which the needs are derived, and requirements transformed.  Before allowing a need into your set, an assessment of the feasibility of the chosen lifecycle concepts must be made in terms of the drivers and constraints including the maturity of critical technologies, cost, schedule, resources, regulations, higher level requirements, and risk.  If not feasible within the stated constraints with acceptable risk, the need and resulting requirement should not be included in the set.  Doing so can negatively impact cost and schedule and can result in a requirement that will not be met and verified. 

A useful tool for assessing risk is the use of Technology Readiness Levels (TRLs) to determine and compute the maturity of a critical technology—a lower TRL represents more risk to the project than a higher TRL.  As discussed in the NRM, as part of risk assessment and during lifecycle concept analysis and maturation critical technologies are identified, their TRL and Advancement Degree of Difficulty (AD<sup>2</sup> ) is assessed, and a technology maturation plan is developed that will result in the critical technology maturity to advance such that it will be feasible in time to meet the system development schedule.  These activities represent a risk to the project and as such this risk must be managed closely. 

Other useful tools include modeling and prototyping to evaluate the feasibility of individual needs and requirements and subsets of needs and requirements.  This means that the design team must be included in an integrated, multidiscipline, collaborative team responsible for the lifecycle concept and needs definition activities to assess the feasibility of a lifecycle concept in terms of physical implementation of the functional or conceptual model as discussed in the NRM and GtNR. 

In some cases, we can recognize and avoid needs and requirements that are clearly impossible or unrealistic (see R26).  The need or requirement is inherently infeasible where the requirement is either internally contradictory or it violates the laws of physics.  More often, feasibility must be examined for sets of needs or requirements associated with a single entity to ensure there is no conflict in the set of requirements (C12). 

The measurement of feasibility is not always easy to assess.  Measurement of feasibility is based on the degree of risk in successfully implementing the requirement within program constraints, unless precluded by physics (cannot be done, period) or requirements conflict.  As stated above, TRLs can be a useful measure of risk for requirements dependent on the maturity of an essential technology. 

Feasibility of individual need and requirement statements can also be assessed during early system verification and design verification activities discussed in the NRM and GtVV. 
### Rules that help establish this characteristic

- R26 - /Realism/AvoidAbsolutes
- R33 - /Tolerance/ValueRange

### Attributes that help establish this characteristic

( Refer to the NRM Section 15.)_ A6 - System Verification or System Success Criteria A8 - System Verification or System Validation Method A26 – Stability/Volatility A36 - Risk (of implementation) A38- Key Driving Need or Requirement (KDN/KDR)
### Activities and concepts associated with this characteristic

(Sections within the NRM)

3.2.1.6 – Formal, Binding Agreement; 3.2.2.1 – Analysis From Which Needs And Requirements Are Derived; 4.3.6.2 – Technology Maturity; 4.3.7.1 – Classes of Risk - Development Risk; 4.5 – Lifecycle Concepts Analysis And Maturation; 4.5.1 – Feasibility; 4.5.7.4 – Zeroing in on a Feasible Architecture and Design; 4.6.3.1 – Managing Unknowns; 4.6.3.4 – Needs Feasibility and Risk; 4.8 – Baseline and Manage Lifecycle Concepts and Needs Definition Outputs; 5.2.2 – Perform Needs Validation; 6.2.1.5 – Managing Unknowns; 6.2.6.3 – Requirements Feasibility and Risk; 6.3 – Baseline and Manage Design Input Requirements; 7.2.2 – Perform Design Input Requirements Validation; 8.1 – Design Definition Process Overview, 8.2 – Early System Verification and System Validation; 8.4 – Design Verification, 14.2.1 – Baseline Needs, Requirements, and Specifications; 14.2.4 – Managing Unknowns
