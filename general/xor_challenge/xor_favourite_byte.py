from pwn import xor
import sys

hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
string = bytes.fromhex(hex_string)

for i in range(256):
    xored = str(xor(string, i))[2:-1]
    if str(xored)[:6] == "crypto":
        print(xored)
        break
