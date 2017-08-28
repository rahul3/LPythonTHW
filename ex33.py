


def while_function(while_num,increment):
    numbers = []
    i = 0
    while i < while_num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers


num1 = while_function(5,2)

print("The numbers: ")

for num in num1:
    print(num)
