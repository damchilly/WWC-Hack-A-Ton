#!/usr/bin/env python
from sys import exit
from random import randint


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

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor,
        'laser_weapon_armory': LaserWeaponArmory,
        # ...
        'finished': Finished,
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_map)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


class Scene(object):
    def enter(self):
        print "This scene is not yet implemented."

##### ADD SCENE CLASSES BELOW ######


##### END OF SCENE CLASSES ######

if __name__ == '__main__':
    game = Engine(Map('central_corridor'))
    game.play()
