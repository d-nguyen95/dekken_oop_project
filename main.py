import movelist
import random
import sys


class Game:
    def __init__(self, frame_advantage=0, player_health=100, opp_health=100, set_wins=0, set_losses=0, game_wins=0,game_losses=0, round_wins=0, round_losses=0):
        self.frame_advantage = frame_advantage
        self.player_health = player_health
        self.opp_health = opp_health
        self.set_wins = set_wins
        self.set_losses = set_losses
        self.game_wins = game_wins
        self.game_losses = game_losses
        self.round_wins = round_wins
        self.round_losses = round_losses


    def round_win(self):
        self.round_wins += 1
        if self.round_wins == 3:
            self.round_wins = 0
            self.round_losses = 0
            self.game_wins += 1
            if self.game_wins == 2:
                self.game_wins = 0
                self.game_losses = 0
                self.set_wins += 1
                if self.set_wins == 2:
                    print(f"You win! Final score {self.set_wins}:{self.set_losses}")
                    restart()
        print(f"Rounds: {self.round_wins}:{self.round_losses}\n Games: {self.game_wins}:{self.game_losses}\n Sets: {self.set_wins}:{self.set_losses}\n")


    def round_loss(self):
        self.round_losses += 1
        if self.round_losses == 3:
            self.round_wins = 0
            self.round_losses = 0
            self.game_losses += 1
            if self.game_losses == 2:
                self.game_wins = 0
                self.game_losses = 0
                self.set_losses += 1
                if self.set_losses == 2:
                    print(f"You lose! Final Score {self.set_wins}:{self.set_losses}\n")
                    restart()
        print(f"Rounds: {self.round_wins}:{self.round_losses}\n Games: {self.game_wins}:{self.game_losses}\n Sets: {self.set_wins}:{self.set_losses}\n")


class Move:
    def __init__(self, name, hitbox, damage, startup, onblock, onhit):
        self.name = name
        self.hitbox = hitbox
        self.damage = damage
        self.startup = startup
        self.onblock = onblock
        self.onhit = onhit


def character_choice():
    player = ""
    opp = ""
    while True:
        choice = int(input("Choose your character: \n1) Devil Jin\n" \
        "2) Zafina\n" \
        ">: \n"))
        if choice == 1:
            player = "dj"
            opp = "zaf"
        elif choice == 2:
            player = "zaf"
            opp = "dj"
        else:
            print("Enter 1 or 2")
            continue

        return player, opp


def restart():
        while True:
            input = str(input("Rematch? y/n?: "))
            if input == "y":
                dekken()
            elif input == "n":
                print("GGEZ")
                sys.exit()
            else:
                print("Enter 'y' or 'n'")
                continue



def play_dekken():
    pass


def dekken():
    player, opp = character_choice()
    play_dekken()
    return dekken()



while True:
    if __name__ == "__main__":
        dekken()