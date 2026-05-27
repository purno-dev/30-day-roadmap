temp=""
vNumber =0
str = input("Enter String to Count Vowel:")
for i in range(0, len(str),1):
    print(str[i])
    temp=str[i].lower()
    if (temp=="a" or temp=="e" or temp=="i" or temp=="o" or temp=="u"):
        vNumber+=1
print(f"Numbers of Vowels is {vNumber}")
