a = ["3", "30", "34", "5", "9"]

for i in a:
    print(i*3)
print(a.sort())

a.sort(reverse=True)

# a.sort(key=lambda x: int(list(x)[0]), reverse=True)
a.sort(key=lambda x: x*3, reverse=True)

print(a)