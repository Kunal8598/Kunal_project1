"""
Ask age from user.

18 above -> Adult
13-17 -> Teenager
13 below -> Child
"""

a = int(input("Enter Your Age = "))
if a > 18:
    print("Adult")
elif 13 < a < 17:
    print("Teenager")
else:
    print("Child")
