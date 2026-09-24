# Issue Tracking & Task Decomposition

> **Module 05: Git & GitHub Workflow | Topic 04**

## 1. Learning Outcomes
- **Actionable Issues:** Structure bug reports and feature requests with clear acceptance criteria.
- **Task Decomposition:** Break large customer requirements into discrete, testable technical tasks.
- **Labels & Milestones:** Organize backlog tickets using semantic labels (`bug`, `enhancement`, `blocked`).
- **Linking PRs to Issues:** Automatically close issues using keyword syntax (`Closes #12`).

## 2. Key Concepts & Standards

### Effective Issue Structure
```markdown
### Problem Statement
Customers currently receive no error message when attempting to checkout with an empty shopping cart.

### Expected Behavior
Attempting to place an order with zero items should raise a `ValidationError` with message "An order must contain at least one item."

### Acceptance Criteria
- [ ] `Order` constructor rejects empty item lists.
- [ ] CLI shows user-friendly error message.
- [ ] Automated pytest test verifies rejection.
```

## 3. Common Mistakes & Gotchas
- **Vague Bug Reports:** "App is broken" without reproduction steps, inputs, and error logs cannot be diagnosed.
- **Working Without Tickets:** Making unassigned changes leads to duplicated effort and unaligned features.

## 4. Practice Tasks
- **Task 1:** Write a comprehensive bug report issue for an edge case where an uploaded CSV contains negative numbers.

## 5. Self-Check Questions
- **Q1:** How do you link a commit or PR to automatically close issue #45 upon merge?
- **Q2:** Why are acceptance criteria critical before starting implementation?
