#!/usr/bin/env python3
import sys

number = sys.argv[1:]

if len(number) < 2:
   print("none")
else:
   print(list(range(int(number[0]), int(number[1]) + 1)))