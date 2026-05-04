from sys import argv
from os.path import exists

script, input_file = argv

print(f"Does the log file exists? {exists(input_file)}")
print("Ready, ENTER DIRECTION to continue, CTRL-C to abort.")

#starting coordinates of a robot
x = 0
y = 0

#log for history
history_log = []

#making a function to update a log-file

def update_log():
    global x, y, history_log
    robot_position = f"x: {x}, y: {y}"

    #writing to a file
    log_file = open(input_file, 'a')
    log_file.write(robot_position + '\n')
    log_file.close()
    print("Robot position:", f"x: {x}, y: {y}")

    # writing to memory
    history_log.append(robot_position) 

print("Robot position:", f"x: {x}, y: {y}")

#entering a command to move: up, down, left, right
#type "history" to show log, type "quit" to quit and clean the file

#infinite loop
while True:
    command = input("Enter command: up, down, left, right, history or quit > ") # input moves us into an infitine loop
    match command:
        case "quit":
            #quiting after entering "quit"
            open(input_file, 'w').close()
            break

        case "up":
            if y < 5:
                y += 1
                update_log()
            else:
                print("Out of range")

        case "down":
            if y > -5:
                y -= 1
                update_log()
            else:
                print("Out of range")

        case "left":
            if x > -5:
                x -= 1
                update_log()
            else:
                print("Out of range")

        case "right":
            if x < 5:
                x += 1
                update_log()
            else:
                print("Out of range")

        case "history":
            for entry in history_log:
                print(entry)

        case _:
            print("Unknown command")