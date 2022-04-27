# Application should implement all features from previous version
# import modules prev 
# Application should simulate rolling between 1 and 6 dice
# call roll_dice
# Application should allow user to set aside dice each roll
# banking method
# Application should allow “banking” current score or rolling again.
# access banker.py
# access roll_dice.py
# Application should keep track of total score
# total score accumulator 
# Application should keep track of current round
# Variable to keep track of round Hey you hit ten thousand
# Application should have automated tests to ensure proper operation


# from game_logic import GameLogic
from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:

    def __init__(self):
        self.banker = Banker()
        
    def play(self, roller=GameLogic.roll_dice):
        
        print('''Welcome to Ten Thousand
(y)es to play or (n)o to decline''')
        num_of_dice = 6
        user_input = input('> ').lower()
        if user_input == 'n':
            print("OK. Maybe another time")
        else:
            print('Starting round 1\nRolling 6 dice...')
            current_bank = 0
            current_shelf = 0
            dice_roll = roller(num_of_dice)
            format_dice_roll = f'*** {self.format_rolls(dice_roll)}***'
            print(format_dice_roll)
            print("Enter dice to keep, or (q)uit:")
            user_input = input('> ').lower()
            if user_input == 'q':
                print(f'Thanks for playing. You earned 0 points')
                return
            
            user_input = tuple(int(x) for x in user_input)
            shelved_points = GameLogic.calculate_score(user_input)
            self.banker.shelf(shelved_points)
            
            print(f'You have {shelved_points} unbanked points and 5 dice remaining\n(r)oll again, (b)ank your points or (q)uit:')
            
            user_input = input('> ').lower()
            if user_input == 'b':
                self.banker.bank(0, shelved_points)
                
                
            print(f'You banked {self.banker.balance} points in round 1\nTotal score is {self.banker.balance} points\nStarting round 2')

        if user_input == 'q':
            print("Thanks for playing. You earned 0 points")

    def format_rolls(self, dice_roll):
        string = ''
        for number in dice_roll:
            string += f'{number} '
        return string


if __name__ == '__main__':
    game = Game()
    banker = Banker()
    game.play()

# Enter dice to keep, or (q)uit:
# Call banking function for input
# > 5
# call shelf got points unbanked
# create a dice tracker
# print
# You have 50 unbanked points and 5 dice remaining
# (r)oll again, (b)ank your points or (q)uit:
# input for banking
# > b
# call bank
# You banked 50 points in round 1
# creating total score var
# Total score is 50 points
# create round var
# loop
# Starting round 2
# Rolling 6 dice...
# *** 6 4 5 2 3 1 ***
# Enter dice to keep, or (q)uit:
# > q
# Thanks for playing. You earned 50 points
