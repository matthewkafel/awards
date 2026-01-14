# PFS ADL Letters Awards via ECM-L - Architecture Document

**Document ID:** 238619119  
**Solution Status:** FINAL  
**Solution Type:** NEW TENANT APP PROPOSED INTEGRATION WITH NEW TENANT (ECM-L)

## Overview

This document describes the technical architecture for integrating **Pension Fiduciary Systems (PFS) Automated Decision Letters (ADL)** with **Enterprise Content Management for Letters (ECM-L)** within the VBMS Awards application.

## What This Document Contains

### 1. Problem Statement & Business Needs
- **Current State**: PFS ADL Letters manually created using Microsoft Word and PCGL (deprecated tool)
- **Challenges**: 
  - No centralized enterprise correspondence management
  - Lack of letter standardization
  - Resource constraints and user inefficiencies
  - No historical validation
- **Solution**: Migrate PFS ADL letter generation to ECM-L architecture

### 2. Architecture Components

#### Key Systems
- **VBMS Awards**: Award processing and decision management
- **ECM-L Components**:
  - Resource Manager - Manages data connections and resources
  - Definition Manager - Manages letter definitions and templates
  - Letter Manager - Creates and manages letter instances
  - ECM-L Service - Renders letters as PDF
- **Awards API**: Provides award data to populate letters
- **Claim Evidence**: Stores finalized letters

#### Integration Points
- Awards → Letter Manager (draft letter generation)
- Awards → ECM-L API (final letter generation)
- Awards API ← Letter Manager (data retrieval)
- Awards → Claim Evidence (PDF storage)

### 3. User Roles & Capabilities

| Role | Capabilities |
|------|-------------|
| **AVSR** | Create, edit, delete, preview PFS ADL letters and award prints |
| **Authorizer** | Finalize awards without concurrence, view final letters |
| **Concur Authorizer** | Finalize awards with concurrence (amounts >$40k), view final letters |
| **LOB Admin** | Manage product scope, resources, letter definitions |
| **Changeset Editor** | Create and modify letter templates |
| **Changeset Publisher** | Approve and schedule letter template changes |

### 4. Process Workflows

#### Draft Letter Generation
1. AVSR selects "GenLetter" in VBMS Awards
2. Letter Manager MFE creates new letter instance
3. System resolves letter definition and retrieves resources
4. AVSR enters required data in dynamic form
5. AVSR previews draft PDF (with watermark)
6. AVSR submits draft for review
7. System fires `LetterInstanceDraftCompleteEvent`

#### Final Letter Generation
1. Authorizer/Concur Authorizer navigates to Current & Proposed page
2. Selects "Authorize" or "Concur Authorize"
3. Views and reviews draft letter
4. Accepts or rejects letter
5. Awards triggers finalization request to ECM-L
6. ECM-L generates final PDF (no watermark)
7. Awards saves final PDF to Claim Evidence
8. Success/error message displayed

### 5. Technical Details

#### Data Models
- **ECM-L Conceptual Data Model (DIV-1)**: High-level concepts and relationships
- **ECM-L Logical Data Model (DIV-2)**: Abstract structure of data entities

#### Deployment
- **BIP Platform**: ECM-L components deployed on Benefits Integration Platform
- **Environment Mapping**: DEV → INTGD → PREPROD → PERF → PROD
- **Monitoring Tools**: AppDynamics, Prometheus, Grafana, CloudTrail, Kibana, OpenSearch

#### Security
- **Authentication**: PIV card via IAM SSOi
- **Authorization**: BAAZ (Benefits Application Authorization framework)
- **Communication**: TLS/SSL encryption

### 6. Integration Requirements

For VBMS Awards to integrate with ECM-L:

1. **Kafka Consumer**: Subscribe to specific Kafka events for letter lifecycle
2. **Awards API Enhancements**: 
   - Gather Awards data
   - Apply validation and transformation logic
   - Construct letter data objects tailored for each letter type
3. **Letter Manager MFE**: Embed in Awards UI for letter creation

### 7. Letter Types & Phases

PFS ADL Letters are classified as **"Phase 4: Complex Inputs"** letters due to:
- Multiple data resource requirements
- Complex input groups needed
- Advanced transformation logic

**Expected Phase 4 Features**:
- Input Groups
- Attachment Selection Inputs
- Recipient Selection Inputs
- Conditional Attachments
- Data Resource Defaults
- Fragment Selection

## Key Benefits

✅ **Centralized Management**: Single system for all correspondence  
✅ **Self-Service**: LOBs can manage letters without IT intervention  
✅ **Standardization**: Consistent letter templates and content  
✅ **Efficiency**: Automated letter generation and routing  
✅ **Compliance**: Version control and audit trails  
✅ **Scalability**: Enterprise solution for multiple LOBs

## Related Documentation

- [ECM-L Architecture](../ecm-l/README.md) - Full ECM-L system architecture
- [VBMS Awards Architecture](../architecture/README.md) - Awards system architecture
- [Create Award Workflow](../create-award-workflow/README.md) - Step-by-step award creation
- [User Guide](../converted/README.md) - VBMS Awards 40.1 User Guide

## For Copilot Queries

Ask questions like:
- "How does PFS ADL integrate with ECM-L?"
- "What is the draft letter generation workflow?"
- "What are the ECM-L components and their roles?"
- "How do Awards and Letter Manager communicate?"
- "What user roles are involved in letter creation?"

## Document Metadata

**Recommended BIP Tenant**: vbms-awards  
**Recommended Apps**:
- bip-vbms-awards-api
- bip-vbms-awards-legacy
- bip-vbms-awards-ui
- bip-docgen-ecm-l-* (ECM-L suite)

**Sponsoring Organization**: OIT  
**Number of Users**: ~5,000 Awards Users  
**Privacy**: PHI and PII (depends on letter template content)  
**508 Compliance**: Yes

---

**File Location**: `docs/awards-letters/content.md`  
**Original PDF**: `238619119_d6fb888250254a2d9b96445818942323-140126-1724-950.pdf`
