---
id: C4
name: Complete
type: characteristic
target_scope: individual_statement
supporting_rules:
- R1
- R2
- R6
- R7
- R9
- R11
- R23
- R24
- R25
- R27
- R33
- R34
- R35
- R39
- R40
page: 33
---

### Definition

The requirement statement sufficiently describes the necessary capability, characteristic, constraint, or quality factor to meet the need, source, or parent requirement from which it was transformed without needing other information to understand the requirement. 

### Rationale

An agreement is not useful unless the obligation is complete and does not need further explanation.  A well-formed requirement needs no further amplification to implement its intent.  As an example, interface requirements should include a reference to the location of the agreement that defines how the entity needs to interact with the entity to which it interfaces (for example, an Interface Control Document (ICD) or Data Dictionary).  Additionally, requirements based on a standard or regulation need to include a reference to the specific location within the standard or regulation from which it was derived. 

Each requirement should be understood in its own right without the overhead of having to understand a number of other requirements. 

Baselined requirement statements should not contain To Be Defined (TBD), To Be Specified (TBS), or To Be Resolved (TBR) clauses.  TBx can be used during the analysis and definition process to indicate ongoing work but should not be in the final requirement set.  Resolution of the TBx designation may be iterative, in which case there should be an acceptable timeframe for the TBx item to be resolved, determined by risks and dependencies.  If the baselined set of requirement contains requirements with a TBx item, it must be made clear in supplier or vendor agreements (for example, SOWs) who is responsible to resolve these items and when.  Refer to the NRM Section 14.2.4 for a detailed discussion concerning managing unknows. 

An incomplete requirement is not Verifiable (C7) nor Correct (C8) due to missing information (the requirement fails to address either “what”, “how well”, or “under what conditions”. 

### Guidance

To be complete, functional/performance requirements must have observable functions (“what”), measurable performance (“how well”) and a statement of conditions (“under what conditions”, for example, triggering events, environments, states and modes).  Such requirements may be insufficient to satisfy the need or parent requirement because of these errors or omissions. 

While fully appreciating that a requirement may require some context, the requirement statement itself should be a complete sentence that does not require reference to other statements to be understood in its basic form.  Note, however, that a requirement can refer to other documents (for example, ICDs, standards, and regulations).  When making these referrals, be specific to the sections of the documents that apply.  Refer to a complete standard or regulation only if all the requirements within the standard or regulation apply to your specific SOI (which is a rare occurrence). 
Caution: When referring to a standard or regulation, remember that standards and regulations are often written at a higher level of abstraction for a class of products similar to your SOI, but not necessarily your SOI specifically.  It is a mistake to just copy and paste a requirement from a standard or regulation.  Instead, you will need to derive requirements specific to your SOI at the appropriate level and then trace the resulting requirement(s) to the standard or regulation from which it was derived.  Also refer to the NRM Section 6.2,1,2 for a more detailed discussion concerning complying with requirements within standards and regulations. 

Requirements should not refer to one another through use of pronouns, nor should the understanding of the requirement assume the existence of a previous or subsequent requirement. This is especially important when requirements are managed within an application or database. 

In a set of requirements contained in some form of “document”, each requirement should be understood in its own right without having to understand the context as communicated in the requirements or headings surrounding it. 

By following a specific pattern for a requirement statement, requirements tend to be “more complete”, since these patterns provide guidance for specific information the requirement statement should include.  See Appendix C for more information on patterns. 

Completeness of individual need and requirement statements can be assessed during early system verification and design verification activities discussed in the NRM and GtVV. 

### Rules that help establish this characteristic

- R1 - /Accuracy/SentenceStructure
- R2 - /Accuracy/UseActiveVoice
- R6 - /Accuracy/Units
- R7 - /Accuracy/AvoidVagueTerms
- R9 - /Accuracy/NoOpenEnded
- R11 - /Concision/SeparateClauses
- R23 - /Singularity/Context
- R24 - /Completeness/AvoidPronouns
- R25 - /Completeness/UseOfHeadings
- R27 - /CONDITIONS/EXPLICIT
- R33 - /Tolerance/ValueRange
- R34 - /Quantification/Measurable
- R35 - /Quantification/TemporalIndefinite
- R39 - /UniformLanguage/StyleGuide
- R40 - /MODULARITY/RELATEDREQUIREMENTS

### Attributes that help establish this characteristic

(Refer to the NRM Section 15.)

A12 – Condition of Use 

A32 - Trace to Interface Definition 
### Activities and concepts associated with this characteristic

(Sections within the NRM)

3.2.1.2 – Power Of Expression; 3.2.1.3 – Managing Sets of Needs And Requirements; 3.2.1.6 – Formal, Binding Agreement; 4.4.3 – Get Stakeholder Agreement; 4.5 – Lifecycle Concepts 
Analysis and Maturation; 4.6.3.1 – Managing Unknowns; 4.8 – Baseline and Manage Lifecycle Concepts and Needs Definition Outputs; 5.1.2 – Perform Needs Verification; 6.2.1 – Transforming Needs into Design Input Requirements; 6.2.1.2 – Considerations For Each Type Of Requirement, Functional/Performance; 6.2.1.5 – Managing Unknowns; 6.2.3.6 – Interface Requirements Audit; 6.3 – Baseline and Manage Design Input Requirements; 7.1.2 – Perform Design Input Requirements Verification; 7.2.2 – Perform Design Input Requirements Validation; 8.1 – Design Definition Process Overview, 8.2 – Early System Verification and System Validation; 8.4 – Design Verification, 14.2.1 – Baseline Needs, Requirements, and Specifications; 14.2.4 – Managing Unknowns
