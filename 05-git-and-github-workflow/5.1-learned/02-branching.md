# Feature Branching & History Hygiene

> **Module 05: Git & GitHub Workflow | Topic 02**

## 1. Learning Outcomes
- **Branch Management:** Create, list, switch, and delete branches cleanly using `git switch` and `git branch`.
- **Branch Naming Conventions:** Adopt standard naming patterns: `feature/`, `bugfix/`, `chore/`.
- **Small Commits:** Craft small, atomic commits focused on a single logical change.
- **Keeping Branches Fresh:** Rebase feature branches against `main` before merging.

## 2. Key Syntax & Concepts

### Branching Commands
```bash
# Create and switch to new branch
git switch -c feature/order-cancel-flow

# List local branches
git branch

# Keep feature branch up-to-date with main using rebase
git fetch origin main
git rebase origin/main

# Delete merged local branch
git branch -d feature/order-cancel-flow
```

### The Fast-Forward vs Merge Commit
| Merge Type | Characteristics | When to Use |
|---|---|---|
| Fast-Forward | Linear commit history, moves HEAD pointer forward | Small private feature branches |
| 3-Way Merge (`--no-ff`) | Creates explicit merge commit recording branch integration | Merging PRs into protected `main` |

## 3. Common Mistakes & Gotchas
- **Developing Directly on Main:** Always create a feature branch to isolate work and enable peer code review.
- **Long-Lived Stale Branches:** Branches lasting weeks diverge heavily from main, making eventual merges painful. Rebase daily.

## 4. Practice Tasks
- **Task 1:** Create `feature/test-branch`, commit a dummy change, switch back to `main`, and verify the dummy change is absent on `main`.

## 5. Self-Check Questions
- **Q1:** Why is `git switch` preferred over the older `git checkout` for branch switching?
- **Q2:** What does `git rebase` do to your branch commits?
