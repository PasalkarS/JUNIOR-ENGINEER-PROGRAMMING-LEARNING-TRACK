# Multi-Page Application Architecture

> **Module 10: Streamlit | Topic 03**

## 1. Learning Outcomes
- **Directory Structure:** Organize multi-page apps using the native `pages/` directory convention.
- **Navigation:** Structure sidebars and page routing seamlessly.
- **Shared State Across Pages:** Share user authentication and configuration across all pages via `st.session_state`.
- **Modular Component Reusability:** Import shared service and UI components cleanly.

## 2. Standard Multi-Page Project Layout
```text
my_streamlit_app/
├── app.py                 # Landing page & session initializer
├── pages/
│   ├── 1_📊_Dashboard.py  # Page 1: Analytics & charts
│   ├── 2_📝_Data_Entry.py # Page 2: Forms & creation
│   └── 3_⚙️_Settings.py   # Page 3: User preferences
└── src/
    ├── services.py        # Shared business logic
    └── database.py        # Shared database persistence
```

### Shared Auth Guard Pattern in `pages/1_📊_Dashboard.py`
```python
import streamlit as st

# Check if authenticated in global session
if not st.session_state.get("authenticated", False):
    st.warning("Please login on the home page first.")
    st.stop()  # Halts execution of this page immediately

st.title("Executive Dashboard")
st.write(f"Welcome, {st.session_state.get('username', 'User')}!")
```

## 3. Common Mistakes & Gotchas
- **Page Ordering:** Streamlit sorts pages alphanumerically by filename. Prefix files with numbers (`1_`, `2_`) to enforce menu order.
- **Calling `st.set_page_config` Repeatedly:** Each page should define its own page title via `st.set_page_config()` as its first command.

## 4. Practice Tasks
- **Task 1:** Build a 2-page Streamlit application where Page 1 collects user input and Page 2 visualizes the aggregated data.

## 5. Self-Check Questions
- **Q1:** Where does Streamlit look for additional pages in a multi-page app?
- **Q2:** What does `st.stop()` do when placed inside an authentication check?
