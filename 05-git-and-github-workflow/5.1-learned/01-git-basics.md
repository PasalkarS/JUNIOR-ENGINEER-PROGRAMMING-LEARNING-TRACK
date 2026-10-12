# 1 — Git Basics

## 1. Introduction to Git

- Git is a version control system used to track changes in files.
- It helps developers maintain different versions of a project.
- Git allows developers to review previous changes and recover from common mistakes.

### Important Points
- Git tracks changes made to files over time.
- It records changes through commits.
- It allows developers to create branches for separate tasks.
- It helps compare different versions of files.
- It supports collaboration between developers.

## 2. What Is Version Control?

Version control is a system that records changes made to files so that previous versions can be reviewed or restored.

### Important Points
- It maintains a history of changes.
- It helps identify when and why a change was made.
- It allows developers to compare versions.
- It makes it easier to recover from mistakes.
- Git is one of the most widely used version control systems.

## 3. Git vs GitHub

### Git
- Git is a version control system.
- It can work locally on a computer.
- It tracks changes and maintains commit history.
- It supports branches, merges, and comparisons.

### GitHub
- GitHub is an online platform for hosting Git repositories.
- It allows developers to share code.
- It supports pull requests, issues, and code reviews.
- It helps teams collaborate on projects.

### Important Points
- Git and GitHub are not the same thing.
- Git can be used without GitHub.
- GitHub uses Git to manage repository history.
- A local Git repository does not automatically upload changes to GitHub.

## 4. Local and Remote Repositories

A repository is a location where a project's files and Git history are stored.

### Local Repository
- Stored on your computer.
- Used to make changes and create commits.
- Can be used without an internet connection for most local operations.

### Remote Repository
- Stored on a remote server, such as GitHub.
- Used to share code and collaborate with others.
- Can receive changes pushed from local repositories.

### Important Points
- A local repository and a remote repository can have different commits.
- `git push` sends local commits to a remote repository.
- `git pull` fetches remote changes and integrates them into the current branch.
- `git fetch` downloads remote updates without integrating them into the current branch.

## 5. Installing and Configuring Git

Git must be installed before you can use its commands.

### Checking the Git Version

```bash
git --version
```

This command displays the installed Git version.

### Configuring Your Username

```bash
git config --global user.name "Your Name"
```

### Configuring Your Email

```bash
git config --global user.email "you@example.com"
```

### Important Points
- The `--global` option applies the configuration to your user account on the computer.
- Git uses the configured name and email in commit metadata.
- These settings do not automatically authenticate you with GitHub.
- You can check your configuration using `git config --list`.

## 6. Creating a Repository — git init

The `git init` command initializes a new Git repository in the current directory.

### Basic Syntax

```bash
git init
```

### Example

```bash
mkdir my-project
cd my-project
git init
```

### Important Points
- `mkdir` creates a directory.
- `cd` moves into the directory.
- `git init` initializes Git tracking in that directory.
- Git creates a hidden `.git` directory to store repository information.
- Your project files are not automatically committed when you initialize a repository.

## 7. Cloning a Repository — git clone

The `git clone` command creates a local copy of an existing repository.

### Basic Syntax

```bash
git clone repository-url
```

### Example

```bash
git clone https://github.com/username/project-name.git
```

### Important Points
- Cloning downloads the repository's files and Git history.
- It normally creates a new directory for the repository.
- The cloned repository is configured with a remote named `origin`.
- You can start working with the repository after cloning it.
- You need access to the repository when it is private.

## 8. Understanding the Git Working Areas

Git organizes file changes into different areas.

### Working Directory
- Contains the project files you work on.
- Changes made to files appear here first.

### Staging Area
- Contains changes selected for the next commit.
- Changes are added using `git add`.

### Local Repository
- Stores committed snapshots and their history.
- Commits are created using `git commit`.

### Basic Workflow

```text
Working Directory
        |
        | git add
        v
Staging Area
        |
        | git commit
        v
Local Repository
```

### Important Points
- Editing a file does not automatically stage it.
- Staging a file does not create a commit.
- A commit records the staged changes.
- You can stage only selected files instead of all changes.

## 9. Checking Repository Status — git status

The `git status` command shows the current state of your repository.

### Basic Syntax

```bash
git status
```

### Important Points
- It identifies the current branch.
- It shows untracked files.
- It shows modified files.
- It shows staged changes ready to be committed.
- It helps you understand what needs to be added or committed.

### Common File States

- **Untracked:** Git is not yet tracking the file.
- **Modified:** A tracked file has changed.
- **Staged:** Changes are selected for the next commit.
- **Committed:** Changes have been recorded in the repository history.

## 10. Staging Changes — git add

The `git add` command places changes in the staging area.

### Staging One File

```bash
git add app.py
```

### Staging Multiple Files

```bash
git add app.py README.md
```

### Staging All Changes in the Current Directory

```bash
git add .
```

### Important Points
- Staging prepares changes for a commit.
- You can stage individual files.
- `git add .` stages new, modified, and deleted files under the current directory, subject to Git's ignore rules.
- Staging does not upload changes to GitHub.
- Review staged changes before committing them.

## 11. Creating Commits — git commit

A commit records the staged changes in the repository history.

### Basic Syntax

```bash
git commit -m "Add product validation"
```

### Important Points
- A commit creates a snapshot of the staged changes.
- The `-m` option provides a commit message.
- Commit messages should describe the purpose of the change.
- A commit usually includes only the changes that were staged.
- Commits are stored locally until they are pushed to a remote repository.

### Good Commit Messages

```text
Add product validation
Fix inventory quantity calculation
Update database setup instructions
Remove unused variables
```

Avoid unclear messages such as:

```text
changes
update
final
test
```

## 12. Viewing Commit History — git log

The `git log` command displays the commit history.

### Basic Syntax

```bash
git log
```

### Compact History

```bash
git log --oneline
```

### Important Points
- It displays previous commits.
- Each commit has a unique identifier called a commit hash.
- It shows the author and commit date.
- Commit messages explain the recorded changes.
- History helps you understand how the project developed.

## 13. Comparing Changes — git diff

The `git diff` command displays differences between versions of files.

### Viewing Unstaged Changes

```bash
git diff
```

Shows changes in tracked files that have not been staged.

### Viewing Staged Changes

```bash
git diff --staged
```

Shows changes that are staged for the next commit.

### Important Points
- `+` lines indicate added content.
- `-` lines indicate removed content.
- Reviewing differences helps catch mistakes before committing.
- `git diff` does not automatically change files.
- Use it with `git status` to understand the state of your work.

## 14. Restoring Changes — git restore

The `git restore` command restores file contents or removes changes from the staging area.

### Discarding Unstaged Changes

```bash
git restore app.py
```

Restores the file to its content in the index, usually discarding unstaged changes.

### Unstaging a File

```bash
git restore --staged app.py
```

Removes the file's changes from the staging area while keeping the working-directory changes.

### Important Points
- Restoring a file can permanently discard uncommitted work.
- `git restore` does not create a new commit.
- `git restore --staged` does not normally discard the file's content changes.
- Check `git status` before and after restoring.
- If you need to keep your changes, save a copy before using a destructive command.

## 15. Introduction to Branches

A branch allows you to work on a separate line of development without immediately changing another branch.

### Listing Branches

```bash
git branch
```

### Creating a Branch

```bash
git branch feature-login
```

### Switching Branches

```bash
git switch feature-login
```

### Creating and Switching to a Branch

```bash
git switch -c feature-login
```

### Important Points
- Branches help separate different tasks.
- The default branch is commonly named `main`.
- You can switch between branches.
- Each branch points to a commit in the repository history.
- A branch is useful for developing a feature or fixing a bug independently.

## 16. Merging Branches

Merging combines changes from one branch into the branch you currently have checked out.

### Basic Syntax

```bash
git switch main
git merge feature-login
```

### Important Points
- Switch to the branch that should receive the changes first.
- The merge command integrates the selected branch into the current branch.
- Git may perform a fast-forward merge when possible.
- Git may create a merge commit when needed.
- A merge conflict can occur when Git cannot automatically combine changes.
- Review and test the merged result.

## 17. Understanding Merge Conflicts

A merge conflict occurs when Git cannot automatically determine how to combine competing changes.

### Common Causes
- Two branches modify the same lines differently.
- One branch deletes a file that another branch modifies.
- Changes overlap in a way Git cannot resolve automatically.

### Important Points
- Git identifies the files that contain conflicts.
- Open each conflicted file and inspect both versions.
- Decide whether to keep one change or combine both.
- Remove conflict markers after resolving the conflict.
- Test the final result before completing the merge.

## 18. Recovering from Common Local Mistakes

Git provides commands to help recover from common mistakes.

### Mistake: Forgot to Stage a File

```bash
git add app.py
```

### Mistake: Staged the Wrong File

```bash
git restore --staged app.py
```

### Mistake: Want to Review Changes Before Committing

```bash
git diff
git diff --staged
```

### Mistake: Want to Check Previous Commits

```bash
git log --oneline
```

### Mistake: Want to Discard Unstaged Changes

```bash
git restore app.py
```

Be careful: this can discard work that has not been committed.

### Important Points
- Use `git status` before choosing a recovery command.
- Understand whether the changes are unstaged, staged, or committed.
- Do not run destructive commands without checking what they will affect.
- If a change is important, create a backup before attempting recovery.
- Recovery depends on the type of mistake and whether the changes were committed.

## 19. Basic Command-Line Git Exercise

### Task

Create a small project and practice the basic Git workflow.

### Steps

1. Create a folder named `git-basics-practice`.
2. Initialize a Git repository using `git init`.
3. Create a file named `README.md`.
4. Add some text to the file.
5. Check the repository using `git status`.
6. Stage the file using `git add README.md`.
7. Review the staged changes using `git diff --staged`.
8. Commit the file using `git commit`.
9. Modify the file and inspect the changes using `git diff`.
10. Stage and commit the second change.
11. Review the commit history using `git log --oneline`.
12. Create a branch named `feature-notes`.
13. Add a new file on that branch and commit it.
14. Switch back to `main` and merge the feature branch.
15. Check the final repository status.

### Pass Criteria

- Can initialize and clone repositories.
- Can identify untracked, modified, and staged files.
- Can stage and commit changes.
- Can review differences and commit history.
- Can restore changes carefully.
- Can create, switch, and merge branches.
- Can recover from common local mistakes without accidentally losing important work.

## 20. Important Git Best Practices

- Check `git status` regularly.
- Review changes before staging and committing.
- Make small, focused commits.
- Write meaningful commit messages.
- Use branches for independent tasks.
- Understand the difference between Git and GitHub.
- Use `git diff` to inspect changes.
- Be careful with commands that discard work.
- Test changes before merging.
- Keep the repository history understandable.
- Never assume uncommitted changes are safely recoverable.
