# marks = [21, 34, 56, 78, 89, 65]
# index = 0
# for i in marks:
#     print(i)
#     if index == 3:
#         print("Awesome")
#     index += 1

# marks = [21, 34, 56, 78, 89, 65]

# for index, value in enumerate(marks):   # Here the index will start from 0
#     print(value)
#     if index == 3:
#         print("Awesome Ranjit")
#
# print()

# for index, value in enumerate(marks, start=1):  # we can give start also now the index will start from 1
#     print(f"Index: {index} {value}")

# import sys
#
# a = [12, 32, 45, 56, 876, 341, 4, 345, 678]
# max_val = sys.maxsize
# min_val = -sys.maxsize-1
# print(f"Python max int value {max_val}")
# print(f"Python min int value {min_val}\n")
#
# c = 0
# for i in a:
#     if i > c:
#         c = i
# print(f"Max value: {c}")
#
# for j in a:
#     if j < max_val:
#         max_val = j
# print(f"Min value: {max_val}")

# import random
#
# def guess_word(word_list):
#     # Select a random word from the list
#     guessed_word = random.choice(word_list)
#     return guessed_word
#
# # Example usage
# word_list = ["apple", "banana", "cherry", "date", "elderberry"]
# guessed_word = guess_word(word_list)
#
# print("The guessed word is:", guessed_word)

import random


def guess_character(characters):
    # Select a random character from the list
    guessed_character = random.choice(characters)
    return guessed_character


# Example usage
character_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c = guess_character(character_set)

print(c)
