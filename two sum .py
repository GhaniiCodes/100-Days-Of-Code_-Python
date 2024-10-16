num = [2,7,11,15]
Target = 9
for i in range (len(num)):
    for j in range(i+1,len(num)):
        if num[i] + num[j] == Target:
            print ((i,j))