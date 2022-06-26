# Followed https://www.youtube.com/watch?v=PXMJ6FS7llk

#%%
# import pandas as pd

# HTML
#%%
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')
print(len(simpsons))
print(simpsons[1])

# CSV
# %%
df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')
print(df_premier21)
df_premier21.rename(columns={'FTHG':'Home_Goals', 'FTAG': 'Away_Goals'}, inplace=True)

# PDF
#===================================================
# Dependencies : tk, ghostscript, camelot-py
# Read first page. flavor parameter defines parsing method
# lattice by default. 
#%%
import camelot
tables = camelot.read_pdf("foo.pdf", pages='1', flavor='lattice') 
print(tables)

tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')
