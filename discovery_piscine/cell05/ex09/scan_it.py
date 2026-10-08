#!/usr/bin/env python3
import sys
import re

def main():
    # Check if exactly 2 arguments are provided (excluding the script name itself)
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    text = sys.argv[2]

    # Find all occurrences of the keyword using the re module
    # re.escape ensures special regex characters are treated as literal text
    matches = re.findall(re.escape(keyword), text)

    # Print the count if found, otherwise print "none"
    if len(matches) == 0:
        print("none")
    else:
        print(len(matches))

if __name__ == "__main__":
    main()
