# 1. ლუწი თუ კენტი
number = int(input("Enter number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


# 2. ასაკობრივი კატეგორია
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")


# 3. შეფასების სისტემა
grade = int(input("Enter grade: "))

if grade < 0 or grade > 100:
    print("Invalid grade")
elif grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
elif grade >= 50:
    print("E")
else:
    print("F")


# 4. დიახ / არა
answer = input("Do you like Python? (yes/no) ").strip().lower()

if answer == "yes":
    print("Great!")
elif answer == "no":
    print("Maybe you will like it later")
else:
    print("Please answer yes or no")


# 5. კალკულატორი
first = float(input("Enter first number: "))
operation = input("Enter operation: ").strip()
second = float(input("Enter second number: "))

if operation == "+":
    print(f"{first} + {second} = {first + second}")
elif operation == "-":
    print(f"{first} - {second} = {first - second}")
elif operation == "*":
    print(f"{first} * {second} = {first * second}")
elif operation == "/":
    print(f"{first} / {second} = {first / second}")
else:
    print("Unknown operation")