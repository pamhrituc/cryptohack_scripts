import sys

encoded = sys.argv[1]
flag = str(bytes.fromhex(encoded))[2:-1]
result = "{\"decoded\": \"" + flag + "\"}"
print(result)
