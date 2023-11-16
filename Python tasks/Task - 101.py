total = 0
highest = 0
lowest = 99999999
for x in range (1,7):
      amount = int(input("How many did you buy in this supermarket "+str(x)))
      if amount > 0:
            cost = float(input("how much did each toilet roll cost?"))
            total = total + (cost*amount)
            if cost > highest:
                  highest = cost
            if cost < lowest:
                  lowest = cost
print("The total amount spent:",total)
print("highest amount spent on a single roll",highest)
print("lowest amount spent on a single roll",lowest)
