# Forms, Session State & Stateful Workflows

> **Module 10: Streamlit | Topic 02**

## 1. Learning Outcomes
- **st.session_state:** Preserve variables and user choices across script reruns.
- **st.form:** Batch multiple input widgets together and rerun only upon explicit form submission.
- **Callbacks:** Execute custom logic immediately before the main script reruns.
- **Multi-Step Workflows:** Implement wizards and tabbed workflows without losing data.

## 2. Key Syntax & Concepts

### Form Batching & Session State
```python
import streamlit as st

# 1. Initialize session state variable if not set
if "submissions" not in st.session_state:
    st.session_state["submissions"] = []

st.subheader("Asset Registration Form")

# 2. Wrap inputs inside st.form to prevent premature reruns
with st.form("new_asset_form", clear_on_submit=True):
    asset_name = st.text_input("Asset Name")
    category = st.selectbox("Category", ["Hardware", "Furniture", "Software"])
    price = st.number_input("Value ($)", min_value=0.0, step=50.0)
    
    # Form submission button
    submitted = st.form_submit_button("Register Asset")
    
    if submitted:
        if not asset_name.strip():
            st.error("Asset name cannot be blank!")
        else:
            record = {"name": asset_name, "category": category, "value": price}
            st.session_state["submissions"].append(record)
            st.success(f"Registered {asset_name} successfully!")

st.write(f"Total Logged in Session: {len(st.session_state['submissions'])}")
```

## 3. Common Mistakes & Gotchas
- **Relying on Local Variables for State:** Regular variables reset to their initial values on every user click. Always store persistent state in `st.session_state`.
- **Modifying Widget Keys Outside Callbacks:** Mutating `st.session_state["my_widget_key"]` after the widget has already rendered triggers errors.

## 4. Practice Tasks
- **Task 1:** Build an interactive shopping cart app using `st.session_state` where users add items from a selectbox and the total balance updates dynamically.

## 5. Self-Check Questions
- **Q1:** Why should forms (`st.form`) be used instead of standalone input widgets for complex forms?
- **Q2:** How do you safely check if a key exists in `st.session_state`?
