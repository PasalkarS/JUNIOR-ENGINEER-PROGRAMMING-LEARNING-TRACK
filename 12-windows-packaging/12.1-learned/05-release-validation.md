# Release Validation & Clean Machine Testing

> **Module 12: Windows Packaging | Topic 05**

## 1. Learning Outcomes
- **The "Works on My Machine" Trap:** Why developers' machines have Python, compilers, and DLLs that end-users lack.
- **Clean Environment Testing:** Test packaged binaries inside a clean Windows Sandbox or fresh VM.
- **Release Smoke Test Checklist:** Follow a structured pre-release verification protocol.
- **Rollback Planning:** Maintain previous stable release versions and rollback procedures.

## 2. Release Validation Checklist Template

```markdown
# Windows Release Smoke Test Checklist: v1.2.0

## Pre-Release Verification
- [ ] Build generated on clean CI or dedicated build machine.
- [ ] Version string in UI matches release tag (`v1.2.0`).
- [ ] Executable file size is within expected range (30-60 MB).

## Clean Machine Validation (Windows Sandbox)
- [ ] Executable launches on machine with NO Python installed.
- [ ] No missing Visual C++ Redistributable errors (`VCRUNTIME140.dll`).
- [ ] Application successfully initializes SQLite database in `%LOCALAPPDATA%`.
- [ ] Able to perform core CRUD workflows.
- [ ] Exporting Excel report produces a valid, uncorrupted `.xlsx` file.
- [ ] Application closes cleanly without lingering background processes.

## Post-Verification
- [ ] Release notes published with changelog.
- [ ] Checksum (SHA-256) generated and published.
```

## 3. Common Mistakes & Gotchas
- **Missing VC++ Runtime:** Forgetting that target machines may lack `VCRUNTIME140.dll`. Bundle the runtime or include it in installer prerequisites.
- **Testing Only in IDE:** Never declare an executable verified until it runs standalone outside your development environment.

## 4. Practice Tasks
- **Task 1:** Compute the SHA-256 checksum of an executable using PowerShell (`Get-FileHash app.exe -Algorithm SHA256`).

## 5. Self-Check Questions
- **Q1:** What tool built into Windows 10/11 Professional is ideal for testing executables on a clean machine?
- **Q2:** Why are SHA-256 checksums published alongside downloadable release binaries?
