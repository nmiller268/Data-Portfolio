#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import sys
import matplotlib.pyplot as plt
import numpy as np

def roll_dice():
    #"""Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

# Get number of games to simulate from command line argument
try:
    num_games = int(sys.argv[1])
except:
    num_games = 1

# Initialize lists to track game outcomes
win_on_roll = [0] * 13
lose_on_roll = [0] * 13

# Simulate games of craps
for i in range(num_games):
    die_values = roll_dice()  # first roll
    sum_of_dice = sum(die_values)
    roll_count = 1

    # determine game status and point, based on first roll
    if sum_of_dice in (7, 11):  # win
        win_on_roll[roll_count] += 1
    elif sum_of_dice in (2, 3, 12):  # lose
        lose_on_roll[roll_count] += 1
    else:  # remember point
        my_point = sum_of_dice
        game_status = 'CONTINUE'
        roll_count += 1

        # continue rolling until player wins or loses
        while game_status == 'CONTINUE' and roll_count <= 12:
            die_values = roll_dice()
            sum_of_dice = sum(die_values)
            roll_count += 1

            if sum_of_dice == my_point:  # win by making point
                win_on_roll[roll_count] += 1
                game_status = 'WON'
            elif sum_of_dice == 7:  # lose by rolling 7
                lose_on_roll[roll_count] += 1
                game_status = 'LOST'

            # after 12 rolls, keep track of wins and losses only
            if roll_count > 12:
                if game_status == 'WON':
                    win_on_roll[0] += 1
                else:
                    lose_on_roll[0] += 1

# Plot game outcomes
rolls = np.arange(13)
win_labels = [f"Win on roll {i}" for i in rolls]
lose_labels = [f"Lose on roll {i}" for i in rolls]
labels = win_labels + lose_labels
wins = win_on_roll + lose_on_roll

fig, ax = plt.subplots()
ax.bar(labels, wins)
ax.set_ylabel('Number of Games')
ax.set_title(f'Simulated Games of Craps ({num_games} Games)')
plt.xticks(rotation=90)
plt.show()

# Calculate game statistics
total_wins = sum(win_on_roll) + win_on_roll[0]
total_losses = sum(lose_on_roll) + lose_on_roll[0]
win_percent = total_wins / num_games * 100
lose_percent = total_losses / num_games * 100

#Display game statistics
print(f'\n{num_games:,d} games of Craps simulated.\n')
print(f'Total games won: {total_wins:,d} ({win_percent:.2f}%)')
print(f'Total games lost: {total_losses:,d} ({lose_percent:.2f}%)')

#Calculate mean, median, and mode of game length
game_lengths = [roll + 1 for roll in range(len(win_on_roll))]
total_rolls = sum(game_lengths)
mean_rolls = total_rolls / num_games
median_rolls = game_lengths[num_games // 2]
mode_rolls = game_lengths[max(range(len(win_on_roll)), key=win_on_roll)]

#Display game length statistics
print(f'\nMean game length: {mean_rolls:.2f}')
print(f'Median game length: {median_rolls}')
print(f'Mode game length: {mode_rolls}')

        
        


# In[18]:


import random
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns


def roll_dice():
    die1 = [random.randrange(1, 7) for i in range (12)]
    die2 = [random.randrange(1, 7) for i in range(12)]

def display_dice(dice):
    die1, die2 = dice # unpack the tuple into variables die1 and die2
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')
    
die_values = roll_dice() # first roll
display_dice(die_values)

#Still figuring out

rolls = [random.randrange(1, 7) for i in range(12)]
values, frequencies = np.unique(rolls, return_counts=True)
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style("whitegrid")
axes = sns.barplot(values, frequencies, palette='bright')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')
axes.set_ylim(top=max(frequencies) * 1.10)
for bar, frequency in zip(axes.patches, frequencies):
 text_x = bar.get_x() + bar.get_width() / 2.0
 text_y = bar.get_height()
 text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
 axes.text(text_x, text_y, text,
 fontsize=11, ha='center', va='bottom')

    
        


# In[ ]:




