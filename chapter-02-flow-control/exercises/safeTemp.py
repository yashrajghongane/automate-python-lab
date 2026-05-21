# Fixing the Safe Temperature Prgram
scale = input("Enter C and F to indace Celcius or Fehrenhei: ")
degree = int(input("Enter the Number of Degrees: "))
if (scale == "C" and degree >= 16 or degree <= 38) or (scale == "C" and degree >= int(60.8) or degree <= int(100.4)):
    print("Safe")
else:
    print("Dangerous")