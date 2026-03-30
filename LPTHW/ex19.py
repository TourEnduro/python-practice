def cheese_and_crackers(cheese_count, boxes_of_crackers, sandwiches):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print(f"You can combine you {cheese_count} cheeses and {boxes_of_crackers} boxes of crackers into {sandwiches} sandwiches")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30, 30-20)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
amount_of_sandwiches = amount_of_crackers - amount_of_cheese

cheese_and_crackers(amount_of_cheese, amount_of_crackers, amount_of_sandwiches)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6, 50 - 10)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000, amount_of_sandwiches)