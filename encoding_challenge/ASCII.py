import ast
import sys

flag = ""
encoded = ast.literal_eval(sys.argv[1])
print(encoded)
for i in encoded:
    flag += chr(i)

result = "{\"decoded\": \"" + flag + "\"}"
print(result)
