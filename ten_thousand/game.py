
# Application should simulate rolling between 1 and 6 dice
# call roll_dice
# Application should allow user to set aside dice each roll
# banking method



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
        
    def greet_user(self):
        """ Start game msg"""
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        user_input = input("> ")
        if user_input == 'n':
            print("OK. Maybe another time") 
            sys.exit()
        
    def quit_game_check(self,user_input):
        if user_input == 'q':
                print(f'Thanks for playing. You earned {self.banker.balance} points')
                sys.exit() 
                
    def handle_cheater(self):
        print("Cheater!!! Or possibly made a typo...")
        print(self.format_dice_roll)
        print("Enter dice to keep, or (q)uit:")
                
        user_input = input('> ').lower().replace(' ','')
                
        self.quit_game_check(user_input)
                
        user_input = tuple(int(x) for x in user_input)
        
        return user_input
    
    def roll_again_check(self, user_input):
        if user_input == 'r':
            print(f"Rolling {self.num_of_dice} dice...")
            dice_roll = self.roller(self.num_of_dice)
            
            self.format_dice_roll = f'*** {self.format_rolls(dice_roll)}***'
            print(self.format_dice_roll)
            
            print("Enter dice to keep, or (q)uit:")
            user_input = input('> ').lower().replace(' ','')
            
            return user_input
                
    def play(self, roller=GameLogic.roll_dice):
        """ The game"""
        self.greet_user()
        self.roller = roller
    #     self.start_game()
    #     self.starting_round()
    #     self.roll_dice()
        
    
            
    # def starting_round(self):
    #      print(f'Starting round 1\nRolling 6 dice...')
         
    # def roll_dice(self):
    #     num_of_dice = 6
    #     dice_roll = self.roller(num_of_dice)
    #     format_dice_roll = f'*** {self.format_rolls(dice_roll)}***'
    #     print(format_dice_roll)
         
         
         
        
        
    
        
        while self.banker.balance <= 10000:
            
            self.round_counter +=1
            

            print(f'Starting round {self.round_counter}\nRolling 6 dice...')
            
            dice_roll = roller(self.num_of_dice)
            self.format_dice_roll = f'*** {self.format_rolls(dice_roll)}***'
            print(self.format_dice_roll)


            print("Enter dice to keep, or (q)uit:")
            user_input = input('> ').lower().replace(' ','')

            
            self.quit_game_check(user_input)
           
            user_input = tuple(int(x) for x in user_input)
            
            while not self.is_valid(user_input, dice_roll):
                user_input = self.handle_cheater()
            
                         
                    
            shelved_points = GameLogic.calculate_score(user_input)
            self.num_of_dice -= len(user_input)
            self.banker.shelf(shelved_points)
                                                        
            print(f'You have {shelved_points} unbanked points and {self.num_of_dice} dice remaining\n(r)oll again, (b)ank your points or (q)uit:')
            user_input = input('> ').lower().replace(' ','')
           

            self.roll_again_check(user_input)
                
                
                # You have 500 unbanked points and 2 dice remaining
                # (r)oll again, (b)ank your points or (q)uit:
                
            if user_input == 'b':
                self.banker.bank()
                
            self.quit_game_check(user_input)
            
            print(f'You banked {shelved_points} points in round {self.round_counter}\nTotal score is {self.banker.balance} points')

            

    def format_rolls(self, dice_roll):
        string = ''
        for number in dice_roll:
            string += f'{number} '
        return string

    def is_valid(self, user_input , dice_roll ):
        test_dice_roll = [x for x in dice_roll]
        # print('dice :', dice_roll )
        check_list = []
        # print(user_input)
        for num in user_input:
            is_in_list = False
            for position in test_dice_roll:
                if num == position:
                    is_in_list = True
                    index = test_dice_roll.index(position)
                    
                    test_dice_roll[index] = 0
                    break
            check_list.append(is_in_list)
        # print('is_cheater called user input', user_input)    
        return all(check_list) 
      
    # def roll_again(self, num_of_dice, roller):
    #     print(f"Rolling {num_of_dice} dice...")
    #     dice_roll = roller(num_of_dice)
    #     format_dice_roll = f'*** {self.format_rolls(dice_roll)}***'
    #     print(format_dice_roll)
    #     print("Enter dice to keep, or (q)uit:")
    #     user_input = input('> ').lower().replace(' ','')
                
if __name__ == '__main__':
    game = Game()
    banker = Banker()
    game.play()


