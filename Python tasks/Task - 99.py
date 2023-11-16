total = 0
for x in range (5):
    choice = input("did you win, lose or draw in your match")
    if choice == "win":
        total = total + 3
    elif choice == "lose":
        total = total + 0
    else:
        total = total + 1
print("total points earned:",total)
if total >= 12:
    print("you have been promoted")
elif total < 6:
    print("you have been relegated")
else:
    print("You are staying in the same division")
