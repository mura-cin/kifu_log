
import re

with open("test.kif", "r") as f:
    input_kifu = f.read().split("\n")

date = ""
date_pattern = "[0-9]{4}/[0-9]{2}/[0-9]{2}"
black = ""                      # 先手
white = ""                      # 後手

for i, k in enumerate(input_kifu):
    if "----" in k: idx = i
info = input_kifu[:idx]
kifu = input_kifu[idx:]

for x in info:
    if len(date) == 0:
        d = re.findall(date_pattern, x)
        if len(d) != 0: date = d[0]
    if "先手" in x: black = x[3:]
    if "後手" in x: white = x[3:]

kifu_list = []
for x in kifu:
    x = x.strip().split(" ")
    if len(x) == 2:
        kifu_list.append(x[1])



