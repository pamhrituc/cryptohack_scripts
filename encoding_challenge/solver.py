from Crypto.Util.number import long_to_bytes
from pwn import * # pip install pwntools
import ast
import base64
import codecs
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()

while received["type"] != "flag":
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    encoded = received["encoded"]
    print(encoded)

    if received["type"] == "base64":
        flag = str(base64.b64decode(encoded))[2:-1]
    
    if received["type"] == "bigint":
        flag = str(long_to_bytes(int(encoded, 0)))[2:-1]
    
    if received["type"] == "hex":
        flag = str(bytearray.fromhex(encoded))[12:-2]
    
    if received["type"] == "rot13":
        flag = codecs.decode(encoded, "rot_13")
    
    if received["type"] == "utf-8":
        flag = ""
        for i in encoded:
            flag += chr(i)

    to_send = {
            "decoded": flag
            }
    
    print("Sending flag: " + flag)

    json_send(to_send)

    received = json_recv()
