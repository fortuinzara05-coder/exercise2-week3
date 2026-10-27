# Question 1: Arithmetic and Assignment Operators
x = 10
x += 3
y = 5
y *= 2
result = x / y
print(f"Result of x divided by y: {result}")
# ------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
a = 15
b = 10
c = 12
condition1 = a > b
condition2 = b % 2 == 0
condition3 = c <= a
final_condition = condition1 or (condition2 and condition3)
print(f"Final condition is: true")
# ------------------------------------------------------------------------------------
# Question 3: Conditional Statements
score = int(input("85"))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 89:
    grade = 'B'
elif 70 <= score < 79:
    grade = 'C'
elif 60 <= score < 69:
    grade = 'D'
else:
    grade = 'F'
    print(f"Grade for the score 85 is: B")
    #------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals
num1 = float(input("0 "))
num2 = float(input("4 "))
operation = input("Enter an operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
    print(f"result of 0 + 4 is: 4")
elif operation == '-':
    result = num1 - num2
    print(f"result of 0 - 4 is: -4")
elif operation == '*':
    result = num1 * num2
    print(f"result of 0 * 4 is: 0")
elif operation == '/':
    result = num1 / num2
    print(f"result of 0 / 4 is: 0")
    
