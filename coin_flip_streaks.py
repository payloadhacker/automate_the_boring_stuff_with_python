import random

num_streaks = 0

for experiment_num in range(0,10000):
    streak_found = False
    flips = [random.randint(0,1) for _ in range(100) ]
    for i in range(len(flips) - 5):
         current_streak = sum(flips[i:i+6])
         if current_streak == 0 or current_streak ==6:
            streak_found = True
            
            break 
    if streak_found:
        num_streaks += 1

print('Chance of streak: %s%%' % (num_streaks / 100))
    

