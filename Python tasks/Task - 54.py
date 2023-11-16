health = int(input("How many health points remained after last attack"))
time = int(input("How long was it since you last got hit?"))
if time <6:
      print("Your current health is",health)
      percentage = (health / 500) * 100
      print("Your current health percentage is: %",percentage)
else:
      timeafter5seconds = time-5
      newhealth = health+(timeafter5seconds*(0.01*500))
      if newhealth > 500:
            newhealth = 500
      print("Your current health is",newhealth)
      percentage = (newhealth / 500) * 100
      print("Your current health percentage is: %",percentage)
