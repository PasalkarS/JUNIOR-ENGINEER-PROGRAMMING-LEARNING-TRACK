# 04 - Reading User Input

user_name = input("Enter your name: ") if __name__ == "__main__" else "Dev"
age_str = "24"
age = int(age_str)

print(f"Welcome, {user_name}! In 5 years you will be {age + 5}.")
