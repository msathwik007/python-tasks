sweets = int(input("How many sweets do you need"))
students = int(input("Enter the number of students"))
cost = float(input("Enter the total cost"))
costeach = cost / students
sweetseach = sweets // students
sweetsremaining = sweets % students
print("Cost each: £",costeach)
print("Sweets each: ",sweetseach)
print("Sweets remaining: ",sweetsremaining)
