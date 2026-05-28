def prime (x):
    isPrime=True
    if (x<=1):
        isPrime=False
    elif (x==2):
        isPrime=True
    elif (x%2==0):
        isPrime=False
    else:
        for i in range(3,x,2):
            if(x%i==0):
                isPrime=False
                break
            isPrime=True
    return isPrime
num = int(input("Enter Number:"))
if (prime(num)):
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is Not Prime Number")

