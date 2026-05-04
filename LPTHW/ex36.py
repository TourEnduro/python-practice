from sys import exit

def stairs():
    print("There is are stairs, leading you to the roof")
    print("You can climb them and make your final jump to the Matrix")
    print("You wake up and see Neo, congratulation, you are safe now")
    print("Here comes Morpheus and asks you to take either Blue or Red pill")

    choice = input('> ')
    if choice == "blue":
        print("You wake up at home and think that everithing you've seen was a dream")
        exit(0)
    elif choice == "red":
        print("You got know, how deep the rabbit hole is")
        exit(0)
    else:
        print("You have to make a choice, man!")
        stairs()

def classroom():
    print("There is a class room, where you should be today")
    print("There is a slightly chance for you to escape")
    print("Do you preffer to Stay, to find a Secret room behind the shelfs, to go to the Toilet or to Simulate your stomacheacke and go home?")
    decision = False

    while True:
        choice = input('> ')

        if choice == "toilet":
            print("All right, you managed to go to a toilet, but here is a problem")
            toilet()
        elif choice == "secret":
            stairs()
        elif choice == "simulate":
            print("You tricked your teacher and made yourself on the way home. You won!")
            exit(0)
        elif choice == "stay":
            print("You fall a sleep in the classroom. You had a dream, that you came to school.")
            print("You found yourself naked O_o")
            start()
        else:
            print("You need to decide right now!")
            classroom()

def toilet():
    print("There are some bustards you hate from the other class")
    print("They are planning to beat the whole shit out of you")
    print("What you choose: to Run, to Hide or to Fight them?")
    decision = False

    while True:
        choice = input('> ')

        if choice == "run":
            print("You fall on a wet floor. Your journey ends here. You died.")
            exit(0)
        elif choice == "fight":
            print("As expected: they bitted the whole shit out of you.")
            print("You wake up in a hospital and there is no one there.")
            print("You here noises behind the window. It sounds like there are zombies out there...")
            exit(0)
        elif choice == "hide":
            print("You locked yourself up in a closet and suddenly you've found a hole behind a mirror")
            print("You climb into it and then you crawl through the tight tunnel")
            stairs()

def start():
    print("You are standing in a hallway of your school")
    print("You are deciding either to go to the classroom or to visit the toilet first")
    decision = False

    while True:
        choice = input('> ')

        if choice == "classroom":
            classroom()
        elif choice == "toilet":
            toilet()
        else:
            print("You haven't found any reason to stay there today and decided to go home. You won!")

start()