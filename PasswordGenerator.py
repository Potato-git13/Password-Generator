import random


def random_string(string_length=8):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z',
               '1', '2', '3', '4', '5', '6', '7', '8', '9',
               '!', '"', '#', '$', '%', '&', '/', '(', ')', '=', '?', '*', ',', '.', '-', ';', ':', '_']
    return ''.join(random.choice(letters) for i in range(string_length))


rand_num = random.randint(0, 99999)
f = open(f"seed {rand_num}.txt", "x")
i = 0
length = int(input(">"))
while i < 999999:
    print(f"{i}")
    f.write(f"{random_string(length)} + {i}\n")
    i += 1
