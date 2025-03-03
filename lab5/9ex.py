import re
with open("row9ex.txt") as f:
    data=f.read()
print(re.findall(r"[A-Z][a-z]*", data))