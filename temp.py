import sys

if sys.argv[1].lower() == "c":
    fahrenheit = round((float(sys.argv[2]) * 9/5) + 32, 2)
    print(str(fahrenheit) + "F")

if sys.argv[1].lower() == "f":
    celcius = round((float(sys.argv[2])-32)*5/9, 2)
    print(str(celcius) + "C")