import base64
import sys

encoded = sys.argv[1]
flag = str(base64.b64decode(encoded))
result = "{\"decoded\": \"" + flag[2:-1] + "\"}"
print (result)
