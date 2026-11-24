import sys
def temperature(c):
    return (c*9/5)+32
    print("Fahrenheit = ",f)
if "__name__"=="__main__":
    c=float(sys.argv[1])
    f=temperature(c)
    print("Fahrenheit = ",f)