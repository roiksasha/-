list_of_nums = []
print("ведіть послідовність чисел");

while True:
    num = int(input())
    if (num ==0):
        break
    else:
        list_of_nums.append(num)
print("Середнє арифметичне послідовність : ", sum(list_of_nums)/len(list_of_nums))
