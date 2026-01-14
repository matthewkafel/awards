# VBMS Awards Architecture Documentation

**VASI ID:** 3354  
**Document Status:** Final (updated for 1/20/26 submission)  
**BIP Tenant**: vbms-awards

## Overview

Complete architectural documentation for the **Veterans Benefits Management System - Awards (VBMSA)** application, which resides on the Benefits Integration Platform (BIP) and provides the Veterans Benefits Administration with processing capabilities to generate and authorize awards for Veterans and their beneficiaries.

## System Information

**Primary Function**: Prepare, calculate, determine, authorize, and maintain award history for Veterans and beneficiaries

**Tenant Apps in Production**:
- `bip-vbms-awards-legacy` (Main application)

**Tenant Apps Not in Production**:
- `bip-vbms-awards-api` (Modernization)
- `bip-vbms-awards-ui` (Modernization UI)

**Configuration Repo**: `bip-vbms-awards-config`

## Key Metrics

| Metric | Value |
|--------|-------|
| **Users** | 4,900 |
| **Deployment Date** | April 2014 |
| **eMASS ID** | 2488 (VBMS Awards) |
| **Estimated Monthly Cost** | $11,323 total |
| - Production | $3,610 |
| - PreProd | $3,606 |
| - Stage | $1,012 |
| - Dev | $3,095 |

## Privacy & Security

**Privacy Classification**: ✅ Both PHI and PII
- Veteran PII: File number/SSN for participant search
- Spouse/Dependent PII: SSN and DOB stored
- Veteran/Recipient: Mailing addresses
- Veteran PHI: Disability decision information

**508 Compliance**: ✅ Yes

## Architecture Components

### Use Cases & Actors

#### User Roles
1. **Awards VSR** - Primary adjudicator for C&P benefits
2. **Authorizer** - Reviews VSR work, provides 2nd signature
3. **Supervisor** - Provides 3rd signature for awards >$25k
4. **Observer** - Read-only access for QA, training
5. **Clothing Allowance Admin** - Manages clothing allowance awards
6. **VBMS-Awards Application Admin** - Configures system settings
7. **Central Office (CO) Rep** - CO user with all VSR/Authorizer/Supervisor operations

#### Main Capabilities
- ✅ View Awards
- ✅ Review Decisions
- ✅ Add, Delete, Update Awards
- ✅ Authorize Awards
- ✅ Concur Awards (for amounts >$25k)
- ✅ Suspend or Resume Beneficiaries
- ✅ Configure Awards Application

### Integration Systems

| System | VASI ID | Purpose | Protocol |
|--------|---------|---------|----------|
| **BEP Services** | 1898 | Access to VBA Corporate Database | SOAP/REST (443) |
| **VBMS Exams** | 1728 | Exam status notifications | SOAP (443) |
| **Correspondence Service** | 3008 | Generate letters & data sheets | SOAP (443) |
| **VBMS Rating** | 3233 | Rating decisions data | SOAP (443) |
| **VBMS Fiduciary** | 3026 | Create/update fiduciary claims | SOAP (443) |
| **Claim Establishment (CEST)** | 3263 | Save draft decisions | REST (443) |
| **Claim Evidence** | 3023 | Store/retrieve evidence files | REST (443) |
| **VetServices Awards API** | 3232 | Attorney fees & debt values | REST (443) |
| **BSS** | 2985 | Authentication via PIV card | REST (443) |

### System Interface Flows

The architecture document includes detailed Service Resource Flows showing:

**Controllers**:
- AccruedDecisionsController
- RecipientsController  
- BrokeringController
- ImportEvidenceListController
- BurialController
- MainController
- CaoController
- AwardsHistoryController
- PublicLaw5302bController
- IssueDispositionController

**Key Operations**: Each controller interacts with multiple BEP services (AwardsService, ClaimsService, AccruedDecisionService, PersonWebService, AddressService, BurialDecnService, FinancialDecnService, etc.)

## Data Models

### Conceptual Data Model (DIV-1)
High-level data concepts showing relationships between:
- Awards
- Claims
- Veterans
- Beneficiaries
- Decisions
- Payments

### Logical Data Model (DIV-2)
Abstract structure with primary entities and relationships

### Physical Data Model (DIV-3)
Detailed database structure (see full architecture document)

## Technology Stack

| Component | Vendor | Product | Version | TRM ID |
|-----------|--------|---------|---------|--------|
| **Application Server** | Oracle | Weblogic | 12 | 19 |
| **Database** | Oracle | Oracle DB | Link 7 | 9 |

## Environment Mapping

| VBMS Environment | BEP Environment | Description |
|------------------|-----------------|-------------|
| **Dev** | DEV | First proof of integration |
| **DEVTest** | Webtest | Alternate dev cycle |
| **SQA** | INTGD | Independent QA verification |
| **UAT** | LinkTest | User acceptance testing |
| **Pdt** | DEV2 | Production code snapshot |
| **Demo** | Academy (ACAD) | Training environment |
| **Perf** | PERF | Load testing |
| **PREPROD** | PREPROD | Pre-production testing |
| **PRODTest** | PRODTest | Production triage |
| **Production** | PROD | Live production |

## Infrastructure & Operations

### Network Configuration
- **Platform**: AWS VPC
- **Network Management**: AWS and VAEC/NSOC
- **Access**: Via AWS console for VPC management
- **Components**: NAT, Firewall policies, Security groups, Load balancers, NACL

### Monitoring & Metrics
**Tools**:
- Kubernetes Dashboard
- AppDynamics
- Oracle Enterprise Manager (OEM)
- Nagios
- Hazelcast
- Splunk

**Purpose**: Real-time monitoring, alerting, issue resolution, trend analysis

### Logging
**LCE (Life Cycle Engineering)**: 
- Centralized log framework
- Normalizes, stores, indexes logs
- Web-based query interface
- Primary IA logging

**Splunk**:
- Real-time WebLogic error logs
- Pre/post-deployment error baselines
- Error trend reporting
- Automated error tracking alerts

### Auditing
**Build Audits**:
- Version Description Document (VDD) verification
- Jira/GitHub work item comparison
- Change log reviews
- Requirements traceability
- Configuration audits (functional & physical)

### Security
**Transport Security**: 
- TLS/SSL with VA-issued certificates

**Service Authentication**:
- JWT with shared secrets
- Secrets stored in Vault

**User Authentication**:
- PIV card via IAM SSOi
- BSS integration for station selection

## Business Process Workflows

The architecture includes detailed process models for:
- Award generation workflow
- Authorization workflow  
- Concurrence workflow
- Suspend/Resume workflow
- GAO (General Accounting Office) override workflow
- History and decision tracking

## Related Documentation

- [PFS ADL Letters Architecture](../awards-letters/README.md) - ECM-L integration for PFS letters
- [ECM-L Architecture](../ecm-l/README.md) - Enterprise correspondence system
- [Create Award Workflow](../create-award-workflow/README.md) - Step-by-step procedures
- [User Guide](../converted/README.md) - VBMS Awards 40.1 User Guide

## For Copilot Queries

Ask questions like:
- "What are the main components of VBMS Awards architecture?"
- "How does Awards integrate with BEP services?"
- "What are the user roles and their permissions?"
- "Explain the environment mapping for VBMS Awards"
- "What monitoring tools are used for Awards?"
- "How does authentication work in VBMS Awards?"

## GitHub Repositories

- **Legacy**: `bip-vbms-awards-legacy` (DVA)
- **Modernization API**: `bip-vbms-awards-api` (DVA)
- **Modernization UI**: `bip-vbms-awards-ui` (DVA)
- **Configuration**: `bip-vbms-awards-config` (DVA)

## Support Links

- **VBMS Awards Tenant**: Tenant Level Documentation
- **BIH (Benefits Integration Hub)**: Integration services
- **MSR**: Solution and support resources

---

**File Location**: `docs/architecture/content.md`  
**Original PDF**: `3354_VBMS Awards Architecture_ae8c9f20b5544d709516604e571959d6-140126-1724-948.pdf`
