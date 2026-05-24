principle = int(input("Enter Principle Amount:"))
interestRate = float(input("Enter Interest Rate in (%):"))
time = int(input("Enter Time in Years:"))
intrest = principle * interestRate * time / 100
print(f"Interest is {intrest}")