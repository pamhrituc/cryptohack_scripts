from pwn import xor
import sys

string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
string_bytes = "\x0e\x0b!?&\x04\x1eH\x0b&!\x7f'4.\x17]\x0e\x07\n<[\x10>%&!\x7f'4.\x17]\x0e\x07~&4Q\x15\x01\x04"

#obtained using fromhex.py from ../encoding_challenge

print(xor(string_bytes, "crypto{"))

#xor string_bytes w/ what we know (flag format is crypto{FLAG})
#bytes are obtained, looking something like myXORkey [a bunch of nonsense]
#use myXORkey to obtain FLAG

print(xor(string_bytes, "myXORkey"))
