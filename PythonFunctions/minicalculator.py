# today we are learn about functions in python
# and we learn then we are move to create mini calculator using functions concepts


#  get two values from user
# and then add them and print the result

print("Welcome to the Mini Calculator!")

print("Addition")
def add_numbers(a, b):
    result = a + b
    return result

num1 = float(input("Enter first number: ")) # convert input to float for decimal support 
num2 = float(input("Enter second number: ")) # convert input to float for decimal support
# call the function to add the numbers
sum_result = add_numbers(num1, num2)
print("The sum is:", sum_result)


# get two values from user
# and then subtract them and print the result

print("Subtraction")
def subtract_numbers(a, b):
    result = a - b
    return result

num1 = float(input("Enter first number: ")) # convert input to float for decimal support 
num2 = float(input("Enter second number: ")) # convert input to float for decimal support
# call the function to subtract the numbers
sub_result = subtract_numbers(num1, num2) # call the function to subtract the numbers and function return value is stored in sub_result
print("The difference is:", sub_result) # print the result of subtraction



# now we get value from user and also get operator from user like user enter + for addition, - for subtraction, * for multiplication, / for division

# function to multiply two numbers
def multiplication(a, b):
    result = a * b
    return result
# function to divide two numbers
def division_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    result = a / b
    return result
# function to find modulus of two numbers
def modulus_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    result = a % b
    return result
def mini_calculator(num1, num2, operator):
    if operator == '+':
        return add_numbers(num1, num2)
    if operator == '-':
        return subtract_numbers(num1, num2)
    if operator == '*':
        return multiplication(num1, num2)
    if operator == '/':
        return division_numbers(num1, num2)
    if operator == '%':
        return modulus_numbers(num1, num2)
    return "Invalid operator"

# get two values from user
num1 = float(input("Enter first number: "))  # convert input to float for decimal support
num2 = float(input("Enter second number: "))  # convert input to float for decimal
# support
operator = input("Enter operator (+, -, *, /, %): ")

result = mini_calculator(num1, num2, operator)
print("The result is:", result)
