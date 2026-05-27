number = int(input("Enter Number for Multiplication table:"))
mul = 0
for i in range(1,11,1):
    mul=number*i
    print(f"{number}X{i}={mul}")