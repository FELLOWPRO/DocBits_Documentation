# Workflow Pattern Guides

**Version:** 1.0
**Last Updated:** October 23, 2025

---

## Overview

This directory contains comprehensive workflow pattern guides that demonstrate how to combine multiple workflow cards to solve common business scenarios. Each pattern provides step-by-step implementation instructions, complete examples, and best practices.

**What are Workflow Patterns?**

Workflow patterns are proven, reusable solutions to common documentation processing challenges. Instead of starting from scratch, you can use these patterns as templates and adapt them to your specific needs.

---

## The Workflow Builder at a glance

Every pattern on this page is assembled in the **Workflow Builder**. You reach it from **Workflow Dashboard → Workflow List → Add Workflow** (or by opening an existing workflow). The dashboard gives you the run history and success/fail rates for all of your workflows:

<figure><img src="../../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard showing run totals, success and fail rates, the workflow-runs chart and recent activity"><figcaption><p>The Workflow Dashboard — run totals, success/fail rates and recent activity for every workflow.</p></figcaption></figure>

The **Workflow List** tab lists every workflow with its type, execution order and trigger. Use **Add Workflow** to create a new one, or click a workflow to open it in the builder:

<figure><img src="../../../.gitbook/assets/workflow_list.png" alt="Workflow List tab listing workflows with type, execution order and trigger"><figcaption><p>The Workflow List — each row is a workflow you can open, toggle on/off or edit.</p></figcaption></figure>

A workflow is built from three groups of cards — **When** (the trigger), **And** (additional conditions) and **Then** (the actions to run). The example below triggers on invoices belonging to a sub-organization and assigns them to a user:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder canvas with When, And and Then cards"><figcaption><p>The Workflow Builder canvas. Each pattern below is just a different combination of When / And / Then cards.</p></figcaption></figure>

Click **Add Card** in any group to open the card library. Cards are organised by category (Compare with Purchase Order, Partner Cards, Document Field, Date &#x26; Time, Document, Logic, Status, Table, Assignee, …) so you can find the building block each pattern calls for:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card dialog showing the card categories and available cards"><figcaption><p>The <strong>Add Card</strong> library — every card referenced in the patterns below is picked from here.</p></figcaption></figure>

---

## Available Patterns

### 1. [API Integration Pattern](api-integration-pattern.md)

**Complexity:** Medium | **Setup Time:** 45-60 minutes

Learn how to integrate DocBits with external APIs to fetch, validate, and store data from external systems.

**Use Cases:**
- Fetch real-time pricing from external systems
- Validate supplier information against master databases
- Look up product details from catalog systems
- Get exchange rates from currency services
- Verify addresses with geocoding services

**Cards Used:** CALL_API, CONDITION_HTTPS_REQUEST_STATUS, ACTION_SET_FIELD_TO_TEXT, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[View Full Pattern →](api-integration-pattern.md)**

---

### 2. [Task Management Pattern](task-management-pattern.md)

**Complexity:** Low-Medium | **Setup Time:** 30-45 minutes

Master the art of creating, assigning, tracking, and managing tasks within DocBits workflows for approval and review processes.

**Use Cases:**
- Create approval workflows
- Assign review tasks to users
- Handle exceptions requiring human intervention
- Escalate issues to managers
- Create multi-level approval chains
- Track task completion and deadlines

**Cards Used:** tasks_create, ACTION_ASSIGN_TO_USER, ACTION_SEND_EMAIL_TO_GROUPS, CONDITION_TASK_STATUS

**[View Full Pattern →](task-management-pattern.md)**

---

### 3. [PO Matching Pattern](po-matching-pattern.md)

**Complexity:** Medium-High | **Setup Time:** 60-90 minutes

Implement comprehensive Purchase Order matching workflows to validate invoices against POs with tolerance-based routing.

**Use Cases:**
- Validate invoices against purchase orders
- Detect pricing errors before payment
- Identify quantity discrepancies
- Enforce procurement controls
- Prevent duplicate payments
- Automate three-way matching

**Cards Used:** PURCHASE_ORDER_FULL_MATCH, CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DOC_TO_PO_QUANTITY, CONDITION_DOC_TO_PO_TAX_LINES

**[View Full Pattern →](po-matching-pattern.md)**

---

### 4. [Decision Logic Pattern](decision-logic-pattern.md)

**Complexity:** Medium | **Setup Time:** 30-45 minutes

Implement complex decision trees and conditional routing logic to process documents through different paths based on business rules.

**Use Cases:**
- Route documents by amount thresholds
- Apply different rules for different document types
- Implement multi-level approval logic
- Handle complex business policies
- Create dynamic routing based on multiple criteria
- Implement approval matrices

**Cards Used:** CONDITION_DOC_FIELD_AMOUNT, CONDITION_DOC_TYPE_IS_ISNOT, CONDITION_SUPPLIER_STATUS_IS_ISNOT, ACTION_ASSIGN_TO_USER

**[View Full Pattern →](decision-logic-pattern.md)**

---

### 5. [Data Transformation Pattern](data-transformation-pattern.md)

**Complexity:** Medium | **Setup Time:** 30-45 minutes

Transform, calculate, format, and enrich document data to prepare for export, perform calculations, and standardize formats.

**Use Cases:**
- Calculate totals, subtotals, taxes
- Convert currencies or units
- Format dates, numbers, text
- Derive values from existing fields
- Enrich data from external sources
- Standardize data formats
- Validate calculations

**Cards Used:** ACTION_CALCULATE_FIELD, ACTION_SET_FIELD_TO_TEXT, ACTION_COPY_FIELD_VALUE, CALL_API, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[View Full Pattern →](data-transformation-pattern.md)**

---

## Pattern Selection Guide

### By Complexity

| Complexity | Patterns | Best For |
|------------|----------|----------|
| **Low-Medium** | [Task Management](task-management-pattern.md) | Beginners, simple workflows |
| **Medium** | [API Integration](api-integration-pattern.md)<br>[Decision Logic](decision-logic-pattern.md)<br>[Data Transformation](data-transformation-pattern.md) | Intermediate users, standard workflows |
| **Medium-High** | [PO Matching](po-matching-pattern.md) | Advanced users, complex validation |

---

### By Use Case

| I Need To... | Use This Pattern |
|--------------|------------------|
| Integrate with external systems | [API Integration Pattern](api-integration-pattern.md) |
| Create approval workflows | [Task Management Pattern](task-management-pattern.md) |
| Validate against purchase orders | [PO Matching Pattern](po-matching-pattern.md) |
| Route based on conditions | [Decision Logic Pattern](decision-logic-pattern.md) |
| Calculate and transform data | [Data Transformation Pattern](data-transformation-pattern.md) |

---

### By Industry/Department

| Industry/Department | Recommended Patterns |
|---------------------|---------------------|
| **Finance/Accounting** | [PO Matching](po-matching-pattern.md), [Task Management](task-management-pattern.md), [Data Transformation](data-transformation-pattern.md) |
| **Procurement** | [PO Matching](po-matching-pattern.md), [Decision Logic](decision-logic-pattern.md), [API Integration](api-integration-pattern.md) |
| **Operations** | [Task Management](task-management-pattern.md), [Decision Logic](decision-logic-pattern.md) |
| **IT/Integration** | [API Integration](api-integration-pattern.md), [Data Transformation](data-transformation-pattern.md) |
| **All Departments** | [Decision Logic](decision-logic-pattern.md), [Task Management](task-management-pattern.md) |

---

## How to Use These Patterns

### Step 1: Choose a Pattern

1. Review the pattern descriptions above
2. Identify which pattern matches your use case
3. Check the complexity and estimated setup time
4. Review the "When to Use" section in the pattern guide

### Step 2: Review Prerequisites

Each pattern guide lists:
- Required knowledge
- Related guides to read first
- Cards that will be used
- Configuration requirements

### Step 3: Follow Step-by-Step Instructions

Each pattern provides:
- Complete workflow example
- Step-by-step implementation guide
- Configuration templates
- Real-world examples
- Troubleshooting tips

### Step 4: Customize to Your Needs

- Adapt the example to your business rules
- Adjust thresholds and tolerances
- Modify routing logic
- Add/remove steps as needed
- Test thoroughly before production use

### Step 5: Monitor and Optimize

- Track workflow performance
- Monitor success rates
- Gather user feedback
- Refine configuration
- Document customizations

---

## Pattern Combinations

Many real-world scenarios require combining multiple patterns:

### Example 1: Complete Invoice Processing

```
1. API Integration Pattern → Fetch current pricing
2. Data Transformation Pattern → Calculate totals
3. PO Matching Pattern → Validate against PO
4. Decision Logic Pattern → Route based on variance
5. Task Management Pattern → Create approval tasks
```

### Example 2: High-Value Invoice Approval

```
1. Data Transformation Pattern → Calculate amounts
2. Decision Logic Pattern → Check thresholds
3. Task Management Pattern → Multi-level approval
4. API Integration Pattern → Notify external systems
```

### Example 3: Exception Handling

```
1. PO Matching Pattern → Detect variances
2. Decision Logic Pattern → Classify exception severity
3. Task Management Pattern → Create review tasks
4. Data Transformation Pattern → Calculate impact
```

---

## Pattern Templates

Each pattern includes these standardized sections:

1. **Overview** - What the pattern does
2. **When to Use** - Appropriate use cases
3. **Complete Example** - Real-world scenario
4. **Step-by-Step** - Implementation instructions
5. **Configuration** - Card setup templates
6. **Workflow Diagram** - Visual representation
7. **Advanced Variations** - Alternative implementations
8. **Error Handling** - Common issues and solutions
9. **Testing Checklist** - Validation steps
10. **Related Patterns** - Complementary patterns
11. **Related Guides** - Reference documentation

---

## Getting Help

### Pattern Support Resources

**Documentation:**
- [Complete Workflow Guide Index](../README.md)
- [Individual Card Guides](../then/action/)
- [Condition Cards Reference](../and/condition-cards-complete-guide.md)
- [Workflow Linking Map](../../../../WORKFLOW_LINKING_MAP.md)

**Additional Resources:**
- [Quick Reference Guide](../../../../WORKFLOW_LINKING_QUICK_REFERENCE.md)
- [October 2025 Release Notes](../changelog/2025-10-october.md)
- [Card Versioning Reference](../../../docs/card_version.md)

**Contact:**
- Pattern Feedback: docs@docbits.com
- Technical Support: support@docbits.com
- Implementation Help: consulting@docbits.com

---

## Pattern Statistics

| Metric | Value |
|--------|-------|
| **Total Patterns** | 5 |
| **Total Cards Covered** | 30+ |
| **Combined Documentation** | ~1,200 lines |
| **Example Scenarios** | 25+ |
| **Configuration Templates** | 15+ |
| **Workflow Diagrams** | 5 complete diagrams |
| **Cross-References** | 87+ internal links |

---

## Contributing to Patterns

Have a workflow pattern that would benefit others?

**Pattern Contribution Guidelines:**

1. **Document Your Workflow**
   - Clear business scenario
   - Step-by-step implementation
   - Working configuration examples
   - Real-world test results

2. **Follow Pattern Template**
   - Use standard section structure
   - Include all required elements
   - Provide diagrams/examples
   - Add troubleshooting guide

3. **Submit for Review**
   - Email to: docs@docbits.com
   - Include: Pattern description, use cases, implementation guide
   - We'll review and potentially add to official documentation

**Benefits:**
- Help other DocBits users
- Get recognized in documentation
- Improve overall product knowledge base
- Receive feedback on your implementation

---

## Changelog

### Version 1.0 (October 23, 2025)
- Initial release of 5 comprehensive workflow patterns
- API Integration Pattern added
- Task Management Pattern added
- PO Matching Pattern added
- Decision Logic Pattern added
- Data Transformation Pattern added
- Cross-reference linking implemented (87 links)
- Pattern selection guide created

---

## Next Steps

**New to Workflow Patterns?**
1. Start with [Task Management Pattern](task-management-pattern.md) - easiest to understand
2. Review [Decision Logic Pattern](decision-logic-pattern.md) - foundational for all workflows
3. Explore [API Integration Pattern](api-integration-pattern.md) - common integration need

**Ready to Implement?**
1. Choose your pattern from the list above
2. Read the complete pattern guide
3. Review prerequisites and related guides
4. Follow step-by-step instructions
5. Test with sample documents
6. Deploy to production
7. Monitor and optimize

**Need More Help?**
- Review [Workflow Documentation Overview](../README.md)
- Check [Quick Reference Guide](../../../../WORKFLOW_LINKING_QUICK_REFERENCE.md)
- Contact support team

---

**Last Updated:** October 23, 2025
**Maintained By:** Documentation Team
**Version:** 1.0
