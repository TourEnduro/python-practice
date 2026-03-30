name = 'Dmitry Sergeev'
age = 35 # not a lie
height = 195 # cm
height_in_inches = round(height / 2.54)
weight = 91 #kg
weight_in_pounds = round(weight * 2.2046) 
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_in_inches} inches tall.")
print(f"He's {weight_in_pounds} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_in_inches + weight_in_pounds
print(f"if I add {age}, {height_in_inches}, and {weight_in_pounds} I get {total}.")