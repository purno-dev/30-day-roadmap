
number = int(input("Enter Number to Check if it's Prime or not:"))
if (number<=1):
    print(f"{number} is not a Prime Number")
elif(number==2):
    print(f"{number} is Prime Number")
else:
    for i in range(2, number,1):
        if (number%i==0):
            print(f"{number} is  not a Prime Number")
            break
        elif(number%i!=0):
            print(f"{number} is Prime Number")
            break



