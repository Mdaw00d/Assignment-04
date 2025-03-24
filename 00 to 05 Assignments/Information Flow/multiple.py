# 04_multiple_returns

def multiple_returns():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email
    

def multiple_returns():
    """Gets user data and prints it."""
    user_data = multiple_returns()
    print(f"Received the following user data: {user_data}")