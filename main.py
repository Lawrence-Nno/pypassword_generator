def pypassword_generator():
    """
    This function generates a random password, the length of the password is determined by the inputs it receives.
    The password must contain at least a letter, number and a special character/symbol
    :return: A string, the password
    """
    import random
    import string

    # A list of the special characters/symbols
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '?', '@']

    # A list of numbers
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Lower and Upper case letters generated using the String module imported above
    alphabets = string.ascii_letters
    password = ""

    # Welcome message
    print("Welcome to Pypassword Generator")

    # A while loop and try and except method to ensure an integer other than 0 is inputted
    while True:
        try:
            no_of_letters = int(input("How many letters would you like in your password?\n"))
        except ValueError:
            print("Number of letters must be an Integer")
        else:
            if no_of_letters == 0:
                print("Number of letters can't be 0")
            else:
                break
    while True:
        try:
            no_of_symbols = int(input("How many symbols would you like in your password?\n"))
        except ValueError:
            print("Number of symbols must be an Integer")
        else:
            if no_of_symbols == 0:
                print("Number of symbols can't be 0")
            else:
                break
    while True:
        try:
            no_of_numbers = int(input("How many numbers would you like in your password?\n"))
        except ValueError:
            print("Number of Numbers must be an Integer")
        else:
            if no_of_numbers == 0:
                print("Number of numbers can't be 0")
            else:
                break

    # List of the randomly chosen characters
    list_of_letters = random.sample(alphabets, no_of_letters)
    list_of_numbers = random.sample(numbers, no_of_numbers)
    list_of_symbols = random.sample(symbols, no_of_symbols)

    # Combines the 3 list of letters, numbers and symbols above
    unique_list = (list_of_letters + list_of_numbers + list_of_symbols)

    # Shuffles the combined list.
    random.shuffle(unique_list)

    # A for loop to form a string, the password from the reshuffled list above.
    for item in unique_list:
        password += item
    print(password)
    return password


if __name__ == '__main__':
    pypassword_generator()

