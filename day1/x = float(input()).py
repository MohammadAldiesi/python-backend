x = float(input("price: "))
tip = float(input("Tip amount (%): "))

tip_calc = x * (tip / 100)
total = x + tip_calc

print("tip: ",tip_calc)
print("total: ",total)


