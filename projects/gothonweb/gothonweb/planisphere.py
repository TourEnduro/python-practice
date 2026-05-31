class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, self.paths.get('*', None))
    
    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory, put
it in the bridge, and blow the ship up after getting into an escape pod.

You're running down the central corridor to the Weapons Armory when a
Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown
costume flowing around his hate filled body. He's blocking the door to
the Armory and about to pull a weapon to blast you.
""")


laser_weapon_armory = Room("Laser Waepon Armory",
"""
Lucky for you they made you learn Gothon insultsin the academy. You
tell the one Gothon joke you know: Lfkhj fluHEU uahfaufa ifwufhka kwufakwu fefehj.
The Gothon stops, tries not to laugh, then busts out laughing and can't move. While he's
laughing you run up and shoot him square in the head putting him down,
then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan
the room for more Gothons that might be hiding. It's dead
quiet, too quiet. You stand up and run to the far side of
the room and find the neutron bomb in its container.
There's a keypad lock on the box and you need the code to
get the bomb out. If you get the code wrong 10 times then
the lock closes forever and you can't get the bomb. The code
is 3 digits.
""")


the_bridge = Room("The Bridge",
"""
The container clicks on opens, letting the gas out.
You see the neutron bomb and grab it. You run to the engine room
as fast as you can to place the bomb in the right spot.

You burst onto the Bridge with the neutron bomb
under your arm and surprise 5 Gothons who trying to take control
of the ship. They haven't pull their weapons out yet, as they see the active bomb
under your arm and don't want to see it off.
""")


escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm and
Gothons start to sweat. You inch backward to the door, open it,
and then carefully place the bomb on the floor , pointing your blaster
at it. You then jump back through the door, 
punch the close button and blast the lock so the
Gothons can't get out. Now that the bomb in placed you run
to the escape pod to get off this tin can.

You rush through the ship desperately trying to make it to
the escape pod before the whole ship explodes. It seemas
like hardly any Gothons are on the ship, so your run is clear
of interference. You get to the chamber with the escape pods,
and now need to pick one to take. Some of them could be damaged but you
don't have time to look. There's 5 pods which do you take?
""")


the_end_winner = Room("The End",
"""
You jump into pod 2 and hit the eject button.
The pod easily slides out into space heading to the planet
below. A it flies to the planet, you look back and see your ship
implode like a bright star, taking out the Gothon ship at the same time.
You won!
""")

the_end_loser = Room("The End",
"""
You jump into a pod and hit the eject button.
the pod escapes out into the void of space, then implodes
as the hull ruptures, cruching you body into
jam jelly.                      
""")

escape_pod.add_paths({
        '2': the_end_winner,
        '*': the_end_loser
})

generic_death = Room("death", "You died.")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0123': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

START = 'central_corridor'

def load_room(name):
    """
    There is a potential security problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(name)

def name_room(room):
    """
    Same possible security problem. Can you trust room?
    What's a better solution than this globals lookup?
    """
    for key, value in globals().items():
        if value == room:
            return key