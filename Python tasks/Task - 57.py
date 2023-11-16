miles = int(input("How many miles are you going to travel?"))
membership = input("Do you have a membership card")
if  membership== "yes":
      hirecost = ((miles-1)*0.25) +2
else:
      hirecost = ((miles-1)*0.25) +(5+2)
dieselcost= miles*0.5
totalcost=  hirecost+dieselcost
print("The total cost is: £",totalcost)
