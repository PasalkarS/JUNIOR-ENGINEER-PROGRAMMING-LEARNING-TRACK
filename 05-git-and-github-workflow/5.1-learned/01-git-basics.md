# Git CLI Basics & Core Workflow

> **Module 05: Git & GitHub Workflow | Topic 01**

## 1. Learning Outcomes
- **Mental Model:** Master the three Git trees: Working Directory, Staging Area (Index), and Repository (HEAD).
- **Core Commands:** Daily workflow using `git status`, `git add`, `git commit`, `git diff`, and `git log`.
- **Inspection & History:** Review historical commits cleanly with formatted logs and diff patches.
- **Safe Recovery:** Discard unstaged changes with `git restore` and unstage with `git restore --staged`.

## 2. Key Syntax & Concepts

### Standard Local Cycle
```bash
# Check status of changed files
git status

# Inspect specific unstaged modifications
git diff

# Stage specific files intentionally (avoid 'git add .')
git add src/service.py tests/test_service.py

# Commit with a descriptive, imperative commit message
git commit -m "feat: implement customer invoice calculation"

# View concise one-line commit log
git log --oneline -n 10
```

### Undoing Local Mistakes
| Action | Command | Safe? |
|---|---|---|
| Unstage a staged file | `git restore --staged <file>` | Yes (keeps file changes) |
| Discard working tree changes | `git restore <file>` | Irreversible (discards uncommitted work) |
| Amend last commit message | `git commit --amend -m "new msg"` | Safe locally before push |

## 3. Common Mistakes & Gotchas
- **Blind Staging:** Running `git add -A` blindly stages temp files, logs, and passwords. Always review `git status` first.
- **Vague Commit Messages:** Messages like "fix stuff" or "updates" obscure git blame. Use conventional prefix: `feat:`, `fix:`, `refactor:`, `test:`.

## 4. Practice Tasks
- **Task 1:** Initialize a scratch repository, stage two files in separate commits, and use `git log --stat` to view file changes.

## 5. Self-Check Questions
- **Q1:** What is the difference between working directory and the staging area?
- **Q2:** Why should secrets and build artifacts be placed in `.gitignore`?
