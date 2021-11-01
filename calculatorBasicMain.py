o = input("Select your operator! (add = 1, subtract = 2, multiply = 3, divide = 4, power of = 5) \n")
g = input("Enter your first number! \n")
h = input("Enter your second number! \n")
ans = ""
whileTrue:
    if (int(o) == 1):
        ans = int(g) + int(h)
    if (int(o) == 2):
        ans = int(g) - int(h)
    if (int(o) == 3):
        ans = int(g) * int(h)
    if (int(o) == 4):
        ans = int(g) / int(h)
    if (int(o) == 5):
        ans = pow(int(g), int(h))
    print("The answer is", ans, "!")
