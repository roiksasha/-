max_num = 0
count = 0
while True:
    num = int(input("Введіть число (0 - кінець послідовності):"))
    if num == 0:
        break
    if num > max_num:
        max_num=num
        count = 1
    elif num == max_num:
        count +=1
print(count)
