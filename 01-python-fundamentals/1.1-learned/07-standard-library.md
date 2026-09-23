# The Python Standard Library

> **Module 01: Python Fundamentals | Topic 07**



## 1. Learning Outcomes

- **Built-in Superpowers:** Leverage batteries-included modules before reaching for third-party packages.
- **Data Structures:** Use Counter and defaultdict from collections for clean data aggregations.
- **Dates and Math:** Handle ISO timestamps with datetime and stats with statistics/math.
- **File & Serialization:** Serialize data with json and work with OS paths via pathlib.

## 2. Essential Standard Modules Quick Reference


| Module | Primary Use Case | Key Functions / Classes |
| --- | --- | --- |
| pathlib | Modern cross-platform path handling | Path.cwd(), Path.exists(), Path.glob() |
| datetime | Date, time, and interval arithmetic | datetime.now(), strftime(), timedelta |
| json | Serialize/deserialize JSON text | json.loads(), json.dumps(), json.dump() |
| collections | Specialized data containers | Counter(), defaultdict(list), deque |
| statistics | Quick mathematical summary | mean(), median(), mode(), stdev() |
| random | Random selection and shuffling | random.choice(), random.randint(), random.shuffle() |



## 3. Code Examples

```python
from collections import Counter, defaultdict
import json
from datetime import datetime, timedelta

# 1. Counter
words = ['apple', 'orange', 'apple', 'banana', 'apple']
counts = Counter(words)  # Counter({'apple': 3, 'orange': 1, 'banana': 1})

# 2. Datetime arithmetic
today = datetime.now()
next_week = today + timedelta(days=7)

# 3. JSON formatting
data = {'service': 'auth', 'uptime': 99.9}
json_str = json.dumps(data, indent=2)
```


## 4. Practice Tasks & Self-Check

- **Task 1:** Build a script that reads a JSON configuration file, overrides specific keys, and computes days until an expiry date.
- **Q1:** Why is `pathlib.Path` preferred over raw string operations or `os.path.join`?
