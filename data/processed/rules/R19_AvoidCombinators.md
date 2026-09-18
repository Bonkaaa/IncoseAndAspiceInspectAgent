---
id: R19
name: AvoidCombinators
type: rule
page: 78
target_scope: individual_statement
established_characteristics:
- C3
- C5
related_rules:
- R16
- R17
- R28
---

## **4.4.2 R19 - /SINGULARITY/AVOIDCOMBINATORS**

**Avoid combinators.**

### Elaboration

Combinators are words that join clauses, such as “and”, “or”, “then”, “unless”, “but”, “as well as” “but also”, “however”, “whether”, “meanwhile”, “whereas”, “on the other hand”, or “otherwise.” Their presence in a requirement usually indicates that multiple requirements should be written. 

Exception: AND, OR, NOT can be used in need and requirement statements as logical conditions and qualifiers as stated in R15. 

See also R16 and R17. 

### Examples

**Unacceptable:** The user shall either be trusted or not trusted. 

[This is unacceptable for several reasons.  The intention is that a user should be classified in one of two ways, but it is also a passive requirement written on the user rather than on the system (R2) and it is ambiguous: the requirement would still be met if the system took the option of treating all users as trusted.] 

**Acceptable:** The Security_System shall categorize each User as [EITHER Trusted OR Not_Trusted). 

**Unacceptable:** _The “command the sidelights” function shall_ ensure the regulatory consistency of lights illumination _by ensuring_ the illumination of sidelights is maintained during the illumination of the side lamps, or the head lights, or the fog lights or the rear fog lights or a combination of these lights. 

[Again, this is unacceptable because it is non-singular, uses dubious grammar, contains elements of purpose, and is generally confusing.] 

**Acceptable:** The Control_Sidelights function shall illuminate the Sidelights while any combination of the following conditions is true: the Side_Lamps are illuminated, the Head_Lamps are illuminated, the Front_Fog_Lamps are illuminated, the Rear_Fog_Lamps are illuminated. 

[Rules 16 and 17 have also been applied to remove combinators and clarify the exact conditions.  Note that the use of “any” in this example is not ambiguous and thus is an exception to R32.  See also R28.] 
### Characteristics that are established by this rule

- C3 - Unambiguous
- C5 - Singular
