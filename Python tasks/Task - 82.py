negative = int(input("How many negatives did you get?"))
if negative == 1:
    for i in range(10):
        print("Prompt")
elif negative == 2:
    for i in range(50):
        print("Reminder")
elif negative == 3:
    for i in range(100):
        print("Warning")
else:
    for i in range(500):
        print("Removal")
