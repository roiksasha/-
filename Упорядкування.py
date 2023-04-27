a = int(input("Введіть перше число"))
b = int(input("Введіть друге число"))

c = int(input("Введіть третє число"))
while not (a<=b<=c):
    if a>b:
        a, b=b,a
    if b>c:
        b,c=c,b

print(a, b, c)
