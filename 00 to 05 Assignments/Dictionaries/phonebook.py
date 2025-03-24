# 01_phonebook

def phonebook():
    phonebooks= {}

    while True:
        phone_num = input("Enter the Phone Number: ")
        name = input("Enter the Name: ")
        if phone_num and name != "":
            phonebooks[phone_num] = name
        elif phone_num == "":
            print("Phone Number is required")
        elif name == "":
            print("Name is required")
        else:
            print("Both Phone Number and Name are required")
        
        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != "yes":
            break
    
    for phone_num, name in phonebooks.items():
        print(f"{name} : {phone_num}")