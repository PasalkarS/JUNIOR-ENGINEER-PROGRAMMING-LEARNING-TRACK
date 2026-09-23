# Pattern Generator
# Demonstrates nested loops to build visual triangle patterns.

size = 5

print("Right-angled Triangle:")
for i in range(1, size + 1):
    print("*" * i)

print("\nInverted Triangle:")
for i in range(size, 0, -1):
    print("*" * i)

print("\nNumbered Pyramid:")
for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
