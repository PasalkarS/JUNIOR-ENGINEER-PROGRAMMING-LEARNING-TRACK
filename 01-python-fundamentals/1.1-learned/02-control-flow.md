02 — Control Flow
1. if
What it is

if is used to execute a block of code when a condition is True.

Important Points
Checks a condition.
Runs the code only when the condition is True.
Uses : after the condition.
The code inside if must be indented.
Basic Syntax
if condition:
    # code
2. elif
What it is

elif means "else if" and is used to check another condition when the previous condition is False.

Important Points
Can have multiple elif statements.
Python checks conditions from top to bottom.
Only the first matching condition is executed.
elif must come after if.
Basic Syntax
if condition:
    # code
elif condition:
    # code
3. else
What it is

else is used to execute code when all previous conditions are False.

Important Points
else does not have a condition.
It must come after if or elif.
Only one else can be used in a condition block.
else is optional.
Basic Syntax
if condition:
    # code
else:
    # code
4. Nested Conditions
What it is

A nested condition is an if statement placed inside another if statement.

Important Points
Used when one condition depends on another.
Nested blocks must be properly indented.
Too many nested conditions can make code difficult to read.
if, elif, and else can be nested.
Basic Syntax
if condition:
    if condition:
        # code
5. for Loop
What it is

A for loop is used to repeat code for each item in a sequence or collection.

Important Points
Commonly used with lists, strings, tuples, and range().
Runs once for each item.
The loop variable stores the current item.
The loop stops after all items have been processed.
Basic Syntax
for item in collection:
    # code
6. while Loop
What it is

A while loop repeats code as long as a condition is True.

Important Points
Checks the condition before each iteration.
The loop stops when the condition becomes False.
Make sure the condition can eventually become False.
Useful when the number of repetitions is not known beforehand.
Basic Syntax
while condition:
    # code
7. range()
What it is

range() generates a sequence of numbers, commonly used with for loops.

Important Points
range(stop) starts from 0.
range(start, stop) starts from start.
The stop value is not included.
range(start, stop, step) allows you to specify the step.
Basic Syntax
range(stop)
range(start, stop)
range(start, stop, step)
8. break
What it is

break is used to immediately stop a loop.

Important Points
Stops the current loop.
Execution continues with the code after the loop.
Can be used in both for and while loops.
Useful when the required result is found before the loop finishes.
Basic Syntax
for item in collection:
    if condition:
        break
9. continue
What it is

continue skips the current iteration and moves to the next iteration of the loop.

Important Points
Does not stop the entire loop.
Only skips the current iteration.
Can be used with for and while loops.
Useful when certain values should be skipped.
Basic Syntax
for item in collection:
    if condition:
        continue
10. Conditional Expressions
What it is

A conditional expression is a short way to write a simple if-else condition in one line.

Important Points
Also called the ternary operator.
Used for simple conditions.
Makes short assignments more compact.
Avoid using it for complex conditions.
Basic Syntax
value = value_if_true if condition else value_if_false
11. Nested Loops
What it is

A nested loop is a loop placed inside another loop.

Important Points
The inner loop runs completely for each iteration of the outer loop.
Can be used with both for and while loops.
Commonly used for patterns and working with tables or grids.
Proper indentation is important.
Basic Syntax
for i in range(3):
    for j in range(3):
        # code
