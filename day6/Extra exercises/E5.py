import re

def is_strong(password):
    return (
        len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"\d", password) and
        re.search(r"[!@#$%^&*]", password)
    )

def exercise5_password_checker():
    try:
        with open("passwords.txt", "r") as f:
            passwords = [line.strip() for line in f if line.strip()]

        strong_passwords = []
        for pwd in passwords:
            if is_strong(pwd):
                strong_passwords.append(pwd)
            else:
                print(f"Weak password skipped: {pwd}")

        with open("strong_passwords.txt", "w") as f:
            for pwd in strong_passwords:
                f.write(pwd + "\n")

        print("Strong passwords saved to strong_passwords.txt")

    except FileNotFoundError:
        print("The passwords.txt file was not found.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    exercise5_password_checker()