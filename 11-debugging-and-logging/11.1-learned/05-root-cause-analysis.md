# Root Cause Analysis (RCA) & Post-Mortems

> **Module 11: Debugging & Logging | Topic 05**

## 1. Learning Outcomes
- **Symptom vs Root Cause:** Treat the underlying disease rather than suppressing the symptom.
- **The 5-Whys Technique:** Drill down through successive causes until finding the systemic failure.
- **Writing RCA Reports:** Document incident timeline, root cause, short-term fix, and permanent remediation.
- **Blameless Culture:** Focus on process, tooling, and test improvements rather than individual blame.

## 2. RCA Report Structure Template

```markdown
# Incident RCA Report: #INC-2026-042

## 1. Executive Summary
On 2026-09-12, the daily sales ETL pipeline failed at 02:00 UTC due to an unhandled duplicate transaction key.

## 2. Impact
- 4,200 orders delayed from financial reporting for 3.5 hours.
- Zero data loss occurred.

## 3. Timeline
- 02:00: Scheduled job triggered.
- 02:05: Pipeline aborted with `sqlite3.IntegrityError: UNIQUE constraint failed`.
- 04:30: On-call engineer alerted.
- 05:15: Hotfix deployed quarantining duplicate rows into audit sheet.
- 05:35: Backfill completed successfully.

## 4. Root Cause Analysis (The 5 Whys)
1. **Why did the pipeline fail?** Unique constraint failed on `order_id`.
2. **Why was order_id duplicated?** An upstream vendor re-transmitted the same batch file twice.
3. **Why did the re-transmission break the pipeline?** The pipeline lacked an idempotent deduplication step.
4. **Why was deduplication missing?** Specification assumed all vendor batches were pre-deduplicated.
5. **Why was this assumption made?** Lack of defensive input contract validation.

## 5. Corrective & Preventative Actions
- [x] Short-term: Added deduplication step to `cleaner.py`.
- [ ] Long-term: Add automated schema & duplicate audit quarantine stage to all ingestors.
- [ ] Testing: Add automated integration test simulating duplicate vendor batch re-delivery.
```

## 3. Common Mistakes & Gotchas
- **Stopping at the First 'Why':** Blaming "vendor sent bad data" misses the real cause: "our code wasn't defensive against duplicate data".
- **Failing to Track Action Items:** Writing an RCA without implementing preventative unit tests guarantees the bug will recur.

## 4. Practice Tasks
- **Task 1:** Write a 5-Whys analysis for a scenario where an application ran out of disk space due to unbounded log growth.

## 5. Self-Check Questions
- **Q1:** What is the primary objective of a blameless post-mortem?
- **Q2:** Why is a preventative automated test an essential output of every bugfix?
