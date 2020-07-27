from PIL import Image, ImageChops
import numpy as np

lemur = Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png", mode='r').convert("1")
flag = Image.open("flag_7ae18c704272532658c10b5faad06d74.png", mode='r').convert("1")

result = ImageChops.logical_xor(lemur, flag)
result.save('result.png')

