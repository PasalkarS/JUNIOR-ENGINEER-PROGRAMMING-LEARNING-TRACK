class ValidationError(Exception):
    pass


def validate_age(age):
    if age < 0:
        raise ValidationError("Age cannot be negative.")

    if age > 120:
        raise ValidationError("Age is not valid.")

    return True


try:
    age = int(input("Enter your age: "))
    validate_age(age)

except ValueError:
    print("Please enter a number.")

except ValidationError as error:
    print("Validation error:", error)

else:
    print("Age is valid.")

finally:
    print("Validation completed.")
