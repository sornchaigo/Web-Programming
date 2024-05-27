response = "True" if 1 else "False"
print(response)

print(None or 0 or 18)

age = int(input("Please enter your age: "))
print(14 <= age <= 90 and age)


a = int(input("Please enter value? "))

cases = {
    0: "One or zero",
    1: "One or zero",
    2: "Two",
    3: "Never executes!",
}

out = ""
if a not in [0, 1, 2, 3]:
    out = "An unknown value"
else:
    out = cases[a]
print(out)


def showMessage(msg):
    print(msg)


print(type(cases))

for i in range(2, 11, 2):
    print(i)
