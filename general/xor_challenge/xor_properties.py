import sys
"""
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

To get the FLAG we just need to XOR the 4th relation w/ the 1rst and 3rd.
"""

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAGKEY123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

KEY123 = hex(int(KEY1, 16) ^ int(KEY23, 16))
FLAG_HEX = str(hex(int(KEY123, 16) ^ int(FLAGKEY123, 16)))[2:]

print(str(bytes.fromhex(FLAG_HEX))[2:-1])
