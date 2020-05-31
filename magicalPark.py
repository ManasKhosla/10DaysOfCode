def traverse(cmap,k,s):
    c = s
    flag = True
    for i in cmap:
        for j in i:
            if j == ".":
                c -= 2
            elif j == "*":
                c += 5
            elif j == "#":
                break
            c -= 1
        print(c)
        if c<k:
            flag = False
            break
    return c,flag


[N,M,K,S] = list(map(int, input().rstrip().split()))


cmap = []
for _ in range(N):
    row = list(map(str, input().rstrip().split()))
    cmap.append(row)

currentStrength = traverse(cmap,K,S)

if currentStrength[1]:
    print('Yes')
    print(currentStrength[0])
else:
    print('No')
    print(currentStrength[0])