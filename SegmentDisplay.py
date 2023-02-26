#!/usr/bin/python3
# Script Name: SegmentDisplay.py
# Description: Simple imitation of segment display :-)
#              Tested on Linux, RHEL 8.5
# Usage: SegmentDisplay.py
# Author: CheerfulAnt@outlook.com
# Version: 1.0
# Date: 5 March 2022 - 21:36 (UTC+02:00)

digits = {
    0: ['### ', '# # ', '# # ', '# # ', '### '],
    1: ['  # ', '  # ', '  # ', '  # ', '  # '],
    2: ['### ', '  # ', '### ', '#   ', '### '],
    3: ['### ', '  # ', '### ', '  # ', '### '],
    4: ['# # ', '# # ', '### ', '  # ', '  # '],
    5: ['### ', '#   ', '### ', '  # ', '### '],
    6: ['### ', '#   ', '### ', '# # ', '### '],
    7: ['### ', '  # ', '  # ', '  # ', '  # '],
    8: ['### ', '# # ', '### ', '# # ', '### '],
    9: ['### ', '# # ', '### ', '  # ', '### ']}

user_digits = input("Enter digits: ")
user_char = int(input("Enter char code for segment display (if enter - default 35 - #): ") or 35)

user_digits_list = list(user_digits)

for i in range(5):
    for digit in user_digits_list:
        for elements in digits[int(digit)][i]:
                print(elements.replace("#", chr(user_char)), end="")
    print()
