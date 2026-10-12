# 3 — Pull Requests

## 1. Introduction to Pull Requests

### What it is
A Pull Request (PR) is a request to merge changes from one branch into another branch. It allows other developers to review the code before it becomes part of the main project.

### Important Points
- A PR is commonly created after completing work on a feature branch.
- It shows the changes made to the project.
- Other developers can review the changes and suggest improvements.
- A PR can be updated when reviewers request changes.
- Once approved, the changes can be merged into the target branch.

---

## 2. Understanding the Pull Request Workflow

### What it is
The Pull Request workflow provides a structured way to develop, review, and merge code safely.

### Important Points
- Start from the main branch.
- Create a feature branch.
- Make changes and commit them.
- Push the branch to GitHub.
- Create a Pull Request.
- Review and update the changes if required.
- Merge the PR after the required approval.

### Basic Workflow

```text
main
 |
 └── Create Feature Branch
          |
          ├── Make Changes
          ├── Commit Changes
          └── Push Branch
                 |
                 └── Create Pull Request
                          |
                          ├── Code Review
                          ├── Make Requested Changes
                          └── Merge into main
```

---

## 3. Creating a Pull Request on GitHub

### What it is
Creating a PR on GitHub allows you to submit your branch changes for review.

### Important Points
- Push your feature branch to GitHub before creating the PR.
- Select the correct base branch and compare branch.
- The **base branch** is where the changes will be merged.
- The **compare branch** contains the changes you want to merge.
- Review the changed files before submitting the PR.
- Add a clear title and description.

### Example

Suppose you created a branch named `feature/product-search`.

```bash
git switch feature/product-search
git add .
git commit -m "Add product search"
git push -u origin feature/product-search
```

After pushing the branch:

1. Open the repository on GitHub.
2. Select **Pull requests**.
3. Click **New pull request**.
4. Select `main` as the base branch.
5. Select `feature/product-search` as the compare branch.
6. Review the changes.
7. Add a title and description.
8. Click **Create pull request**.

---

## 4. Writing a Good Pull Request Description

### What it is
A PR description explains what changed, why the change was needed, and how it was tested.

### Important Points
- Use a clear and meaningful title.
- Explain the purpose of the changes.
- Mention the important files or features changed.
- Describe the tests performed.
- Mention known limitations or incomplete work.
- Link the related issue when applicable.

### Example

**Title:**

```text
Add product search functionality
```

**Description:**

```markdown
## Summary
- Added product search functionality.
- Added support for searching products by name.

## Testing
- Tested with existing product names.
- Tested with a product name that does not exist.

## Related Issue
Closes #12
```

A good description helps reviewers understand the change without having to guess its purpose.

---

## 5. Understanding Code Reviews

### What it is
A code review is the process of checking proposed code changes before they are merged into the project.

### Important Points
- Reviewers inspect the code for correctness and readability.
- They check whether the changes meet the requirements.
- They may identify bugs, missing tests, or design problems.
- They can leave comments on specific lines of code.
- They may approve the PR or request changes.
- Review feedback helps improve code quality.

### What Reviewers Check
- Does the code solve the intended problem?
- Is the code easy to understand?
- Are there any obvious bugs or edge cases?
- Are errors handled properly?
- Are tests included where needed?
- Does the change follow the project's coding conventions?

---

## 6. Understanding Review Comments

### What it is
Review comments are messages left by reviewers to ask questions, explain concerns, or suggest improvements to the proposed changes.

### Important Points
- Read the complete comment before responding.
- Understand the problem the reviewer identified.
- Ask for clarification if the feedback is unclear.
- Make the required changes when appropriate.
- Explain your reasoning respectfully if you disagree.
- Mark conversations as resolved when the concern has been addressed.

### Example

A reviewer comments:

```text
This function does not handle an empty search string.
Please add a check for this case.
```

A suitable response:

```text
Good catch. I have added validation for an empty search string.
```

Review comments should be treated as part of collaboration, not as personal criticism.

---

## 7. Handling Requested Changes

### What it is
A reviewer may request changes before approving a PR. You should update your existing branch to address the feedback.

### Important Points
- Switch to the branch associated with the PR.
- Make the necessary code changes.
- Test the updated code.
- Commit and push the changes.
- GitHub automatically updates the existing PR.
- You usually do not need to create a new PR for the same work.

### Basic Syntax

```bash
git switch feature/product-search
```

After editing the files:

```bash
git status
git diff
git add .
git commit -m "Handle empty product searches"
git push
```

### Example Workflow

```text
Reviewer requests changes
          |
          v
Understand the feedback
          |
          v
Update the code
          |
          v
Test the changes
          |
          v
Commit and push
          |
          v
Respond to the review comment
          |
          v
Wait for another review
```

---

## 8. Responding Professionally to Review Feedback

### What it is
Professional communication helps developers resolve problems efficiently and maintain a collaborative working environment.

### Important Points
- Be polite and clear.
- Acknowledge useful feedback.
- Explain what you changed.
- Provide evidence when discussing a technical disagreement.
- Avoid defensive or personal responses.
- Do not claim that an issue is fixed until you have checked it.

### Example Responses

**When you agree with the feedback:**

```text
Thanks for pointing this out. I have updated the validation logic.
```

**When you need clarification:**

```text
Could you clarify how this case should behave when the input is empty?
```

**When you disagree:**

```text
I understand the concern. I used this approach because the requirement
allows multiple matching results. Would you prefer a different behavior?
```

**When you have completed the requested change:**

```text
Updated the function and added a test for the reported case.
```

---

## 9. Understanding Pull Request Approvals

### What it is
An approval indicates that a reviewer has checked the proposed changes and considers them acceptable according to the project's review requirements.

### Important Points
- Reviewers can approve a PR.
- Reviewers can request changes.
- Reviewers can leave comments without formally approving or rejecting the PR.
- Some repositories require one or more approvals before merging.
- Required automated checks must also pass when configured.
- Approval does not replace testing or project requirements.

### Common Review States

| State | Meaning |
|---|---|
| Comment | The reviewer has left feedback. |
| Approve | The reviewer approves the changes. |
| Request changes | The reviewer wants changes before approval. |

The exact rules depend on the repository's settings.

---

## 10. Understanding Merge Strategies

### What it is
A merge strategy determines how the changes from a Pull Request are incorporated into the target branch.

### Important Points

**Merge commit**
- Combines the changes and creates a merge commit.
- Preserves the branch history.

**Squash and merge**
- Combines the PR's commits into one commit on the target branch.
- Creates a simpler, more compact history.

**Rebase and merge**
- Replays the PR commits onto the target branch.
- Produces a linear history without a merge commit.

### Comparison

| Strategy | Main Purpose |
|---|---|
| Merge commit | Preserve branch history and the merge point |
| Squash and merge | Combine PR commits into one commit |
| Rebase and merge | Maintain a linear commit history |

The project may specify which strategy should be used. Follow the repository's workflow rather than choosing arbitrarily.

---

## 11. Linking Pull Requests to Issues

### What it is
Linking a PR to a GitHub issue connects the implementation to the requirement or bug report it addresses.

### Important Points
- Issues describe work that needs to be done.
- PRs propose the code changes for that work.
- Linking them makes progress easier to track.
- GitHub can automatically close supported linked issues when the PR is merged into the repository's default branch.

### Example

In the PR description:

```markdown
Closes #12
```

This links the PR to issue number `12`.

Other supported keywords include `Fixes #12` and `Resolves #12`.

Use the actual issue number from your repository.

---

## 12. Understanding Draft Pull Requests

### What it is
A Draft Pull Request is used to share work that is not yet ready for final review or merging.

### Important Points
- It allows developers to share work in progress.
- Reviewers can see the proposed changes early.
- It communicates that the work is not ready for final approval.
- You can mark it as ready for review when it is complete.
- Draft PRs cannot be merged until they are marked ready for review.

Draft PRs are useful when you need early feedback or want to communicate progress.

---

## 13. Checking Pull Request Changes

### What it is
Before submitting or updating a PR, inspect the changes to ensure that only the intended modifications are included.

### Important Points
- Check which files have changed.
- Review added and removed lines.
- Remove unrelated changes.
- Confirm that the correct branch is being used.
- Run relevant tests before requesting review.

### Basic Commands

```bash
git status
git diff
git diff --staged
git log --oneline
```

These commands help you inspect the working directory, staged changes, and commit history before pushing your work.

---

## 14. Common Pull Request Mistakes

### What it is
Common PR mistakes can make code reviews harder and introduce unnecessary risk into a project.

### Important Points
- Creating a PR from the wrong branch.
- Using a vague title such as `Changes` or `Update`.
- Writing a description that does not explain the purpose.
- Including unrelated file changes.
- Creating very large PRs that are difficult to review.
- Ignoring reviewer comments.
- Pushing changes without testing them.
- Merging before required approvals or checks are complete.
- Forgetting to connect the PR to its related issue.

### Good Practice
Keep each PR focused on one feature, fix, or clearly defined task.

---

## 15. Task — Submit and Revise a Pull Request After Review

### Objective
Create a Pull Request for a small feature, respond to review feedback, update the code, and prepare the PR for merging.

### Steps

1. Start with an up-to-date `main` branch.
2. Create a branch named `feature/product-search`.
3. Implement a simple product search function.
4. Test the function with valid input, empty input, and a product that does not exist.
5. Commit the changes.
6. Push the branch to GitHub.
7. Create a PR targeting `main`.
8. Write a clear title and description.
9. Ask a teammate to review the PR, or simulate review feedback.
10. Address at least one review comment.
11. Test the updated code.
12. Commit and push the revision.
13. Reply to the review comment explaining the change.
14. Confirm that the required reviews and checks are complete before merging.

### Example Branch and Commit Commands

```bash
git switch main
git pull
git switch -c feature/product-search
```

After implementing and testing the feature:

```bash
git add .
git commit -m "Add product search"
git push -u origin feature/product-search
```

After receiving review feedback and making the requested changes:

```bash
git add .
git commit -m "Handle empty product searches"
git push
```

Create and manage the PR through GitHub.

---

## 16. Completion Checklist

- [ ] I can explain what a Pull Request is.
- [ ] I can create a PR from a feature branch.
- [ ] I can write a clear PR title and description.
- [ ] I can inspect proposed changes.
- [ ] I understand review comments, approvals, and requested changes.
- [ ] I can update an existing PR after review feedback.
- [ ] I can respond professionally to reviewers.
- [ ] I understand common merge strategies.
- [ ] I can link a PR to a GitHub issue.
- [ ] I can prepare a PR for merging after the required checks.

### Pass Criteria

You can create a Pull Request, explain your changes, respond professionally to review feedback, update the code, and prepare the PR for merging according to the repository's workflow.
