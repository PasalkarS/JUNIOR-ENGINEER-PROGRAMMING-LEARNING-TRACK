# The Scientific Debugging Methodology

> **Module 11: Debugging & Logging | Topic 01**

## 1. Learning Outcomes
- **Avoid Trial-and-Error:** Replace random code changes with a disciplined, systematic debugging loop.
- **The 7-Step Method:** Reproduce -> Isolate -> Hypothesize -> Inspect Evidence -> Fix -> Verify -> Prevent Recurrence.
- **Minimal Reproducible Example (MRE):** Strip away unrelated code to produce a tiny test case reproducing the bug.
- **Regression Tests:** Write a failing test verifying the bug BEFORE applying the fix.

## 2. The 7-Step Systematic Debugging Cycle

```
 1. REPRODUCE    --> Create a reliable, consistent reproduction script.
 2. ISOLATE      --> Narrow down failure to the exact module/function.
 3. HYPOTHESIZE  --> Form a testable theory about the root cause.
 4. INSPECT      --> Examine variables, tracebacks, and logs.
 5. FIX          --> Make the minimal necessary code change.
 6. VERIFY       --> Confirm the reproduction script now succeeds.
 7. PREVENT      --> Add automated regression test so it never returns.
```

## 3. Common Mistakes & Gotchas
- **Changing Multiple Things at Once:** Altering three variables simultaneously makes it impossible to know which change resolved the issue.
- **Fixing Symptoms Instead of Causes:** Putting `try: ... except Exception: pass` suppresses the crash without addressing why bad data occurred.

## 4. Practice Tasks
- **Task 1:** Given a buggy function that crashes on empty lists, create a 5-line Minimal Reproducible Example demonstrating the failure.

## 5. Self-Check Questions
- **Q1:** Why is writing a failing test before applying a bugfix considered best practice?
- **Q2:** What constitutes a Minimal Reproducible Example?
