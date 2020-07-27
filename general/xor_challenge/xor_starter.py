import ast
import sys

string = sys.argv[1]
number = int(sys.argv[2])
result = ""
for character in string:
    character_ascii = ord(character)
    result += chr(character_ascii ^ number)

print(result)
