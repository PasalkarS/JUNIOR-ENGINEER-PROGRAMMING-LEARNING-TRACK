# 20 - Script Entry Point Pattern
# Standard pattern to make a file importable and executable.

def run_checks():
    status = "System Ready"
    print(f"[STATUS]: {status}")

if __name__ == "__main__":
    print("Script started directly.")
    run_checks()
