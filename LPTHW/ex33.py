i = 0
var = int(input('>'))
numbers = []


def counter(i):
    while i < var:
      print(f"At the top i is {i}")
      numbers.append(i)
      i += 1
      print("Numbers now: ", numbers)
      print(f"At the bottom i is {i}")

counter(i)
    

#print("The numbers: ")

#for num in numbers:
#    print(num)