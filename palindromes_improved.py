# Function to check if a string is a palindrome
def is_palindrome(string):
    """Check if a string is a palindrome.
    
    Args:
        string (str): The string to check for palindrome.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    string = string.lower().replace(' ','')
    return string == string[::-1]

# Function to check if a string is a palindrome using reversed() method
def is_palindrome_reversed(string):
    """Check if a string is a palindrome using reversed() method.
    
    Args:
        string (str): The string to check for palindrome.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    string = string.lower().replace(' ','')
    reverse_string = ''.join(reversed(string))
    return string == reverse_string

# Function to check if a string is a palindrome using a for loop
def is_palindrome_for_loop(string):
    """Check if a string is a palindrome using a for loop.
    
    Args:
        string (str): The string to check for palindrome.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    string = string.lower().replace(' ','')
    reverse_string = ''
    for char in string:
        reverse_string = char + reverse_string
    return string == reverse_string

# Function to check if a string is a palindrome using a while loop
def is_palindrome_while_loop(string):
    """Check if a string is a palindrome using a while loop.
    
    Args:
        string (str): The string to check for palindrome.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    string = string.lower().replace(' ','')
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

# Function to check if a string is a palindrome using recursion
def is_palindrome_recursive(string):
    """Check if a string is a palindrome using recursion.
    
    Args:
        string (str): The string to check for palindrome.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    string = string.lower().replace(' ','')
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return is_palindrome_recursive(string[1:-1])

# Function to check if an integer is a palindrome
def is_palindrome_integer(number):
    """Check if an integer is a palindrome.
    
    Args:
        number (int): The integer to check for palindrome.
        
    Returns:
        bool: True if the integer is a palindrome, False otherwise.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    number_str = str(number)
    return number_str == number_str[::-1]

# Function to check if an integer is a palindrome using arithmetic operations
def is_palindrome_integer_arithmetic(number):
    """Check if an integer is a palindrome using arithmetic operations.
    
    Args:
        number (int): The integer to check for palindrome.
        
    Returns:
        bool: True if the integer is a palindrome, False otherwise.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    original_number = number
    reverse_number = 0
    while number > 0:
        remainder = number % 10
        reverse_number = reverse_number * 10 + remainder
        number //= 10
    return original_number == reverse_number

# Test cases
def test_palindrome_functions():
    test_strings = ["Madam Im Adam", "Was it a car or a cat I saw", "", "hello", "12321"]
    test_integers = [121, 12321, 12345, 121212, -12321]
    
    print("Testing string palindromes:")
    for string in test_strings:
        print(f"'{string}' is palindrome:", is_palindrome(string))
        print(f"'{string}' is palindrome (reversed):", is_palindrome_reversed(string))
        print(f"'{string}' is palindrome (for loop):", is_palindrome_for_loop(string))
        print(f"'{string}' is palindrome (while loop):", is_palindrome_while_loop(string))
        print(f"'{string}' is palindrome (recursive):", is_palindrome_recursive(string))
    
    print("\nTesting integer palindromes:")
    for number in test_integers:
        print(f"{number} is palindrome (typecast):", is_palindrome_integer(number))
        print(f"{number} is palindrome (arithmetic):", is_palindrome_integer_arithmetic(number))

# Run test cases
test_palindrome_functions()
