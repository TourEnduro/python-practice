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

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""You are in the Central Corridor and see Gothon coming towards you.
                        There is a sign behide Gothon's room saying 'Weapod Armory'.
                        That's where you have to get. What would you do?"""))

        action = input('> ')

        if action == "shoot!":
            print(dedent("""
                         You were trying to hit Gothon with your laser blaster, but he was too fast for you.
                         He came closer and closer to you, dodging from your lasers and when he got closer enough -
                         he made a hit with his claw and chopped your head off
                         """))
            return 'death'
        elif action == 'dodge!':
            print(dedent("""
                        Your body moves faster ther ever, when Gothon's blaster tryes to reach you,
                         you remember your old time learinig kung-fu with the master and it seems like you overcome your abilities,
                         but suddenly you step on the wet floor and you foot slip away, you heat the wall with your head.
                         That give enough time to Gothon to come closer and eat your head.
                         """))
            return 'death'
        elif action == 'tell a joke!':
            print(dedent("""
                        Suddenly you remembered, that you've learned a few words on Gothon's mother lenguage,
                        you tell him a joke, as you know: Lfkhj fluHEU uahfaufa ifwufhka kwufakwu fefehj. It worked out,
                        he starts to lough and steps back for a while, which gives you a few second to shoot him with a blaster right in his head.
                        You jump over his body and find the door to Weapon Armory room.
                         """))
            return 'laser_weapon _armory'
        
        else:
            print("DOES NOT COMPUTE!")
            return 'central corridor'
        
class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
                    You do a dive roll into the Weapon Armory, crouch and scan
                     the room for more Gothons that might be hiding. It's dead
                     quiet, too quiet. You stand up and run to the far side of
                     the room and find the neutron bomb in its container.
                     There's a keypad lock on the box and you need the code to
                     get the bomb out. If you get the code wrong 10 times then
                     the lock closes forever and you can't get the bomb. The code
                     is 3 digits.
                     """))
        code == f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input('[keypad]> ')
        guesses = 0

        while guess != code and guess < 10:
            print("SCHWUNK!")
            guess += 1
            guess = input('[keypad]> ')
        if guess == code:
            print(dedent("""
                    The container clicks on opens, letting the gas out.
                         You see the neutron bomb and grab it. You run to the engine room
                         as fast as you can to place the bomb in the right spot.
                    """)) 
        else:
            print(dedent("""
                    You tipped the possible code the last time and you hear the sound of
                    mechanism that seals the conteiner forever. You decide to sit here and
                    finally Gothons decide to blow up the ship from their own ship. You die,
                    """))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
                    You burst onto the Bridge with the neutron bomb
                     under your arm and surprise 5 Gothons who trying to take control
                     of the ship. They haven't pull their weapons out yet, as they see the active bomb
                     under your arm and don't want to see it off.
                    """))
        action = input('')

        if action == "throw the bomb":
            print(dedent("""
                    In a panic you throw a bomb right into the group of Gothons and
                    run away from them, but the shoot you in the back killing you. You die seeing the other Gothon
                    trying to disarm the bomb, but he activates it and blows up the ship.
                    """))
            return 'death'
        elif action == "slowly place the bomb":
            print(dedent("""
                    You point your blaster at the bomb under your arm and
                    Gothons start to sweat. You inch backward to the door, open it,
                    and then carefully place the bomb on the floor , pointing your blaster
                    at it. You then jump back through the door, 
                    punch the close button and blast the lock so the
                    Gothons can't get out. Now that the bomb in placed you run
                    to the escape pod to get off this tin can.
                    """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
                    You rush through the ship desperately trying to make it to
                     the escape pod before the whole ship explodes. It seemas
                     like hardly any Gothons are on the ship, so your run is clear
                     of interference. You get to the chamber with the escape pods,
                     and now need to pick one to take. Some of them could be damaged but you
                     don't have time to look. There's 5 pods which do you take?
                    """))
        good_pod = randint(1,5)
        guess = input('[pod #]> ')

        if int(guess) != good_pod:
            print(dedent("""
                    You jump into a pod {guess} and hit the eject button.
                         the pod escapes out into the void of space, then implodes
                         as the hull ruptures, cruching you body into
                         jam jelly.
                    """))
            return 'death'
        else:
            print(dedent("""
                    You jump into pod {guess} and hit the eject button.
                         The pod easily slides out into space heading to the planet
                         below. A it flies to the planet, you look back and see your ship
                         implode like a bright star, taking out the Gothon ship at the same time.
                         You won!
                    """))
            return 'finished'
        
class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapod_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()