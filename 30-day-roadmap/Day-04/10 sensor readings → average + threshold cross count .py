import random
temp = 0
thresheold = 35
thres_count=0
reading = []
avg = 0
for i in range(0,11,1):
    temp =random.uniform(20,38)
    reading.append(temp)
    if (temp>=thresheold):
        thres_count+=1
avg = sum(reading)/len(reading)

print(f"Threshold Cross {thres_count} Times and Average is {avg:.2f}")

