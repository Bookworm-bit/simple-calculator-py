import math

while True:
    o = input("Select your operator! (add = 1, subtract = 2, multiply = 3, divide = 4, power of = 5) \n")
    g = input("Enter your first number! \n")
    h = input("Enter your second number! \n")
    try:
        int(o)
    except ValueError:
        print("Please enter an integer value for your choice of operation!")
    ans = ""
    if (int(o) == 1):
        ans = float(g) + float(h)
    if (int(o) == 2):
        ans = float(g) - float(h)
    if (int(o) == 3):
        ans = float(g) * float(h)
    if (int(o) == 4):
            ans = float(g) / float(h)
    if (int(o) == 5):
        ans = pow(float(g), float(h))
    print("The answer is", flaot(ans))
