def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thank you for using this function")
    return mfx

@greet
def Average(*Numbers):
    sum = 0
    for i in Numbers:
        sum += i
    print("Average is:", sum / len(Numbers))



A = int(input("How many numbers you want to enter : "))
for i in range (1,A+1):
    B = int(input(f"Enter the {i} Number : "))

Average(B)
    