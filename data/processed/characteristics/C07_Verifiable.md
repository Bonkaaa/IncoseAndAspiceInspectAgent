---
id: C7
name: Verifiable
type: characteristic
target_scope: individual_statement
supporting_rules:
- R1
- R2
- R3
- R4
- R5
- R6
- R7
- R8
- R9
- R10
- R11
- R12
- R13
- R15
- R16
- R17
- R18
- R24
- R26
- R27
- R28
- R32
- R33
- R34
- R35
page: 38
---

### Definition

The requirement statement is structured and worded such that its realization can be verified to the approving authority’s satisfaction. 

### Rationale

Unless a requirement is written in a way that allows design verification or system verification, there is no way to tell if it has been satisfied and that the obligation has been met. 

Each requirement statement must include the necessary information such that success criteria can be defined, and the SOI can be verified such that that success criteria has been met, i.e., there is no ambiguity regarding what the requirement statement communicates and there are no missing characteristics within the requirement, i.e., the requirement is complete. 

An unverifiable requirement can result in multiple, objective observers (for example, designers or testers) interpreting the requirement differently making it difficult to verify the SOI meets the requirement. 

Verifiability is a necessary condition for establishing the characteristics: Appropriate (C2), Unambiguous (C3), Complete (C4), Singular (C5), Feasible (C6), Conforming (C9), Consistent (C11), and Comprehensible (C13).  Therefore, verifiability should be addressed as the initial criterion and a basis for examining these other characteristics. 

### Guidance

It is important not to confuse the phrase “requirement verification” vs. “design verification” or “system verification” as shown in Figure 5 and discussed in Section 1.7 and 1.8.  This characteristic, verifiable, is about design and system verification – showing that the design can be verified such that, when realized, will result in a SOI that meets the requirement and verifying that the realized SOI meets the requirement. 

Write each requirement statement in a way that allows the design or system to be verified that the requirement has been met by one of the four standard verification methods (inspection, analysis, demonstration, or test).  Various kinds of requirements are verifiable in different ways, and this will influence the way the requirement is written.  In general, to be verifiable, a requirement should be measurable.  (Refer to the NRM and GtVV for a detailed discussion on verification and validation across the lifecycle.) 
A requirement is considered to be verifiable if: 

- 1) a verification case can be determined from the requirement statement that allows for complete examination of all aspects of the requirement and precise determination of all values, including tolerances, such that success or failure can be determined, and 

- 2) the requirement content is adequate to completely define the expected behavior, characteristics, conditions, and success criteria for the actual verification activity. 

The measure of verifiability is the completeness and quality of the requirement: does it contain all the necessary information to establish what, how well, and under what conditions, i.e., is it Complete (C4)? 

Each requirement must have all the necessary information to be verifiable – the wording of the requirement is unambiguous (C3) and will have the same meaning to all observers or readers. 

This can be facilitated by use of a standard template as described in Appendix C – see also characteristic Conforming (C9). 

A customer may specify, “The aircraft’s range shall be as long as possible.” This statement is ambiguous and unverifiable.  This type of requirement is a signal that a trade study is needed to establish a verifiable maximum range requirement.  [Note: This is a good example of a need written as a requirement.  While “The stakeholders need the aircraft’s range to be as long as possible” is an acceptable level of abstraction for a need statement, it is not acceptable as a requirement.] 

The most usual causes for a requirement not to be verifiable are: 

- no clear definition of the correct functional behavior, conditions, and states. 

- lack of accuracy or feasibility in the ranges of acceptable performance. 

- use of ambiguous terms. 

- failure to define a feasible lifecycle concept and associated stakeholder need from which the requirement was transformed. 

- the requirement is not feasible. 

When writing requirement statements, use a verification point-of-view to imagine yourself performing the verification activity and define what evidence is needed to show that the requirement’s intent has been achieved as defined by the success criteria. 

It is a recommended best practice to define the verification success criteria, strategy, and method attributes when forming the requirement statement.  When this is done, the quality of the requirement statement will improve resulting in this characteristic (verifiable). 

Whether the SOI will be able to be verified against a requirement can be assessed during early system verification and design verification activities discussed in the NRM and GtVV. 

Useful questions to ask of a requirement statement are: 

- How will I know if the requirement has been met?  If the requirement has been properly quantified, it will provide a precise answer to this question. 

- What are the mandatory and desirable levels of performance required?  The result of this may be that several values are provided describing the tolerance and trade-space allowed for this requirement. 

- Is what the requirement states what I want to verify the SOI against?  If not, then rewrite the requirement to state what is intended. 

For example, it is best to verify you obtain specific performance data rather than verifying the system has sensors to provide that data.  It may have the sensors, but do they result in the actual quantity and quality of data needed?  This is also a good example of design input versus design 
output.  The need for the data is a design input, the sensors used to obtain this data are design outputs.  All too often, when a design output requirement is stated there was a failure to state why the design output was needed – the proper design input.  Because of this it could seem the SOI passed system verification, but in reality, it did not –the SOI was verified against the wrong requirement! 
### Rules that help establish this characteristic

- R1 - /Accuracy/SentenceStructure
- R2 - /Accuracy/UseActiveVoice
- R3 - /Accuracy/SubjectVerb
- R4 - /Accuracy/UseDefinedTerms
- R5 - /Accuracy/UseDefiniteArticles
- R6 - /Accuracy/Units
- R7 - /Accuracy/AvoidVagueTerms
- R8 - /Accuracy/NoEscapeClauses
- R9 - /Accuracy/NoOpenEnded
- R10 - /Concision/SuperfluousInfinitives
- R11 - /Concision/SeparateClauses
- R12 - /NonAmbiguity/CorrectGrammar
- R13 - /NonAmbiguity/CorrectSpelling
- R15 - /NonAmbiguity/AvoidNot
- R16 - /NonAmbiguity/AvoidNot
- R17 - /NonAmbiguity/Oblique
- R18 - /Singularity/SingleSentence
- R24 - /Completeness/AvoidPronouns
- R26 - /Realism/AvoidAbsolutes
- R27 - /Conditions/Explicit
- R28 - /Conditions/ExplicitLists
- R32 - /Quantifiers/Universals
- R33 - /Tolerance/ValueRange
- R34 - /Quantification/Measurable
- R35 - /Quantification/TemporalIndefinite

### Attributes that help establish this characteristic

( Refer to the NRM Section 15.)

A6 – System Verification or System Validation Success Criteria A8 - System Verification or System Validation Method A32 - Trace to Interface Definition 
### Activities and concepts associated with this characteristic

(Sections within the NRM)

3.2.1.1 – Communication; 3.2.1.2 – Power of Expression; 3.2.1.6 – Formal Binding Agreement; 3.2.1.7 – System Verification and System Validation; 3.2.2.5 – Support Simulations; 4.4.3 – Get 
Stakeholder Agreement; 4.5 – Lifecycle Concepts Analysis and Maturation; 4.6.3.1 – Managing Unknowns; 6.2 – Perform Design Input Requirements Definition; 6.2.1.2 – Considerations For Each Type Of Requirement, 6.2.1.5 – Managing Unknowns; 6.2.3.6 – Interface Requirements Audit; 6.2.5 – Plan for System Verification; 7.1.2 – Perform Design Input Requirements Verification; 8.1 – Design Definition Process Overview, 8.2 – Early System Verification and System Validation; 8.4 – Design Verification, 14.2.4 – Managing Unknowns 14.2.9 – Managing System Verification and System Validation.
