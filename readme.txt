this readme is to log my thought process

The idea behind this project is to build tekken_rps again using oop


Want to add option to choose character, play as dj or zaf

try to associate a player variable to relevant dict in movelist.py
try using a loop to unpack dict into contructor and automate instantiating move objects
maybe need empty list for loop to save move objects into
    honestly might just hardcode data for now and revisit this idea later

try to make game an object with functions that increment/reaasign values to track score stats
frame advantage will need to be updated a lot
could probably do a health bar here too

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