def make_upper(text):
    return text.upper()


def make_lower(text):
    return text.lower()


def format_name(first_name, last_name):
    return first_name + " " + last_name


def repeat_text(text, times=2):
    return text * times


def join_words(*words):
    return " ".join(words)


def show_details(**details):
    for key, value in details.items():
        print(key, ":", value)


print(make_upper("hello"))
print(make_lower("HELLO"))
print(format_name("Sam", "Patil"))
print(repeat_text("Hi", 3))
print(join_words("Python", "is", "easy"))

show_details(name="Sam", age=24, role="QA")
