import sys

encoded = sys.argv[1]
flag = str(bytearray.fromhex(encoded))
result = "{\"decoded\": \"" + flag[12:-2] + "\"}"
print(result)
