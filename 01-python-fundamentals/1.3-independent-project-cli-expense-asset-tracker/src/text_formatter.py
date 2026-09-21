"""
Simple Text File Formatter & Counter
Beginner-friendly script to read a file, count lines/words, and reformat text.
"""

def count_stats(text):
    lines = len(text.splitlines())
    words = len(text.split())
    chars = len(text)
    return lines, words, chars

def format_text(text, style):
    if style == "1":
        return text.title()
    elif style == "2":
        return text.upper()
    elif style == "3":
        return text.lower()
    return text

def main():
    print("--- Simple Text Formatter ---")
    file_path = input("Enter path to a text file: ").strip()

    # Handling invalid file input
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find the file '{file_path}'.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Edge case: empty file
    if not content.strip():
        print("Notice: The file is empty!")
        return

    # Count stats
    lines, words, chars = count_stats(content)
    print(f"\nStats for '{file_path}':")
    print(f"  - Lines: {lines}")
    print(f"  - Words: {words}")
    print(f"  - Characters: {chars}")

    print("\nHow would you like to reformat it?")
    print("1. Title Case")
    print("2. UPPERCASE")
    print("3. lowercase")
    print("4. Keep as-is")

    choice = input("Select an option (1-4): ").strip()
    if choice in ("1", "2", "3"):
        result = format_text(content, choice)
        print("\n--- Formatted Preview ---")
        print(result[:300] + ("\n..." if len(result) > 300 else ""))

        save_choice = input("\nSave formatted text to a new file? (y/n): ").strip().lower()
        if save_choice == "y":
            out_file = input("Enter new file name: ").strip()
            try:
                with open(out_file, "w", encoding="utf-8") as f:
                    f.write(result)
                print(f"Saved successfully to '{out_file}'.")
            except Exception as e:
                print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
