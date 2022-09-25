import pandas as pd
import random

# reads csv file
df = pd.read_csv('taylor_swift_lyrics.csv', encoding='windows-1254')

# initialize a count and score for the game
x = 0
score = 0

# Prompts the user on whether they would like to select the album the lyrics come from
choose_album = input('Would you like to select what album the lyrics are from (Y/N)? ')

if choose_album == 'N': # version of game where the user plays with all albums
    while x < 3:
        n = random.randint(0, len(df)) # generate a random number in the range of the length of the csv file
        lyric = df.at[n, 'lyric'] # get a random lyric
        print(lyric)
        guess = input('What song is this lyric from: ') # stores the user's guess
        # checks if the user's guess was correct and continues accordingly
        if guess == df.at[n, 'track_title']:
            x = x + 1  # advances round count
            print('Correct! ' + str((3 - x)) + ' round(s) remaining.')
            score = score + 1 # increases score for correct answer
        else:
            x = x + 1 # advances round count
            print('Incorrect! ' + str((3 - x)) + ' round(s) remaining.')
elif choose_album == 'Y': # version of game where user plays with only one album
    album_name = input('Enter album name: ') # prompts user for the album they want to use

    df_choice = df[df['album'] == album_name] # narrows dataframe to only lyrics in the specified album

    list_idx = list(df_choice.index) # lists indexes of narrowed dataframe

    # creates a minimum and maximum bound for the random number
    min_idx = min(list_idx)
    max_idx = max(list_idx)

    while x < 3:
        n = random.randint(min_idx, max_idx) # generate a random number
        lyric = df_choice.at[n, 'lyric'] # get a random lyric

        print(lyric)

        guess = input('What song is this lyric from: ') # prompts the user for their guess

        # checks if the user's guess was correct and continues accordingly
        if guess == df_choice.at[n, 'track_title']:
            x = x + 1  # advances round count
            print('Correct! ' + str((3 - x)) + ' round(s) remaining.')
            score = score + 1 # increases score for correct answer
        else:
            x = x + 1 # advances round count
            print('Incorrect! ' + str((3 - x)) + ' round(s) remaining.')

# displays user's statistics
print('Your statistics: ')
print('Total correct: ' + str(score))
print('Total incorrect: ' + str(3 - score))
print('Grade: ' + str(round(float(score / 3 * 100), 2)) + '%')