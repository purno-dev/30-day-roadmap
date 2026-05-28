def facto (x):
    fact=1
    for i in range(1,x+1,1):
        fact*=i
    return fact

num = int(input("Enter Number to Factorial Value:"))
print(f"Factorial of {num} is {facto(num)}")

