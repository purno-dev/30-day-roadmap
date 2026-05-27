n = int(input("Enter Number for Factorial Value:"))
fact = 1
for i in range(1, n+1,1):
    
    fact*=i
    
    if (i==n):
        break
print(f"Factorial of {n} is = {fact}")