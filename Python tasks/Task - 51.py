choice = input("Would you like to convert to Celsius or Fahrenheit")
if choice == "Fahrenheit":
      temperature = float(input("Enter a temperature in Celsius"))
      formula = (temperature * 9/5) + 32
      print("The temperature in Fahrenheit is: ", formula)
else:
      temperature = float(input("Enter a temperature in Fahrenheit"))
      formula = (temperature - 32) * 5/9
      print("The temperature in Celsius is: ", formula)
