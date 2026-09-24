# Pull Requests, Code Reviews & Team Collaboration

> **Module 05: Git & GitHub Workflow | Topic 03**

## 1. Learning Outcomes
- **Writing Effective PRs:** Provide clear context, acceptance criteria, and test evidence in PR descriptions.
- **Conducting Code Reviews:** Review diffs systematically for correctness, test coverage, and style.
- **Addressing Review Comments:** Push clean follow-up commits to the branch to resolve requested changes.
- **Merge Strategies:** Compare squash-and-merge, rebase-and-merge, and standard merge commits.

## 2. Key Concepts & Standards

### Professional PR Description Template
```markdown
## Summary
Implements stock reservation and automated rollback upon order cancellation.

## Changes Made
- Added `cancel_order()` method to `OrderService`
- Restores product stock upon successful cancellation
- Added unit tests covering all state machine transitions

## Verification & Testing
- `pytest tests/ -v` (12 passed in 0.15s)
- Tested manual CLI cancellation flow
```

## 3. Common Mistakes & Gotchas
- **Massive 2000-Line PRs:** Reviewers cannot thoroughly inspect huge changesets. Break work into small PRs (< 400 lines).
- **Force Pushing Over Active Reviews:** Force-pushing during an open review invalidates comment threads and confuses reviewers.

## 4. Practice Tasks
- **Task 1:** Draft a PR description template containing summary, test evidence, and breaking changes sections.

## 5. Self-Check Questions
- **Q1:** What are the advantages of "Squash and Merge" for feature branches?
- **Q2:** How should you respond when a reviewer requests changes to your implementation?
