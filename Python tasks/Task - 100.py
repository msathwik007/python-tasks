positive = 0
zero = 0
negative = 0
odd = 0
even = 0
for x in range (5):
      number = int(input("Enter a number"))
      if number % 2 == 0:
            even = even+1
      else:
            odd = odd+1
      if number>0:
            positive = positive+1
      elif number <0:
            negative = negative+1
      else:
            zero = zero+1
print("Positives: ",positive)
print("negative: ",negative)
print("zero: ",zero)
print("even: ",even)
print("odd: ",odd)
