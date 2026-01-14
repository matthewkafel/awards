# Create Award in VBMS and then Authorize - Quick Reference

**Document Type:** Step-by-Step Workflow Guide  
**Environments:** DEV, SQA, WebTest, TEST, LinkTest, UAT, Stage/UAT, PreProd

## Purpose

This document provides a concise, step-by-step workflow for creating and authorizing awards in VBMS Awards. This is a reference guide for VSRs and Authorizers performing the award generation and authorization process.

## Prerequisites

✅ AVSR (Awards VSR) account for award creation  
✅ Authorizer account for award authorization  
✅ Veteran must be Verified in the system  
✅ Claim established for the Veteran  

## Workflow Overview

```
1. Login as AVSR → 2. Create Award → 3. Generate Proposed Award
                                            ↓
4. Authorize (different user) ← 5. Review Proposed Award
```

---

## Part 1: Create Award (AVSR Role)

### Step-by-Step Instructions

| Step | Action | Details |
|------|--------|---------|
| **1** | Login to VBMS Awards | Use your AVSR account credentials |
| **2** | Search for Veteran | Enter Filename or SSN in search |
| **3** | Select Claim Type | Click the Claim Type hyperlink for the Veteran |
| **4** | Add New Award | Click the "Add New Award" button |
| **5** | Select Award Type | Choose "Compensation/Pension Live" |
| **6** | Accept | Click the "Accept" button |
| **7** | Record Decisions | Click the "Record Decisions" button |
| **8** | Display All Claims | Click the "Display All Claims" button |
| **9** | Select Claim | Check the box in "Available Claims" (left side) |
| **10** | Add Claim | Click "Add" to move to "Selected Claims" (right side) |
| **11** | Generate Award | Click the "Generate Award" button |
| **12** | Continue Generation | Click "Continue Generation" button |

### Result
✅ You now have a **Proposed Award** ready for Authorization

**Important Note**: Awards will NOT generate if the Veteran is not Verified in the system.

---

## Part 2: Authorize Award (Authorizer Role)

### Step-by-Step Instructions

| Step | Action | Details |
|------|--------|---------|
| **1** | Close All Sessions | Close all Edge browser sessions completely |
| **2** | Login as Authorizer | Use your Authorizer account credentials |
| **3** | Search for Veteran | Enter Filename or SSN in search |
| **4** | Select Award Type | Click the Award Type link for the Veteran |
| **5** | Record Decisions | Click the "Record Decisions" button |
| **6** | Review Current/Proposed | Click "Review Current/Proposed" |
| **7** | Authorize | Click the "Authorize" button |
| **8** | Continue Authorization | Click the "Continue Authorization" button |
| **9** | Accept Letter | Click the "Accept Letter" button |
| **10** | Confirm | Click the "OK" button |

### Result
✅ **Award is now Authorized!** The claimant is now eligible.

---

## Key Requirements

### User Separation
⚠️ **CRITICAL**: The AVSR who creates the award **CANNOT** be the same user who authorizes it. This is a separation of duties control.

### Veteran Verification
⚠️ **REQUIRED**: The Veteran must be Verified in VBMS before an award can be generated.

### Session Management
💡 **BEST PRACTICE**: When switching roles (AVSR → Authorizer), close all browser sessions completely to avoid permission conflicts.

---

## Common Award Types

While this guide focuses on "Compensation/Pension Live", other award types available:

- **Compensation/Pension Death (CPD)**
- **Accrued Benefits**
- **Burial Benefits**
- **REPS (Educational Assistance)**
- **Clothing Allowance**

See the [VBMS Awards User Guide](../converted/README.md) for detailed scenarios for each award type.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Award won't generate | Verify the Veteran is marked as "Verified" in system |
| Can't authorize | Ensure you're using a different account than the creator |
| Claims not appearing | Click "Display All Claims" to refresh the available claims list |
| Authorization fails | Verify you have Authorizer role permissions |
| Session conflicts | Close all browser sessions and start fresh |

---

## Related Documentation

- **[VBMS Awards User Guide](../converted/README.md)**: Comprehensive guide with 100+ scenarios
- **[VBMS Awards Architecture](../architecture/README.md)**: System architecture and integrations
- **[PFS ADL Letters](../awards-letters/README.md)**: Automated decision letter integration
- **[Workflows Documentation](../workflows.md)**: Detailed process flows

---

## For Training Environments

This workflow works in **all VBMS Awards environments**:
- ✅ DEV - Development
- ✅ SQA - Quality Assurance  
- ✅ WebTest - Web Testing
- ✅ TEST - Integration Testing
- ✅ LinkTest - UAT Testing
- ✅ UAT - User Acceptance
- ✅ Stage/UAT - Staging
- ✅ PreProd - Pre-Production

**Note**: Do NOT practice in Production (PROD) environment.

---

## Quick Command Reference

**Most Common Path**:
```
AVSR: Search → Claim → Add Award → CPL → Record → Generate
Authorizer: Search → Award → Review → Authorize → Accept
```

**Two-Signature Process** (Standard):
1. AVSR creates and generates
2. Authorizer reviews and authorizes

**Three-Signature Process** (Amount >$40,000 or overrides):
1. AVSR creates and generates
2. Authorizer reviews and authorizes
3. Concur Authorizer provides 3rd signature (concurrence)

See [Authorize Award](../converted/README.md#authorize-award) and [Concur Award](../converted/README.md#concur-award) sections in the User Guide for details on multi-signature requirements.

---

**File Location**: `docs/create-award-workflow/content.md`  
**Original PDF**: `Create Award in VBMS and then Au_a488b41857dd4fd2911ce89439462335-140126-1724-946.pdf`  
**Document Length**: Concise quick-reference (1 page in original PDF)
