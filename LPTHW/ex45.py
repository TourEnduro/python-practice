from sys import exit
from random import randint
from textwrap import dedent


class Engine(Object):
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
    def __init__(self):
        print(dedent("""
              You find yourself on the floor of a crashed spaceship.
              You don't remember why are you here and what happend.
              It's quite messy around you. You know that you have to get out to find some help.
              What would you do? ('Give up', 'Break window', 'Open door')
              """))
        action = input('> ')

        if action == 'give up':
            print("Great choice, you starve to death. Congratulations! Game over.")

        

class Planet(Scene):
    def enter(self):
        pass

class Death(Scene):
    def enter(self):
        pass

class Door(Scene):
    def enter(self):
        pass

class Monsters(Scene):
    def enter(self):
        pass

class Base(Scene):
    def enter(self):
        pass

class Scrapmarket(Scene):
    def enter(self):
        pass