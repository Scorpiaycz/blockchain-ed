dec = input("Enter address in decimal: ")
total = 0

for i in range(len(dec)):
    total += int(dec[i])

print("Sum of decimal: ", total)