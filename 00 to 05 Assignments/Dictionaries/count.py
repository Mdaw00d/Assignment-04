# 00_count_nums

def count_nums():
    counts = {}
    while True:
        try:
            num = int(input("Enter a number: "))
            counts[num] = counts.get(num, 0) + 1
        except ValueError:
            break

    for num, count in counts.items():
        print(f"{num} appears {count} times.")
