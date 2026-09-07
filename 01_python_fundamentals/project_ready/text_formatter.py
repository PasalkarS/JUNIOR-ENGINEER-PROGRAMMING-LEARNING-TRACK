"""
text_formatter.py - File-based text formatting and analysis utility.

Reads text files, computes textual metrics (line, word, and character counts),
and transforms text into Title Case, Uppercase, Lowercase, or Cleaned formats.
Gracefully handles missing files, empty files, and permission errors.
"""

import sys
import os
import re
import argparse
from typing import Dict, Any


def compute_statistics(text: str) -> Dict[str, Any]:
    """Compute line count, word count, and character metrics for text."""
    lines = text.splitlines()
    words = re.findall(r"\b\w+\b", text)
    non_space_chars = len(re.sub(r"\s", "", text))

    avg_word_length = sum(len(w) for w in words) / len(words) if words else 0.0

    return {
        "lines": len(lines),
        "words": len(words),
        "characters_total": len(text),
        "characters_non_space": non_space_chars,
        "avg_word_length": avg_word_length,
    }


def reformat_text(text: str, mode: str) -> str:
    """
    Apply formatting transformation to text.
    
    Modes:
        - title: Convert words to Title Case
        - upper: Convert entire text to UPPERCASE
        - lower: Convert entire text to lowercase
        - sentence: Capitalize first word after sentence terminators (.!?)
        - clean: Trim trailing spaces and collapse excess blank lines
    """
    mode = mode.lower().strip()
    if mode == "title":
        return text.title()
    elif mode == "upper":
        return text.upper()
    elif mode == "lower":
        return text.lower()
    elif mode == "sentence":
        # Capitalize after sentence boundaries
        return re.sub(r"(^\s*[a-z]|[\.\?\!]\s*([a-z]))", lambda m: m.group().upper(), text)
    elif mode == "clean":
        lines = [line.rstrip() for line in text.splitlines()]
        # Remove consecutive empty lines
        cleaned_lines = []
        for line in lines:
            if line == "" and cleaned_lines and cleaned_lines[-1] == "":
                continue
            cleaned_lines.append(line)
        return "\n".join(cleaned_lines)
    else:
        raise ValueError(f"Unknown format mode '{mode}'. Supported: title, upper, lower, sentence, clean.")


def read_file_safely(file_path: str) -> str:
    """
    Read content from a path with extensive validation.
    
    Raises:
        FileNotFoundError: If path does not exist.
        IsADirectoryError: If path is a folder.
        ValueError: If file is empty or non-text.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: '{file_path}'. Please check the path and try again.")

    if os.path.isdir(file_path):
        raise IsADirectoryError(f"Target path '{file_path}' is a directory, not a text file.")

    if os.path.getsize(file_path) == 0:
        raise ValueError(f"File '{file_path}' is completely empty (0 bytes). Nothing to format.")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        raise ValueError(f"File '{file_path}' contains binary or non-UTF-8 characters. Only text files are supported.")

    if not content.strip():
        raise ValueError(f"File '{file_path}' contains only whitespace. Cannot perform meaningful formatting.")

    return content


def interactive_menu() -> None:
    print("=" * 55)
    print("           CLI Text Formatter & Analyzer")
    print("=" * 55)

    path = input("\nEnter path to text file: ").strip()
    try:
        content = read_file_safely(path)
    except Exception as e:
        print(f"\n[Error] {e}")
        return

    stats = compute_statistics(content)
    print("\n--- Document Statistics ---")
    print(f"  Lines:            {stats['lines']}")
    print(f"  Words:            {stats['words']}")
    print(f"  Total Characters: {stats['characters_total']}")
    print(f"  Non-space Chars:  {stats['characters_non_space']}")
    print(f"  Avg Word Length:  {stats['avg_word_length']:.2f} chars")

    print("\nAvailable transformations:")
    print("  [1] Title Case")
    print("  [2] UPPERCASE")
    print("  [3] Lowercase")
    print("  [4] Sentence Case")
    print("  [5] Clean Whitespace")
    print("  [q] Skip Formatting")

    choice = input("\nSelect transformation [1-5, q]: ").strip().lower()
    mode_map = {
        "1": "title",
        "2": "upper",
        "3": "lower",
        "4": "sentence",
        "5": "clean",
    }

    if choice in mode_map:
        mode = mode_map[choice]
        formatted = reformat_text(content, mode)

        print("\n--- Formatted Preview (First 5 lines) ---")
        preview_lines = formatted.splitlines()[:5]
        for line in preview_lines:
            print(f"  {line}")
        if len(formatted.splitlines()) > 5:
            print("  ...")

        save = input("\nSave formatted output to a file? [y/N]: ").strip().lower()
        if save in ("y", "yes"):
            out_path = input("Enter destination file path: ").strip()
            try:
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(formatted)
                print(f"[Success] Formatted text written to '{out_path}'.")
            except Exception as e:
                print(f"[Error saving file] {e}")
    else:
        print("Formatting skipped.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze and reformat text files.")
    parser.add_argument("--file", "-f", help="Path to input text file")
    parser.add_argument("--mode", "-m", choices=["title", "upper", "lower", "sentence", "clean"], help="Formatting mode")
    parser.add_argument("--output", "-o", help="Optional output path to save formatted text")
    parser.add_argument("--stats-only", action="store_true", help="Print document stats and exit")

    args = parser.parse_args()

    if args.file:
        try:
            content = read_file_safely(args.file)
            stats = compute_statistics(content)

            print(f"File: {args.file}")
            print(f"Lines: {stats['lines']} | Words: {stats['words']} | Characters: {stats['characters_total']}")

            if args.stats_only:
                return

            mode = args.mode or "title"
            formatted = reformat_text(content, mode)

            if args.output:
                with open(args.output, "w", encoding="utf-8") as f:
                    f.write(formatted)
                print(f"Formatted output ({mode}) saved to: {args.output}")
            else:
                print(f"\n--- Output ({mode}) ---")
                print(formatted)

        except Exception as e:
            print(f"[Error] {e}", file=sys.stderr)
            sys.exit(1)
    else:
        interactive_menu()


if __name__ == "__main__":
    main()
