# assigning amount of cars:
cars = 100
# assigning each car's capacity:
space_in_a_car = 4.0
# assigning amount of drivers:
drivers = 30
# and amount of passengers:
passengers = 90
# calculating free cars:
cars_not_driven = cars - drivers
# calculating busy cars:
cars_driven = drivers
# calculating carpool capacity:
carpool_capacity = cars_driven * space_in_a_car
# calculation average passengers per car:
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")