---
id: C12
name: Feasible
type: characteristic
target_scope: set_of_statements
supporting_rules:
- R26
- R33
- R34
page: 51
---

### Definition

Sets of needs and requirements can be realized within entity constraints (for example, cost, schedule, technical) with acceptable risk. 

### Rationale

Just as there is little point in agreeing to an obligation for an individual need or requirement that is not feasible, the sets of needs and requirements must be achievable within the appropriate constraints including cost, schedule, and risk.   If feasibility is not addressed early in the development process, it can lead to wasted effort and cost. 

### Guidance

While individual need and requirement statements may be feasible, they may not be so when placed in combination with others.  That is, the combination of feasible individual needs or requirements does not necessarily sum to a feasible set of needs or requirements.  (Like the old saying “The straw that broke the camel’s back”.) 

For example, the following are feasible, individual requirements for a laptop computer: weighs less than 1.4 kg, has a storage capacity of 1 TByte, has 4 GByte of RAM, has a wireless network interface, has an Ethernet network interface, has a USB interface, has an HDMI interface, can be dropped from 1 meter without damage, can survive in temperatures of ±50°C, and retails for less than $900.  While each of those requirements seems perfectly feasible, even at first glance to a non-expert, we cannot be so readily sure that the set is feasible (that is, all requirements can be met simultaneously).  As soon as we go past a couple of dimensions, our human intuition quickly deserts us. 

If the related individual needs or requirements are distributed throughout the need or requirement set, it is even more difficult to assess the feasibility of the set.  As was stated for individual need and requirement statements, determining feasibility of a set of needs or requirements is not always completely known and is often assessed in terms of acceptable risk consistent with the development lifecycle stage. 

In the solution space, there should be at least one and preferably multiple feasible sets of lifecycle concepts that will result in the problem being solved or opportunity to be realized that drove the need for the SOI.  The lifecycle concepts should be technically feasible (such as in terms of technology maturity level and advancement), and feasible within the constraints of the project (such as cost, schedule, technical, ethical, and regulatory compliance) with a level of risk consistent with the lifecycle stage. 

As discussed in the NRM, as part of risk assessment and during lifecycle concept analysis and maturation critical technologies are identified, their TRL and Advancement Degree of Difficulty (AD<sup>2</sup> ) is assessed, and a technology maturation plan is developed that will result in the critical technology maturity to advance such that it will be feasible in time to meet the system development schedule.  These activities represent a risk to the project and as such this risk must be managed closely. 

A set of needs cannot be feasible if any of the individual needs are not feasible (C6).  Feasibility of a specific need statement must be determined in the context of all needs for a specific entity set and can be evaluated without regard to the sources from which they were derived. 
Needs within the same entity set of needs are analyzed together with respect to program constraints and technology maturity to determine feasibility.  A set of needs could not be feasible due to inconsistency (C11), physical impossibility, or excessive program risk. 

Before allowing a set of needs to be baselined, an assessment of the feasibility of the chosen lifecycle concepts should be made in terms of the drivers, constraints, and risk.  If not feasible within the stated constraints with risk appropriated for that lifecycle stage, the set of needs will not be feasible nor will be the resulting set of requirements that are transformed from that set of needs. 

A set of requirements cannot be feasible if any of the individual requirements are not feasible (C6).  Feasibility of a specific requirement must be determined in the context of all requirements for a specific entity set and can be evaluated without regard to the parent requirements. 

Requirements within the same entity set of requirements are analyzed together with respect to project constraints, technology maturity, and risk to determine feasibility.  A set of requirements may not be feasible due to inconsistency (C11), physical impossibility, or excessive program risk. Feasibility of the sets of needs and requirements can be assessed during early system validation as well as during design validation activities discussed in the NRM and GtVV. 

Additional characteristics mapped to feasible include “Consistent” (C11) and “Able to be validated” (C14) for the set of requirements. 

An approach that can be used is to consider the set of needs or requirements to be a “bucket” which is bound by cost, schedule, and technology.  When adding individual needs or requirements to the bucket, whether the individual needs or requirements “fit” within these constraints must be determined.  When the bucket is full, the addition of any more needs or requirements puts the project at increased risk.  The bucket analogy is also useful for addressing change.  If a bucket is full, and someone wants to add an additional need or requirement to the bucket, the question of feasibility must be addressed.  Can the bucket be made bigger?  Can something of lower priority be taken out?  Is the project willing to accept more risk?  If the answer is no, then the project must say no to the change!  Refer the NRM for a more detailed discussion concerning the use of both the needs bucket and requirements bucket when addressing feasibility and risk. 
### Rules that help establish this characteristic

- R26 - /Realism/AvoidAbsolutes
- R33 - /Tolerance/ValueRange
- R34 - /Quantification/Measurable

### Attributes that help establish this characteristic

(_ Refer to the NRM Section 15.)

A26 – Stability/Volatility A31 - Status (of implementation) A36 – Risk (of implementation) A38 - Key Driving Need or Requirement (KDN/KDR) 
### Activities and concepts associated with this characteristic

(Sections within the NRM)

3.2.2.1 – Analysis from Which Needs and Requirements are Derived; 4.3.6.2 – Technology Maturity; 4.3.7.1 – Classes of Risk – Development Risk; 4.5.1 – Feasibility; 4.5.7.4 – Zeroing in on a Feasible Architecture and Design; 4.6.3.4 – Needs Feasibility and Risk; 4.8 – Baseline and 
Manage Lifecycle Concepts and Needs Definition Outputs; 5.2.2 – Perform Needs Validation; 6.2 – Perform Design Input Requirements Definition; 6.2.6.3 – Requirements Feasibility and Risk; 6.3 – Baseline and Manage Design Input Requirements; 7.2.2 – Perform Design Input Requirements Validation; 8.1 – Design Definition Process Overview, 8.2 – Early System Verification and System Validation; 8.5 – Design Validation, 14.2.1 – Baseline Needs, Requirements, and Specifications;
