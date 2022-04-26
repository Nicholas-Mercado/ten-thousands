from collections import Counter
import random
class GameLogic:

    def __init__(self):
        pass

    @staticmethod
    def calculate_score(values):
        sumof = []
        roll = Counter(values)
        flag = True
        if set(values) == set([1, 2, 3, 4, 5, 6]): 
              return 1500 
        if len(values) == 6:
            print('line 15')
            for value in roll.values():
                print(roll.values())
                if value != 2:
                    flag = False 
            if flag:
                return 1500 
                
        if int(roll.get(1) or 0) >= 1:
            if roll.get(1) == 1:
                sumof.append(100)
            if roll.get(1) == 2:
                sumof.append(200)
            if roll.get(1) >= 3:
                sumof.append((roll.get(1)-2) * 1000)
        if int(roll.get(5) or 0) >= 1:
            if roll.get(5) == 1:
                sumof.append(50)
            if roll.get(5) == 2:
                sumof.append(100)
            if roll.get(5) >= 3:
                sumof.append((roll.get(5)-2) * 500)
        if int(roll.get(2) or 0) >= 3:
            sumof.append((((roll.get(2)-2)) * 200))
        if int(roll.get(3) or 0) >= 3:
            sumof.append((((roll.get(3)-2)) * 300))
        if int(roll.get(4) or 0) >= 3:
            sumof.append((((roll.get(4)-2)) * 400))
        if int(roll.get(6) or 0) >= 3:
            sumof.append((((roll.get(6)-2)) * 600))
    
        # print(sumof)    
        final_total = sum(sumof)
        # print(final_total)
        return final_total
             
 

    @staticmethod
    def roll_dice(values):
        pass
        # x = random.randint(1, values)
        # print(x)
        # return x


GameLogic.calculate_score((1, 2, 3, 4, 5, 6))

# GameLogic.roll_dice(1)
