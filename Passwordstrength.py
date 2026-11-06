"""Password Strength Analyzer - Week 1 project.

Educational command-line tool. It evaluates basic password characteristics.
Use sample passwords only; do not enter passwords used for real accounts.
"""
import re


def analyze_password(password: str) -> tuple[str, int, list[str]]:
    checks = [
        (len(password) >= 8, "Use at least 8 characters."),
        (bool(re.search(r"[A-Z]", password)), "Add an uppercase letter (A-Z)."),
        (bool(re.search(r"[a-z]", password)), "Add a lowercase letter (a-z)."),
        (bool(re.search(r"[0-9]", password)), "Add a number (0-9)."),
        (bool(re.search(r"[^A-Za-z0-9]", password)), "Add a special character (for example, ! or #)."),
    ]

    score = sum(passed for passed, _ in checks)
    levels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    suggestions = [message for passed, message in checks if not passed]
    return levels[score], score, suggestions


def main() -> None:
    print("=== Password Strength Analyzer ===")
    print("Educational demo: enter a sample password, not a real account password.")
    while True:
        password = input("\nEnter a password (or type 'exit' to quit): ")
        if password.lower() == "exit":
            print("Goodbye.")
            break
        if not password:
            print("Please enter a sample password.")
            continue

        strength, score, suggestions = analyze_password(password)
        print(f"\nPassword strength: {strength} ({score}/5 checks passed)")
        if suggestions:
            print("Suggestions:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
        else:
            print("All five basic checks passed.")
        print("Note: This simple score does not guarantee password security.")


if __name__ == "__main__":
    main()
