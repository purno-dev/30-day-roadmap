isPrime =True
number = int(input("Enter Number to Check if it's Prime or not:"))
if (number<=1):
    
    isPrime =False
elif(number==2):
    isPrime =True
else:
    for i in range(2, number,1):
        if (number%i==0):
            isPrime =False
            break

if isPrime:
    print(f"{number} is Prime Number")
else:
    print(f"{number} is not a Prime Number")



