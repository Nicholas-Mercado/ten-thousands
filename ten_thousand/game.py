
import sys
if __name__ == '__main__':
    from game_logic import GameLogic
    from banker import Banker
    
else:
    import sys
    from ten_thousand.game_logic import GameLogic
    from ten_thousand.banker import Banker


class Game:

    def __init__(self):
        self.banker = Banker()
        self.round_counter = 0
        self.format_dice_roll  = ''
        self.num_of_dice = 6
        self.user_input = ''
        self.dice_roll = 0
        
    def greet_user(self):
        """ Start game msg"""
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        self.user_input = input("> ")
        if self.user_input == 'n':
            print("OK. Maybe another time") 
            sys.exit()
        
    def quit_game_check(self):
        if self.user_input == 'q':
                print(f'Thanks for playing. You earned {self.banker.balance} points')
                sys.exit() 
                
    def handle_cheater(self):
        print("Cheater!!! Or possibly made a typo...")
        print(self.format_dice_roll)
        print("Enter dice to keep, or (q)uit:")
                
        self.user_input = input('> ').lower().replace(' ','')
                
        self.quit_game_check()
                
        self.dice_kepted = tuple(int(x) for x in self.user_input)
        
    
    def roll_again_check(self):
        if self.user_input == 'r':
            print(f"Rolling {self.num_of_dice} dice...")
            self.dice_roll = self.roller(self.num_of_dice)
            
            self.format_dice_roll = f'*** {self.format_rolls(self.dice_roll)}***'
            print(self.format_dice_roll)
            
            print("Enter dice to keep, or (q)uit:")
            self.user_input = input('> ').lower().replace(' ','')
            
            return self.user_input
        
    def bank_check(self):
                
                if self.user_input == 'b':
                    print(f'You banked {self.banker.shelved} points in round {self.round_counter}')
                    self.banker.bank()
                    print(f'Total score is {self.banker.balance} points')
                    
                
    def format_rolls(self, dice_roll):
        string = ''
        for number in dice_roll:
            string += f'{number} '
        return string

    def is_kepted_dice_valid(self):
        test_dice_roll = [x for x in self.dice_roll]
        check_list = []
        for num in self.dice_kepted:
            is_in_list = False
            for position in test_dice_roll:
                if num == position:
                    is_in_list = True
                    index = test_dice_roll.index(position)
                    
                    test_dice_roll[index] = 0
                    break
            check_list.append(is_in_list)
        return all(check_list)
            
    def play(self, roller=GameLogic.roll_dice):
        """ The game"""
        self.greet_user()
        self.roller = roller
 
         
        
        while self.banker.balance <= 10000:
            self.round_counter +=1
            self.num_of_dice = 6
            
            print(f'Starting round {self.round_counter}\nRolling 6 dice...')
            self.dice_roll = roller(self.num_of_dice)
            self.format_dice_roll = f'*** {self.format_rolls(self.dice_roll)}***'
            print(self.format_dice_roll)
            print("Enter dice to keep, or (q)uit:")
            
            self.user_input = input('> ').lower().replace(' ','')

            self.quit_game_check()
           
            self.dice_kepted = tuple(int(x) for x in self.user_input)
            
            while not self.is_kepted_dice_valid():
                self.handle_cheater()
            
                           
            self.banker.shelf(GameLogic.calculate_score(self.dice_kepted))
            
            self.num_of_dice -= len(self.user_input)
                                                        
            print(f'You have {self.banker.shelved} unbanked points and {self.num_of_dice} dice remaining\n(r)oll again, (b)ank your points or (q)uit:')
            self.user_input = input('> ').lower().replace(' ','')
           
            
            self.roll_again_check()
            self.bank_check()
            self.quit_game_check()
            
            

            

    
      
    
if __name__ == '__main__':
    game = Game()
    banker = Banker()
    game.play()


