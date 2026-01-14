# VBMS Awards Processing Workflows

This document details the standard workflows for processing awards in VBMS version 40.1.

## Standard Award Processing Workflow

### Overview
The award processing workflow in VBMS follows a structured path from claim decision to payment notification.

```
Claim Decision → Award Calculation → Award Letter Generation → 
Quality Review → Notification Distribution → Payment Processing
```

### Step-by-Step Process

#### 1. Claim Decision Finalized
**Trigger**: Rating Veterans Service Representative (RVSR) completes claim evaluation

**Actions**:
- Rating decision entered into VBMS
- Decision document added to eFolder
- System validates all required fields
- Award eligibility determined

**Required Information**:
- Veteran identification
- Service-connected conditions and ratings
- Effective date of award
- Dependency information
- Payment calculation factors

#### 2. Award Calculation
**System**: VETSNET integration

**Process**:
- VBMS sends rating data to VETSNET
- VETSNET calculates monthly payment amount
- Considers all factors:
  - Disability rating percentages
  - Number of dependents
  - Special monthly compensation eligibility
  - Concurrent receipt rules
  - Other benefit offsets
- Calculation results returned to VBMS

**Validation Checks**:
- Payment amount reasonableness
- Dependency verification
- Effective date validation
- Historical payment comparison

#### 3. Award Letter Generation
**System**: VBMS-A (Awards module)

**Automated Actions**:
- Appropriate template selected based on award type
- Personalized content populated:
  - Veteran name and contact information
  - Award details and amounts
  - Effective dates
  - Payment schedule
  - Rights and appeals information
- PDF generated
- Letter added to eFolder

**Template Types**:
- Initial award notification
- Increased award notification
- Decreased award notification
- Denial with partial award
- Special monthly compensation awards

#### 4. Quality Review
**Responsibility**: Awards Authorizer or Quality Reviewer

**Manual Review Steps**:
1. Open claim in VBMS work queue
2. Review rating decision for accuracy
3. Verify award calculation
4. Check notification letter content
5. Confirm veteran contact information
6. Approve or return for correction

**Automated Checks**:
- Mathematical accuracy of calculations
- Template field population
- Required information completeness
- System data consistency

**Decision Points**:
- **Approve**: Proceed to distribution
- **Return for Correction**: Back to appropriate step
- **Escalate**: Complex cases to supervisor

#### 5. Notification Distribution
**Methods**:
- **Postal Mail**: Physical letter sent to veteran's address
- **Electronic Notification**: If veteran opted in for digital communications
- **Representative Copy**: Sent to VSO if applicable

**System Actions**:
- Update claim status to "Notification Sent"
- Record distribution date
- Generate tracking information
- Update veteran's eFolder

**Timeline**:
- Electronic: Same business day
- Postal: 3-5 business days for delivery

#### 6. Payment Processing
**Financial Integration**:
- Award data transmitted to VA financial systems
- Payment scheduled based on effective date
- First payment processing initiated
- Recurring payments scheduled

**Payment Delivery**:
- Direct deposit (preferred method)
- Paper check if no banking information
- Fiduciary payment if appointed

**Confirmation**:
- Payment confirmation in VBMS
- Veteran can verify via VA.gov or eBenefits
- Representative notification if requested

## Special Workflows

### Clothing Allowance Workflow

#### Automated Process
1. **Eligibility Check**: System reviews for qualifying conditions
   - Prosthetic/orthotic device use
   - Skin medication that damages clothing
   - Service-connected condition requiring special garments

2. **Annual Review**: Automated check each year for continuing eligibility

3. **Auto-Approval**: If criteria met, automatic approval without manual intervention

4. **Payment Processing**: Direct payment scheduled

5. **Notification**: Automated letter confirming award

#### Manual Intervention Points
- First-time applications
- Changed circumstances
- Appeals or disputes

### Dependency Change Workflow

#### Trigger Events
- Marriage
- Divorce
- Birth/adoption of child
- Child turning 18
- Child in school (18-23)
- Death of dependent

#### Process Steps
1. **Notification Received**:
   - Veteran submits VA Form 21-686c
   - Evidence documents uploaded to eFolder

2. **Verification**:
   - Supporting documentation reviewed
   - Database checks (marriage/death records)
   - School enrollment verification if applicable

3. **Award Recalculation**:
   - VETSNET recalculates with new dependency status
   - Effective date determined
   - New award amount calculated

4. **Notification**:
   - Award adjustment letter generated
   - Explains change and new amount
   - Effective date clearly stated

5. **Payment Adjustment**:
   - New payment amount effective from specified date
   - Retroactive payments if applicable
   - Overpayment recovery initiated if needed

### Appeal Workflow

#### Appeal Filed
1. **Notice of Disagreement (NOD)** received
2. **System Update**: Claim status changed to "On Appeal"
3. **Payments Continue**: At current level unless changed by new decision
4. **Case Assignment**: To Decision Review Officer (DRO) or Higher-Level Reviewer

#### Review Process
1. **Evidence Review**: All new and existing evidence considered
2. **DRO Review Meeting**: Optional veteran meeting
3. **Decision**:
   - Affirm original decision
   - Increase award
   - Decrease award
   - Remand for additional development

#### Post-Decision
1. **Supplemental Statement of the Case (SSOC)** if needed
2. **Award adjustment** if decision changed
3. **Notification** of appeal outcome
4. **Further appeal rights** explained

### Increase/Decrease Workflow

#### Increased Award
**Triggers**:
- New service-connected condition
- Worsening of existing condition
- Additional evidence of severity

**Process**:
1. New examination scheduled if required
2. Rating reevaluation
3. Award recalculation
4. Retroactive payment to effective date
5. New award notification

#### Decreased Award
**Triggers**:
- Improvement in condition
- Loss of dependent
- Reduction examination results

**Process**:
1. Proposed reduction notice (due process)
2. 60-day waiting period for response
3. Review of any new evidence submitted
4. Final decision
5. Award reduction effective date
6. Overpayment determination if applicable

### Emergency/Expedited Processing

#### Qualifying Criteria
- Veteran experiencing homelessness
- Extreme financial hardship
- Terminal illness
- Medal of Honor recipient
- Former POW
- Age 85 or older

#### Expedited Process
1. **Priority Flagging**: Claim marked for expedited handling
2. **Fast-Track Review**: Assigned to specialized team
3. **Accelerated Timeline**: Target completion in days vs. weeks
4. **Interim Payment**: If applicable, temporary payment while processing
5. **Standard Follow-up**: Regular workflow completion

### Retroactive Payment Workflow

#### Calculation
- Determine effective date of award
- Calculate monthly amounts from effective date to present
- Account for any interim payments
- Include interest if applicable

#### Payment Processing
1. **Lump Sum Preparation**: Total retroactive amount calculated
2. **Quality Check**: Verification of calculation
3. **Payment Authorization**: Approved by appropriate authority
4. **Distribution**: Separate payment from ongoing monthly benefit
5. **Documentation**: Detailed breakdown provided to veteran

## Workflow Best Practices

### For VA Staff

1. **Complete Documentation**: Ensure all required information in claim file
2. **Timely Processing**: Work claims in priority order
3. **Quality Over Speed**: Accuracy prevents rework and appeals
4. **Communication**: Keep veterans informed of status
5. **Collaboration**: Consult with specialists when needed

### For Representatives

1. **Evidence Submission**: Upload all supporting documents promptly
2. **Complete Forms**: Ensure all VA forms fully completed
3. **Follow-up**: Monitor claim status regularly
4. **Veteran Communication**: Keep veteran informed
5. **Timely Response**: Respond to VA requests quickly

### Common Pitfalls to Avoid

- Incomplete dependency information
- Missing or unclear medical evidence
- Incorrect effective date calculations
- Failure to identify special monthly compensation eligibility
- Not updating veteran contact information
- Insufficient documentation for expedited processing

## Workflow Monitoring

### Performance Metrics
- Average days to complete each step
- Queue depth at each stage
- Error rates and rework percentage
- Veteran satisfaction scores

### Queue Management
- Work oldest claims first (FIFO - First In, First Out)
- Exception for expedited cases
- Balance workload across team
- Monitor for bottlenecks

## System Notifications and Alerts

### Automated Alerts
- Claim approaching target date
- Missing information detected
- Quality check failure
- Payment processing issue
- Veteran inquiry received

### User Notifications
- New claims assigned
- Claims returned for correction
- Supervisor review required
- System maintenance scheduled

For detailed feature information, see [Features](features.md). For system overview, see [Overview](overview.md).
