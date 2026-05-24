firstNumber = int(input("Enter First Number:"))
secondNumber =int(input("Enter Second Number:"))
thirdNumber = int(input("Enter Third Number:"))
if (firstNumber > secondNumber and firstNumber > thirdNumber):
    print(f"{firstNumber} is the largest number")
elif (secondNumber > firstNumber and secondNumber > thirdNumber):
    print(f"{secondNumber} is the largest number")
else:
    print(f"{thirdNumber} is the largest number")