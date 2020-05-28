num = int(input())

upper = num
middle = int((num+1)/2)
lower = 1
ws = int(upper-middle-1)

while num>0:
    if (num == upper):
        print("*"+ " "*ws + "*" + "*"*ws + "*")
    if (upper > num) and (num > middle):
        print("*"+ " "*ws + "*")
    if (num == middle):
        print("*"*upper)
    if (middle > num) and (num > lower):
        print(" "+ " "*ws + "*" + " "*ws + "*")
    if (num == lower):
        print("*"+ "*"*ws + "*" + " "*ws + "*")
    num -= 1
