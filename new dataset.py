import pandas
import unidecode
import sys
from collections import defaultdict
import operator

df = pandas.read_csv('/Users/ammar/Downloads/tmp/results.csv')
ndf = pandas.DataFrame(columns=['home_team', 'away_team', 'home_score', 'away_score'])

unique_country = set()
unique_country.update(df['home_team'].values.tolist())
unique_country.update(df['away_team'].values.tolist())
sorted_countries = list(unique_country)
sorted_countries.sort(key=str.lower)
ndf['country'] = sorted_countries

num_of_matches = [0] * 248
num_of_matches_won = [0] * 248
num_of_wc_matches = [0] * 248
num_of_wc_matches_won = [0] * 248
num_of_goals = [0] * 248

for index, row in df.iterrows():
    ht = row['home_team']
    at = row['away_team']
    hsc = row['home_score']
    asc = row['away_score']
    t = row['tournament']
    w = row['wining_team']
    d = row['difference']

    hti = sorted_countries.index(ht)
    num_of_matches[hti] += 1
    ati = sorted_countries.index(at)
    num_of_matches[ati] += 1

    if w.lower() != 'draw':
        wi = sorted_countries.index(w)
        num_of_matches_won[wi] += 1

    if t == 'FIFA World Cup':
        num_of_wc_matches[hti] += 1
        num_of_wc_matches[ati] += 1

        num_of_wc_matches_won[wi] += 1

    num_of_goals[hti] += int(hsc)
    num_of_goals[ati] += int(asc)

ndf['number_of_matches'] = num_of_matches
ndf['number_of_matches_won'] = num_of_matches_won
ndf['number_of_WC_matches'] = num_of_wc_matches
ndf['number_of_WC_matches_won'] = num_of_wc_matches_won
ndf['number_of_goals'] = num_of_goals


ndf.to_csv('/Users/ammar/Downloads/tmp/t3.csv', encoding='utf-8')
