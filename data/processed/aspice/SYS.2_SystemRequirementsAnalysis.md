---
id: SYS.2
name: System Requirements Analysis
standard: Automotive SPICE PAM v4.0
type: process
pages:
- 36
- 37
base_practices:
- 'SYS.2.BP1: Specify system requirements'
- 'SYS.2.BP2: Structure system requirements'
- 'SYS.2.BP3: Analyze system requirements'
- 'SYS.2.BP4: Analyze the impact on the system context'
- 'SYS.2.BP5: Ensure consistency and establish bidirectional traceability'
- 'SYS.2.BP6: Communicate agreed system requirements and impact on the system context'
output_information_items:
- 17-00 Requirement
- 17-54 Requirement Attribute
- 15-51 Analysis Results
- 13-51 Consistency Evidence
- 13-52 Communication Evidence
---

# SYS.2 - System Requirements Analysis 

 

 

## Process Purpose 

The purpose is to establish a structured and analyzed set of system requirements consistent with the stakeholder requirements. 

## Process Outcomes 

- 1) System requirements are specified. 

- 2) System requirements are structured and prioritized. 

- 3) System requirements are analyzed for correctness and technical feasibility. 

- 4) The impact of system requirements on the operating environment is analyzed. 

- 5) Consistency and bidirectional traceability are established between system requirements and stakeholder requirements. 

- 6) The system requirements are agreed and communicated to all affected parties. 

## Base Practices 

### SYS.2.BP1: Specify system requirements

Use the stakeholder requirements to identify and document the functional and non-functional requirements for the system according to defined characteristics for requirements. 

_Note 1: Characteristics of requirements are defined in standards such as ISO IEEE 29148, ISO 26262-8:2018, or the INCOSE Guide For Writing Requirements._ 

_Note 2: Examples for defined characteristics of requirements shared by technical standards are verifiability (i.e., verification criteria being inherent in the requirements text), unambiguity/comprehensibility, freedom from design and implementation, and not contradicting any other requirement)._ 

### SYS.2.BP2: Structure system requirements

Structure and prioritize the system requirements. 

_Note 3: Examples for structuring criteria can be grouping (e.g., by functionality) or product variants identification._ 

_Note 4: Prioritization can be done according to project or stakeholder needs via e.g., definition of release scopes. Please refer to SPL.2.BP1._ 

### SYS.2.BP3: Analyze system requirements

Analyze the specified system requirements including their interdependencies to ensure correctness, technical feasibility, and to support project management regarding project estimates. 

_Note 5: See MAN.3.BP3 for project feasibility and MAN.3.BP5 for project estimates._ 

_Note 6: Technical feasibility can be evaluated based on e.g., platform or product line, or by means of prototype development or product demonstrators._ 
 

### SYS.2.BP4: Analyze the impact on the system context

Analyze the impact that the system requirements will have on elements in the relevant system context. 

### SYS.2.BP5: Ensure consistency and establish bidirectional traceability

Ensure consistency and establish bidirectional traceability between system requirements and stakeholder requirements. 

_Note 7: Bidirectional traceability supports consistency, facilitates impact analyses of change requests, and supports the demonstration of coverage of stakeholder requirements. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other._ 

_Note 8: There may be non-functional stakeholder requirements that the system requirements do not trace to. Examples are process requirements. Such stakeholder requirements are still subject to verification._ 

### SYS.2.BP6: Communicate agreed system requirements and impact on the system context

Communicate the agreed system requirements, and results of the impact analysis on the system context, to all affected parties. 

## Work Products & Practice Mapping

|**SYS.2 System Requirements Analysis**|Outcome 1|Outcome 2|Outcome 3|Outcome 4|Outcome 5|Outcome 6|
|---|---|---|---|---|---|---|
|**Output Information Items**|||||||
|17-00 Requirement|X|X|||||
|17-54 Requirement Attribute||X|X||||
|15-51 Analysis Results|||X|X|||
|13-51 ConsistencyEvidence|||||X||
|13-52 Communication Evidence||||||X|
|**Base Practices**|||||||
|BP1: Specifysystem requirements|X||||||
|BP2: Structure system requirements||X|||||
|BP3: Analyze system requirements|||X||||
|BP4: Analyze the impact on the system context||||X|||
|BP5: Ensure consistencyand establish bidirectional traceability|||||X||
|BP6: Communicate agreed system requirements and impact on<br>the system context||||||X|

## Output Information Item Characteristics (Annex B)

The following characteristics define the expected content and structure of the work products/information items produced by SYS.2, as specified in Automotive SPICE PAM v4.0 Annex B:

### 17-00: Requirement

- An expectation of functions and capabilities (e.g., non-functional requirements), or one of its interfaces
- from a black-box perspective
- that is verifiable, does not imply a design or implementation decision, is unambiguous, and does not introduce contradictions to other requirements.
- A requirements statement that implies, or represents, a design or implementation decision is called “Design Constraint”.
- Examples for requirements aspects at the system level are thermal characteristics such as
  - heat dissipation
  - dimensions
  - weight
  - materials
- Examples of aspects related to requirements about system interfaces are
  - connectors
  - cables
  - housing
- Examples for requirements at the hardware level are
  - lifetime and mission profile, lifetime robustness
  - maximum price
  - storage and transportation requirements
  - functional behavior of analog or digital circuits and logic
  - quiescent current, voltage impulse responsiveness to crank, start-stop, drop-out, load dump
  - temperature, maximum hardware heat dissipation
  - power consumption depending on the operating state such as sleep-mode, start-up, reset conditions
  - frequencies, modulation, signal delays, filters, control loops
  - power-up and power-down sequences, accuracy and precision of signal acquisition or signal processing time
  - computing resources such as memory space and CPU clock tolerances
  - maximum abrasive wear and shearing forces for e.g., pins or soldering joints
  - requirements resulting from lessons learned
  - safety related requirements derived from the technical safety concept

### 17-54: Requirement Attribute

- Meta-attributes that support structuring and definition of release scopes of requirements.
- Can be realized by means of tools.

_NOTE: usage of requirements attributes may further support analysis of requirements._


### 15-51: Analysis Results

- Identification of the object under analysis.
- The analysis criteria used, e.g.:
  - selection criteria or prioritization scheme used
  - decision criteria
  - quality criteria
- The analysis results, e.g.:
  - what was decided/selected
  - reason for the selection
  - assumptions made
  - potential negative impact
- Aspects of the analysis may include
  - correctness
  - understandability
  - verifiability
  - feasibility
  - validity

### 13-51: Consistency Evidence

- Demonstrates bidirectional traceability between artifacts or information in artifacts, throughout all phases of the life cycle, by e.g.,
  - tool links
  - hyperlinks
  - editorial references
  - naming conventions
- Evidence that the content of the referenced or mapped information coheres semantically along the traceability chain, e.g., by
  - performing pair working or group work
  - performing by peers, e.g., spot checks
  - maintaining revision histories in documents
  - providing change commenting (via e.g., meta-information) of database or repository entries

_Note: This evidence can be accompanied by e.g., Definition of Done (DoD) approaches._


### 13-52: Communication Evidence

- All forms of interpersonal communication such as
  - e-mails, also automatically generated ones
  - tool-supported workflows
  - meeting, verbally or via meeting minutes (e.g., daily standups)
  - podcast
  - blog
  - videos
  - forum
  - live chat
  - wikis
  - photo protocol
