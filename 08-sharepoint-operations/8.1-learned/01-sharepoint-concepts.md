# SharePoint Information Architecture & Models

> **Module 08: SharePoint Operations | Topic 01**

## 1. Learning Outcomes
- **Information Architecture:** Understand Sites, Site Collections, Subsites, Lists, and Document Libraries.
- **Lists vs Libraries:** Distinguish tabular metadata rows (Lists) from binary file storage (Libraries).
- **Columns & Views:** Differentiate Choice, Lookup, Managed Metadata, and Calculated column types.
- **Permissions Hierarchy:** Understand Site-level vs List-level inherited and broken permissions.

## 2. Key Architecture Comparison

| Concept | SharePoint Entity | Relational / OS Analogy |
|---|---|---|
| Site | `Web` / `Site` | Database or application workspace |
| List | `List` (Custom) | Relational database table |
| List Item | `ListItem` | Single row of record data |
| Document Library | `List` (Type: 101) | Folder with custom metadata attached to each file |
| Internal Name | `StaticName` | Database column name (immutable, no spaces) |
| Display Name | `Title` | UI column label shown to business users |

## 3. Common Mistakes & Gotchas
- **Internal Name vs Display Name:** In code/REST APIs, columns MUST be queried by their internal name (e.g. `Order_x0020_Date`), NOT their user-facing display name.
- **List Item Limit (Threshold):** SharePoint default query limit is 5,000 items. Queries exceeding 5,000 unindexed items will be blocked.

## 4. Practice Tasks
- **Task 1:** Map a corporate asset tracking requirement (asset ID, serial number, owner, purchase date) into SharePoint List column definitions.

## 5. Self-Check Questions
- **Q1:** What is the primary difference between a SharePoint List and a Document Library?
- **Q2:** Why should you always use internal field names in automation scripts?
