from sys import argv

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party")
    print("Get a blanket.\n")

print("We can give the function number directly")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("we can do math inside too!:")
cheese_and_crackers(10+20,5+6)

print("And we can combine the two, variables and math")
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)


from sys import argv

def addition_2(argv[1], argv[2]):
    return int(argv[1])+int(argv[2])
