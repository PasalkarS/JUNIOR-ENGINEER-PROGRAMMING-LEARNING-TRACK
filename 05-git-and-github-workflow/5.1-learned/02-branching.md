# 13.2 — Branching

## 1. Introduction to Branching

- A branch is a separate line of development in a Git repository.
- Branches allow developers to work on different features or fixes without directly changing the main branch.
- They help keep development work organized and independent.

### Important Points
- The default branch is commonly named `main`.
- A feature branch is created for a specific task.
- Each branch points to a commit in the repository history.
- Changes made on one branch do not automatically appear on another branch.
- Branches make it easier to review and test changes before merging them.

## 2. Understanding the Main Branch and Feature Branches

### Main Branch
- The main branch usually contains the primary version of the project.
- It should remain stable according to the team's workflow.
- Completed work is commonly merged into this branch.

### Feature Branch
- A feature branch is used to develop a particular feature, fix, or improvement.
- It keeps unfinished work separate from the main branch.
- It can be merged after the work is reviewed and tested.

### Important Points
- Avoid making unrelated changes directly on the main branch when the team uses feature branches.
- Create a separate branch for each independent task.
- Choose the correct base branch before starting work.
- Follow the repository's documented branching policy.

## 3. Creating and Switching Branches

Git provides commands to create branches and switch between them.

### Creating a Branch

```bash
git branch feature-login
```

Creates a branch named `feature-login`.

### Switching to a Branch

```bash
git switch feature-login
```

Switches to the existing branch.

### Creating and Switching to a Branch

```bash
git switch -c feature-login
```

Creates the branch and switches to it.

### Listing Branches

```bash
git branch
```

Lists local branches. The current branch is marked with an asterisk.

### Important Points
- Use descriptive branch names.
- Check the current branch before making changes.
- Git may prevent switching branches if doing so would overwrite uncommitted changes.
- Commit or safely save important work before switching branches.

## 4. Branch Naming Conventions

Branch names should clearly describe the task being performed.

### Common Branch Prefixes

- `feature/` — for new functionality.
- `fix/` — for bug fixes.
- `docs/` — for documentation changes.
- `refactor/` — for code restructuring.
- `test/` — for testing-related changes.

### Examples

```text
feature/user-login
feature/product-search
fix/incorrect-total
docs/update-readme
refactor/database-connection
test/order-validation
```

### Important Points
- Use names that describe the task.
- Keep branch names short and readable.
- Use a consistent naming style.
- Avoid vague names such as `new-branch`, `changes`, or `test123`.
- Include an issue number when required by the team, such as `feature/42-user-login`.

## 5. Working on a Feature Branch

A feature branch keeps the changes for one task separate from other development work.

### Basic Workflow

```bash
git switch main
git switch -c feature/product-search
```

Make the required changes, then stage and commit them:

```bash
git add product_search.py
git commit -m "Add product search"
```

### Important Points
- Start from the correct base branch.
- Implement only the intended task.
- Review the changes before committing.
- Keep commits focused on one logical change.
- Test the feature before sharing it.
- Push the branch when it is ready to be shared or reviewed.

## 6. Making Small and Focused Commits

A commit should represent one logical unit of work.

### Example

Instead of making one large commit:

```text
Update application
```

Use focused commits:

```text
Add product search function
Validate product search input
Add tests for product search
Update product search documentation
```

### Important Points
- Small commits are easier to review.
- Clear commit messages explain the purpose of a change.
- Focused commits make troubleshooting easier.
- Avoid combining unrelated tasks into one commit.
- Review staged changes using `git diff --staged` before committing.

## 7. Checking Branch Status and Changes

Before committing or switching branches, check the current repository state.

### Checking Status

```bash
git status
```

### Viewing the Current Branch

```bash
git branch
```

### Viewing Unstaged Changes

```bash
git diff
```

### Viewing Staged Changes

```bash
git diff --staged
```

### Viewing Recent Commits

```bash
git log --oneline
```

### Important Points
- `git status` identifies staged, unstaged, and untracked changes.
- `git diff` shows changes that have not been staged.
- `git diff --staged` shows changes prepared for a commit.
- `git log --oneline` displays a compact commit history.
- Always confirm that you are working on the intended branch.

## 8. Understanding Remote Branches

A remote branch represents a branch on a remote repository, such as GitHub.

### Checking Remote Information

```bash
git remote -v
```

### Viewing Local and Remote-Tracking Branches

```bash
git branch -a
```

### Important Points
- A local branch exists in your local repository.
- A remote branch exists in the remote repository.
- A remote-tracking branch records your local view of a remote branch.
- Remote-tracking information can become outdated until you fetch updates.
- The remote named `origin` is commonly created when cloning a repository.

## 9. Fetching Changes — git fetch

The `git fetch` command downloads updates from a remote repository without merging them into the current branch.

### Basic Syntax

```bash
git fetch origin
```

### Important Points
- Fetching updates remote-tracking branch information.
- It does not automatically merge changes into your current branch.
- It allows you to inspect remote changes before integrating them.
- Fetching is useful before updating your feature branch.
- Use `git log` or `git diff` to inspect changes after fetching.

## 10. Pulling Changes — git pull

The `git pull` command fetches remote updates and integrates them into the current branch.

### Basic Syntax

```bash
git pull
```

### Important Points
- `git pull` combines fetching and integration.
- Integration may use a merge or a rebase, depending on the command options and Git configuration.
- Pulling can produce merge conflicts.
- Review your current branch and working-tree status before pulling.
- Follow the team's preferred method for updating branches.

## 11. Keeping a Feature Branch Current

A feature branch may become outdated when new commits are added to its base branch.

### Updating with Merge

```bash
git fetch origin
git switch feature/product-search
git merge origin/main
```

This merges the fetched version of `main` into the feature branch.

### Updating with Rebase

```bash
git fetch origin
git switch feature/product-search
git rebase origin/main
```

This reapplies the feature branch's commits on top of the updated base branch.

### Important Points
- Both approaches can incorporate newer base-branch changes.
- A merge preserves the existing branch history and may create a merge commit.
- A rebase creates new commit IDs for the commits it reapplies.
- Rebase may require conflict resolution.
- Avoid rebasing shared commits unless the team agrees to it.
- After updating, run relevant tests and review the changes.

## 12. Merge vs Rebase

### Merge
- Integrates changes from another branch.
- Preserves the existing commit history.
- May create a merge commit.
- Useful when preserving the history of branch integration is important.

### Rebase
- Reapplies commits on top of another base commit.
- Produces a more linear history.
- Changes the commit IDs of the commits being reapplied.
- Useful when the team prefers a linear history.

### Important Points
- Neither method is universally best.
- Follow the team's workflow.
- Resolve conflicts carefully.
- Test the branch after integration.
- Avoid rewriting published history without coordination.

## 13. Pushing a Branch to GitHub

The `git push` command sends local commits to a remote repository.

### Basic Syntax

```bash
git push -u origin feature/product-search
```

### Important Points
- `origin` is the remote repository name in this example.
- `feature/product-search` is the branch being pushed.
- The `-u` option sets the upstream relationship for future pushes and pulls.
- The branch must be pushed before teammates can review its changes on GitHub.
- Authentication and repository permissions may be required.

After the upstream is configured, later pushes can often use:

```bash
git push
```

## 14. Deleting Branches

Branches can be deleted after their work is no longer needed.

### Deleting a Merged Local Branch

```bash
git branch -d feature/product-search
```

### Force-Deleting a Local Branch

```bash
git branch -D feature/product-search
```

### Important Points
- `git branch -d` normally prevents deletion if Git believes the branch contains unmerged work.
- `git branch -D` forces deletion and can discard access to unmerged commits through that branch name.
- Confirm that important work has been merged or saved before deleting a branch.
- Remote branches are deleted separately.
- Follow the team's cleanup policy.

## 15. Implementing Three Independent Tasks Using Branches

### Task 1 — Add a Feature

Create a branch:

```bash
git switch main
git switch -c feature/add-product
```

Implement the feature, then commit it:

```bash
git add .
git commit -m "Add product creation"
```

### Task 2 — Fix a Bug

Start from the updated base branch after the first task is integrated:

```bash
git switch main
git pull
git switch -c fix/product-price
```

Make the fix, then commit it:

```bash
git add .
git commit -m "Fix product price calculation"
```

### Task 3 — Update Documentation

Create another branch:

```bash
git switch main
git pull
git switch -c docs/update-readme
```

Update the documentation, then commit it:

```bash
git add README.md
git commit -m "Update project README"
```

### Important Points
- Each task has its own branch.
- Each branch should contain only changes related to its task.
- Start later tasks from the updated base branch when appropriate.
- Push branches to GitHub for review.
- Merge completed work according to the team's workflow.
- Run tests and verify the result after integration.

## 16. Maintaining a Clean Git History

A clean history makes project changes easier to understand.

### Important Points
- Use meaningful commit messages.
- Keep commits focused.
- Avoid committing generated files or secrets.
- Do not include unrelated changes in a feature branch.
- Review the diff before committing.
- Update branches according to team policy.
- Avoid force-pushing to shared branches without coordination.
- Delete completed branches when appropriate.

## 17. Common Branching Mistakes

### Making Changes on the Wrong Branch
- Check the current branch with `git status` or `git branch`.
- Switch to the correct branch before starting work.

### Including Unrelated Changes
- Review staged changes before committing.
- Stage only the files required for the task.

### Forgetting to Push a Branch
- Use `git push -u origin branch-name` to publish the branch.

### Working on an Outdated Branch
- Fetch recent changes.
- Merge or rebase the updated base branch according to team policy.

### Deleting Unmerged Work
- Check whether the branch's commits have been integrated.
- Avoid force-deleting branches unless you understand the consequences.

### Important Points
- Check repository status frequently.
- Keep independent tasks separate.
- Do not assume local commits are available on GitHub.
- Test changes after merging or rebasing.

## 18. Branching Best Practices

- Create a separate branch for each independent task.
- Use descriptive branch names.
- Start from the correct base branch.
- Make small, focused commits.
- Review changes before committing.
- Fetch updates regularly when working with others.
- Keep feature branches current using the team's preferred method.
- Push branches when they are ready to be shared.
- Avoid rewriting shared history without agreement.
- Test changes before merging.
- Delete branches only when their work is no longer needed.

## 19. Branching Completion Checklist

- [ ] Can create, list, switch, and delete branches.
- [ ] Can use descriptive branch names.
- [ ] Can make small and focused commits.
- [ ] Can inspect changes using `git diff`.
- [ ] Can fetch and integrate remote changes.
- [ ] Can push a feature branch to GitHub.
- [ ] Can explain the difference between merge and rebase.
- [ ] Can maintain three independent tasks using separate branches.
- [ ] Can keep repository history organized and understandable.
