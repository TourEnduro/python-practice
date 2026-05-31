import pytest
from gothonweb.planisphere import Room, load_room, START, generic_death, laser_weapon_armory, the_bridge, escape_pod, the_end_winner, the_end_loser


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    assert gold.name == "GoldRoom"
    assert gold.paths == {}

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert center.go('north') == north
    assert center.go('south') == south

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert start.go('west') == west
    assert start.go('west').go('east') == start
    assert start.go('down').go('up') == start

def test_gothon_game_map():
    start_room = load_room(START)
    assert start_room.go('shoot!') == generic_death
    assert start_room.go('dodge!') == generic_death

    room = start_room.go('tell a joke')
    assert room == laser_weapon_armory

def test_laser_weapon_armory():
    assert laser_weapon_armory.go('0123') == the_bridge
    assert laser_weapon_armory.go('9999') == generic_death

def test_the_bridge():
    assert the_bridge.go('throw the bomb') == generic_death
    assert the_bridge.go('slowly place the bomb') == escape_pod

def test_escape_pod():
    assert escape_pod.go('2') == the_end_winner
    assert escape_pod.go('5') == the_end_loser