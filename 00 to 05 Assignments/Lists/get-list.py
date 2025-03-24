# 07_get_list   

def get_list():
    list = []
    while True:
        user_input = input("Enter the value: ")
        if user_input == "":
            print(list)
            break
        else:
            list.append(user_input)