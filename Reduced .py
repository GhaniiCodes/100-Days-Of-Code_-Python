import functools as func
Target = 10
A = []
Length = int(input("Enter the length of list : "))
for i in range (1, Length+1):
    Input = int(input(f"Enter {i} element of list : "))
    A.append(Input)

print ("Original List : ",A)

pairs = []

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] + A[j] == Target:
            pairs.append ((i, j))

print (pairs)
    