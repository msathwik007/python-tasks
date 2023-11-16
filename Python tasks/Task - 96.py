total = 0
attempts = int(input("How many attempts"))
for x in range (attempts):
      time = int(input("How long did it take in seconds to solve it?"))
      total = total + time
average = total / attempts
print("The total time is:",total)
print("The average time is",average)
