# Application should implement all features from previous version
# import modules prev 
# Application should simulate rolling between 1 and 6 dice
# call roll_dice
# Application should allow user to set aside dice each roll
# banking method
# Application should allow “banking” current score or rolling again.
# access banker.py
#access roll_dice.py
# Application should keep track of total score
# total score accumulator 
# Application should keep track of current round
# Variable to keep track of round Hey you hit ten thousand
# Application should have automated tests to ensure proper operation



from game_logic import GameLogic
# from ten_thousand.game_logic import GameLogic
class Game:

    def play(self, roller=GameLogic.roll_dice):
        print(
'''Welcome to Ten Thousand
(y)es to play or (n)o to decline''')
        num_of_dice = 6
        user_input = input('> ').lower()
        if user_input == 'n' :
            print("OK. Maybe another time")
            
        else:
            print(
'''Starting round 1
Rolling 6 dice...''')
            dice_roll = roller(num_of_dice)
            format_dice_roll = f'*** {self.format_rolls(dice_roll)}***'
            print(format_dice_roll)
            print("Enter dice to keep, or (q)uit:")
            user_input = input('> ').lower()
            if user_input == 'q':
                print("Thanks for playing. You earned 0 points")

    def format_rolls(self, dice_roll):
        string = ''
        for number in dice_roll:
            string += f'{number} '
        return string
    
if __name__ == '__main__':
    game = Game()
    game.play()
