class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        pass

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
        print("You are in the Central Corridor and see Gothon coming towards you")
        print("There is no way out except a tiny hole on the wall. Oh, it's a ventilation!")

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()