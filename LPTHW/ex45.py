from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene it is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Spaceship(Scene):
    def enter(self):
        print(dedent("""
              You find yourself on the floor of a crashed spaceship.
              You don't remember why are you here and what happend.
              It's quite messy around you. You know that you have to get out to find some help.
              What would you do? ('Give up', 'Break window', 'Open door')
              """))
        action = input('> ')

        if action == 'give up':
            print("Great choice, you starve to death. Congratulations! Game over.")
            return 'death'

        if action == 'break window':
            print(dedent("""
                         You came to the front part of your spaceship and see a crack on the window.
                         You pick up your backpack and hit the window with a heavy metal part you found on a floor.
                         You jump out the window. There is only sand of an unknown planet around you.
                         Which way to go? West or East?                     
                         """))
            return 'planet'
        
        if action == 'open door':
            print(dedent("""
                  Your ship became to be a mess of stuff, so that it's even hard to come through it.
                  You managed to come to the exit door, but it seems to be locked.
                  You see sparkes jumping out of a control panel. You open it with a knife, that was in your pocket.
                  Wires seems to be demaged, you need to reconnect them. Choose to right combination of wires:
                  '1' stands for red, '2' stands for green and '3' stands for blue.
                  """))
            
            right_combination = f"{randint(1,3)}{randint(1,3)}{randint(1,3)}"
            combination = input('Connect the wires in order> ')
            guesses = 0

            while combination != right_combination and guesses < 3:
                print("SCHWUNK!")
                guesses += 1
                combination = input('Connect the wires in order> ')
            if combination == right_combination:
                print(dedent("""
                             After connecting the last wire you here the 'click' sound and the exit door opens.
                             Dry air hits your face. You jump out on sand and see an empty desert of an unknown planet.
                             Which way to go? West or East? 
                             """))
                return 'planet' 
            else:
                print(dedent("""
                            You've tryed it again and suddenly you get the electricity shock from the wires.
                            You fell on the floor and die.
                            """))
            return 'death'

class Death(Scene):

    death_cases = [
            "You stept on the wet floor and found out it was acid, you die here",
            "You died. You kinds suck at this",
            "Your Mom called you home, so you just left",
            "Looooser",
            "You better call your friends next time. You suck",
            "You're worse than your Dad's jokes"
        ]

    def enter(self):
        print(Death.death_cases[randint(0, len(self.death_cases)-1)])
        exit(1)        

class Planet(Scene):
    def enter(self):
        print(dedent("""
                    You need to pick the direction, where to go:
                    """))
        
        direction = input('> ')

        if direction == "west":
            return 'monsters'
        
        elif direction == "east":
            return 'death'
        else:
            print("You have to make a choice!")
            return 'planet'

class Monsters(Scene):
    def enter(self):
        print(dedent("""
                        You went in the direction of west. You went many miles before you found out, that you beeng hunted.
                        During the night you started a campfire and found out that local monsters already came too close to you.
                        What would you do: 'Run', 'Fight' or 'Pet them'?
                        """))
        decision = input('> ')

        if decision == 'run':
            print("Congratulations. You've been chased and they got you. You became a dinner for local animals")

        elif decision == 'fight':
            print(dedent("""
                         You tryed your best to hit any of them with your pocket knife, but it's not a good weapod against these scopions-look-like animals.
                         After another attempt you got one of them, then another one and finally the third one.
                         You are exhausted and feel a releaf, but suddenly you noticed, that you were hit and been poisoned.
                         You need to find some help or to come back to your ship. What do you choose?
                         """))
            decision = input('> ')

            if decision == 'help':
                print("That's the wise decision. So you keep heading west")
                return 'base'
            
            elif decision == 'back':
                print("You crawled for a day, maybe two, but the poison got you. You died in the desert")
                return 'death'
        elif decision == 'pet':
            print(dedent("""
                        You've noticed, that this creatures weren't that angry as you thought.
                        You decided to pet one of them and it reacted pretty friendly.
                        You feed them from your dryed food from hand, they surrounded you and you slept till the morning.
                        In the morning you hopped on one off them and they brought you to the local market.
                        You talked to the local merchant ant explained him the situation. He gave you credit for some spare parts for your ship.
                        You brought them back to your ship, fixed it and started the engine. It worked! You're heading home now.
                        Good job, you won!
                        """))
            return 'finished'
        else:
            print("Dude, you have to decide something!")
            return 'monsters'

class Base(Scene):
    def enter(self):
        print(dedent("""
                     You crawled to the mountains. It took a day, but you managed,
                     You see footprints on the ground. There must be people or even a base!
                     You found help, spend a week healing your wound.
                     Local people taught you how to speak their language, gave you provision and a ship.
                     You came back home, congratulation.
                     """))
        exit(0)

class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return 'finished'
    
class Map(object):

    scenes = {
        'spaceship': Spaceship(),
        'planet': Planet(),
        'monsters': Monsters(),
        'base': Base(),
        'death': Death(),
        'finished': Finished(),
    }
      
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)
      
a_map = Map('spaceship')
a_game = Engine(a_map)
a_game.play()