import random

def randDice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    print(f"The total is: {total}")
    return total

grand_total = 0

for number in range(100):
    grand_total += randDice()

average = grand_total / 100
print(f"The average is: {average:.2f}")