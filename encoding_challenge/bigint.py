from Crypto.Util.number import long_to_bytes
import base64
import sys

encoded = sys.argv[1]
flag = long_to_bytes(int(encoded, 0))
result = "{\"decoded\": \"" + str(flag)[2:-1] + "\"}"
print (result)
