from sys import exit
from random import randint

class Choice(object):
    def __init__(self, keyword, description, resulttext, result):
        self.keyword = keyword
        self.description = description
        self.resulttext = resulttext
        self.result = result

    def choose(self):
        print(self.resulttext)
        return self.result


class Menu(object):
    def __init__(self, options):
        self.option_menu = {}
        for option in options:
            self.option_menu[option.keyword] = option

    def prompt(self):
        for keyword, option in self.option_menu.items():
            print keyword, ':', option.description

        acceptable = self.option_menu.keys()
        choice = None
        while choice is None:
            choice = raw_input()
            if choice not in acceptable:
                print "Sorry, try again."
                choice = None
        chosen = self.option_menu[choice]
        print chosen.resulttext
        return chosen.result




class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
        self.deathcounter = 0

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('quit')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            if next_scene_name == "death":
                self.deathcounter += 1
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()
        print "You died", self.deathcounter, "times."   
        raw_input("Press enter to continue.")

class Death(Scene):
    quips = [
        "You died.  You kinda suck at this.",
        "You died. Your mom would be proud...if she were smarter.",
        "You died, you are such a loser.",
        "You died. I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]

        action = raw_input("Try again? Press Y or N ")

        if action in ["Y", "y"]:
            print "You have just been gifted another life!"
            return 'door'

        if action in ["N", "n"]:
            print "Oh, that's too bad...loser."
            return 'quit'

        else:
            print "Sorry! That's not a valid option."
            return 'death'

class Quit(Scene):
    def enter(self):
        pass
        


# Diana’s

class Door(Scene):
    def enter(self):
        print "This is a love story..."
        print " A lovely young princess named Leila fell in love with a dashing young dumbass named Valium."
        print " They met one balmy night in a magical land aptly named The Good Night,"
        print " They moved in together six months later and adopted a baby dragon Pyro."
        print " The good knight Valium has, as of last night, gotten himself in a bit of a jam,"
        print " getting kidnapped by a bunch of bandits, and now Leila has to rescue him one and only true love."
        print " Leila has to go open the door and start her quest. She walks to the door."
        print " Leila (you) stands in front of the door"
        print " Leila can:"

        push = Choice('push', 'Try to push the door.', 'Great! You did it! Go on and get to rescue that lovely idiot.','forest')
        pull = Choice('pull', 'Try to pull the door.', 'The door handle breaks because you pulled it too hard.\n You fall and break your head. You are dead!','death') 

        action = Menu([push, pull]).prompt()
        return action
 


#Nicoles

class Forest(Scene):
 
    def enter(self):

        print "You are in the forest"
        print "Leila needs to find the bandits tower."
        print "Leila can get directions if she..."
        print "1 asks a swallow"
        print "2 asks a deer"
        print "3 asks a rabbit"

        guess = raw_input("> ")
        
        if guess == "1":
            print "Wrong choice! The swallow dies."
            return 'death'
        elif guess == "2":
            print "Wrong answer! The deer runs off."
            return 'death'
        elif guess == "3":
            print "Great job! That rabbit's dynamite...You really should get yourself a bunny."
            print "The rabbit takes Leila and Pyro down a rabbit hole to the bandits tower."
            return 'banditstower'
        else:
                print "Sorry! That's not a valid option."
                return 'forest'
    
     

class BanditsTower(Scene):
    def enter(self):
            print "Leila, Valium and Pyro need to escape the bandits."
            print "Leila can:"
            print "1 Get Pyro to throw fireballs at them"
            print "2 Push them one by one into the moat"
            print "3 Surrender"
             
            action = raw_input("> ")
             
            if action == "1":
                print "Pyro sets Valium on fire by sneezing."
                pause = raw_input()
                return 'death'
                        
             
            elif action == "2":
                print "They all fall into the moat around bandit's tower while fighting"
                return 'moat'
                        

            elif action == "3":
                print "They all die since he forgot his Allegra"
                return 'death'
                        
            else:
                print "Sorry! That's not a valid option."
                return 'banditstower'


class Moat(Scene):

    def enter(self):
        
        print "Leila, Valium, and Pyro need to escape the narwhals in the moat."
        print "Leila's options are:" 
        print "1 get Pyro to throw fireballs at them"
        print "2 swim faster than the narwals"
        print "3 play dead"
        action = raw_input("> " )
        if action == "1":
            print "Pyro's fire is doused under water"
            return 'death'
        elif action == "2":
            print "The narwhals catch them"
            return 'death'
        elif action == "3":
            print "The narwhals swim past them and the 3 escape."
            return 'castle'
        else:
                print "Sorry! That's not a valid option."
                return 'moat'


#Nicoles

class Castle(Scene):
 
    def enter(self):

        print "Leila, Valium and Pyro are back in the castle."
        print "They need to get ready for their /'Heroes Welcome' but Valium is asleep. Leila can: "
        print "1 kiss him"
        print "2 asks her matron to wake him up"
        print "3 get Pyro to wake him up"
        print "Don't you just hate it when you are in bed with three different women" 
        print "and the least attractive one of them says: 'Save it for me.'Jim Carrey"
        action = raw_input("> ")
        
        if action == "1":
            print "She has to do over her lipstick and is late to the party."
            return 'death'
        elif action == "2":
            print "Valium wakes up."
            return 'finished'
        elif action == "3":
            print "Pyro sets Valium on fire."
            return 'death'
        else:
            print "Sorry! That's not a valid option."
            return 'castle'

class Finished(Scene):
    def enter(self):
        print "You won! Good job."

        action = raw_input("Play again? Press Y or N")

        if action == "Y":
            print "You have just been gifted another life!"
            return 'door'

        if action == "N":
            print "Oh, that's too bad...loser."
            return 'quit'

        else:
            print "Sorry! That's not a valid option."
            return 'finished'


class Map(object):
    scenes = {
        'door': Door(),
        'forest': Forest(),
        'banditstower': BanditsTower(),
        'moat': Moat(),
        'castle': Castle(),
        'death': Death(),
        'finished': Finished(),
        'quit': Quit(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('door')
a_game = Engine(a_map)
a_game.play()
