import pandas
import unidecode
import sys

colors = {
    'black': '\033[0;30m',
    'black_b': '\033[1;30m',
    'white': '\033[0;37m',
    'white_b': '\033[1;37m',
    'red': '\033[0;31m',
    'red_b': '\033[1;31m',
    'green': '\033[0;32m',
    'green_b': '\033[1;32m',
    'yellow': '\033[0;33m',
    'yellow_b': '\033[1;33m',
    'blue': '\033[0;34m',
    'blue_b': '\033[1;34m',
    'magenta': '\033[0;35m',
    'magenta_b': '\033[1;35m',
    'cyan': '\033[0;36m',
    'cyan_b': '\033[1;36m',
    'b': '\033[1m',
    'reset': '\033[0m',
    # Erases the entire current line and moves the cursor back to the start of it
    'erm': '\033[2K\r',
}

def print_in_color(text, color, bold=False, end_with_newline=True, on_same_line=False):
    if bold:
        color += '_b'
    color_code = colors[color]
    if on_same_line:
        print('{erm}{color_code}{text}{reset_code}'.format(erm=colors['erm'], color_code=color_code, text=text,
                                                           reset_code=colors['reset']), end='', flush=True)
    else:
        if end_with_newline:
            print('{color_code}{text}{reset_code}'.format(color_code=color_code, text=text, reset_code=colors['reset']),
                  flush=True)
        else:
            print('{color_code}{text}{reset_code}'.format(color_code=color_code, text=text, reset_code=colors['reset']),
                  end='', flush=True)


df = pandas.read_csv('/Users/ammar/Downloads/tmp/results.csv')

print_in_color('First team: ', 'yellow', bold=True, end_with_newline=False)
home_team = unidecode.unidecode(input()).lower()

print_in_color('Second team: ', 'green', bold=True, end_with_newline=False)
away_team = unidecode.unidecode(input()).lower()

matches = []

for index, row in df.iterrows():
    date = row['date']
    ht = unidecode.unidecode(row['home_team']).lower()
    at = unidecode.unidecode(row['away_team']).lower()
    hsc = row['home_score']
    asc = row['away_score']
    t = unidecode.unidecode(row['tournament']).lower()
    w = unidecode.unidecode(row['wining_team']).lower()
    d = row['difference']

    if (home_team == ht and away_team == at) or (home_team == at and away_team == ht):
      matches.append([date, ht, at, hsc, asc, t, w, d])

h_wins = len([x for x in matches if x[6] == home_team])
h_wper = round(100 * h_wins / len(matches), 2)
a_wins = len([x for x in matches if x[6] == away_team])
a_wper = round(100 * a_wins / len(matches), 2)
draw = len([x for x in matches if x[6].lower() == 'draw'])
d_per = round(100 * draw / len(matches), 2)

h_goals = 0
for m in matches:
    if m[1] == home_team:
        h_goals += m[3]
    else:
        h_goals += m[4]
a_goals = 0
for m in matches:
    if m[1] == away_team:
        a_goals += m[3]
    else:
        a_goals += m[4]

tournaments = set([x[5] for x in matches])


print_in_color('\n======================================', 'white', end_with_newline=True)

print_in_color(home_team.title(), 'yellow', bold=True, end_with_newline=False)
print_in_color(' and ', 'white', end_with_newline=False)
print_in_color(away_team.title(), 'green', bold=True, end_with_newline=False)
print_in_color(' played ', 'white', end_with_newline=False)
print_in_color(len(matches), 'red', bold=True, end_with_newline=False)
print_in_color(' matches against each other. ', 'white', end_with_newline=True)

print()
print_in_color(home_team.title(), 'yellow', bold=True, end_with_newline=False)
print_in_color(' won in ', 'white', end_with_newline=False)
print_in_color(str(h_wins), 'red', bold=True, end_with_newline=False)
print_in_color(' matches (', 'white', end_with_newline=False)
print_in_color(str(h_wper) + '%', 'cyan', bold=True, end_with_newline=False)
print_in_color(').', 'white', end_with_newline=True)

print_in_color(away_team.title(), 'green', bold=True, end_with_newline=False)
print_in_color(' won in ', 'white', end_with_newline=False)
print_in_color(str(a_wins), 'red', bold=True, end_with_newline=False)
print_in_color(' matches (', 'white', end_with_newline=False)
print_in_color(str(a_wper) + '%', 'cyan', bold=True, end_with_newline=False)
print_in_color(').', 'white', end_with_newline=True)

print_in_color(str(draw), 'red', bold=True, end_with_newline=False)
print_in_color(' matches ended in a draw (', 'white', end_with_newline=False)
print_in_color(str(d_per) + '%', 'cyan', bold=True, end_with_newline=False)
print_in_color(').', 'white', end_with_newline=True)

print()
print_in_color(home_team.title(), 'yellow', bold=True, end_with_newline=False)
print_in_color(' scored ', 'white', end_with_newline=False)
print_in_color(h_goals, 'magenta', bold=True, end_with_newline=False)
print_in_color(' goals against ', 'white', end_with_newline=False)
print_in_color(away_team.title() + '.', 'green', bold=True, end_with_newline=True)

print_in_color(away_team.title(), 'green', bold=True, end_with_newline=False)
print_in_color(' scored ', 'white', end_with_newline=False)
print_in_color(a_goals, 'magenta', bold=True, end_with_newline=False)
print_in_color(' goals against ', 'white', end_with_newline=False)
print_in_color(home_team.title(), 'yellow', bold=True, end_with_newline=True)



print()
print_in_color('They played: ', 'white', end_with_newline=True)
for t in tournaments:
  c = len([x for x in matches if x[5] == t])
  print_in_color('  ' + str(c) + ' ', 'yellow', bold=True, end_with_newline=False)
  print_in_color(t.title(), 'green', bold=True, end_with_newline=False)  
  print_in_color(' matches', 'white', end_with_newline=True)
  
print_in_color('\n======================================', 'white', end_with_newline=True)

