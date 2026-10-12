# 4 — GitHub Issues

## 1. Introduction to GitHub Issues

### What it is
GitHub Issues is a feature used to track bugs, features, improvements, and other tasks in a project. It helps a team organize work and understand what needs to be done.

### Important Points
- Issues describe work that needs attention.
- Each issue has a title and description.
- Issues can include labels, assignees, and milestones.
- Developers can discuss requirements and ask questions through comments.
- Issues help track progress from the initial requirement to completion.

---

## 2. Understanding the Purpose of Issues

### What it is
An issue provides a central place to describe a problem or a task before implementation begins.

### Important Points
- A bug issue describes something that is not working correctly.
- A feature issue describes new functionality to implement.
- An improvement issue describes how an existing feature can be made better.
- A documentation issue tracks missing or incorrect documentation.
- Issues help developers understand the purpose of their work.

### Common Types of Issues

| Type | Purpose | Example |
|---|---|---|
| Bug | Report incorrect behavior | Product search returns incorrect results |
| Feature | Request new functionality | Add product search |
| Improvement | Improve existing functionality | Make search results easier to read |
| Documentation | Update project documentation | Add setup instructions |
| Maintenance | Handle technical maintenance | Update outdated dependencies |

---

## 3. Writing a Clear Issue Title

### What it is
An issue title briefly explains the task or problem that needs to be addressed.

### Important Points
- Keep the title short and specific.
- Describe the actual task or problem.
- Avoid vague titles such as `Fix bug` or `Update code`.
- Use action-oriented wording for feature requests.
- Make the title understandable without requiring the reader to guess.

### Examples

**Poor titles:**
- Fix the code
- Update the project
- Search problem

**Better titles:**
- Fix product search returning incorrect results
- Add product search by name
- Update installation instructions in README

A good title communicates the task clearly at a glance.

---

## 4. Writing an Issue Description

### What it is
An issue description explains the problem, requirement, expected behavior, and other information needed to complete the task.

### Important Points
- Explain what needs to be done.
- Provide relevant background information.
- Describe the current behavior when reporting a bug.
- Describe the expected behavior.
- Include examples when they clarify the requirement.
- Mention constraints or dependencies when relevant.

### Basic Structure

```markdown
## Description
Explain the task or problem.

## Expected Behavior
Describe what should happen.

## Requirements
- Requirement 1
- Requirement 2
- Requirement 3

## Additional Information
Add relevant details, examples, or references.
```

### Example

```markdown
## Description
Add a search feature to the product inventory system.

## Expected Behavior
Users should be able to search for products by name.

## Requirements
- Accept a product name as input.
- Display matching products.
- Show a clear message when no products match.
- Handle empty search input.

## Additional Information
The feature should work with the existing product records.
```

---

## 5. Understanding Acceptance Criteria

### What it is
Acceptance criteria are specific conditions that must be satisfied for a task to be considered complete.

### Important Points
- They define the expected outcome.
- They help developers understand when the work is finished.
- They should be clear and testable.
- They reduce confusion between developers and reviewers.
- They can be used to create test cases.

### Example

**Issue:** Add product search by name.

**Acceptance Criteria:**
- Users can enter a product name.
- Matching products are displayed.
- A message appears when no matching product exists.
- Empty input is handled appropriately.
- Existing product records remain unchanged.

### Why Acceptance Criteria Matter

Without acceptance criteria, a developer may implement a search function that technically works but does not handle empty input or missing products.

Clear criteria help everyone agree on what a completed feature should do.

---

## 6. Breaking Requirements into Smaller Tasks

### What it is
Task decomposition is the process of dividing a large requirement into smaller, manageable tasks.

### Important Points
- Large tasks can be difficult to estimate and review.
- Smaller tasks are easier to understand and test.
- Each task should have a clear purpose.
- Tasks should have specific expected outcomes.
- Related tasks can be linked to a parent issue or tracked using a task list.

### Example

**Main Requirement:** Build a product inventory search feature.

Break it into smaller tasks:

```markdown
- [ ] Review the existing product data structure.
- [ ] Implement product name matching.
- [ ] Handle empty search input.
- [ ] Handle searches with no matching results.
- [ ] Test the search functionality.
- [ ] Update the README documentation.
```

Each item represents a specific piece of work.

### Benefits
- Easier progress tracking.
- Clearer responsibilities.
- Simpler testing.
- More manageable Pull Requests.
- Better understanding of dependencies.

---

## 7. Using GitHub Issue Labels

### What it is
Labels categorize issues and help developers quickly identify the type, priority, or status of a task.

### Important Points
- Labels make issues easier to organize.
- A single issue can have multiple labels.
- Teams can create their own labels.
- Labels should have consistent meanings across the repository.
- A label does not replace a clear title or description.

### Common Labels

| Label | Purpose |
|---|---|
| `bug` | Something is not working correctly |
| `feature` | New functionality |
| `documentation` | Documentation changes |
| `enhancement` | Improvement to existing functionality |
| `priority: high` | Work that needs urgent attention |
| `good first issue` | A task suitable for new contributors |
| `help wanted` | Additional assistance is welcome |

These are examples. Labels are customizable and may differ between repositories.

---

## 8. Assigning Issues and Tracking Progress

### What it is
GitHub allows issues to be assigned to people and organized using milestones or project boards.

### Important Points
- Assignees indicate who is responsible for the task.
- Milestones group issues around a release or goal.
- GitHub Projects can organize work into views such as To do, In progress, and Done.
- Comments can record decisions and implementation updates.
- Assignment does not automatically mean that the issue is completed.

### Example Workflow

```text
Open Issue
    |
    v
Understand Requirements
    |
    v
Assign Task
    |
    v
Implement Changes
    |
    v
Test Implementation
    |
    v
Create Pull Request
    |
    v
Review and Merge
    |
    v
Close Issue
```

---

## 9. Connecting Issues to Pull Requests

### What it is
Linking an issue to a Pull Request connects the original task with the code changes that implement it.

### Important Points
- The issue explains what needs to be done.
- The PR explains and presents the proposed implementation.
- Reviewers can trace the changes back to the requirement.
- GitHub supports keywords that automatically close linked issues when the PR is merged into the repository's default branch.

### Example

Suppose the issue number is `#15`.

Add the following to the PR description:

```markdown
Closes #15
```

Other supported keywords include:

```markdown
Fixes #15
Resolves #15
```

Use the actual issue number from your repository.

---

## 10. Working from an Issue

### What it is
Working from an issue means using its requirements and acceptance criteria to guide implementation instead of starting with unclear or undocumented instructions.

### Important Points
- Read the complete issue before writing code.
- Understand the problem and expected outcome.
- Identify missing information.
- Ask questions if the requirements are unclear.
- Break the work into smaller tasks when necessary.
- Create a branch dedicated to the issue.
- Test the implementation against the acceptance criteria.

### Example Workflow

Suppose issue `#15` requests product search functionality.

Create a branch:

```bash
git switch main
git pull
git switch -c feature/15-product-search
```

Implement the feature, then inspect and commit your changes:

```bash
git status
git diff
git add .
git commit -m "Add product search functionality"
```

Push the branch:

```bash
git push -u origin feature/15-product-search
```

Create a Pull Request and link it to issue `#15`.

---

## 11. Identifying Ambiguous Requirements

### What it is
An ambiguous requirement does not provide enough information to determine the expected behavior confidently.

### Important Points
- Do not assume important behavior without checking.
- Identify missing rules and edge cases.
- Ask specific questions to clarify expectations.
- Update the issue description when decisions are made.
- Make sure acceptance criteria reflect the agreed behavior.

### Example

**Ambiguous requirement:**

```text
Add product search.
```

Questions to clarify:
- Should the search match the full product name or part of the name?
- Should the search ignore uppercase and lowercase differences?
- What should happen when no products match?
- Should an empty search display all products or an error message?
- Should the search support multiple matching products?

### Improved Requirement

```text
Allow users to search products by partial product name.
Search should ignore uppercase and lowercase differences.
Display all matching products.
Show a message when no products match.
Reject empty search input with a clear message.
```

Clear requirements reduce rework and improve implementation quality.

---

## 12. Writing Implementation Notes

### What it is
Implementation notes record important technical decisions, dependencies, or details that help someone complete a task.

### Important Points
- Explain relevant parts of the existing codebase.
- Identify dependencies or related components.
- Record important technical constraints.
- Mention areas that require special attention.
- Avoid prescribing unnecessary implementation details when multiple valid approaches exist.

### Example

```markdown
## Implementation Notes
- Use the existing product records.
- Keep search logic separate from user input handling.
- Do not modify stored product data during a search.
- Add tests for empty input and unmatched products.
```

Implementation notes should guide the developer without making the issue unnecessarily complicated.

---

## 13. Common Mistakes When Creating Issues

### What it is
Poorly written issues can create confusion, delays, and unnecessary changes.

### Important Points
- Writing vague titles.
- Providing insufficient context.
- Mixing several unrelated tasks into one issue.
- Omitting expected behavior.
- Using acceptance criteria that cannot be tested.
- Forgetting important edge cases.
- Assigning work before clarifying major requirements.
- Closing an issue without verifying that the requirements are met.
- Duplicating an existing issue without checking the repository.

### Good Practice
Before creating an issue, check whether a similar issue already exists and ensure the new issue describes a clear, actionable task.

---

## 14. Task — Convert a Requirement into Actionable GitHub Issues

### Objective
Take a broad requirement and convert it into clear issues that a developer can implement and test.

### Requirement

Build a basic product inventory system that allows users to:
- Add products.
- Search for products.
- Update product prices.
- View all products.

### Steps

1. Read the complete requirement.
2. Identify the separate features.
3. Create an issue for each feature.
4. Write a clear title for every issue.
5. Describe the expected behavior.
6. Add testable acceptance criteria.
7. Identify edge cases.
8. Add suitable labels.
9. Break larger tasks into smaller checklists.
10. Identify dependencies between tasks.
11. Review each issue to ensure it is actionable.

### Example Issue

**Title:** Add product price update functionality

```markdown
## Description
Allow users to update the price of an existing product.

## Requirements
- Identify the product to update.
- Accept the new price.
- Validate the new price.
- Display a message when the product does not exist.
- Display a confirmation when the update succeeds.

## Acceptance Criteria
- An existing product's price can be updated.
- A negative price is rejected.
- A missing product is handled clearly.
- The updated price is displayed correctly.

## Testing
- Test a valid price update.
- Test a negative price.
- Test an unknown product ID.
```

### Expected Outcome
The requirement should become a set of focused issues with clear titles, descriptions, and acceptance criteria. Another developer should be able to understand the work without repeatedly asking what the task means.

