
# Application should simulate rolling between 1 and 6 dice
# call roll_dice
# Application should allow user to set aside dice each roll
# banking method







if __name__ == '__main__':
    from game_logic import GameLogic
    from banker import Banker
    
else:
    from ten_thousand.game_logic import GameLogic
    from ten_thousand.banker import Banker


class Game:

    def __init__(self):
        self.banker = Banker()
        
    def play(self, roller=GameLogic.roll_dice):
        # game opening************************
        print('''Welcome to Ten Thousand
(y)es to play or (n)o to decline''')
        
        round_counter = 0
        
        user_input = input('> ').lower()
        if user_input == 'n':
            print("OK. Maybe another time")  
            return
        # FULL GAME ************************
        while self.banker.balance <= 10000:
            # variables
            num_of_dice = 6
            round_counter +=1
            
            # START ROUNDS **************************************
            print(f'Starting round {round_counter}\nRolling 6 dice...')
            dice_roll = roller(num_of_dice)
            format_dice_roll = f'*** {self.format_rolls(dice_roll)}***'
            print(format_dice_roll)
            print("Enter dice to keep, or (q)uit:")
            user_input = input('> ').lower()
            # print(dice_roll)
            # print(user_input)
            # Quit *************************************************
            if user_input == 'q':
                print(f'Thanks for playing. You earned {self.banker.balance} points')
                return
            # Shelf points *****************************************
            user_input = tuple(int(x) for x in user_input)
            num_of_dice -= len(user_input)
            shelved_points = GameLogic.calculate_score(user_input)
            
            if not self.is_cheater(user_input, dice_roll):
                print("Cheater!!! Or possibly made a typo...")
                print(format_dice_roll)
                print("Enter dice to keep, or (q)uit:")
                user_input = input('> ').lower()
            else:
                self.banker.shelf(shelved_points)
                
                                                            
                print(f'You have {shelved_points} unbanked points and {num_of_dice} dice remaining\n(r)oll again, (b)ank your points or (q)uit:')
                user_input = input('> ').lower()
                
                if user_input == 'r':
                    dice_roll = roller(num_of_dice)
                    format_dice_roll = f'*** {self.format_rolls(dice_roll)}***'
                    print(format_dice_roll)
                if user_input == 'b':
                    self.banker.bank()
                if user_input == 'q':
                    print(f'Thanks for playing. You earned {self.banker.balance} points')
                    return    
                
            print(f'You banked {shelved_points} points in round {round_counter}\nTotal score is {self.banker.balance} points')

            

    def format_rolls(self, dice_roll):
        string = ''
        for number in dice_roll:
            string += f'{number} '
        return string

    def is_cheater(self, user_input , dice_roll ):
        test_dice_roll = dice_roll
        check_list = []
        
        for num in user_input:
            is_in_list = False
            for position in test_dice_roll:
                if num == position:
                    is_in_list = True
                    index = test_dice_roll.index(position)
                    
                    test_dice_roll[index] = 0
                    print(test_dice_roll)
                    break
            check_list.append(is_in_list)
            
        print(check_list)
        return all(check_list) 
      
if __name__ == '__main__':
    game = Game()
    banker = Banker()
    game.play()


