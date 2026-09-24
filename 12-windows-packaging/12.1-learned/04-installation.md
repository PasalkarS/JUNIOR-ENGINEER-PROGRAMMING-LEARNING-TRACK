# Installers, Shortcuts & Windows Deployment

> **Module 12: Windows Packaging | Topic 04**

## 1. Learning Outcomes
- **Installer Tooling:** Understand MSI / Inno Setup installers vs portable ZIP archives.
- **Start Menu Shortcuts:** Create clean user entry points and desktop shortcuts.
- **Silent Installation:** Support enterprise deployments using silent flags (`/VERYSILENT /SUPPRESSMSGBOXES`).
- **Clean Uninstallation:** Ensure user registry keys and shortcuts are removed cleanly upon uninstall.

## 2. Deployment Packaging Strategies

| Format | Pros | Cons | Target Audience |
|---|---|---|---|
| **Portable ZIP** | Zero admin rights needed, unpack and run | No Start Menu shortcuts, manual updates | Developers, internal engineers |
| **Inno Setup (EXE)** | Small installer, creates shortcuts, uninstaller included | Requires running an installer setup | Business end-users |
| **MSI Package** | Group Policy deployment (GPO), corporate standard | More complex authoring tools (WiX) | IT Enterprise Admins |

## 3. Common Mistakes & Gotchas
- **Deleting User Data on Uninstall:** Uninstallers should remove binaries and shortcuts, but prompt before wiping user databases in `%APPDATA%`.
- **Omitting Uninstaller Testing:** Always test the uninstall procedure to ensure it doesn't leave orphaned registry keys or processes.

## 4. Practice Tasks
- **Task 1:** Create a clean ZIP release package containing the frozen executable, sample data, and a `README.txt` setup guide.

## 5. Self-Check Questions
- **Q1:** What is the difference between a portable ZIP package and an Inno Setup installer?
- **Q2:** Why do enterprise IT departments prefer silent installer flags?
