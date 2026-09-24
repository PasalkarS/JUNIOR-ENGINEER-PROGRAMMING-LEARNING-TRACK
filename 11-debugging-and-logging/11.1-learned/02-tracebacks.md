# Reading Stack Traces & Runtime Inspection

> **Module 11: Debugging & Logging | Topic 02**

## 1. Learning Outcomes
- **Traceback Anatomy:** Read Python stack traces from bottom to top to identify failing lines and call chains.
- **Common Exceptions:** Instantly recognize `KeyError`, `IndexError`, `TypeError`, `AttributeError`, and `ValueError`.
- **Interactive Debugging (`pdb` / `breakpoint()`):** Pause program execution and inspect local variables live.
- **Post-Mortem Analysis:** Analyze crashes with `sys.last_traceback`.

## 2. Key Syntax & Concepts

### Reading a Python Traceback
```text
Traceback (most recent call last):
  File "app.py", line 45, in <module>
    main()
  File "app.py", line 22, in main
    service.process_order(order)
  File "service.py", line 88, in process_order
    total = item["price"] * item["qty"]
KeyError: 'price'
```
**Interpretation:**
- Start at the **bottom**: `KeyError: 'price'` tells you a dictionary lookup failed.
- Line 88 in `service.py` is the immediate location of failure.
- The call stack originated from `main()` on line 45 in `app.py`.

### Using `breakpoint()` for Interactive Inspection
```python
def calculate_metrics(items: list[dict]):
    total = 0
    for item in items:
        # Pauses execution and opens interactive PDB debugger in terminal!
        if item.get("val") is None:
            breakpoint()
        total += item["val"]
    return total
```
**Essential PDB Commands:**
- `n` (next line)
- `s` (step into function)
- `c` (continue execution)
- `p var_name` (print variable value)
- `q` (quit debugger)

## 3. Common Mistakes & Gotchas
- **Reading Tracebacks Top-Down:** The root error type and message are always printed at the bottom of the trace.
- **Leaving `breakpoint()` in Production:** Forgetting a breakpoint inside shipped code halts background worker tasks indefinitely.

## 4. Practice Tasks
- **Task 1:** Insert `breakpoint()` into an arithmetic function and inspect argument values interactively.

## 5. Self-Check Questions
- **Q1:** What built-in Python function drops you into an interactive debugger session?
- **Q2:** What does an `AttributeError: 'NoneType' object has no attribute 'x'` typically mean?
