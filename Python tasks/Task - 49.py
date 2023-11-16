number = int(input("Enter a number"))
currentunit= input("What is the current unit? bit,byte or kilobyte")
newunit= input("What is unit do you want to convert to? bit,byte or kilobyte")
if currentunit == "bit" and newunit=="byte":
      print(number/8, "bytes")
elif currentunit == "bit" and newunit=="kilobyte":
      print(number/8000, "kilobytes")
elif currentunit == "byte" and newunit=="bit":
      print(number*8, "bits")
elif currentunit == "byte" and newunit=="kilobyte":
      print(number/1000, "kilobyte")
elif currentunit == "kilobyte" and newunit=="byte":
      print(number*1000, "bytes")
elif currentunit == "kilobyte" and newunit=="bit":
      print(number*8000, "bits")
