# Control Flow & Branching Logic

> **Module 01: Python Fundamentals | Topic 02**



## 1. Learning Outcomes

- **Conditionals:** Construct clean, non-redundant if-elif-else branching.
- **Iteration:** Master for loops with range(), enumerate(), and while loops.
- **Loop Control:** Use break and continue purposefully to control execution flow.
- **Defensive Flow:** Avoid infinite loops and off-by-one errors in boundary logic.

## 2. Key Syntax & Concepts


### Branching: if / elif / else

Python evaluates conditions sequentially. Order conditions from most specific to least specific:

```python
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'

# Conditional expression (ternary)
status = 'Pass' if score >= 60 else 'Fail'
```


### Loops: for and while

Use `for` when iterating over known ranges or sequences. Use `while` for condition-driven cycles:

```python
# range(start, stop, step) - note: stop is exclusive
for i in range(1, 6, 2):
    print(i)  # 1, 3, 5

# while loop with guard condition
count = 3
while count > 0:
    print(count)
    count -= 1
```


### Loop Control: break and continue

```python
for num in [1, 2, 3, 4, 5]:
    if num == 2:
        continue  # skip 2
    if num == 4:
        break     # stop at 4
    print(num)    # prints 1, 3
```


## 3. Common Mistakes & Gotchas

- **Off-By-One with range():** range(1, 5) generates [1, 2, 3, 4], NOT up to 5. The stop parameter is always exclusive.
- **Infinite While Loops:** Forgetting to update the loop counter or sentinel inside the while block causes an infinite loop.
- **Modifying Lists While Iterating:** Never remove items from a list while iterating over it directly. Iterate over a slice or copy instead: `for x in my_list[:]:`.

## 4. Practice Tasks

- **Task 1:** Implement a CLI menu loop that displays 4 options and repeats until the user chooses 'Exit'.
- **Task 2:** Write a prime number checker for integers between 2 and 50 using nested loops and break.

## 5. Self-Check Questions

- **Q1:** What values does range(5, 0, -1) yield?
- **Q2:** When should you prefer a for loop over a while loop?
