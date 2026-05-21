# Dishonest Capacity Calculator
print("Enter TB or GB for advertized unit: ")
unit = input("-> ")

if unit == 'TB' or unit == 'tb':
    discrepency = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepency = 1000000000 / 1073741824

print("Enter the Advertized Capacity:")
advertized_capacity = (input("-> "))
advertized_capacity = float(advertized_capacity)

real_capacity = str(round(advertized_capacity * discrepency,2))
print("The Real Capacity is " + real_capacity + unit)