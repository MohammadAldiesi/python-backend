class InvalidLengthError(Exception):
    pass

class InvalidCharacterError(Exception):
    pass

def exercise3_user_registration():
    try:
        username = input("Enter username: ")

        if len(username) < 5 or len(username) > 15:
            raise InvalidLengthError("Username must be between 5 and 15 characters.")

        if not username.isalnum():
            raise InvalidCharacterError("Username must contain only letters and numbers.")

        with open("users.txt", "a") as f:
            f.write(username + "\n")
        print("User registered successfully.")

    except InvalidLengthError as e:
        print("Length Error:", e)
    except InvalidCharacterError as e:
        print("Character Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("Registration attempt completed.")
if __name__ == "__main__":
    exercise3_user_registration()