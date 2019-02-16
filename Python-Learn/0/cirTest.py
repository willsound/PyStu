s="PYTHON"

for c in s:
    if c=="T":
        continue
    print(c,end="")
print("\n")
for c in s:
    if c=="T":
        break
    print(c,end="")
print("\n")

while s!="":
    for c in s:
        print(c,end="")
    s=s[:-1]
    print("*")
