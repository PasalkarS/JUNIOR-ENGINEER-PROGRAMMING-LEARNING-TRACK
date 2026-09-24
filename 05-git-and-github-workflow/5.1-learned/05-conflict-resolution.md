# Conflict Resolution & Merge Recovery

> **Module 05: Git & GitHub Workflow | Topic 05**

## 1. Learning Outcomes
- **Understanding Conflicts:** Identify why conflicts happen (divergent modifications to identical lines).
- **Conflict Markers:** Read and interpret Git conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
- **Resolution Strategy:** Integrate both changes meaningfully instead of blindly choosing one side.
- **Rebase Conflict Handling:** Step through `git rebase --continue` and abort safely with `git rebase --abort`.

## 2. Key Syntax & Concepts

### Resolving Conflict Markers
```text
<<<<<<< HEAD (Current branch / upstream)
db_port = 5432
=======
db_port = int(os.environ.get("PORT", 5432))
>>>>>>> feature/env-config (Incoming commit)
```

### Resolution Commands
```bash
# 1. Inspect conflicted files
git status

# 2. Open conflicted files in editor, remove markers, combine logic

# 3. Mark conflict as resolved
git add config.py

# 4. Continue rebase or merge
git rebase --continue

# 5. Run test suite to verify no regressions were introduced!
pytest -v
```

## 3. Common Mistakes & Gotchas
- **Leaving Conflict Markers Behind:** Accidentally committing `<<<<<<< HEAD` causes Python `SyntaxError`.
- **Forgetting to Test After Merge:** Never push resolved conflicts without running tests locally first.

## 4. Practice Tasks
- **Task 1:** Simulate a merge conflict by editing the same line in two branches and resolve it cleanly using rebase.

## 5. Self-Check Questions
- **Q1:** What command cancels an in-progress merge conflict and returns to a clean state?
- **Q2:** What does `<<<<<<< HEAD` indicate during a merge versus a rebase?
