import pandas as pd


def check_required_columns(df, required_columns):
    errors = []

    for column in required_columns:
        if column not in df.columns:
            errors.append(
                "Missing required column: " + column
            )

    return errors


def check_missing_values(df):
    errors = []

    for column in df.columns:
        missing_count = df[column].isna().sum()

        if missing_count > 0:
            errors.append(
                column
                + " has "
                + str(missing_count)
                + " missing values"
            )

    return errors


def check_duplicates(df, column):
    errors = []

    duplicate_count = df[column].duplicated().sum()

    if duplicate_count > 0:
        errors.append(
            str(duplicate_count)
            + " duplicate values found in "
            + column
        )

    return errors


def check_positive_values(df, column):
    errors = []

    invalid_count = (df[column] <= 0).sum()

    if invalid_count > 0:
        errors.append(
            str(invalid_count)
            + " invalid values found in "
            + column
        )

    return errors


data = {
    "Customer_ID": [101, 102, 103, 103],
    "Name": ["Rahul", "Priya", None, "Amit"],
    "Amount": [5000, -1000, 3000, 4000]
}

df = pd.DataFrame(data)

errors = []

errors.extend(
    check_required_columns(
        df,
        ["Customer_ID", "Name", "Amount"]
    )
)

errors.extend(check_missing_values(df))

errors.extend(
    check_duplicates(df, "Customer_ID")
)

errors.extend(
    check_positive_values(df, "Amount")
)

print("----- DATA QUALITY REPORT -----")

if len(errors) == 0:
    print("No data quality problems found.")
else:
    for error in errors:
        print("-", error)
