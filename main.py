donuts_box = 36
print ("text " + str(donuts_box))

life = int(input("How many lives do you have? "))
if life > 0:
  life = life -1
  print("Your life = " + str(life))
elif life == 0:
  print("GAME OVER")
else:
  print("Hmmm... something doesn't seem right")