# Data UX, Filtering, Downloads & Empty States

> **Module 10: Streamlit | Topic 04**

## 1. Learning Outcomes
- **Interactive DataFrames:** Use `st.dataframe` with column configurations and selection.
- **File Downloads:** Generate CSV and Excel download buttons with `st.download_button`.
- **Empty States:** Provide graceful guidance when search filters return zero results.
- **Feedback & Alerts:** Display progress bars, success toasts, warning banners, and error callouts.

## 2. Key Syntax & Concepts

### Table Filtering & CSV Download
```python
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "Product": ["Monitor", "Keyboard", "Mouse", "Laptop"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics"],
    "Stock": [15, 45, 0, 8]
})

# Dynamic Search Filter
query = st.text_input("Filter by product name:").strip().lower()
filtered_df = df[df["Product"].str.lower().str.contains(query)] if query else df

# Empty State Handling
if filtered_df.empty:
    st.info(f"No products found matching '{query}'. Try a different keyword.")
else:
    st.dataframe(filtered_df, use_container_width=True)
    
    # Download Button
    csv_bytes = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Filtered Results (CSV)",
        data=csv_bytes,
        file_name="filtered_products.csv",
        mime="text/csv"
    )
```

## 3. Common Mistakes & Gotchas
- **Recomputing CSVs on Every Render:** Converting a large DataFrame to CSV inside `st.download_button` can lag. Cache conversion functions with `@st.cache_data`.
- **Blank Screens on Zero Results:** Leaving a screen completely blank when queries return empty confuses users. Always provide an explicit `st.info` empty state.

## 4. Practice Tasks
- **Task 1:** Build a dataset viewer with a multi-select category filter and an Excel download button.

## 5. Self-Check Questions
- **Q1:** What parameter makes `st.dataframe` stretch across the full browser width?
- **Q2:** Why are empty-state messages critical for user experience?
