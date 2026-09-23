# String Formatting Utilities
# Pure functions for text normalization and masking.

def mask_card_number(card_number: str) -> str:
    """Mask credit card number leaving only the last 4 digits visible."""
    clean = card_number.replace("-", "").replace(" ", "")
    if len(clean) < 4:
        return clean
    return "*" * (len(clean) - 4) + clean[-4:]

def slugify(text: str) -> str:
    """Convert title into a clean URL-friendly slug."""
    clean = text.strip().lower()
    return "-".join(clean.split())

def truncate(text: str, max_length: int = 30) -> str:
    """Truncate string cleanly with ellipsis if length exceeds limit."""
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."

if __name__ == "__main__":
    print("Masked Card:", mask_card_number("1234-5678-9012-3456"))
    print("Slugified:  ", slugify("Hello Junior Engineer Track!"))
    print("Truncated:  ", truncate("This is an exceptionally long piece of text", 20))
