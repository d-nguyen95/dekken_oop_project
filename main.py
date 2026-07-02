import random
import sys
from modules import Move


def character_choice():
    '''this function determines character choice'''
    player = ""
    opp = ""
    while True:
        choice = int(input(
        "Choose your character:\n \n1) Devil Jin \n2) Zafina\n \n>>> "))
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
            play = str(input("Rematch? y/n?: "))
            if play == "y":
                dekken()
            elif play == "n":
                print("GG")
                sys.exit()
            else:
                print("Enter 'y' or 'n'")
                continue


def prepare_game():
        from modules import Game
        '''instantiate game object'''
        current_game = Game()
        return current_game


def load_dj():
        from modules import Move
    #what i want here is to loop through move dictionary taking each key to be the name of the variable that holds each object, unpack the dictionary into the Move() constructor with star notation and add to the empty list. ideally the return value will be a list of djmove objects that will be easy to access later. i will hardcode each object and manually add to a list for now.
    # djmoves = []
    # for move in movelist.devil_jin:
    #     move = movelist.devil_jin[move]
    #     move = Move(*movelist.devil_jin[move])
    #     djmoves.append(move)
        '''instantiate dj move objects'''
        ewgf = Move("Electric Wind God Fist", "high", 23, 13, 5, 39)
        b4 = Move("Steel Pedal", "mid,", 20, 17, -8, 6)
        db2 = Move("Malicious Mace", "low", 15, 21, -13, 3)
        ws2 = Move("Alaya", "mid", 20, 14, -12, 59)
        b12 = Move("Aratama Strike", "mid", 21, 20, 3, 7)
        dj = [ewgf, b4, db2, ws2, b12]

        return dj
    

def load_zaf():
        '''instantiate zaf move objects'''
        ff4 = Move("Roundhouse Kick", "mid", 16, 17, -8, 6)
        df2 = Move("Lamashtu Claw", "mid", 13, 16, -12, 22)
        d3 = Move("Earwig Pincer", "low", 14, 22, -15, 5)
        ws2 = Move("Rising Claw", "mid", 20, 18, -14, 28)
        f3 = Move("Scarecrow Sidekick", "high", 28, 17, 3, 14)
        zaf = [ff4, df2, d3, ws2, f3]

        return zaf


def fight(player, opp, game):
    '''this function handles combat'''


    def get_rand_move(n, move_list):
        '''this function gets n amount of random moves in provided list with no repeats. Nested because only need it here'''
        if n == 1:
            return move_list[random.randint(0, len(move_list)) - 1]
        else:
            movelist_copy = list(move_list)
            random_moves = []
            for _ in range(n):
                for _ in movelist_copy:
                    current_rand_num = random.randint(0, len(movelist_copy))
                    random_moves.append(movelist_copy[current_rand_num - 1])
                    movelist_copy.remove(movelist_copy[current_rand_num - 1])
            return random_moves
        
   
    while game._player_health > 0 or game._opp_health > 0:
        if game._opp_health <= 0:
            game.round_win()
        elif game._player_health <= 0:
            game.round_loss()
        else:
            if opp[0].name == "Roundhouse Kick":
                opp_name = "Zafina"
            else:
                opp_name = "Devil Jin"

            opp_move_current = get_rand_move(1, opp)
            print(f"\n{opp_name} is going to use {opp_move_current.name}\n")
            move_choice = get_rand_move(3, player)
            player_move_current = int(input(f"Response:\n \n1) {move_choice[0].name} \n2) {move_choice[1].name} \n3) {move_choice[2].name} \n4) Block \n5) Quit\n \n>>> "))
            match player_move_current:
                case 1:
                    game.clash(move_choice[0], opp_move_current)
                case 2:
                    game.clash(move_choice[1], opp_move_current)
                case 3:
                    game.clash(move_choice[2], opp_move_current)
                case 4:
                    game._frame_advantage = abs(opp_move_current.onblock)
                    game._player_health -= 5
                    game.game_state()
                case 5:
                    print("gg")
                    sys.exit()
                case _:
                    print("enter 1, 2, 3, 4 or 5")


def dekken():
    player, opp = character_choice()
    game = prepare_game()
    if player == "dj":
        player = load_dj()
        opp = load_zaf()
    else:
        player = load_zaf()
        opp = load_dj()
    
    fight(player, opp, game)


if __name__ == "__main__":
    dekken()