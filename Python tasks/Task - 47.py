temp = float(input("Enter a temperature"))
rain = input("Is it raining outside?")
if temp < 13 and rain == "yes":
    print("Wear a coat and bring an umbrella")
elif temp < 13 and rain == "no":
    print("Wear a coat")
elif temp >= 13 and rain == "yes":
    print("bring an umbrella")
else:
    print("you don't need a coat or an umbrella")
