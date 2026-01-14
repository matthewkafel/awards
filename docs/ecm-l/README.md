# Enterprise Correspondence Management - Letters (ECM-L) Architecture

**Solution Type:** Enterprise System  
**Target Scale:** ~40,000 users across 20 Lines of Business, 20 million letters annually  
**Cost Advantage:** 22% cost savings vs. Salesforce alternative

## Overview

This document contains the **complete architecture specification** for the Enterprise Correspondence Management - Letters (ECM-L) system. ECM-L is a centralized, enterprise-level correspondence management system that enables multiple Lines of Business (LOBs) to effectively generate letters relating to Veteran Benefits without IT intervention.

## What is ECM-L?

**ECM-L** is a true enterprise correspondence platform that:
- ✅ **Decouples** letter generation from VBMS umbrella
- ✅ **Empowers** LOBs to self-manage letter templates and definitions
- ✅ **Standardizes** letter creation across VA
- ✅ **Eliminates** IT bottlenecks for letter changes
- ✅ **Provides** version control and audit trails
- ✅ **Supports** multi-tenant isolation for different LOBs

## Core Components

### 1. Resource Manager
**Purpose**: Manages connections to external APIs and data resources

**Capabilities**:
- Create/manage Connection Configurations
- Define Resources (Data/File) 
- Configure Key Parameter Types
- Test API integrations
- Lifecycle management (DRAFT → AVAILABLE → RETIRED → DECOMMISSIONED)

### 2. Definition Manager (Template Manager)
**Purpose**: Manages letter templates and definitions

**Capabilities**:
- Create/edit Template Versions (Full & Fragment)
- Manage Changesets for versioned releases
- Define letter Workflows
- Configure inputs, restrictions, conditional logic
- Test templates with Test Scenarios
- Approval workflows

### 3. Letter Manager
**Purpose**: Create and manage individual letter instances

**Capabilities**:
- Instantiate letters from templates
- Fill in user inputs and data
- Preview draft PDFs (with watermark)
- Submit for review
- Finalize letters (no watermark)
- Lifecycle: DRAFT → READY FOR REVIEW → FINALIZED

### 4. ECM-L Service
**Purpose**: Core rendering and orchestration engine

**Capabilities**:
- Render letters as PDF
- Process Kafka events
- Coordinate between components
- Handle data from Resources

## Key Concepts

### Lifecycle States

The document provides extensive lifecycle diagrams for:

| Element | States |
|---------|--------|
| **Connection Configuration** | INTAKE → PROVISIONED → AVAILABLE → RETIRED → DECOMMISSIONED |
| **Resource Version** | DRAFT → AVAILABLE → RETIRED / DELETED |
| **Changeset** | DRAFT → READY TO TEST → READY FOR APPROVAL → APPROVED → SCHEDULED → PUBLISHED |
| **Template Version** | DRAFT → COMPLETED → TESTED → APPROVED → AVAILABLE → RETIRED |
| **File Version** | DRAFT → COMPLETED → APPROVED → AVAILABLE → RETIRED |
| **Letter Instance** | DRAFT → READY FOR REVIEW → FINALIZED / CANCELLED / ARCHIVED |
| **Workflow** | DRAFT → AVAILABLE → RETIRED / DELETED |

### User Roles

| Role | Responsibilities |
|------|------------------|
| **LOB Administrator** | Manage product scope, resources, workflows |
| **Changeset Editor** | Create/modify templates, test scenarios |
| **Changeset Publisher** | Approve/schedule template releases |
| **Letter Editor** | Create/edit draft letters |
| **Letter Finalizer** | Review and finalize letters |

## Data Models

### Resource Manager Entities
- **Line of Business**: Organization unit
- **Connection Configuration**: API connection details
- **Resource**: External data source
- **Resource Version**: Versioned resource configuration
- **Key Parameter Type**: LOB-specific contextual data type

### Template Manager Entities
- **Workflow**: Letter creation subprocess
- **Template**: Letter definition (Full or Fragment)
- **Template Version**: Versioned template content
- **File Version**: Attached PDF/Image files
- **Changeset**: Grouped template changes for release
- **Test Scenario**: Template validation tests
- **Label**: Template categorization
- **Restriction**: Conditional rules for template availability
- **Input**: User data collection fields

### Letter Manager Entities
- **Letter Instance**: Instantiated letter
- **Key Parameter**: Context identifier (e.g., Claim ID)

## Integration Capabilities

### Claim Evidence & Package Manager

**Claim Evidence**: Document storage for Veterans' files  
**Package Manager**: Mail distribution system

**Configuration Options**:
- Workflow-level: Use Claim Evidence for storage
- Workflow-level: Use Package Manager for distribution  
- Template-level: Mark templates as exempt from Claim Evidence
- Template-level: Mark templates as exempt from Package Manager

**Requirement**: Package Manager requires Claim Evidence (can't distribute what isn't stored)

## Intake Process

### Line of Business Intake
1. Submit **LOB Intake Form** via Jira
2. Integration meeting with ECM-L team
3. Configuration loaded into Resource Manager
4. LOB provisioned with self-service capabilities

### Connection Configuration Intake
1. Submit **Connection Configuration Intake Form**
2. Dev Team creates Change Request
3. Secret/Issuer keys provisioned in Vault
4. Connection Configuration marked PROVISIONED
5. LOB Admin tests and marks AVAILABLE

### System Registry
- Register automated systems that generate letters
- Collect POC information
- Enable alerts for template changes affecting downstream systems

## Process Workflows

The architecture includes **comprehensive BPMN diagrams** for:

1. **Connection Configuration Intake** - Provisioning new API connections
2. **Connection Configuration Decommissioning** - Retiring old connections
3. **Connection Configuration Replacement** - Migrating to new connections
4. **Resource Version Management** - Create/Update/Retire resources
5. **Workflow Management** - Configure workflows with templates
6. **Changeset Lifecycle** - Draft → Test → Approve → Schedule → Publish
7. **Template Version Creation** - Build new template versions
8. **Template Testing** - Validate templates with test scenarios
9. **Changeset Approval** - Review and approve changes
10. **Changeset Scheduling** - Schedule template releases
11. **Letter Finalization** - Draft → Review → Finalize

## Input Types

ECM-L supports extensive input capabilities:

### Simple Inputs
- ✅ Text fields
- ✅ Number fields
- ✅ Boolean (checkboxes)
- ✅ Date/Time fields
- ✅ Address inputs
- ✅ Phone inputs
- ✅ Option selection (dropdowns)

### Complex Inputs
- ✅ Input Groups (repeating sections)
- ✅ Attachment Selection
- ✅ Field Group Options
- ✅ Recipient Selection
- ✅ Data Resource Defaults

### Advanced Features
- ✅ Conditional Logic
- ✅ Fragment Inclusion (reusable template sections)
- ✅ Conditional Attachments
- ✅ Remote Image Support
- ✅ Data Resource Population
- ✅ QR Codes & Barcodes

## Implementation Phases

The roadmap defines **4 phases** with detailed Jira tickets:

**Phase 1: Infrastructure**
- New tenant apps, repos
- BAAZ integration
- Intake process

**Phase 2: Core Management**
- Changeset & Template Management
- Simple Input Support
- Stand-alone Letter Management

**Phase 3: Advanced Inputs**
- Complex Inputs (Input Groups, Attachments)
- Inclusions (Fragments)
- Image Resources
- Connection Configuration Support

**Phase 4: Complex Integration**
- Full API Functionality
- Data Resource Population
- Child Letters
- Barcode Support
- Claim Evidence & Package Manager Integration

## Security

### Authentication
- **BAAZ Framework**: Benefits Application Authorization Services
- **Open Policy Agent (OPA)**: Policy-based access control
- **Self-Service**: LOBs manage their own policies

### Data Provenance
Complete audit trail for every letter:
- Who created it (user)
- When created (timestamp)
- What template version (versioned)
- What data used (source tracked)
- What resources accessed (API logged)

### Transport Security
- TLS/SSL encryption
- Vault for secrets management
- JWT for service authentication

## Deployment

**Platform**: Benefits Integration Platform (BIP)  
**Environments**: DEV → TEST → INT → IV&V/SQA → UAT → PAT → PREPROD → PERF → PROD

**Monitoring**:
- AppDynamics, Prometheus, Grafana
- CloudTrail, Kibana, OpenSearch
- Fluentd for log aggregation

## Cost & Scale

**Cost Analysis**:
- **Custom ECM-L**: Lower total cost of ownership
- **vs. Salesforce**: 22% cost advantage
- **Benefits**: No vendor lock-in, superior performance, better multi-tenant isolation

**Scale Targets**:
- 40,000 users across VA
- 20 Lines of Business
- 20 million letters annually
- Sub-second response times

## Technical Advantages

1. **Performance Optimization**: Built for VA scale
2. **Multi-Tenant Isolation**: Strict separation between LOBs
3. **Customization Flexibility**: No platform constraints
4. **Cost Efficiency**: Lower licensing costs
5. **Vendor Independence**: No Salesforce lock-in
6. **Enterprise Control**: Full system ownership

## Related Documentation

- **[PFS ADL Letters](../awards-letters/README.md)**: First ECM-L use case (Pension Fiduciary)
- **[VBMS Awards Architecture](../architecture/README.md)**: Awards system integration
- **[User Guide](../converted/README.md)**: VBMS Awards 40.1 operations

## For Copilot Queries

Ask questions like:
- "What are the ECM-L components and their purposes?"
- "Explain the Changeset lifecycle in ECM-L"
- "How do LOBs onboard to ECM-L?"
- "What is the letter creation workflow?"
- "How does ECM-L handle template versioning?"
- "What input types does ECM-L support?"
- "Explain the Connection Configuration intake process"
- "How does ECM-L integrate with Claim Evidence?"
- "What are the security features of ECM-L?"
- "What is the roadmap for ECM-L phases?"

## Document Statistics

**Content Size**: 164 KB extracted text  
**Scope**: Complete architecture specification  
**Includes**:
- 10+ detailed lifecycle diagrams
- 15+ process workflow BPMNs
- Complete data models (DIV-1, DIV-2)
- Comprehensive intake procedures
- Full implementation roadmap
- 100+ Jira ticket references

---

**File Location**: `docs/ecm-l/content.md`  
**Original PDF**: `Enterprise Correspondence Manage_7ba8a24f090a4e87880a540b40bd4d05-140126-1728-952.pdf`
