from footballTimeCalculator import convertFootballToReal

minutes = float(input("Please enter the current number of Football Minutes: "))
converted = float(convertFootballToReal(minutes))
print("Converted time: ", converted)
print("This is equal to %s real hours." % converted / 60)
