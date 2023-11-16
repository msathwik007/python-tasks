pc = input("Do you play games on a PC")
console = input("Do you play games on a console?")
if pc == "yes" and console == "yes":
    print("Game master")
elif pc == "yes" and console == "no":
    print("PC master")
elif pc == "no" and console == "yes":
    print("Console master")
else:
    print("Error")
