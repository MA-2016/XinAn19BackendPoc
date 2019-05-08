# CAPEC Data Resolving Package

* A webpage containing the rendered HTML representation of the desired CAPEC ID, and all dependent Attack Patterns, Views, or Categories.
* A compressed XML file containing the desired CAPEC ID, dependent Attack Patterns, Views, Categories, and all required External References.
* A compressed CSV file containing the fields of the desired Attack Patterns related to this View.

Note! Use XML format data file, not CSV.

## Build Graph Database

* Install Neo4j: https://pan.baidu.com/s/1WsXfmnU7jIg6OBUvdFeS4g#list/path=%2Fneo4j-release%2Fneo4j%2F3.5.4&parentPath=%2Fneo4j-release
* Start Neo4j: open command line and enter the directory you installing Neo4j, run ```bin/neo4j start```. Then wait a moment and run ```bin/neo4j status``` to check if Neo4j is started
* run ```python3 dbBuilder.py```

---

## Mechanisms of Attack

The Mechanisms of Attack representation organizes attack patterns hierarchically based on mechanisms that are frequently employed when exploiting a vulnerability.

This graph shows the tree-like relationships between attack patterns that exist at different levels of abstraction. At the highest level, categories exist to group patterns that share a common characteristic. Within categories, meta level attack patterns are used to present a decidedly abstarct characterization of a methodology or technique. Below these are standard and detailed level patterns that are focused on a specific methodology or technique used.

Reference: http://capec.mitre.org/data/slices/1000.html

* ID: an integer
* Name
* Abstraction: - Meta, Standard, Detailed
* Status: - Draft, Stable
* Description
* Alternate Terms: NULL
* Likelihood Of Attack: 是攻击的可能性 - Low, Medium, High
* Typical Severity: 严重程度 - Very Low, Low, Medium, High, Very High
* Ralated Attack Patterns: 相关攻击模式, eg.```::NATURE:ChildOf:CAPEC ID:220::NATURE:PeerOf:CAPEC ID:34::```, formatted:
```
::NATURE:ChildOf
 :CAPEC ID:220
::NATURE:PeerOf
 :CAPEC ID:34
::
```
* Execution Flow: 执行步骤, fields include STEP PHASE DESCRIPTION TECHNIQUE. Note, it's possible the semicolon before TECHNIQUE is missing . eg.```::STEP:1:PHASE:Explore:DESCRIPTION:[Survey] The attacker surveys the target application, possibly as a valid and authenticated user:TECHNIQUE:Spidering web sites for all available links:TECHNIQUE:Brute force guessing of resource names:TECHNIQUE:Brute force guessing of user names / credentials:TECHNIQUE:Brute force guessing of function names / actions::STEP:2:PHASE:Explore:DESCRIPTION:[Identify Functionality] At each step, the attacker notes the resource or functionality access mechanism invoked upon performing specific actions:TECHNIQUE:Use the web inventory of all forms and inputs and apply attack data to those inputs.:TECHNIQUE:Use a packet sniffer to capture and record network traffic:TECHNIQUE:Execute the software in a debugger and record API calls into the operating system or important libraries. This might occur in an environment other than a production environment, in order to find weaknesses that can be exploited in a production environment.::STEP:3:PHASE:Experiment:DESCRIPTION:[Iterate over access capabilities] Possibly as a valid user, the attacker then tries to access each of the noted access mechanisms directly in order to perform functions not constrained by the ACLs.:TECHNIQUE:Fuzzing of API parameters (URL parameters, OS API parameters, protocol parameters)::``` formatted:
```
::STEP:1
 :PHASE:Explore
 :DESCRIPTION:[Survey] The attacker surveys the target application, possibly as a valid and authenticated user
 :TECHNIQUE:Spidering web sites for all available links
 :TECHNIQUE:Brute force guessing of resource names
 :TECHNIQUE:Brute force guessing of user names / credentials
 :TECHNIQUE:Brute force guessing of function names / actions
::STEP:2
 :PHASE:Explore
 :DESCRIPTION:[Identify Functionality] At each step, the attacker notes the resource or functionality access mechanism invoked upon performing specific actions
 :TECHNIQUE:Use the web inventory of all forms and inputs and apply attack data to those inputs.
 :TECHNIQUE:Use a packet sniffer to capture and record network traffic
 :TECHNIQUE:Execute the software in a debugger and record API calls into the operating system or important libraries. This might occur in an environment other than a production environment, in order to find weaknesses that can be exploited in a production environment.
::STEP:3
 :PHASE:Experiment
 :DESCRIPTION:[Iterate over access capabilities] Possibly as a valid user, the attacker then tries to access each of the noted access mechanisms directly in order to perform functions not constrained by the ACLs.
 :TECHNIQUE:Fuzzing of API parameters (URL parameters, OS API parameters, protocol parameters)
::
```
* Prerequisites: 发生前提. eg. ```::The application must be navigable in a manner that associates elements (subsections) of the application with ACLs.::The various resources, or individual URLs, must be somehow discoverable by the attacker::The administrator must have forgotten to associate an ACL or has associated an inappropriately permissive ACL with a particular navigable resource.::``` formatted
```
::The application must be navigable in a manner that associates elements (subsections) of the application with ACLs.
::The various resources, or individual URLs, must be somehow discoverable by the attacker::The administrator must have forgotten to associate an ACL or has associated an inappropriately permissive ACL with a particular navigable resource.
::
```
* Skill Required: fields include SKILL LEVEL (Low Medium High). eg. ```::SKILL:In order to discover unrestricted resources, the attacker does not need special tools or skills. He only has to observe the resources or access mechanisms invoked as each action is performed and then try and access those access mechanisms directly.:LEVEL:Low::``` formatted
```
::SKILL:In order to discover unrestricted resources, the attacker does not need special tools or skills. He only has to observe the resources or access mechanisms invoked as each action is performed and then try and access those access mechanisms directly.
 :LEVEL:Low
::
```
* Resources Required: eg. ```::The requirements vary depending upon the nature of the API. For application-layer APIs related to the processing of the HTTP protocol, one or more of the following may be needed: a MITM (Man-In-The-Middle) proxy, a web browser, or a programming/scripting language.::``` formatted
```
::The requirements vary depending upon the nature of the API. For application-layer APIs related to the processing of the HTTP protocol, one or more of the following may be needed: a MITM (Man-In-The-Middle) proxy, a web browser, or a programming/scripting language.
::
```
* Indicators: 备注. eg. ```::If the application does bound checking, it should fail when the data source is larger than the size of the destination buffer. If the application's code is well written, that failure should trigger an alert.::``` formatted
```
::If the application does bound checking, it should fail when the data source is larger than the size of the destination buffer. If the application's code is well written, that failure should trigger an alert.
::
```
* Concequences: eg. ```::SCOPE:AvailabilityTECHNICAL IMPACT:Unreliable Execution::SCOPE:Confidentiality:SCOPE:Integrity:SCOPE:AvailabilityTECHNICAL IMPACT:Execute Unauthorized Commands:NOTE:Confidentiality Integrity Availability Execute Unauthorized Commands Run Arbitrary Code::SCOPE:ConfidentialityTECHNICAL IMPACT:Read Data::SCOPE:IntegrityTECHNICAL IMPACT:Modify Data::SCOPE:Confidentiality:SCOPE:Access Control:SCOPE:AuthorizationTECHNICAL IMPACT:Gain Privileges::``` formatted
```
::SCOPE:Availability
 TECHNICAL IMPACT:Unreliable Execution
::SCOPE:Confidentiality
 :SCOPE:Integrity
 :SCOPE:Availability
 TECHNICAL IMPACT
 :Execute Unauthorized Commands
 :NOTE:Confidentiality Integrity Availability Execute Unauthorized Commands Run Arbitrary Code
::SCOPE:Confidentiality
 TECHNICAL IMPACT:Read Data
::SCOPE:Integrity
 TECHNICAL IMPACT:Modify Data
::SCOPE:Confidentiality
 :SCOPE:Access Control
 :SCOPE:Authorization
 TECHNICAL IMPACT:Gain Privileges
::
```
* Mitigations: 解决建议. eg. ```::In a J2EE setting, administrators can associate a role that is impossible for the authenticator to grant users, such as NoAccess, with all Servlets to which access is guarded by a limited number of servlets visible to, and accessible by, the user. Having done so, any direct access to those protected Servlets will be prohibited by the web container. In a more general setting, the administrator must mark every resource besides the ones supposed to be exposed to the user as accessible by a role impossible for the user to assume. The default security setting must be to deny access and then grant access only to those resources intended by business logic.::```
* Example Instances: eg. ```::Implementing the Model-View-Controller (MVC) within Java EE's Servlet paradigm using a Single front controller pattern that demands that brokered HTTP requests be authenticated before hand-offs to other Action Servlets. If no security-constraint is placed on those Action Servlets, such that positively no one can access them, the front controller can be subverted.::```
* Related Weaknesses: eg: ```::285::732::276::693::721::434::```
* Taxonomy Mappings: 分类映射, eg. ```TAXONOMY NAME:ATTACK:ENTRY ID:1044:ENTRY NAME:File System Permissions Weakness::``` formatted
```
TAXONOMY NAME:ATTACK
 :ENTRY ID:1044
 :ENTRY NAME:File System Permissions Weakness
::
```
* Notes: eg. ```TYPE:Other:NOTE:Large quantities of data is often moved from the target system to some other adversary controlled system. Data found on a target system might require extensive resources to be fully analyzed. Using these resources on the target system might enable a defender to detect the adversary. Additionally, proper analysis tools required might not be available on the target system.::::TYPE:Other:NOTE:This attack differs from Data Interception and other data collection attacks in that the attacker actively queries the target rather than simply watching for the target to reveal information.::``` formatted
```
TYPE:Other
 :NOTE:Large quantities of data is often moved from the target system to some other adversary controlled system. Data found on a target system might require extensive resources to be fully analyzed. Using these resources on the target system might enable a defender to detect the adversary. Additionally, proper analysis tools required might not be available on the target system.
::
::TYPE:Other
 :NOTE:This attack differs from Data Interception and other data collection attacks in that the attacker actively queries the target rather than simply watching for the target to reveal information.
::
```

### Relationship Types
* ChildOf
* PeerOf
* CanFollow
* CanPrecede
* CanAlsoBe

## Domains of Attack

The Domains of Attack representation organizes items by the target domains for each attack pattern.

## WASC Threat Classification 2.0

This view provides a mapping between the WASC Threat Classification 2.0 and CAPEC.

## Comprehensive CAPEC Dictionary

This view (slice) covers all the elements in CAPEC, include Attack Patterns, Categories, Views, External Reference. OK, for now, this view is enough to fit our need.

Reference: http://capec.mitre.org/data/slices/2000.html