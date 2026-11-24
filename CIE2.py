import sys
def temperature(c):
    return (c*9/5)+32
    c=float(sys.argv[1])
    print("Fahrenheit = ",temperature(c))
if "__name__"=="__main__":
    temperature()
