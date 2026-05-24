# Simple Calculator

print("=" * 50)
print("             Simple Python Clculator")
print("=" * 50)
firstNumber = int(input("Enter First Number:"))
secondNumber = int(input("Enter Second Number:"))
option = str(input("Enter Option(+,-,*,/): "))

if option =='+':
    print(F"Your Answer is: {firstNumber + secondNumber}")
elif option == '-':
    print(F"Your Answer is: {firstNumber - secondNumber}")
elif option == '*':
    print(F"Your Answer is: {firstNumber * secondNumber}")
else:
    print(F"Your Answer is: {firstNumber / secondNumber}")