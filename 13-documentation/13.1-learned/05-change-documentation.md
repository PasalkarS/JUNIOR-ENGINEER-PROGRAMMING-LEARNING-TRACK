# Change Management, Release Notes & Handover Packs

> **Module 13: Documentation | Topic 05**

## 1. Learning Outcomes
- **Semantic Versioning (SemVer):** Understand `MAJOR.MINOR.PATCH` version bumps.
- **Changelog Standards:** Maintain `CHANGELOG.md` following Keep a Changelog standards.
- **Release Notes:** Write user-facing summaries of new features, bug fixes, and breaking changes.
- **Handover Packs:** Package codebase documentation for seamless handoff to maintenance teams.

## 2. Keep a Changelog Standard
```markdown
# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [1.2.0] - 2026-09-24

### Added
- Excel export support with styled corporate headers and auto-fit column widths.
- Automated duplicate record quarantine in data validation pipeline.

### Changed
- Refactored order total calculations into pure functions for improved testability.

### Fixed
- Resolved `ZeroDivisionError` occurring when total revenue equaled zero.

### Security
- Replaced insecure string concatenation with parameterized SQLite queries.
```

## 3. Common Mistakes & Gotchas
- **Dumping Raw Git Commits into Release Notes:** "Merge branch 'fix-stuff'" is unhelpful to users. Group and explain changes by user impact.
- **Silent Breaking Changes:** Modifying database schemas or API arguments without bumping the MAJOR version breaks downstream clients.

## 4. Practice Tasks
- **Task 1:** Draft a changelog entry for a release that introduces a new CSV import feature and patches a memory leak.

## 5. Self-Check Questions
- **Q1:** According to Semantic Versioning, when must the MAJOR version number be incremented?
- **Q2:** What are the standard section headers in a Keep a Changelog document?
