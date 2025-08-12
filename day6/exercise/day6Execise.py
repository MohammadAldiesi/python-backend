# exercise_day6.py
import os

class Exception_1(Exception):
    pass


try:
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "input.txt")

    with open(file_path, "r") as f:
        text = f.read()

    words = text.split()
    freq = {}

    for word in words:
        word = word.strip(".,!?()[]{}\"'").lower()
        freq[word] = freq.get(word, 0) + 1

    for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")

except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print("An unexpected error occurred:", e)
