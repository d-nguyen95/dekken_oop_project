class Game:
    '''this class will handle tracking of gamestate'''
    def __init__(
            self, 
            frame_advantage=0, 
            player_health=100, 
            opp_health=100, 
            set_wins=0, 
            set_losses=0, 
            game_wins=0,
            game_losses=0, 
            round_wins=0, 
            round_losses=0
            ):
        
        self._frame_advantage = frame_advantage
        self._player_health = player_health
        self._opp_health = opp_health
        self._set_wins = set_wins
        self._set_losses = set_losses
        self._game_wins = game_wins
        self._game_losses = game_losses
        self._round_wins = round_wins
        self._round_losses = round_losses
 
    def round_stats(self):
        print(f'Rounds {self._round_wins}:{self._round_losses}')


    def game_stats(self):
        print(f'Games {self._game_wins}:{self._game_losses}')
           
           
    def set_stats(self):
        print(f'Sets {self._set_wins}:{self._set_losses}')


    def game_state(self):
        print(f"\nFrame Advantage: {self._frame_advantage} \nYou: {self._player_health}hp \nOpp: {self._opp_health}hp")


    def clash(self, playermove, oppmove):
        '''this function handles damage calculation'''
        if playermove.startup - self._frame_advantage < oppmove.startup + self._frame_advantage:
            self._opp_health -= playermove.damage
            self._frame_advantage = playermove.onhit
            self.game_state()
        elif playermove.startup - self._frame_advantage > oppmove.startup + self._frame_advantage:
            self._player_health -= oppmove.damage
            self._frame_advantage = abs(oppmove.onhit)
            self.game_state()
        else:
            self._player_health -= oppmove.damage
            self._opp_health -= playermove.damage
            self._frame_advantage = 0
            self.game_state()


    def reset_rounds(self):
        self._round_wins = 0
        self._round_losses = 0
        self._player_health = 100
        self._opp_health = 100
        self._frame_advantage = 0

        
    def reset_games(self):
        self._game_wins = 0
        self._game_losses = 0


    def round_win(self):
        '''this function increments round/game/set wins'''
        self._round_wins += 1
        self._player_health = 100
        self._opp_health = 100
        self._frame_advantage = 0
        self.round_stats()
        if self._round_wins == 3:
            self._game_wins += 1
            self.reset_rounds()
            self.game_stats()
            if self._game_wins == 2:
                self._set_wins += 1
                self.reset_rounds()
                self.reset_games()
                self.set_stats()
                
    

    def round_loss(self):
        '''this function increments round/game/set losses'''
        self._round_losses += 1
        self._player_health = 100
        self._opp_health = 100
        self._frame_advantage = 0
        self.round_stats()
        if self._round_losses == 3:
            self._round_wins = 0
            self._round_losses = 0
            self._game_losses += 1
            self.reset_rounds()
            self.game_stats()
            if self._game_losses == 2:
                self._game_wins = 0
                self._game_losses = 0
                self._set_losses += 1
                self.reset_rounds()
                self.reset_games()
                self.set_stats()


    def game_over(self):
        if self._set_losses == 2:
            print(f"You lose! Final Score {self._set_wins}:{self._set_losses}\n")
            return self._set_losses == 2
        elif self._set_wins == 2:
            print(f"You win! Final score {self._set_wins}:{self._set_losses}\n")
            return self._set_wins == 2
        else:
            return False



class Move:
    '''this class will form the objects that hold relevent battle data'''
    def __init__(self, name, hitbox, damage, startup, onblock, onhit):
        self.name = name
        self.hitbox = hitbox
        self.damage = damage
        self.startup = startup
        self.onblock = onblock
        self.onhit = onhit


    def __str__(self, stat):
        print(f"self.{stat}")
    