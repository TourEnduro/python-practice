from sys import argv
from os.path import exists

script, input_file = argv

print(f"Does the log file exists? {exists(input_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
#starting coordinates of a robot
x = 0
y = 0

#log for history
history_log = []

def update_log():
    global x, y, history_log
    robot_position = f"x: {x}, y: {y}"

    #writing to a file
    log_file = open(input_file, 'a')
    log_file.write(robot_position + '\n')
    log_file.close()

    # writing to memory
    history_log.append(robot_position) 

print("Robot position:", f"x: {x}, y: {y}")

#entering a command to move: up, down, left, right

#infinite loop
while True:
    command = input("Enter command: ") # input moves us into an infitine loop
    
    if command == "quit":
        open(input_file, 'w').close()
        break

    elif command == "up":
        y += 1
        update_log()

    elif command == "down":
        y -= 1
        update_log()

    elif command == "left":
        x -= 1
        update_log()

    elif command == "right":
        x += 1
        update_log()

    elif command == "history":
        for entry in history_log:
            print(entry)

    else:
        print("Unknown command")
    #making a range
    if x > 5:
        x -= 1
        print("out of range")
    elif x < -5:
        x += 1
        print("out of range")
    elif y > 5:
        y -= 1
        print("out of range")
    elif y < -5:
        y += 1
        print("out of range")
    else:
        print("Robot position:", f"x: {x}, y: {y}")