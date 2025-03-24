# 03_powerful_passwords

import hashlib

def hashlib_login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email or password != "":
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
    else:
        print("Email and password are required")


    stored_logins = {
    "user1@example.com": hashlib.sha256("password123".encode()).hexdigest(),
    "user2@example.com": hashlib.sha256("securepass".encode()).hexdigest(),
    }

    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    isCorrect =  email in stored_logins and stored_logins[email] == hash_password(password)
    print(f"The user {email} is {isCorrect}")
