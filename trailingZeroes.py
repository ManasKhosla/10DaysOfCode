#So here we have to calculate trailing zeroes of the factorials of the given number
#To do that we should first find out how many (2x5) pairs are there
#As 2 will occur obviously more times than 5 as it is also a factor of many other even numbers,
#We can just count number of occurances of 5 by equation (occ=[n/5]+[n/5^2]+[n/5^3]+...)

from math import floor

num = int(input())

occ, i = 0, 1
flag = True

while flag:
    eq_part = floor(num/5**i)

    #condition to get out of the loop
    if eq_part == 0:
        flag = False
    else:
        occ += eq_part
        i += 1

print(occ)