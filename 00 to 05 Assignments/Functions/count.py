# 02_count_even

def count_even(list1):
    even_counter=0
    for i in list1:
        if i % 2 == 0:
            even_counter+=1
    print(f"Total numbers of even is {even_counter}")