# Streamlit Foundations & Execution Model

> **Module 10: Streamlit | Topic 01**

## 1. Learning Outcomes
- **The Rerun Execution Model:** Understand that Streamlit reruns the entire Python script from top to bottom on every user interaction.
- **Basic UI Widgets:** Render inputs (`st.text_input`, `st.number_input`, `st.button`, `st.selectbox`).
- **Data Display:** Output DataFrames (`st.dataframe`, `st.table`), metrics (`st.metric`), and markdown.
- **Layout Containers:** Structure dashboards with `st.columns`, `st.sidebar`, and `st.expander`.

## 2. Key Syntax & Concepts

### Hello Streamlit App Pattern
```python
import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Operations Dashboard", layout="wide")

# Sidebar Controls
st.sidebar.header("Filter Controls")
selected_region = st.sidebar.selectbox("Select Region", ["North", "South", "East", "West"])

# Main Dashboard Content
st.title("Enterprise Operations Portal")
st.write(f"Displaying metrics for: **{selected_region}**")

# Column Layout
col1, col2, col3 = st.columns(3)
col1.metric("Active Units", "1,240", "+12%")
col2.metric("Efficiency", "94.2%", "+1.5%")
col3.metric("Error Rate", "0.08%", "-0.02%")
```

## 3. Common Mistakes & Gotchas
- **Forgetting the Top-to-Bottom Rerun:** Heavy computations (loading large CSVs or training models) will re-execute on every button click unless cached with `@st.cache_data`.
- **Calling `st.set_page_config` Late:** `st.set_page_config()` must be the very first Streamlit command called in your script.

## 4. Practice Tasks
- **Task 1:** Build a 2-column Streamlit app where entering a principal amount and interest rate in column 1 displays calculated monthly payments in column 2.

## 5. Self-Check Questions
- **Q1:** When does Streamlit rerun a script?
- **Q2:** What is the difference between `st.dataframe()` (interactive) and `st.table()` (static)?
