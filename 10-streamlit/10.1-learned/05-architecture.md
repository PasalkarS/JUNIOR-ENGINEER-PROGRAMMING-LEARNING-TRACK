# Clean Architecture for Streamlit Apps

> **Module 10: Streamlit | Topic 05**

## 1. Learning Outcomes
- **Separation of Concerns:** Keep SQL queries and calculation algorithms out of UI scripts.
- **Streamlit Layering:** `UI View (st.*) -> Service Layer -> Repository Layer -> Database`.
- **Caching Strategies:** Accelerate loads using `@st.cache_data` (for DataFrames) and `@st.cache_resource` (for DB connections).
- **Testability:** Test domain calculations with pytest without spinning up the Streamlit UI.

## 2. Layered Architecture & Caching Example
```python
import streamlit as st
import sqlite3

# 1. Cached Resource: Database Connection (Created once!)
@st.cache_resource
def get_database_connection():
    return sqlite3.connect("app.db", check_same_thread=False)

# 2. Cached Data: Heavy Query (Re-run only when query parameters change)
@st.cache_data(ttl=300)  # Expire after 5 minutes
def load_sales_summary(year: int):
    conn = get_database_connection()
    return pd.read_sql("SELECT * FROM sales WHERE year = ?", conn, params=(year,))

# 3. Pure UI Layer: Consumes service data
def render_sales_page():
    st.title("Sales Analytics")
    year = st.selectbox("Year", [2024, 2025, 2026])
    data = load_sales_summary(year)
    st.dataframe(data)
```

## 3. Common Mistakes & Gotchas
- **Putting Business Logic in Widgets:** Embedding tax math or database inserts directly inside widget event blocks destroys testability.
- **Caching Un-Hashable Objects:** `@st.cache_data` requires arguments to be hashable or serializable.

## 4. Practice Tasks
- **Task 1:** Refactor a script with raw SQL queries in UI buttons into a clean repository and service architecture with `@st.cache_resource`.

## 5. Self-Check Questions
- **Q1:** What is the difference between `@st.cache_data` and `@st.cache_resource`?
- **Q2:** Why should business logic be kept in separate Python modules outside of Streamlit UI files?
