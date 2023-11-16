positive = 0
negative = 0
mild = 0
severe = 0
number = int(input("How many patients need to be tested?"))
for x in range (number):
      fever = input("Do you have a fever? yes or no")
      cough = input("Do you have a dry cough? yes or no")
      if fever == "yes" and cough == "yes":
            print("You have tested positive for the virus")
            positive = positive + 1
            symptoms = input("Are the symptoms mild or severe?")
            if symptoms == "mild":
                  mild = mild+1
            else:
                  severe = severe+1
      else:
            print("You have tested negative for the virus")
            negative = negative + 1
print("Positive: ",positive)
print("Negative: ",negative)
print("Mild symptoms: ",mild)
print("Severe symptoms: ",severe)
