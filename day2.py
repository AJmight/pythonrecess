# def product(a, b,c):
#     return a * b * c
# print(product(1, 2, 3))

# def divide(a, b):
#     return a / b
# print(divide(10, 2))

# division=lambda x,y: x / y
# print(division(10, 2))
# cube=lambda x : x**3
# print(cube(3))
# greetings= lambda first,second : first + second
# print(greetings("Hi, ", "Guys!"))
# even= lambda x: x if x%2==0 else "Odd"
# print(even(1))
# pupil_check=lambda x: "Olevel" if x<=17 and x>=13 else "Alevel"
# print(pupil_check(15))

#write a program to handle errrors 
# ask prog to ask for two numbers using input and then divide them use infinite looop 
#to keep asking valid input until user enters valid numbers
def divide(x, y):
        return x / y

while True:
    try:
        x = float(input("Enter the first number (x): "))
        y = float(input("Enter the second number (y): "))
        result = divide(x, y)
        print(f"The result of {x} / {y} is: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a valid y.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except TypeError:
        print("Invalid type. Please enter numbers.")
    finally:
        print("Hope it worked out well!")

          
  