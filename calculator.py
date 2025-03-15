import math

# Basic operations
def add(nums):
    return sum(nums)

def sub(nums):
    result = nums[0]
    for i in nums[1:]:
        result -= i
    return result

def multiply(nums):
    result = nums[0]
    for i in nums[1:]:
        result *= i
    return result

def division(nums):
    result = nums[0]
    for i in nums[1:]:
        if i == 0:
            raise ValueError("Cannot divide by zero.")
        result /= i
    return result

# Single input functions
def square(num):
    return num ** 2

def cube(num):
    return num ** 3

def sqrt(num):
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(num)

def cbrt(num):
    return num ** (1 / 3)

def power(nums):
    result = nums[0]
    for i in nums[1:]:
        result = result ** i
    return result

def exppower(num):
    return math.exp(num)

def log(nums):
    if nums[0] <= 0 or nums[1] <= 0:
        raise ValueError("Logarithm values must be positive.")
    return math.log(nums[0], nums[1])

def lon(num):
    if num <= 0:
        raise ValueError("Natural log value must be positive.")
    return math.log(num)

# Trigonometric functions (convert degrees to radians)
def sin(num):
    return math.sin(math.radians(num))

def cos(num):
    return math.cos(math.radians(num))

def tan(num):
    return math.tan(math.radians(num))

# Factorial with base case
def fact(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if num == 0 or num == 1:
        return 1
    return num * fact(num - 1)

# Input handling
def proper_numbers(prompt):
    '''Function to get proper numbers from user'''
    nums_list = []
    while True:
        nums = input(f"{prompt} (Press Enter to stop): ").strip()
        if nums == '':
            if not nums_list:
                print("You have to enter at least one value.")
                continue
            break
        try:
            num = float(nums)
            nums_list.append(num)
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    return nums_list[0] if len(nums_list) == 1 else nums_list

def get_single_number(prompt):
    '''Function to get a proper single number'''
    while True:
        num = input(prompt).strip()
        try:
            num = int(num)
        except ValueError:
            print('Invalid input. Please enter valid input again: ')
        else:
            return num

def defining_options():
    '''Function to define options to perform operations'''
    symbols_dict = {
        1: 'Addition',
        2: 'Subtraction',
        3: 'Multiplication',
        4: 'Division',
        5: 'Power',
        6: 'Log(number, base)',
        7: 'Square',
        8: 'Cube',
        9: 'Square Root',
        10: 'Cube Root',
        11: 'Natural Log',
        12: 'Exponential Power',
        13: 'Sine (degrees)',
        14: 'Cosine (degrees)',
        15: 'Tangent (degrees)',
        16: 'Factorial'
    }
    print("\nChoose an operation:")
    for key, value in symbols_dict.items():
        print(f"{key}: {value}")

def choose_option():
    '''Function to choose the operation'''
    while(True):
        num = get_single_number("Enter a number to choose an operation: ")
        if (num < 1 or num > 16):
            print("Enter a number in the given operations range: ")
        return num


def perform_operation(nums, symbol):
    '''Function to perform the operation'''
    operation_dict = {
        1: add,
        2: sub,
        3: multiply,
        4: division,
        5: power,
        6: log,
        7: square,
        8: cube,
        9: sqrt, 
        10: cbrt,
        11: lon,
        12: exppower,
        13: sin,
        14: cos,
        15: tan,
        16: fact
    }
    
    try:
        if symbol in [1, 2, 3, 4, 5, 6]:
            return operation_dict[symbol](nums)
        else:
            return operation_dict[symbol](nums)
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    is_continue = 'y'
    while is_continue == 'y':
        defining_options()
        operation = choose_option()

        if operation in range(1, 7):
            nums = proper_numbers('Enter numbers for the operation:')
            result = perform_operation(nums, operation)
        else:
            num = get_single_number('Enter a number:')
            result = perform_operation(num, operation)

        if result is not None:
            print(f"The result is: {result}")
        
        is_continue = input(f"Do you want to continue (y/n): ").strip().lower()
    
    print("Thank you for using the calculator. Goodbye!")

if __name__ == '__main__':
    main()
