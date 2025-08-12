def exercise1_palindrome():
    try:
        with open("input_words.txt", "r") as f:
            words = [line.strip() for line in f if line.strip()]

        palindromes = [word.upper() for word in words if word.lower() == word[::-1].lower()]

        with open("palindromes.txt", "w") as f:
            for p in palindromes:
                f.write(p + "\n")

        print("Palindromes saved to palindromes.txt")

    except FileNotFoundError:
        print("The input_words.txt file was not found.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    exercise1_palindrome()
