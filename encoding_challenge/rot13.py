import codecs
import sys

encoded = sys.argv[1]
flag = codecs.decode(encoded, "rot_13")
result = "{\"decoded\": \"" + flag + "\"}"
print(result)
