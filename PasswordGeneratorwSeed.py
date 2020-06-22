# for comments on what the code does go to PasswordGenerator.py
# this one just adds the seed
import random


def random_string(string_length=8, seedk=1):
    # adding the seed
    # a seed means the passwords will always be the same but diffrent depending on their length
    random.seed(seedk)
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z',
               '1', '2', '3', '4', '5', '6', '7', '8', '9',
               '!', '"', '#', '$', '%', '&', '/', '(', ')', '=', '?', '*', ',', '.', '-', ';', ':', '_']
    return ''.join(random.choice(letters) for i in range(string_length))


f = open("seed.txt", "x")
i = 0
length = int(input("string len>"))
while i < 999999:
    print(f"{random_string(length, i)} + {i}")
    f.write(f"{random_string(length, i)} + {i}\n")
    i += 1
