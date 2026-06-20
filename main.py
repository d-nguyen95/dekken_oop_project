import movelist
import random


class Game:
    data = {'frame_advantage' : 0,
            'set_wins' : 0,
            'set_losses' : 0,
            'game_wins' : 0,
            'game_losses' : 0,
            'round_wins' : 0,
            'round_win' : 0}


    def __init__(self):

    def set_win():
        game.data['set_win'] += 1



class Move:
    def __init__(self, name, hitbox, damage, startup, onblock, onhit):
        self.name = name
        self.hitbox = hitbox
        self.damage = damage
        self.startup = startup
        self.onblock = onblock
        self.onhit = onhit


def play_dekken():


def dekken():
    player = ""
    choice = int(input("Choose your character: \n1) Devil Jin\n" \
    "2) Zafina\n" \
    ">: "))
    if choice == 1:
        player = "devil_jin"
    else:
        player = "zafina"


while True:
    if __name__ == "__main__":
        dekken()