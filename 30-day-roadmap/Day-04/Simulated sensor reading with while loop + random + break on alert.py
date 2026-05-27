import random


while True:
    sensorValue = random.uniform(0, 38)
    print(f"{sensorValue:.2f}")
    if (sensorValue>=35):
        break
print("Very Hot")


