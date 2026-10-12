# 5 — Conflict Resolution

## 1. Introduction to Git Conflicts

### What it is
A Git conflict occurs when Git cannot automatically combine changes from different branches. This commonly happens when multiple developers modify the same part of a file.

### Important Points
- Conflicts can occur during merging, rebasing, or applying certain commits.
- Git identifies the conflicting sections.
- The developer must inspect the changes and decide how to combine them.
- Resolving a conflict requires understanding the purpose of both changes.
- After resolving a conflict, the code should be checked and tested.

---

## 2. Understanding How Conflicts Occur

### What it is
Conflicts occur when Git cannot determine which changes should be kept automatically.

### Important Points
- Two branches may modify the same line differently.
- One branch may modify a file while another deletes it.
- Changes may overlap in a way that prevents automatic merging.
- Changes to separate parts of a file can often be merged automatically.
- Not every change made by multiple developers causes a conflict.

### Example

Suppose the `main` branch contains:

```python
product_price = 100
```

A feature branch changes it to:

```python
product_price = 150
```

Another branch changes the same line to:

```python
product_price = 200
```

Git cannot determine which price is correct. You must understand the requirement before deciding how to resolve the conflict.

---

## 3. Understanding Conflict Markers

### What it is
Git inserts conflict markers into a file to identify the sections that need manual resolution.

### Important Points
- `<<<<<<<` marks the beginning of one version.
- `=======` separates the two versions.
- `>>>>>>>` marks the end of the other version.
- The text between the markers shows the conflicting changes.
- All conflict markers must be removed after the conflict is resolved.

### Example

```python
<<<<<<< HEAD
product_price = 150
=======
product_price = 200
>>>>>>> feature/update-price
```

In a typical merge, `HEAD` represents the version from the branch you currently have checked out. The other section represents the incoming branch's changes.

You must decide what the correct result should be. For example, if the agreed price is `150`, the resolved code would be:

```python
product_price = 150
```

The example is simplified; the correct result always depends on the actual requirement.

---

## 4. Preparing Before Resolving Conflicts

### What it is
Preparation helps prevent accidental loss of work and makes conflicts easier to understand.

### Important Points
- Check the current branch before starting.
- Review the working directory for uncommitted changes.
- Commit or safely preserve your existing work.
- Read the changes being merged.
- Understand the purpose of both branches.
- Avoid starting a merge or rebase when unrelated local changes could be affected.

### Basic Commands

```bash
git status
git branch
git log --oneline --graph --all
git diff
```

These commands help you inspect the working directory, current branch, commit history, and uncommitted changes.

---

## 5. Resolving a Merge Conflict

### What it is
A merge conflict is resolved by combining the required changes into a final version of the affected file.

### Important Points
- Start a merge between the intended branches.
- Check which files have conflicts.
- Open each conflicting file.
- Read both versions carefully.
- Edit the file to produce the correct final result.
- Remove all conflict markers.
- Test the resolved code.
- Stage the resolved files and complete the merge.

### Basic Workflow

Suppose you are merging `feature/update-price` into `main`.

```bash
git switch main
git merge feature/update-price
```

If Git reports a conflict, inspect the working directory:

```bash
git status
```

Open the conflicting file and edit the conflicting sections.

After resolving the file:

```bash
git diff
git add product.py
git status
```

If the merge is ready to complete, create the merge commit:

```bash
git commit
```

Git normally provides a default merge commit message that you can keep or edit.

### Important Note
Do not stage a conflicted file until you have resolved its conflict markers and verified the intended result.

---

## 6. Understanding `ours` and `theirs`

### What it is
During a conflict, Git tools often use the terms `ours` and `theirs` to distinguish the two versions involved.

### Important Points
- In a normal merge, `ours` generally refers to the checked-out branch.
- In a normal merge, `theirs` generally refers to the branch being merged in.
- During a rebase, the interpretation can be different from what beginners expect.
- Keeping one complete version may discard valid changes from the other version.
- Inspect both versions before choosing either one.

### Common Commands

```bash
git checkout --ours product.py
git checkout --theirs product.py
```

These commands replace the selected file with one side of the conflict. Use them only when you have confirmed that keeping that version is correct.

On newer Git versions, the equivalent `git restore` options are also available:

```bash
git restore --ours product.py
git restore --theirs product.py
```

**Warning:** These commands can discard the other side's changes in that file. They should not be used blindly as a shortcut to resolve a conflict.

---

## 7. Resolving Conflicts in Multiple Files

### What it is
A single merge or rebase can produce conflicts in several files. Each file must be checked and resolved appropriately.

### Important Points
- Use `git status` to identify all conflicted files.
- Resolve each file individually.
- Do not assume every conflict has the same correct solution.
- Stage each resolved file.
- Inspect the final combined changes.
- Run relevant tests after all conflicts are resolved.

### Example

Suppose Git reports conflicts in:

```text
models.py
services.py
tests/test_services.py
```

A suitable workflow is:

1. Open `models.py` and resolve its conflict.
2. Open `services.py` and resolve its conflict.
3. Open `tests/test_services.py` and resolve its conflict.
4. Check that no conflict markers remain.
5. Inspect the final changes.
6. Run the tests.
7. Stage the resolved files and complete the operation.

---

## 8. Understanding Rebase Conflicts

### What it is
A rebase conflict occurs when Git tries to replay commits onto another base but cannot apply one or more changes automatically.

### Important Points
- Rebase applies commits one at a time onto a new base.
- A conflict may occur while replaying an individual commit.
- You must resolve the affected files for that commit.
- You must stage the resolved files before continuing.
- A rebase can involve multiple conflicts at different stages.
- Rebasing shared branches requires care because it rewrites commit history.

### Basic Workflow

Suppose you are updating `feature/product-search` using the latest `main` branch:

```bash
git switch feature/product-search
git fetch origin
git rebase origin/main
```

If a conflict occurs:

```bash
git status
```

Resolve the affected files, then stage them:

```bash
git add product.py
git rebase --continue
```

Repeat the resolution process if another conflict occurs.

### Important Commands

**Continue the rebase after resolving conflicts:**

```bash
git rebase --continue
```

**Cancel the rebase and return to the pre-rebase state:**

```bash
git rebase --abort
```

**Skip the current commit:**

```bash
git rebase --skip
```

Use `--skip` only when you understand why the commit can be omitted. It can discard the changes introduced by that commit.

---

## 9. Aborting a Merge or Rebase

### What it is
Aborting cancels an in-progress merge or rebase and returns the repository to its state before that operation began, subject to Git's safeguards and any unrelated changes.

### Important Points
- Abort when you need to stop and reconsider the operation.
- Understand which operation is currently in progress.
- Do not use abort commands after the operation has already completed.
- Check `git status` before and after aborting.
- Preserve important work before starting operations that may change files.

### Commands

**Abort an in-progress merge:**

```bash
git merge --abort
```

**Abort an in-progress rebase:**

```bash
git rebase --abort
```

After aborting, inspect the repository:

```bash
git status
git log --oneline --graph --all
```

---

## 10. Understanding Conflicts During Pulls

### What it is
A pull downloads changes from a remote repository and integrates them into the current branch. Conflicts can occur if your local work and remote changes cannot be combined automatically.

### Important Points
- `git pull` commonly fetches and then merges remote changes.
- Depending on configuration, a pull may use rebase instead.
- Check your current branch before pulling.
- Commit or preserve local changes when appropriate.
- Read Git's output to determine whether a merge or rebase is in progress.
- Resolve the conflict according to the operation Git started.

### Basic Commands

```bash
git status
git pull
```

If a merge conflict occurs, resolve the files and complete the merge.

If a rebase conflict occurs, resolve the files, stage them, and continue the rebase.

Avoid repeatedly running `git pull` without first resolving an operation that is already in progress.

---

## 11. Validating Code After Conflict Resolution

### What it is
Validation confirms that the combined changes work correctly and that conflict resolution has not introduced bugs or removed required behavior.

### Important Points
- Check the final contents of every resolved file.
- Remove all conflict markers.
- Inspect the staged changes.
- Run relevant tests.
- Check that both sets of required changes are preserved.
- Verify edge cases and affected functionality.
- Review the repository status before committing.

### Basic Commands

```bash
git diff
git diff --staged
git status
```

For a Python project, run the relevant tests. For example:

```bash
python -m unittest
```

This command runs tests discovered by Python's `unittest` framework. Use the test command appropriate for your project.

### Conflict Marker Check

Search the affected files for these markers:

```text
<<<<<<<
=======
>>>>>>>
```

These strings can occur legitimately in unusual files, so inspect any matches rather than deleting them automatically.

---

## 12. Common Conflict Resolution Mistakes

### What it is
Incorrect conflict resolution can silently remove functionality, introduce bugs, or discard another developer's work.

### Important Points
- Choosing `ours` or `theirs` without inspecting the changes.
- Deleting conflict markers without deciding what code should remain.
- Keeping one side and unintentionally losing required changes from the other.
- Staging files before fully resolving them.
- Forgetting to test the final combined code.
- Using `git rebase --skip` without understanding its effect.
- Rebasing shared branches without coordinating with collaborators.
- Force-pushing rewritten history without considering other developers.
- Assuming that a successful merge means the application is correct.

### Good Practice
Understand both versions, produce the correct combined result, and validate the behavior before completing the operation.

---

## 13. Task — Resolve Deliberately Conflicting Branches

### Objective
Create two branches that modify the same line differently, produce a merge conflict, and resolve it without blindly choosing one side.

### Steps

1. Create a small Git repository or use a practice repository.
2. Create a file named `product.py`.
3. Add the following code and commit it on `main`:

```python
product_price = 100
print("Product price:", product_price)
```

4. Create a branch named `feature/update-price`.
5. Change the price to `150` and commit the change.
6. Return to `main`.
7. Change the same line to `200` and commit the change.
8. Merge the feature branch into `main`.
9. Inspect the conflict markers.
10. Decide the correct final price based on the requirement.
11. Edit the file and remove the conflict markers.
12. Inspect and test the resolved code.
13. Stage the file and complete the merge.

### Example Commands

Initialize and create the starting commit:

```bash
git init
```

After creating `product.py`:

```bash
git add product.py
git commit -m "Add initial product price"
git switch -c feature/update-price
```

Change the price to `150`, then commit:

```bash
git add product.py
git commit -m "Update product price to 150"
```

Return to `main` and make a different change to the same line:

```bash
git switch main
```

Change the price to `200`, then commit:

```bash
git add product.py
git commit -m "Update product price to 200"
```

Start the merge:

```bash
git merge feature/update-price
```

Git should report a conflict because both branches changed the same line differently.

After resolving the file and confirming the correct final result:

```bash
git diff
git add product.py
git status
git commit
```

### Expected Outcome
You should understand why the conflict occurred, inspect both versions, choose the correct final result based on the requirement, and complete the merge after validation.

---

