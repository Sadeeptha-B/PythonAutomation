# Coded by following, 
#https://www.youtube.com/watch?v=PXMJ6FS7llk

import pandas as pd

# HTML
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')
print(len(simpsons))
print(simpsons[1])

# CSV
df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')
print(df_premier21)
df_premier21.rename(columns={'FTHG':'Home_Goals', 'FTAG': 'Away_Goals'}, inplace=True)

# PDF
