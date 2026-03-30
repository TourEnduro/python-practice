#starting coordinates of a robot
x = 0
y = 0
print("Robot position:", "x:", x, "y:", y)
#entering a command to move: up, down, left, right

#infinite loop
while True:
    command = input("Enter command: ") # input moves us into an infitine loop
    
    if command == "quit":
        quit()
    elif command == "up":
        y = y + 1
    elif command == "down":
        y = y - 1
    elif command == "left":
        x = x - 1
    elif command == "right":
        x = x + 1
    else:
        print("Unknown command")
    #showing robot's new position
    print("Robot position:", "x:", x, "y:", y)