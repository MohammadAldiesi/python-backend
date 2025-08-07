class Exercises:
    class Sets:
        def remove_duplicates(self, x):
            unique_values = list(set(x))
            print("Unique Values:", unique_values)

        def union(self, x):
            A, B = x
            print("Union:", A | B)

        def intersection(self, x):
            A, B = x
            print("Intersection:", A & B)

        def difference(self, x):
            A, B = x
            print("Difference (A - B):", A - B)

        def symmetric_difference(self, x):
            A, B = x
            print("Symmetric Difference:", A ^ B)

        def unique_words(self, x):
            words = set(x.split())
            print("Unique Words:", words)
            print("Number of Unique Words:", len(words))

    class Dictionaries:
        def create_student(self, x):
            student = x
            print("Student Dictionary:", student)

        def word_frequency(self, x):
            word_freq = {}
            for word in x.split():
                word_freq[word] = word_freq.get(word, 0) + 1
            print("Word Frequency:", word_freq)

        def squares_dict(self, x):
            squares = {i: i ** 2 for i in range(1, x + 1)}
            print("Squares Dictionary:", squares)

    class Walrus:
        def input_validation(self, x=None):
            while (n := int(input("Enter a number greater than 10: "))) <= 10:
                pass
            print("Accepted number:", n)

    class Merge:
        def resolve_conflict(self, x):
            dict1, dict2 = x
            merged = {}
            for k in dict1.keys() | dict2.keys():
                if k in dict1 and k in dict2:
                    merged[f"{k}_resolved"] = dict1[k] + dict2[k]
                else:
                    merged[k] = dict1.get(k, dict2.get(k))
            print("Merged Dictionary:", merged)

sets = Exercises.Sets()
dictionaries = Exercises.Dictionaries()
walrus = Exercises.Walrus()
merge = Exercises.Merge()

# Usage:
print("-------------Exercise 1: Sets-------------")
sets.remove_duplicates([3, 5, 7, 5, 9, 3])
sets.union(({1, 2, 3, 4}, {3, 4, 5, 6}))
sets.intersection(({1, 2, 3, 4}, {3, 4, 5, 6}))
sets.difference(({1, 2, 3, 4}, {3, 4, 5, 6}))
sets.symmetric_difference(({1, 2, 3, 4}, {3, 4, 5, 6}))
sets.unique_words("hello world hello python python world hello")

print("-------------Exercise 2: Dictionaries-------------")
dictionaries.create_student({"name": "John", "age": 21, "courses": ["Math", "CS"]})
dictionaries.word_frequency("hello world hello")
dictionaries.squares_dict(5)

print("-------------Exercise 3: Walrus Operator-------------")
walrus.input_validation()

print("-------------Exercise 4: Merge Dictionaries with Conflict Resolution-------------")
merge.resolve_conflict(({"a": 1, "b": 2}, {"b": 3, "c": 4}))
