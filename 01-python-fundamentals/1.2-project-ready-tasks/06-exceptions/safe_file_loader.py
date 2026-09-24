from pathlib import Path


def read_file(filename):
    try:
        file = Path(filename)
        text = file.read_text(encoding="utf-8")

    except FileNotFoundError:
        print("File not found.")

    except UnicodeDecodeError:
        print("Invalid file encoding.")

    except Exception as error:
        print("Something went wrong:", error)

    else:
        print("File read successfully.")
        print(text)

    finally:
        print("File operation completed.")


read_file("example.txt")
