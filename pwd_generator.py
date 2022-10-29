#generate random password

import imp


import random

lower_case = "abcdefghijkmnlopqrstuvwxyz"
upper_case = "ABCDEFGHIJKMNLOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@!#$%&*/\?"

use_for = lower_case + upper_case + number + symbols
length_for_pass = input("Enter length of password:")

password = "".join(random.sample(use_for,length_for_pass))

print(password)