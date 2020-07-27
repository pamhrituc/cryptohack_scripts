import ast
import sys

flag = ""
encoded = ast.literal_eval(sys.argv[1])
for i in encoded:
    flag += chr(i)

result = "{\"decoded\": \"" + flag + "\"}"
print(result)
