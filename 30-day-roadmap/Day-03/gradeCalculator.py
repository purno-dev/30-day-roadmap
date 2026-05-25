mark = int(input("Enter Youtr Mark for Calculating Grade:"))
if (mark <= 100 and mark >= 80):
    print(f"The grade is for {mark} is A+")
elif ( mark <= 79 and mark >=70):
    print(f"The grade is for {mark} is A")
elif ( mark <= 69 and mark >=60):
    print(f"The grade is for {mark} is A-")
elif ( mark <= 59 and mark >=50):
    print(f"The grade is for {mark} is B")
elif ( mark <= 49 and mark >=40):
    print(f"The grade is for {mark} is C")
elif ( mark <= 39 and mark >=33):
    print(f"The grade is for {mark} is D")
else:
    print(f"The grade is for {mark} is F")