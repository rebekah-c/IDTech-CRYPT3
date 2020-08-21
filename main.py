import random

# this is the game of Random, my range is from 3 to 18
computer_number = random.randrange(3, 18)

print(computer_number)

for x in range(0, 3):
  print(computer_number)

number_of_leaves = 15
for x in range(1, number_of_leaves+1):
  print("A leaf fell onto the ground. " + str(x) + " leaves have fallen")
print("All done.")