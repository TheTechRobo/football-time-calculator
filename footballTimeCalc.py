def convertFootballToReal(minutes):
    return minutes * 2.5

def _Interactive():
    minutes = float(input("Please enter the current number of Football Minutes: "))
    converted = convertFootballToReal(minutes)
    print("Converted time: ", converted)
    print("This is equal to %s real hours." % converted / 60)

if __name__ == "__main__":
    _Interactive()
