data = [5, 3, 8, 3, 5, 2, 9, 8, 2]
unique_data = list(set(data))
print("Unique values:", unique_data)

text = "this is a test this is only a test"
words = text.split()
word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("Word frequency:", word_freq)
