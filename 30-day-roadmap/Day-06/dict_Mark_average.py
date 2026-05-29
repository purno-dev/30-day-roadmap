student = {
   "rafi":800,
   "purno": 900,
   "sahil":505,
   "sruti":785
}
mark = []
Sum=0
avg=0
item_count = 0
for key in student:
    mark.append(student[key])
    Sum+=student[key]
    item_count+=1
print(f"Average of {mark} is {Sum/item_count:.2f}")
    