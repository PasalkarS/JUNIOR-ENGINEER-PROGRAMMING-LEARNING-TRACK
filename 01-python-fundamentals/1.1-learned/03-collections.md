# Collections, Mutability, and Complexity

> **Module 01: Python Fundamentals | Topic 03**



## 1. Learning Outcomes

- **Collection Types:** Choose appropriately between lists, tuples, sets, and dictionaries.
- **Comprehensions:** Write readable list, set, and dictionary comprehensions.
- **Mutability & Copying:** Understand reference sharing vs shallow copy vs deepcopy.
- **Complexity Intuition:** Recognize O(1) hash table lookups vs O(n) sequence scans.

## 2. Comparison of Built-in Collections


| Type | Ordered? | Mutable? | Unique Only? | Best Use Case |
| --- | --- | --- | --- | --- |
| list | Yes | Yes | No | Sequences where order & duplicates matter |
| tuple | Yes | No | No | Fixed records, dictionary keys, immutable data |
| set | No | Yes | Yes | Fast membership testing (in), deduplication |
| dict | Yes (3.7+) | Yes | Keys are unique | Key-value lookups, structured entities |



## 3. Key Syntax


### Comprehensions

```python
# List comprehension
evens_squared = [x**2 for x in range(10) if x % 2 == 0]

# Dict comprehension
word_lengths = {w: len(w) for w in ['apple', 'banana', 'fig']}

# Set comprehension (deduplicates automatically)
unique_initials = {name[0] for name in ['Alice', 'Bob', 'Anna']}
```


### Copying & References

Assignment (`b = a`) only copies the reference, not the underlying data. Modifying `b` will modify `a`.

```python
import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()        # Nested lists are still shared!
deep = copy.deepcopy(original)   # Completely independent clone
```


## 4. Common Mistakes & Gotchas

- **O(n) in List vs O(1) in Set:** Checking `item in my_list` scans item by item (O(n)). Checking `item in my_set` is instant O(1) hash lookup.
- **KeyError in Dictionaries:** Accessing `d['missing']` crashes. Use `d.get('missing', default_value)` instead.

## 5. Practice Tasks & Self-Check

- **Task 1:** Create an inventory dictionary where items can be added, updated, and queried for low stock (< 5 units).
- **Q1:** Why cannot a list be used as a dictionary key, but a tuple can?
