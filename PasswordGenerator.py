import random
import time

def random_string(string_length, must_start):
    # define the password length
    len_start = len(must_start)
    string_length = string_length - len_start

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z',
               '1', '2', '3', '4', '5', '6', '7', '8', '9',
               '!', '"', '#', '$', '%', '&', '/', '(', ')', '=', '?', '*', ',', '.', '-', ';', ':', '_']
    # returning the result
    wout_start = ''.join(random.choice(letters) for i in range(string_length))
    out = must_start + wout_start
    return out

# collecting the input
length = int(input("length >"))
must_start_inp = input("must start with >")
pass_amount = int(input("amount of passwords >"))
# creating the filename
time = time.strftime("%Y-%m-%d-%H:%M:%S")
filename = f"passwords-{time}"

with open(filename, "w") as f:
    counter = 0

    while counter < pass_amount:
        print(f"{counter}")
        # writing to the file
        f.write(f"{random_string(length, must_start_inp)}\n")
        counter += 1
