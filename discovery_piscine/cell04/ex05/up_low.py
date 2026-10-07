#!/usr/bin/env python3
word = input()
result = ""
for char in word:
    if char.isupper():
        result = result + char.lower()
    elif char.islower():
        result = result + char.upper()
    else:
        result = result + char
print(result)