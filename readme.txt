this readme is to log my thought process

The idea behind this project is to build tekken_rps again using oop to learn and practice oop concepts
such as classes, objects, encapsulation, abstraction, inheritance etc.

Dekken will be a command line game emulating a 2d fighter


Want to add option to choose character, play as dj or zaf


            try to associate a player variable to relevant dict in movelist.py
            try using a loop to unpack dict into contructor and automate instantiating move objects
            maybe need empty list for loop to save move objects into
                # honestly might just hardcode data for now and revisit this idea later, something about bunch/munch module, or namedtuples to solve unpacking dict problem, but tuples are immutable so probably cant use namedtuple. im also using nested dict which makes it slightly more complex


try to make game an object with functions that increment/reaasign values to track score stats
frame advantage will need to be updated a lot
could probably do a health bar here too
damage calc will probs be Game class method which takes self, player_move and opp_move as args

round order:
-show opponent random move choice
-give player random choice of 3 moves
-get player choice
-calculate damage
-repeat until health <= 0
-next round

-round win/loss + 1
-first to 3 rounds
-game win/loss + 1, reset round wins to 0
-first to 2 games
-set win/loss + 1, reset game wins to 0

combat logic

maybe define fuctions in move class like

def damage_calc(self, opp_move)
    if self.startupframes - frame advantage > opp_move.startupframes + frame advantage
        opponent health bar -= self.damage
        frame advantage = self.onhit
    else:
        player health bar -= opp_move.damage
        frameadvantage = opp_move.onhit

or make this a Game.method like i mentioned earlier

visualise the steps (pseudo-code i believe):
    start game, (import random most likely)

    load a whiteboard to keep score (def Game class and construct game object)

    load a whiteboard with dj and zaf moves (def dj/zaf parent class and def move subclass, contruct move objects, store dj move objects in one list and zaf move objects in another)

    player chooses character (get input, 1 = dj, 2 = zaf, if input == 1: player = dj, opp = zaf, else: player = zaf, opp = dj)

        may need a function to return 2 values: "player, opponent" and save to "player, opponent" variables

        def choose_character()
            return player, opp

        player, opp = choose_character()
    
    round starts (if player is dj, player uses dj move object list and opp uses zaf move object list - and vice versa)

    show opp move choice (get a random opp move from the list and store it in opp_move variable, print it)

        (make func to get an amount of random moves and return them, save that to variable/s)

        random move function will take 2 args: 'character' and 'number of move's=1 (set default entry to 1)

        this will take a copy (look into deep vs shallow) of dj/zaf move objects list

        iterate over copy_character[list] n amount of times picking a random choice

        since lists are accessed by numerical index, will need a random number between 0 and len(character[list])

        need a copy so we can delete each selection to avoid repeated selections.

        need a dynamic value for list length since it will decrease with each iteration

        will need error checking, will have to enter a value between 1 and max length when calling function, but only i am gonna use it so... should do anyway for practice i guess

        return moves, maybe store return values from each iteration in a list and then return the list
            or, if n = 1, just get a move and return it
            else,
                moves = []
                through error checking n will be 2-5
                iterate over movelist copy n times, append random choice to new list, delete from movelist copy
            
            return moves

        eg: 
        player = dj
        opp = zaf
        oppmove1 = random_move(opp)   #this should get a random zaf move
        playermoves = [] #maybe this line is unnecessary
        playermoves = random_move(player, 3)   #hopefully this gets 3 different dj moves, syntax most definitely might be maybe wrong here
        hoping to access player move attributes like so:
            playermoves[1].startup
            playermoves[2].damage
            etc...

        




