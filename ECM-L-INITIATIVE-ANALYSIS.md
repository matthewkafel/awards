# ECM-L Initiative: Letter Catalog & Transition Plan

**Initiative Goal**: Catalog manually-generated letters from Compensation Service (CS) and Pension & Fiduciary (P&F) and create transition plans for migration to ECM-L

**Status**: Initial Analysis Based on Available Documentation  
**Date**: January 14, 2026

---

## Executive Summary

Based on analysis of the converted PDF documentation, this document provides an initial catalog of manually-generated letters and transition planning for ECM-L integration.

### Key Findings

1. **Current State**: PFS ADL Letters currently generated using deprecated PCGL (Personal Computer Generated Letters) tool and Microsoft Word
2. **First Use Case**: PFS Automated Decision Letters (ADL) for Awards identified as Phase 4 integration
3. **Legacy System**: VBMS Correspondence Service currently used as interim solution
4. **Target State**: Full ECM-L integration with self-service letter management

---

## Part 1: Letter Catalog

### 1.1 Pension & Fiduciary (P&F) Letters

#### PFS Automated Decision Letters (ADL)

| Attribute | Details |
|-----------|---------|
| **Technical POC** | Simon Dessus, Michael Hart, Jennifer Feuer |
| **Validated by POC** | ✅ (Referenced in architecture doc) |
| **Letter Types** | - DIC Grant<br>- Pension Grant<br>- Excess Income Denial |
| **Template Name** | PFS ADL Definition (specific templates per letter type) |
| **Current System** | PCGL (deprecated) + Microsoft Word + VBMS Correspondence (interim) |
| **Workflow** | PFS ADL Main Business Process |
| **Storage** | Claim Evidence (S3 Bucket) |
| **Distribution** | Package Manager (pending) |
| **Triggers** | - Award generation in VBMS Awards<br>- Authorization by Authorizer<br>- Concurrence by Concur Authorizer (for amounts >$40k) |
| **Data Sources** | - Awards API<br>- Veteran API<br>- Participant API<br>- Evidence API<br>- Claims API<br>- POA API<br>- BEP Services<br>- VBA Corporate Database |

**Letter Subtypes Identified**:
1. **PFS DIC Grant Letter** - Dependency and Indemnity Compensation approval
2. **PFS Pension Grant Letter** - Pension benefit approval  
3. **PFS Excess Income Denial Letter** - Denial due to income exceeding threshold

**Associated Award Print**: eDoc (Award datasheet) generated alongside letter

---

### 1.2 Compensation & Pension (C&P) Awards Letters

Based on VBMS Awards 40.1 User Guide analysis:

#### Compensation/Pension Live (CPL) Letters

| Attribute | Details |
|-----------|---------|
| **Letter Type** | Award Decision Letters |
| **Current System** | VBMS Correspondence Service |
| **Workflow** | Generate → Authorize → Concur (if needed) |
| **Triggers** | - Award generation (by AVSR)<br>- Authorization (by Authorizer)<br>- Concurrence (by Concur Authorizer) |
| **Data Sources** | - VBMS Rating<br>- BEP Services (Awards, Claims, Dependencies)<br>- Military Service Data<br>- Financial Data |
| **Storage** | eFolder via Correspondence Service |
| **Key Decision Points** | - Rating decisions<br>- Dependency changes<br>- Financial assessments<br>- Benefit adjustments |

**Scenarios Covered** (100+ in User Guide):
- Basic compensation awards
- Dependency additions/removals (spouse, children)
- Financial income assessments
- Pension awards with income
- Aid & Attendance
- Clothing allowance
- Multiple service periods

#### Burial Benefit Letters

| Attribute | Details |
|-----------|---------|
| **Letter Types** | - Service-Connected (SC) Burial<br>- Non-Service-Connected (NSC) Burial<br>- Plot Allowance<br>- Transportation Allowance<br>- Marker/Engraving Reimbursement |
| **Current System** | VBMS Correspondence Service |
| **Workflow** | Burial claim → Decision → Generate letter |
| **Triggers** | - Veteran death<br>- Burial claim establishment<br>- SC death rating |
| **Claimant Types** | - Funeral homes<br>- Individual persons<br>- State cemeteries |
| **Data Sources** | - VBMS Rating (SC death decision)<br>- BEP Burial Decision Service<br>- Claimant information |

#### DIC Letters (Dependency and Indemnity Compensation)

| Attribute | Details |
|-----------|---------|
| **Letter Types** | - DIC Spouse Award<br>- DIC Child Award<br>- Veteran's Rate Month of Death |
| **Current System** | VBMS Correspondence Service |
| **Workflow** | Service-connected death → Eligibility → Award generation |
| **Triggers** | - SC death rating<br>- Death in service<br>- 38 U.S.C. 1318 entitlement |
| **Special Scenarios** | - 8&8 criteria (8 years totally disabled)<br>- Minor children<br>- School children<br>- Multiple children with/without spouse |
| **Data Sources** | - VBMS Rating (death decision)<br>- BEP Person/Participant services<br>- Dependency data<br>- School attendance info |

#### REPS Letters (Reserve Educational Assistance Program)

| Attribute | Details |
|-----------|---------|
| **Letter Type** | REPS Benefit Award |
| **Current System** | VBMS Correspondence Service |
| **Workflow** | Eligibility determination → Award calculation → Letter generation |
| **Triggers** | - REPS eligibility decision<br>- School enrollment |
| **Data Sources** | - Branch of service<br>- Earned income, Base FMAX, Base PIA<br>- School name and enrollment dates<br>- Number of REPS family members |

---

### 1.3 Clothing Allowance Letters

| Attribute | Details |
|-----------|---------|
| **Letter Type** | Annual Clothing Allowance Award |
| **Current System** | VBMS Correspondence Service |
| **Workflow** | Diagnostic code verification → GAO (if needed) → Award → Letter |
| **Triggers** | - Approved diagnostic code<br>- Annual renewal |
| **Data Sources** | - Diagnostic codes (configured in Admin)<br>- Veteran prosthetic/orthotic device info |
| **Special Requirements** | - Admin-configured diagnostic codes<br>- Clothing Allowance Admin role required |

---

### 1.4 Accrued Benefit Letters

| Attribute | Details |
|-----------|---------|
| **Letter Type** | Posthumous Award/Accrued Benefits |
| **Current System** | VBMS Correspondence Service |
| **Workflow** | Death of beneficiary → Accrued calculation → Distribution to survivors |
| **Triggers** | - Veteran death<br>- Entitlement established prior to death |
| **Claimant Types** | - Spouse<br>- Children<br>- Parents<br>- Other dependents |
| **Data Sources** | - Posthumous award calculations<br>- Relationship to deceased<br>- Shares distribution |

---

### 1.5 Specialized Decision Letters

#### Fee Allocation Notice

| Attribute | Details |
|-----------|---------|
| **Letter Type** | Attorney Fee Allocation |
| **Current System** | VBMS Correspondence Service |
| **Workflow** | Generated during award authorization |
| **Triggers** | - Attorney representation<br>- Award authorization |
| **Data Sources** | - Awards API (attorney fee amount)<br>- POA API |

#### Fiduciary Letters

| Attribute | Details |
|-----------|---------|
| **Letter Type** | Incompetency/Fiduciary Notices |
| **Current System** | VBMS Correspondence Service + VBMS Fiduciary |
| **Workflow** | Incompetency decision → EP-590 auto-establishment → Letter |
| **Triggers** | - Proposed incompetency decision (from Rating)<br>- Award authorization |
| **Data Sources** | - VBMS Rating (incompetency decision)<br>- VBMS Fiduciary |
| **Auto-Actions** | - EP-590 automatically established<br>- EP-290 for restored competency |

---

## Part 2: Current State Analysis

### 2.1 Problems with Current Manual Process

**PCGL (Personal Computer Generated Letters)**:
- ❌ Desktop-based, deprecated
- ❌ No standardization enforcement
- ❌ No version control
- ❌ Manual "stitching" of letter content
- ❌ Inconsistent templates across users
- ❌ Local file storage (no centralization)
- ❌ No formal review process

**VBMS Correspondence (Interim)**:
- ⚠️ Requires IT intervention for changes
- ⚠️ Not self-service for LOBs
- ⚠️ Tightly coupled to VBMS
- ⚠️ Limited template management
- ✅ Better than PCGL but not enterprise solution

### 2.2 Benefits of ECM-L Migration

1. **Centralized Management**
   - Single source of truth for all letter templates
   - Version-controlled template library
   - Audit trail for all changes

2. **Self-Service**
   - LOBs can update templates without IT
   - Changeset approval workflow
   - Test scenarios before release

3. **Standardization**
   - Enforced template structure
   - Consistent branding
   - Regulatory compliance built-in

4. **Efficiency**
   - Automated letter generation
   - Data population from APIs
   - Reduced manual errors

5. **Scalability**
   - Multi-tenant architecture
   - Supports 40,000 users
   - 20 million letters annually

---

## Part 3: Transition Plan

### 3.1 Phase-Based Approach

#### Phase 1: Infrastructure & Onboarding (Current)
**Jira Tickets**: VBMSR-32947, VBMSR-32948

**Activities**:
- ✅ ECM-L infrastructure established
- ✅ BAAZ integration complete
- ✅ Intake process defined
- 🔄 Awards LOB onboarding in progress

**Deliverables**:
- LOB Intake Form completed
- Connection Configuration for Awards API
- Workflow configurations

#### Phase 2: PFS ADL Letters (Priority)
**Jira Tickets**: VBMSR-30957, VBMSR-31242, VBMSR-30953, VBMSR-27690

**Activities**:
1. Migrate PFS ADL letter templates to ECM-L Definition Manager
2. Configure Resources for Awards data (Awards API, Veteran API, etc.)
3. Create Workflows for DIC Grant, Pension Grant, Excess Income Denial
4. Develop Test Scenarios
5. Integrate VBMS Awards with Letter Manager MFE

**Timeline**: Pending Phase 4 completion (Complex Inputs)

**Reason for Phase 4 Dependency**: PFS ADL letters require:
- Input Groups
- Attachment Selection Inputs
- Recipient Selection
- Data Resource Defaults
- Conditional logic

#### Phase 3: Standard C&P Award Letters
**Target**: After PFS ADL success

**Activities**:
1. Catalog existing C&P letter templates from Correspondence Service
2. Map data sources to ECM-L Resources
3. Convert letter templates to ECM-L format
4. Create Changesets for template versions
5. Pilot with select ROs

**Letter Types to Migrate**:
- Basic compensation awards
- Dependency change notices
- Pension award letters
- Burial benefit letters
- DIC award letters

#### Phase 4: Specialized & Complex Letters

**Activities**:
1. REPS letters
2. Clothing allowance letters
3. Accrued benefit letters
4. Fee allocation notices
5. Fiduciary letters

---

### 3.2 Technical Integration Requirements

#### For VBMS Awards to Integrate with ECM-L:

1. **Kafka Consumer**
   ```
   Subscribe to:
   - LetterInstanceDraftCompleteEvent
   - LetterInstanceFinalizedEvent
   ```

2. **Awards API Enhancements**
   ```
   New Endpoints:
   - GET /awards/{awardId}/data-for-letter
   - GET /awards/{awardId}/participants
   - GET /awards/{awardId}/decisions
   - GET /awards/{awardId}/dependencies
   ```

3. **Letter Manager MFE Embedding**
   ```
   Embed in:
   - Current and Proposed Award page
   - Record Decisions page
   ```

4. **Data Transformation Logic**
   ```
   Awards must transform:
   - Rating decisions → Letter data objects
   - Financial decisions → Letter data objects
   - Dependency decisions → Letter data objects
   - Adjustment decisions → Letter data objects
   ```

---

### 3.3 BPMN: Current Process

```
[AVSR creates award] 
    → [AVSR generates award in VBMS Awards]
    → [Awards calls Correspondence Service]
    → [Correspondence generates letter + eDoc]
    → [Letter stored in eFolder]
    → [Authorizer reviews and authorizes]
    → [Correspondence finalizes letter]
    → [Letter uploaded to eFolder]
```

**Issues**:
- IT required to modify letter templates
- No self-service for LOBs
- Limited version control
- No formal approval workflow for template changes

---

### 3.4 BPMN: Proposed ECM-L Process

```
[AVSR creates award]
    → [AVSR generates award in VBMS Awards]
    → [Awards calls Letter Manager API]
    → [Letter Manager resolves Template Definition]
    → [Letter Manager retrieves data from Resources]
    → [Awards API provides award-specific data]
    → [Letter Manager populates Letter Instance]
    → [AVSR previews DRAFT PDF]
    → [AVSR submits for review]
    → [LetterInstanceDraftCompleteEvent fired]
    → [Awards receives event]
    → [Authorizer reviews and authorizes award]
    → [Awards calls ECM-L to finalize letter]
    → [ECM-L Service renders final PDF]
    → [LetterInstanceFinalizedEvent fired]
    → [Awards stores PDF in Claim Evidence]
    → [Package Manager distributes (if configured)]
```

**Benefits**:
- ✅ LOB Admin can update templates without IT
- ✅ Changeset approval workflow
- ✅ Test scenarios validate changes
- ✅ Version control automatic
- ✅ Audit trail comprehensive
- ✅ Multi-tenant isolation

---

### 3.5 LOB Integration Steps

#### Step 1: Submit Intake Form
- Complete ECM-L LOB Intake Form
- Identify Connection Configurations needed
- Submit Jira ticket

#### Step 2: Integration Meeting
- Meet with ECM-L team
- Review capabilities
- Discuss letter migration strategy
- Plan connection configurations

#### Step 3: Connection Configuration Setup
- Submit Connection Configuration Intake Forms
- DevOps provisions secrets/issuer keys
- Test connections
- Mark AVAILABLE

#### Step 4: Resource Configuration
- Create Resources in Resource Manager
- Define Key Parameter Types
- Configure data paths
- Test resource retrieval

#### Step 5: Template Migration
- Convert existing templates to ECM-L format
- Create Template Versions in Changesets
- Define inputs and restrictions
- Add conditional logic
- Configure attachments

#### Step 6: Workflow Setup
- Create Workflows for each letter generation process
- Assign Templates to Workflows
- Configure Claim Evidence storage
- Configure Package Manager distribution

#### Step 7: Testing
- Create Test Scenarios for each Template
- Test with sample data
- Validate PDF rendering
- Regression testing

#### Step 8: Approval & Scheduling
- Submit Changesets for approval
- Changeset Publisher reviews
- Schedule release
- Coordinate with downstream systems

#### Step 9: Go-Live
- Monitor Changeset publication
- Verify Templates AVAILABLE
- Test letter generation end-to-end
- Monitor for issues

#### Step 10: Decommission Legacy
- Retire PCGL usage
- Sunset Correspondence Service integration
- Update procedures
- Train users

---

## Part 4: Data Sources Mapping

### 4.1 Connection Configurations Needed

| Resource | API | Purpose |
|----------|-----|---------|
| **Awards Data** | Awards API | Award amounts, decisions, effective dates |
| **Veteran Info** | Veteran API | Name, SSN, service history |
| **Participants** | Participant API | Beneficiaries, dependents, POA |
| **Evidence** | Evidence API | Supporting documents |
| **Claims** | Claims API | Claim details, contentions |
| **POA** | POA API | Power of Attorney info |
| **BEP Services** | BEP | VBA Corporate Database access |

### 4.2 Key Parameter Types

| Parameter | Usage |
|-----------|-------|
| **Award ID** | Context for award-specific letters |
| **Veteran ID** | Participant/Veteran identification |
| **Claim ID** | Associate letters with claims |
| **Beneficiary ID** | For DIC/dependent letters |
| **Award Type** | CPL, CPD, Burial, REPS, etc. |

---

## Part 5: Risk Assessment

### 5.1 Migration Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Data compatibility** | High | Thorough data mapping and transformation testing |
| **User adoption** | Medium | Training, pilot programs, change management |
| **System downtime** | High | Phased rollout, parallel operation period |
| **Template accuracy** | High | Extensive testing, legal review, regression tests |
| **Performance** | Medium | Load testing, monitoring, scaling infrastructure |
| **Integration issues** | High | Comprehensive integration testing, fallback plans |

### 5.2 Success Criteria

✅ **Functional**:
- All letter types migrated successfully
- No loss of functionality
- Letter quality maintained or improved
- Response times acceptable

✅ **Operational**:
- LOBs can self-manage templates
- IT workload reduced
- User satisfaction improved
- Error rates decreased

✅ **Compliance**:
- All regulatory requirements met
- Audit trail complete
- Security standards maintained
- 508 compliance verified

---

## Part 6: Recommendations

### 6.1 Immediate Actions

1. **Complete PFS ADL Integration** (Priority 1)
   - Serves as pilot for ECM-L
   - Addresses immediate pain point (PCGL deprecation)
   - Demonstrates value to stakeholders

2. **Document All Current Letters** (Priority 1)
   - Complete inventory of C&P letters
   - Map to data sources
   - Identify unique requirements

3. **Establish Governance** (Priority 2)
   - Define roles and responsibilities
   - Create approval workflows
   - Establish change management process

### 6.2 Long-Term Strategy

1. **Expand to Other LOBs**
   - Benefits Management Services
   - Veterans Health Administration
   - Memorial Affairs

2. **Enhance Capabilities**
   - Multi-language support
   - Advanced conditional logic
   - Real-time preview improvements
   - Mobile optimization

3. **Continuous Improvement**
   - User feedback loops
   - Template analytics
   - Performance optimization
   - Cost optimization

---

## Part 7: Next Steps

### For CS/P&F Team:

1. ✅ Review this catalog
2. ⏭️ Validate letter list is complete
3. ⏭️ Identify additional manual letters not captured
4. ⏭️ Prioritize letters for migration
5. ⏭️ Assign Technical POCs for each letter type
6. ⏭️ Schedule working sessions with ECM-L team

### For ECM-L Team:

1. ✅ Complete Phase 4 features
2. ⏭️ Support PFS ADL integration
3. ⏭️ Document lessons learned
4. ⏭️ Create template migration toolkit
5. ⏭️ Prepare training materials

### For Awards Team:

1. ⏭️ Complete Kafka consumer implementation
2. ⏭️ Enhance Awards API with letter data endpoints
3. ⏭️ Embed Letter Manager MFE
4. ⏭️ Test integration end-to-end
5. ⏭️ Plan legacy system sunset

---

## Appendices

### Appendix A: Jira Tickets Referenced

**PFS ADL Integration**:
- VBMSR-30957: DIC Grant PFS ADL
- VBMSR-31242: Pension Grant PFS ADL
- VBMSR-30953: Excess Income Denial PFS ADL
- VBMSR-27690: PFS ADL capability

**ECM-L Infrastructure**:
- VBMSR-32947: Infrastructure setup
- VBMSR-32948: BAAZ integration

**Template Management**: 
- VBMSR-32955: Create Changeset
- VBMSR-32956: Manage Template Versions
- VBMSR-32957: Test Template Versions
- VBMSR-32958: Schedule Changesets

**Letter Management**:
- VBMSR-32964: Stand Alone Letter Manager
- VBMSR-32966: Letter Instance Lifecycle
- VBMSR-33100: View PDF Rendered

### Appendix B: Source Documents

1. **238619119** - PFS ADL Letters Awards via ECM-L
2. **3354** - VBMS Awards Architecture
3. **4003AQ** - VBMS 40.1 Awards User Guide
4. **Enterprise Correspondence Management** - ECM-L Architecture

### Appendix C: Glossary

- **ADL**: Automated Decision Letter
- **AVSR**: Awards VSR (Veterans Service Representative)
- **BAAZ**: Benefits Application Authorization Services
- **BEP**: Benefits Gateway Service
- **BPMN**: Business Process Model and Notation
- **C&P**: Compensation and Pension
- **CPD**: Compensation/Pension Death
- **CPL**: Compensation/Pension Live
- **DIC**: Dependency and Indemnity Compensation
- **ECM-L**: Enterprise Correspondence Management - Letters
- **LOB**: Line of Business
- **P&F**: Pension & Fiduciary
- **PCGL**: Personal Computer Generated Letters
- **PFS**: Pension Fiduciary Systems
- **REPS**: Reserve Educational Assistance Program
- **VSR**: Veterans Service Representative

---

**Document Owner**: ECM-L Integration Team  
**Last Updated**: January 14, 2026  
**Status**: Initial Analysis - Pending Validation by CS/P&F POCs  
**Next Review**: Upon receipt of feedback from Technical POCs
