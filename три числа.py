a = int(input("Введіть перше число"))
b = int(input("Введіть друге число"))

c = int(input("Введіть третє число"))

if a>=b and a>=c:
    m = a
elif b>=c:
    m = b
else:
    m=c
print("Найбільше число",m)
