---
hidden: true
---

# Workflow Card Release & Version History

## Version Control Principles

<figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 13.41.53.png" alt=""><figcaption>Workflow Version Control System</figcaption></figure>

### Version 8.5.2024 - Core Versioning Features

The DocBits Workflow Engine implements robust version control for all workflow cards:

1. **Version Control**: Each card can have multiple versions, each representing a different set of conditions or actions. This allows you to experiment with or tweak the rules without affecting the currently active workflow.
2. **Seamless Upgrades**: When you need to update a rule or condition due to changes in your document processing requirements, you can create a new version of the card. This approach ensures that any modifications are deliberate and tested before they replace the current version. It minimizes errors and potential disruptions in your document processing.
3. **Maintaining Consistency**: Keeping the original card version unchanged until you decide to upgrade ensures that ongoing processes are not affected. You can run tests and validations on the new version without impacting live data or workflows.
4. **Flexibility and Testing**: Multiple versions enable testing different scenarios in a controlled environment. You can see the effects of new rules or changes on your document processing workflow without making permanent changes. Once you are satisfied with the results, you can then choose to apply the new version.

---

## Card Versioning Overview

### Statistics

| Metric | Value |
|--------|-------|
| **Cards with Multiple Versions** | 30+ |
| **Total Version Records** | 90+ |
| **Current Active Versions** | 81+ |
| **Deprecated Versions** | 9 |
| **Fully Disabled Cards** | 2 |
| **Latest Version (Max)** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |

### Version Range
- **Minimum:** v1
- **Maximum:** v5
- **Average Versions per Card:** 3

---

## Detailed Card Version Changes

### 🔧 ACTION CARDS - External Integration & Execution

#### 1. CALL_API
**Versions:** v1, v2 (Current: v2)

📖 **Guide:** [Call External API Guide](../then/action/call-api-guide.md)

| Version | Translation | Status | Key Changes |
|---------|-------------|--------|-------------|
| v1 | No | Active | Basic API call without translation keys |
| v2 | Yes | ✅ Current | Added `trnsl_%call_api` for multi-language support |

**What Changed:** Added internationalization (i18n) support with translation keys. Functionality remains identical.

**Before (v1):**
```
Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**After (v2):**
```
trnsl_%call_api trnsl_be_% Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Recommendation:** Use v2 for all new workflows (includes language support)
**Backward Compatibility:** ✅ v1 still works

---

#### 2. HTTPS Request (HTTPS_REQUEST)
**Versions:** v1, v2 (Current: v2)

| Version | Translation | Status | Key Changes |
|---------|-------------|--------|-------------|
| v1 | No | Active | Simple HTTP request |
| v2 | Yes | ✅ Current | Added `trnsl_%send_https_request` translation keys |

**What Changed:** Added translation support. Core webhook/request functionality unchanged.
**Recommendation:** Use v2 (multi-language support)

---

#### 3. ACTION_RUN_DOCOPERATOR_SCRIPT ⚠️
**Versions:** v2 (Current), v3, v4 (Deprecated & Disabled)

| Version | Translation | Status | Key Changes |
|---------|-------------|--------|-------------|
| v2 | Yes | Active | Original DocOperator implementation |
| v3 | Yes | Active | Added "Execute the prompt" parameter for additional control |
| v4 | Yes | ❌ DEPRECATED & DISABLED | Removed "Execute" parameter (reverted) |

**Evolution Path:** v2 → v3 (added parameter) → v4 (reverted - not recommended)

**What Changed:**
- v2 → v3: Added optional execution control parameter for more flexibility
- v3 → v4: Removed the parameter after further analysis (deprecated)

**Recommendation:** Use v3 for new workflows (latest active version with all features)
**Migration:** If using v4, switch to v3 ⚠️

---

#### 4. ACTION_TASK_FOR_GROUP
**Versions:** v2, v3 (Deprecated), v4 (Current)

📖 **Guide:** [Task Assignment Guide](../then/task/task-assignment-guide.md)

| Version | Changes | Status | Type Parameter |
|---------|---------|--------|-----------------|
| v2 | Original implementation | Active | "Task" (fixed) |
| v3 | + Decision tree support | ❌ DEPRECATED | "Task" (fixed) |
| v4 | - Decision tree, + Generic type | ✅ Current | Generic type (flexible) |

**Evolution:** v2 → v3 (decision tree experiment) → v4 (generic types, decision tree removed)

**v2 → v3 Change (Decision Tree Experiment):**
```
Before: "Create a new Task with the title: [param] ... and assign to group [param]"
After:  "Create a new Task with the title: [param] ... and assign to group [param].
         Use decision tree, if available: [param]"
```

**v3 → v4 Change (Generic Types + Decision Tree Removal):**
```
Before (v3): "Create a new Task with the title: [param] ... "
After (v4):  "Create a new [param] with the title: [param] ... "
```

**What Changed:**
- v2 → v3: Added `decision tree, if available: [param]` parameter
- v3 → v4:
  - ❌ Removed decision tree parameter
  - ✅ Changed "Task" → generic `[param]` (supports Task, Ticket, Issue, etc.)
  - Added translation key `trnsl_%task_for_group_v4`

**Why:** v3 decision tree approach was experimental. v4 provides better flexibility with generic work item types.
**Recommendation:** Use v4 (current, most flexible)

---

#### 5. ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP
**Versions:** v2, v3 (Current)

| Version | Task Type | Status | Key Difference |
|---------|-----------|--------|-----------------|
| v2 | "task" (fixed) | Active | Original version |
| v3 | Generic type | ✅ Current | Changed to flexible `[param]` |

**What Changed:** v2 → v3: "Create a new task" → "Create a new [param]" (supports any work item type)
**Recommendation:** Use v3

---

#### 6. RUN_WORKFLOW
**Versions:** v1, v2 (Current)

**What Changed:** v1 → v2: Added `trnsl_%run_workflow` translation keys
**Recommendation:** Use v2

---

### 📊 PO COMPARISON & VALIDATION CARDS

#### 1. CONDITION_DOC_TO_PO_UNIT_PRICE ⭐ (Most Evolved - 5 Versions)
**Versions:** v2, v3, v4, v5 (Current)

📖 **Guide:** [PO Matching Complete Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#2-unit-price-comparison-document-vs-po)

| Version | Changes | Status | Tolerance | Comparison |
|---------|---------|--------|-----------|------------|
| v2 | Basic price comparison | Active | ❌ No | Basic |
| v3 | Same as v2 | Active | ❌ No | Basic |
| v4 | + Compare mode parameter | Active | ❌ No | ✅ Yes |
| v5 | + Tolerance parameters | ✅ Current | ✅ Yes (amount + unit) | ✅ Yes |

**Evolution Path:** v2 → v3 (no change) → v4 (comparison modes) → v5 (tolerance thresholds)

**v2 → v3:** No functional change (same translation key)

**v3 → v4 Change (Comparison Mode Added):**
```
Before: "[document] unit price is [operator] to purchase order"
After:  "[document] unit price is [operator] to purchase order. Compare as [mode]"
```

**v4 → v5 Change (Tolerance Parameters Added):**
```
Before: "[document] unit price is [operator] to purchase order. Compare as [mode]"
After:  "[document] unit price is [operator] to purchase order, with tolerance of [amount] [unit].
         Compare as [mode]"
```

**What Changed:**
- **v2 → v3:** No functional change
- **v3 → v4:** Added `Compare as [param]` - Support different comparison operators
- **v4 → v5:** Added tolerance parameters:
  - `with tolerance of [amount] [unit]`
  - Example: "with tolerance of 2 %" or "with tolerance of 100 EUR"
  - Supports: %, EUR, $, and other currencies

**Use Cases:**
- v2/v3: Strict matching (exact prices only)
- v4: Different comparison methods
- v5: Flexible variance acceptance (e.g., accept 2% price differences) ✅ RECOMMENDED

**Recommendation:** Use v5 for modern PO matching workflows

---

#### 2. CONDITION_OC_TO_PO_ITEMS
**Versions:** v1 (Deprecated), v2, v3, v4 (Current)

| Version | Changes | Status | Compare Feature |
|---------|---------|--------|-----------------|
| v1 | No translation, no method | ❌ DEPRECATED | Basic |
| v2 | + Translation keys, + method | Active | Basic method |
| v3 | Same as v2 | Active | Basic method |
| v4 | + Compare mode parameters | ✅ Current | ✅ Flexible |

**What Changed:**
- **v1 → v2:** Added `trnsl_%in_order_confirmations_matches_purchase_order` + comparison method parameter
- **v2 → v3:** No change
- **v3 → v4:** Added `Compare as [param1] [param2]` for flexible comparison modes

**Recommendation:** Use v4 (avoid v1 which is deprecated)

---

#### 3. CONDITION_DATES_OPERATOR_OC_LINE_ITEMS
**Versions:** v2, v3 (Current)

| Version | Tolerance Days | Accepted Tolerance Days | Status |
|---------|-----------------|------------------------|--------|
| v2 | ❌ No | ❌ No | Active |
| v3 | ✅ Yes | ✅ Yes | ✅ Current |

**What Changed:** v2 → v3: Added tolerance parameters:
- `with [param] days as tolerance`
- `and [param] as accepted tolerance days`

**Example:** Accept delivery dates within 5 days of promised date
**Recommendation:** Use v3

---

#### 4. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY
**Versions:** v2, v3, v4 (Current)

| Version | Comparison Mode | Status |
|---------|-----------------|--------|
| v2 | Basic | Active |
| v3 | Basic (no change) | Active |
| v4 | ✅ Flexible mode selection | ✅ Current |

**What Changed:** v3 → v4: Added `compare [param]` for different comparison approaches
**Recommendation:** Use v4

---

#### 5. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE
**Versions:** v2, v3, v4 (Current)

| Version | Comparison Mode | Status |
|---------|-----------------|--------|
| v2 | Standard | Active |
| v3 | Standard (no change) | Active |
| v4 | ✅ Flexible | ✅ Current |

**What Changed:** v3 → v4: Added `compare [param]` parameter
**Recommendation:** Use v4

---

#### 6. CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA
**Versions:** v2, v3 (Current)

| Version | Delivery Type | Master Data Table | Status |
|---------|---------------|-------------------|--------|
| v2 | "Confirmed" (fixed) | Fixed reference | Active |
| v3 | [Configurable param] | Dynamic [param] | ✅ Current |

**What Changed:** v2 → v3:
- Changed "Confirmed delivery" → `[param] delivery` (flexible delivery type)
- Changed fixed table reference → `stored in [param]` (dynamic table selection)

**Flexibility:** v3 allows different delivery date types and supplier tables
**Recommendation:** Use v3

---

#### 7. CONDIITON_UNIT_OF_MEASURE_EQUAL
**Versions:** v2, v3 (Current)

| Version | Supplier Table Reference | Status |
|---------|--------------------------|--------|
| v2 | "supplier item price table" (fixed) | Active |
| v3 | [Dynamic param] | ✅ Current |

**What Changed:** v2 → v3: Fixed table reference → `stored in [param]` (allows dynamic table selection)
**Recommendation:** Use v3

---

### 👥 ASSIGNMENT & ROUTING CARDS

#### 1. DOC_USER_ASSIGN
**Versions:** v1, v2, v3 (Deprecated)

| Version | Translation | Decision Tree | Status |
|---------|-------------|---------------|--------|
| v1 | No | ❌ No | Active |
| v2 | Yes | ❌ No | ✅ Current |
| v3 | Yes | ✅ Yes | ❌ DEPRECATED |

**Evolution:** v1 (no i18n) → v2 (with i18n) → v3 (+ decision tree experiment, now deprecated)

**What Changed:**
- v1 → v2: Added translation keys
- v2 → v3: Added decision tree support (experimental, deprecated)

**Recommendation:** Use v2 (stable with i18n support)

---

#### 2. DOC_GROUP_ASSIGN
**Versions:** v2, v3 (Deprecated)

| Version | Decision Tree | Status |
|---------|---------------|--------|
| v2 | ❌ No | ✅ Current |
| v3 | ✅ Yes | ❌ DEPRECATED |

**What Changed:** v2 → v3: Added `Use decision tree, if available [param]` (later deprecated)
**Recommendation:** Use v2

---

#### 3. OC_ASSIGN_DOC
**Versions:** v1, v2 (Current)

**What Changed:** v1 → v2: Added `trnsl_%oc_assign_doc` translation keys
**Recommendation:** Use v2

---

### 📋 TASK MANAGEMENT CARDS

#### 1. tasks_create ⭐ (Most Evolved Task Card - 4 Versions)
**Versions:** v1 (Deprecated), v2 (Deprecated), v3 (Deprecated), v4 (Current)

📖 **Guide:** [Task Assignment Guide](../then/task/task-assignment-guide.md#card-tasks_create--create-task-and-assign-to-user)

| Version | Translation | Decision Tree | Work Item Type | Status |
|---------|-------------|---------------|-----------------|--------|
| v1 | No | No | "Task" (fixed) | ❌ DEPRECATED |
| v2 | Yes | No | "Task" (fixed) | ❌ DEPRECATED |
| v3 | Yes | Yes | "Task" (fixed) | ❌ DEPRECATED |
| v4 | Yes | No | [Generic param] | ✅ Current |

**Evolution Timeline:**
```
v1 (original)
  ↓ (add translation)
v2 (with i18n)
  ↓ (experiment with decision tree)
v3 (+ decision tree, BUT deprecated after this)
  ↓ (remove decision tree, add generic types)
v4 (CURRENT - flexible work items)
```

**v1 → v2 Change (Translation Keys Added):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "trnsl_%tasks_create trnsl_be_% Create a new Task with the title: [param] ... and assign to user [param]"
```

**v2 → v3 Change (Decision Tree Experiment):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "Create a new Task with the title: [param] ... and assign it to the user [param].
         Use decision tree, if available: [param]"
```

**v3 → v4 Change (Generic Types + Decision Tree Removal):**
```
Before: "Create a new Task with the title: [param] ... "
After:  "Create a new [param] with the title: [param] ... "
```

**What Changed:**
- **v1 → v2:** Added `trnsl_%tasks_create` translation keys
- **v2 → v3:**
  - Added decision tree support: `Use decision tree, if available: [param]`
  - Changed "assign to user" → "assign it to the user"
- **v3 → v4:**
  - ❌ Removed decision tree parameter
  - ✅ Changed "Task" → generic `[param]` (supports Task, Ticket, Issue, etc.)
  - Updated translation key to `trnsl_%tasks_create_v4`

**Decision Tree Note:** v3 used decision trees to dynamically assign tasks. This approach was experimental and deprecated in v4 in favor of direct parameter-based work item type selection.

**Recommendation:** Use v4 exclusively for new workflows
**Migration:** If using v1, v2, or v3, upgrade to v4 ✅

---

#### 2. OC_TASK
**Versions:** v1, v2 (Current)

**What Changed:** v1 → v2: Added `trnsl_%oc_task` translation keys
**Recommendation:** Use v2

---

#### 3. ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK
**Versions:** v1, v3 (Current - v2 Skipped)

| Version | Work Item Type | Status |
|---------|-----------------|--------|
| v1 | "Task" (fixed) | Active |
| v3 | [Generic param] | ✅ Current |

**What Changed:** v1 → v3: Generic type evolution (v2 was skipped in production)
**Recommendation:** Use v3

---

#### 4. ACTION_DECISION_TREE_CREATE_TASKS
**Versions:** v2, v3 (Current)

| Version | Assignment Text | Status |
|---------|-----------------|--------|
| v2 | "Assign task with title" | Active |
| v3 | "Assign [generic] with title" | ✅ Current |

**What Changed:** v2 → v3:
- Changed "Assign task" → "Assign [generic param]"
- Changed "return of decision" → "return of decision table" (clearer terminology)

**Recommendation:** Use v3

---

### 🔄 DOCUMENT CONTROL CARDS

#### APPROVE
**Versions:** v1, v2 (Current)
**Change:** Added `trnsl_%approve_doc` translation keys
**Recommendation:** Use v2

---

#### REJECT
**Versions:** v1, v2 (Current)
**Change:** Added `trnsl_%reject_doc` translation keys
**Recommendation:** Use v2

---

#### STAUS_CHANGE (Status Change)
**Versions:** v1, v2, v3 (Current)

| Version | Workflow Trigger | Status |
|---------|-----------------|--------|
| v1 | ❌ No | Active |
| v2 | ❌ No | Active |
| v3 | ✅ Yes | ✅ Current |

**What Changed:** v2 → v3: Added `trigger Workflows [param]` - Auto-trigger workflows on status change
**Recommendation:** Use v3

---

#### EXPORT
**Versions:** v1, v2, v3 (Current)

| Version | Validation | Status |
|---------|------------|--------|
| v1 | ❌ No | Active |
| v2 | ❌ No | Active |
| v3 | ✅ Yes | ✅ Current |

**What Changed:** v2 → v3: Added `Start Export with Validation: [param]`
**Recommendation:** Use v3

---

### 🧮 DATA MANIPULATION CARDS

#### CALC_COLUMNS, CALC_COLUMNS_REGEX, EDIT_COLUMN, AI_CALC_MTZ_ETZ
**Pattern:** v1 → v2 (translation keys added)
**Recommendation:** Use v2 for all

---

#### CONDITION_DECISION_TREE_DATA
**Versions:** v2, v3 (Current)

| Version | Data Usage | Status |
|---------|------------|--------|
| v2 | "Use return data in later cards" | Active |
| v3 | "[Explicit param] returned data for use in subsequent cards" | ✅ Current |

**What Changed:** v2 → v3: More explicit control over decision tree data extraction
**Recommendation:** Use v3

---

### ❌ DISABLED CARDS (Do Not Use)

#### DOC_SUBORG_CHANGE
**Versions:** v1, v2 (both disabled)
**Status:** No longer supported
**Alternative:** Use document assignment features

---

#### RUN_SCRIPT
**Versions:** v2, v3 (both disabled)
**Status:** Replaced by ACTION_RUN_DOCOPERATOR_SCRIPT
**Alternative:** Use ACTION_RUN_DOCOPERATOR_SCRIPT v3

---

## 🎯 Common Version Patterns

### Pattern 1: Translation Key Adoption (v1 → v2)
**Affected:** 15+ cards

**Change:** Added `trnsl_%[card_name]` translation keys
```
v1: Plain text (no i18n)
v2: trnsl_%[key] trnsl_be_% Plain text (with i18n)
```

**Cards:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS, and more
**Impact:** Enables multi-language support

---

### Pattern 2: Decision Tree Integration (v2 → v3) - DEPRECATED
**Affected:** 5 cards (ACTION_TASK_FOR_GROUP, tasks_create, DOC_USER_ASSIGN, DOC_GROUP_ASSIGN, ACTION_DECISION_TREE_CREATE_TASKS)

**Change:** Added optional decision tree parameter
```
v2: Standard task/assignment logic
v3: + "Use decision tree, if available: [param]"
```

**Status:** ❌ Mostly deprecated (except ACTION_DECISION_TREE_CREATE_TASKS)
**Reason:** Simpler direct-parameter approach preferred

---

### Pattern 3: Generic Type Evolution (v3 → v4)
**Affected:** 4 cards (tasks_create, ACTION_TASK_FOR_GROUP, ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP, ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK)

**Change:** "Task" → generic type parameter
```
v3: Create a new Task with title: [param]
v4: Create a new [param] with title: [param]
```

**Impact:** Supports Task, Ticket, Issue, and other work item types
**Benefit:** Greater flexibility and reusability

---

### Pattern 4: Tolerance Parameters (PO Cards)
**Affected:** 6 cards (CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DATES_OPERATOR_OC_LINE_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY, etc.)

**Change:** Added tolerance/variance support
```
v2: Value [operator] Reference Value
v3+: Value [operator] Reference with tolerance [amount] [unit]
```

**Examples:**
- "with tolerance of 2 %"
- "with tolerance of 100 EUR"
- "with 5 days as tolerance"

**Impact:** Realistic matching criteria (not all values need to match exactly)

---

### Pattern 5: Comparison Mode Parameters
**Affected:** 3 cards (COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE, CONDITION_OC_TO_PO_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY)

**Change:** Added flexible comparison method selection
```
v3: Standard comparison
v4: + "Compare as [param1] [param2]"
```

**Impact:** Support different comparison algorithms

---

## ✅ Version Recommendations

### For New Workflows
**Rule:** Always use the highest enabled version number
- Provides latest features
- Best support
- Most tested
- Recommended approach

### For Existing Workflows
**Safe Approach:**
- Continue using current version if it works
- Plan gradual migration to newer versions
- Test upgrades in sandbox first

### Migration Priority

| Priority | Cards | Action |
|----------|-------|--------|
| **High** | tasks_create v1/v2/v3, ACTION_TASK_FOR_GROUP v3, CONDITION_DOC_TO_PO_UNIT_PRICE v2/v3/v4 | Upgrade to current version |
| **Medium** | Other v1/v2 translation upgrades, PO cards v2/v3 | Consider upgrading |
| **Low** | Cards with no functional changes | Optional |

---

## ⚠️ Deprecated Versions - Do Not Use

| Card | Version | Reason | Use Instead |
|------|---------|--------|-------------|
| tasks_create | v1, v2, v3 | Very old, or decision tree deprecated | v4 |
| ACTION_TASK_FOR_GROUP | v3 | Decision tree approach deprecated | v4 |
| DOC_USER_ASSIGN | v3 | Decision tree approach deprecated | v2 |
| DOC_GROUP_ASSIGN | v3 | Decision tree approach deprecated | v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Very old | v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Very old | v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Features reverted | v3 |

---

## 🔄 Fully Disabled Cards - Cannot Use

| Card | Versions | Reason | Alternative |
|------|----------|--------|-------------|
| DOC_SUBORG_CHANGE | v1, v2 | No longer supported | Document assignment cards |
| RUN_SCRIPT | v2, v3 | Replaced by DocOperator | ACTION_RUN_DOCOPERATOR_SCRIPT v3 |

---

## Related Documentation

- 📖 [Card Versioning Reference](../changelog/card-versioning.md) - Detailed version information
- 📚 [Workflow Guides](../) - Step-by-step card usage
- 🔄 [Card Version Database](../docs/card_version.md) - Complete version history
- 📋 [Workflow Logs](../workflow-logs/) - Execution and debugging

---

**Last Updated:** October 23, 2025
**Status:** Complete Version History
**Database Source:** postgres-dev-docflow
