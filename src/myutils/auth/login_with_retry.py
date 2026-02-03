import re

# Simple in-memory "database"
users_db = {
    "khush": "khush123",
    "swaraj": "swaraj123",
    "joy": "joy789",
}


def is_valid_password(password: str) -> bool:
    """
    Check if password meets requirements:
    - Minimum 6 characters
    - Must contain at least one letter and one number
    """
    if len(password) < 6:
        return False
    if not re.search(r"[A-Za-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True


def register_user():
    """
    Registers a new user with username and valid password
    """
    username = input("Enter a username to register: ").strip()
    if username in users_db:
        print("Username already exists. Please try a different username.")
        return

    password = input("Enter password: ").strip()
    if not is_valid_password(password):
        print(
            "Password must be at least 6 characters long and contain both letters and numbers."
        )
        return

    users_db[username] = password
    print(f"User '{username}' registered successfully!")


def login_simulator(max_attempts: int = 3):
    """
    Simulates login for existing users with retry logic.

    Args:
        max_attempts (int): Maximum number of allowed login attempts.
    """
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if username in users_db:
            if users_db[username] == password:
                print(f"Login successful! Welcome, {username}.")
                return
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")

        attempts += 1
        remaining = max_attempts - attempts
        if remaining:
            print(f"Attempts remaining: {remaining}\n")

    print("Too many failed login attempts. Please try again later.")


# Demo flow
while True:
    choice = input(
        "\nChoose an option:\n" "1. Register\n" "2. Login\n" "3. Exit\n" "Enter: "
    ).strip()

    if choice == "1":
        register_user()
    elif choice == "2":
        login_simulator()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid option. Try again.")
