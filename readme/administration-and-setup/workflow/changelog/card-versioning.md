# Card Versioning System - October 2025 Update

**Document:** Workflow Card Versioning Overview
**Last Updated:** October 23, 2025
**Status:** Complete

---

## Overview

The DocBits Workflow Engine uses **integer-based versioning** to manage card evolution while maintaining backward compatibility. This document provides an overview of the versioning system.

---

## What is Card Versioning?

### Concept
Each workflow card can have multiple versions, allowing the system to:
- Add new features without breaking existing workflows
- Support deprecated functionality while phasing it out
- Evolve card capabilities over time
- Maintain backward compatibility

### Version Structure
- **Format:** Integer values (1, 2, 3, 4, 5...)
- **Identification:** Composite key of (card_type, card_version)
- **Status:** Each version has deprecated/enabled flags

### Example
The `tasks_create` card has evolved through 4 versions:
- **v1:** Original task creation (deprecated)
- **v2:** Added translation support (deprecated)
- **v3:** Experimental decision tree support (deprecated)
- **v4:** Generic work item type support (current active)

---

## Key Statistics

### Versioning Overview
| Metric | Value |
|--------|-------|
| **Cards with Multiple Versions** | 30+ |
| **Total Version Records** | 90+ |
| **Versions per Card (average)** | 3 |
| **Maximum Versions** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |
| **Deprecated Versions** | 9 |
| **Fully Disabled Cards** | 2 |

### Version Distribution
- **2 Versions:** 14 cards (simpler evolution)
- **3 Versions:** 11 cards (moderate evolution)
- **4 Versions:** 4 cards (significant evolution)
- **5 Versions:** 1 card (most evolved: CONDITION_DOC_TO_PO_UNIT_PRICE)

---

## Common Version Patterns

### Pattern 1: Translation Key Adoption (v1 → v2)

**Affected:** 15+ cards

**Change:**
```
v1: Plain text: "Call Api: [param] with method: [param]"
v2: With i18n: "trnsl_%call_api trnsl_be_% Call Api: [param]..."
```

**Purpose:** Enable multi-language support

**Cards:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS, and more

**Migration:** Safe - no functional changes

---

### Pattern 2: Decision Tree Integration (v2 → v3)

**Affected:** 5 cards

**Change:** Addition of decision tree parameter

```
v2: Create a new Task with title: [param], description: [param]...
v3: (same as v2) + "Use decision tree, if available: [param]"
```

**Purpose:** Support decision table results

**Cards:**
- tasks_create (v3 deprecated)
- ACTION_TASK_FOR_GROUP (v3 deprecated)
- DOC_USER_ASSIGN (v3 deprecated)
- DOC_GROUP_ASSIGN (v3 deprecated)
- ACTION_DECISION_TREE_CREATE_TASKS

**Status:** Deprecated - decision tree approach was experimental

---

### Pattern 3: Generic Type Evolution (v3 → v4)

**Affected:** 4 cards

**Change:** "Task" becomes flexible work item type

```
v3: Create a new Task with the title: [param]
v4: Create a new [param] with the title: [param]
```

**Purpose:** Support Tasks, Tickets, Issues, and other work item types

**Cards:**
- tasks_create (v4 current)
- ACTION_TASK_FOR_GROUP (v4 current)
- ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP (v3 current)
- ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK (v3 current)

**Current Status:** Active and recommended

---

### Pattern 4: Tolerance Parameters (PO Cards)

**Affected:** 6 PO comparison cards

**Change:** Addition of tolerance/variance support

```
v2: Document value [operator] Purchase Order value
v3+: Document value [operator] PO value with tolerance [amount] [unit]
```

**Purpose:** Allow acceptable variance in matching (e.g., 2% price difference OK)

**Key Cards:**
- CONDITION_DOC_TO_PO_UNIT_PRICE (evolved to v5 with tolerance)
- CONDITION_DATES_OPERATOR_OC_LINE_ITEMS (v2 → v3)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY

**Benefit:** More realistic matching criteria

---

### Pattern 5: Comparison Mode Parameters

**Affected:** 3 PO comparison cards

**Change:** Support for different comparison algorithms

```
v3: Standard comparison logic
v4: Same logic + "Compare as [param]" parameter
```

**Purpose:** Flexible comparison methods

**Cards:**
- COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE (v2-4)
- CONDITION_OC_TO_PO_ITEMS (v3-4)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v3-4)

---

### Pattern 6: Workflow Triggers

**Affected:** STAUS_CHANGE only

**Change:** Auto-trigger workflows on status change

```
v2: Change Status to [param]
v3: Change Status to [param], trigger Workflows [param]
```

**Purpose:** Cascade status changes across workflows

---

## Most Evolved Cards

### 1. CONDITION_DOC_TO_PO_UNIT_PRICE (5 versions)

**Evolution Path:** v2 → v3 → v4 → v5

- **v2:** Basic unit price comparison
- **v3:** Same translation key (v2)
- **v4:** Added comparison mode parameter
- **v5:** Added tolerance threshold parameter

**Current:** v5 (with tolerance support)

---

### 2. CONDITION_OC_TO_PO_ITEMS (4 versions)

**Evolution Path:** v1 → v2 → v3 → v4

- **v1:** Basic item matching (deprecated)
- **v2:** Added comparison method parameter
- **v3:** Enhanced with translation keys
- **v4:** Added compare mode parameter

**Current:** v4

**Avoid:** v1 (deprecated)

---

### 3. tasks_create (4 versions)

**Evolution Path:** v1 → v2 → v3 → v4

- **v1:** Original implementation (deprecated)
- **v2:** Added translation support (deprecated)
- **v3:** Added decision tree (deprecated)
- **v4:** Generic work item types (current)

**Current:** v4 (recommended)

**Timeline:**
```
v1 → deprecated (old)
  → v2 → deprecated (translation added)
    → v3 → deprecated (decision tree experiment)
      → v4 → CURRENT & ACTIVE
```

---

## Deprecation Status

### Fully Deprecated Versions (Do Not Use)

| Card | Version | Reason | Alternative |
|------|---------|--------|-------------|
| tasks_create | v1 | Very old | Use v4 |
| tasks_create | v3 | Decision tree deprecated | Use v4 |
| ACTION_TASK_FOR_GROUP | v3 | Decision tree deprecated | Use v4 |
| DOC_USER_ASSIGN | v3 | Decision tree deprecated | Use v2 |
| DOC_GROUP_ASSIGN | v3 | Decision tree deprecated | Use v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Very old | Use v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Very old | Use v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Features reverted | Use v3 |

### Fully Disabled Cards (Cannot Use)

| Card | Versions | Notes |
|------|----------|-------|
| DOC_SUBORG_CHANGE | v1, v2 | Unsupported functionality |
| RUN_SCRIPT | v2, v3 | Replaced by ACTION_RUN_DOCOPERATOR_SCRIPT |

---

## Version Recommendations

### By Use Case

**New Workflow Creation:**
- Always use the **highest enabled version number**
- Provides latest features and improvements
- Supported and documented

**Existing Workflow Maintenance:**
- Continue using current version if it works
- Plan migration when feasible
- No urgent need to upgrade

**Legacy Workflow Migration:**
- Identify version currently in use
- Plan upgrade path
- Test thoroughly before deploying

---

## How Versions Work

### Version Selection
When creating a workflow, you select which version of a card to use. Example:
- Use `tasks_create v4` for new task creation (recommended)
- Use `tasks_create v2` if legacy systems require it (older but works)
- Do NOT use `tasks_create v1` (deprecated)

### Backward Compatibility
- Newer versions don't break older workflows
- Old workflows continue working with their original version
- Can upgrade workflows gradually

### Technical Implementation
Versions are managed at the database level:
```
card_templates table (PostgreSQL)
- card_type: Identifies the card (e.g., "tasks_create")
- card_version: Version number (e.g., 2, 3, 4)
- deprecated: Boolean flag
- enabled: Boolean flag
- text: Card description/parameters
```

---

## For Documentation Purposes

### Understanding Version Info
When you see "Card v3" in documentation:
- It refers to version 3 of that specific card
- Check [Full Versioning Reference](../../docs/card_version.md) for details
- Verify which version is recommended

### Checking Your Version
To know which version you're using:
1. Open the card in your workflow
2. Check the version number displayed
3. Compare with recommendations in guides

### Version Evolution Timeline
- **2024-2025:** Ongoing evolution
- **October 2025:** Complete versioning documentation
- **Future:** Continued improvements

---

## Related Documentation

### Comprehensive Reference
→ [Full Card Versioning Reference](../../docs/card_version.md)

Includes:
- All 30+ cards with versions
- Detailed text evolution for each
- Specific parameter changes
- SQL queries for version lookup

### Card-Specific Guides
→ [Workflow Guides](../)

Documentation for each card with version recommendations

### Version History Details
Each guide includes version information and migration notes

---

## Quick Reference

### Cards with Most Versions
1. CONDITION_DOC_TO_PO_UNIT_PRICE - 5 versions
2. CONDITION_OC_TO_PO_ITEMS - 4 versions
3. tasks_create - 4 versions
4. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE - 3 versions
5. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY - 4 versions

### Most Common Evolution Pattern
**Translation Key Adoption (v1 → v2)** - 15+ cards

### Most Significant Change
**Generic Type Evolution (v3 → v4)** - Changed from "Task" to flexible work item type

### Fully Disabled
- DOC_SUBORG_CHANGE
- RUN_SCRIPT

---

## Frequently Asked Questions

### Q: Which version should I use?
A: Use the **highest enabled version** unless you have a specific reason to use an older version.

### Q: Can I upgrade my workflow to a newer version?
A: Yes, but test thoroughly. Some versions have different parameter requirements.

### Q: What happens if I use a deprecated version?
A: It continues to work, but you won't get new features. Migration recommended.

### Q: Can I use a disabled card?
A: No, disabled cards cannot be used. Use the recommended alternative instead.

### Q: How do I know if my card needs upgrading?
A: Check the [Full Versioning Reference](../../docs/card_version.md) for your card type and follow the recommendations.

---

## Best Practices

1. **New Workflows:** Use latest stable version
2. **Updates:** Check for new versions periodically
3. **Testing:** Test version upgrades in sandbox first
4. **Documentation:** Refer to card-specific guides for version details
5. **Migration:** Plan upgrades incrementally
6. **Support:** Contact support if version compatibility questions arise

---

## Summary Table

| Card Type | Current Version | Total Versions | Status | Notes |
|-----------|-----------------|----------------|--------|-------|
| tasks_create | 4 | 4 | Active | Most evolved; v3 deprecated |
| CONDITION_DOC_TO_PO_UNIT_PRICE | 5 | 4 | Active | Highest version count |
| CONDITION_OC_TO_PO_ITEMS | 4 | 4 | Active | v1 deprecated |
| ACTION_TASK_FOR_GROUP | 4 | 3 | Active | v3 deprecated |
| ACTION_RUN_DOCOPERATOR_SCRIPT | 3 | 3 | Active | v4 deprecated/disabled |
| Most cards | 2 | 2 | Active | v1 → v2 pattern |

---

## See Also

- 📖 [Full Card Versioning Reference](../../docs/card_version.md)
- 🔗 [Workflow Guides](../)
- 📋 [October 2025 Release Notes](./2025-10-october.md)
- 🔄 [Workflow Linking Analysis](../../WORKFLOW_LINKING_MAP.md)

---

**Last Updated:** October 23, 2025
**Source:** postgres-dev-docflow database
**Status:** Complete Reference
