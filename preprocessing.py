import pandas
import unidecode

df = pandas.read_csv('/Users/ammar/Downloads/results.csv')

african = ['Algeria',
 'Angola',
 'Benin',
 'Botswana',
 'Burkina',
 'Burundi',
 'Cameroon',
 'Cape Verde',
 'Central African Republic',
 'Chad',
 'Comoros',
 'Congo',
 'Congo, Democratic Republic of',
 'Djibouti',
 'Egypt',
 'Equatorial Guinea',
 'Eritrea',
 'Ethiopia',
 'Gabon',
 'Gambia',
 'Ghana',
 'Guinea',
 'Guinea-Bissau',
 'Ivory Coast',
 'Kenya',
 'Lesotho',
 'Liberia',
 'Libya',
 'Madagascar',
 'Malawi',
 'Mali',
 'Mauritania',
 'Mauritius',
 'Morocco',
 'Mozambique',
 'Namibia',
 'Niger',
 'Nigeria',
 'Rwanda',
 'Sao Tome and Principe',
 'Senegal',
 'Seychelles',
 'Sierra Leone',
 'Somalia',
 'South Africa',
 'South Sudan',
 'Sudan',
 'Swaziland',
 'Tanzania',
 'Togo',
 'Tunisia',
 'Uganda',
 'Zambia',
 'Zimbabwe']


asian = ['Afghanistan',
 'Bahrain',
 'Bangladesh',
 'Bhutan',
 'Brunei',
 'Burma (Myanmar)',
 'Cambodia',
 'China',
 'East Timor',
 'India',
 'Indonesia',
 'Iran',
 'Iraq',
 'Israel',
 'Japan',
 'Jordan',
 'Kazakhstan',
 'Korea, North',
 'Korea, South',
 'Kuwait',
 'Kyrgyzstan',
 'Laos',
 'Lebanon',
 'Malaysia',
 'Maldives',
 'Mongolia',
 'Nepal',
 'Oman',
 'Pakistan',
 'Philippines',
 'Qatar',
 'Russian Federation',
 'Saudi Arabia',
 'Singapore',
 'Sri Lanka',
 'Syria',
 'Tajikistan',
 'Thailand',
 'Turkey',
 'Turkmenistan',
 'United Arab Emirates',
 'Uzbekistan',
 'Vietnam',
 'Yemen']

europian = ['Albania',
 'Andorra',
 'Armenia',
 'Austria',
 'Azerbaijan',
 'Belarus',
 'Belgium',
 'Bosnia and Herzegovina',
 'Bulgaria',
 'Croatia',
 'Cyprus',
 'Czech Republic',
 'Denmark',
 'Estonia',
 'Finland',
 'France',
 'Georgia',
 'Germany',
 'Greece',
 'Hungary',
 'Iceland',
 'Ireland',
 'Italy',
 'Latvia',
 'Liechtenstein',
 'Lithuania',
 'Luxembourg',
 'Macedonia',
 'Malta',
 'Moldova',
 'Monaco',
 'Montenegro',
 'Netherlands',
 'Norway',
 'Poland',
 'Portugal',
 'Romania',
 'San Marino',
 'Serbia',
 'Slovakia',
 'Slovenia',
 'Spain',
 'Sweden',
 'Switzerland',
 'Ukraine',
 'United Kingdom',
 'Vatican City']

n_american = ['Antigua and Barbuda',
 'Bahamas',
 'Barbados',
 'Belize',
 'Canada',
 'Costa Rica',
 'Cuba',
 'Dominica',
 'Dominican Republic',
 'El Salvador',
 'Grenada',
 'Guatemala',
 'Haiti',
 'Honduras',
 'Jamaica',
 'Mexico',
 'Nicaragua',
 'Panama',
 'Saint Kitts and Nevis',
 'Saint Lucia',
 'Saint Vincent and the Grenadines',
 'Trinidad and Tobago',
 'United States']

oceanian = ['Australia',
 'Fiji',
 'Kiribati',
 'Marshall Islands',
 'Micronesia',
 'Nauru',
 'New Zealand',
 'Palau',
 'Papua New Guinea',
 'Samoa',
 'Solomon Islands',
 'Tonga',
 'Tuvalu',
 'Vanuatu']

s_american = ['Argentina',
 'Bolivia',
 'Brazil',
 'Chile',
 'Colombia',
 'Ecuador',
 'Guyana',
 'Paraguay',
 'Peru',
 'Suriname',
 'Uruguay',
 'Venezuela']

for index, row in df.iterrows():
    dt = row['date']
    d = dt.split('-')
    if len(d) < 3:
        d = dt.split('/')
    d = d[2] + '/' + d[1] + '/' + d[0]
    d = str(d)
    df.at[index, 'date'] = d


df[['Home_continent', 'away_continent']] = df[['Home_continent', 'away_continent']].astype(str)

# Code used to create ct.txt
# unknown_con = set()
# for index, row in df.iterrows():
#     if row['Home_continent'] == 'unknown':
#         unknown_con.add(row['home_team'])
#     if row['away_continent'] == 'unknown':
#         unknown_con.add(row['away_team'])
# with open('/Users/ammar/Downloads/tmp/ct.txt', 'w') as f:
#     for x in unknown_con:
#         f.write(x)
#         f.write('\n')

cc = {}
with open('/Users/ammar/Downloads/tmp/ct.txt', 'r') as f:
    for line in f:
        cc[line.split('=')[0].strip()] = line.split('=')[1].strip()

for index, row in df.iterrows():
    # unidecode.unidecode() to convert all non-english letters like è and ü to English 
    # in order to perform the comparison only
    if unidecode.unidecode(row['home_team']).lower() in [unidecode.unidecode(c).lower() for c in african]:
        df.at[index, 'Home_continent'] = 'Africa'
    elif unidecode.unidecode(row['home_team']).lower() in [unidecode.unidecode(c).lower() for c in asian]:
        df.at[index, 'Home_continent'] = 'Asia'
    elif unidecode.unidecode(row['home_team']).lower() in [unidecode.unidecode(c).lower() for c in europian]:
        df.at[index, 'Home_continent'] = 'Europe'
    elif unidecode.unidecode(row['home_team']).lower() in [unidecode.unidecode(c).lower() for c in s_american]:
        df.at[index, 'Home_continent'] = 'South America'
    elif unidecode.unidecode(row['home_team']).lower() in [unidecode.unidecode(c).lower() for c in n_american]:
        df.at[index, 'Home_continent'] = 'North America'
    elif unidecode.unidecode(row['home_team']).lower() in [unidecode.unidecode(c).lower() for c in oceanian]:
        df.at[index, 'Home_continent'] = 'Oceania'
    else:
        df.at[index, 'Home_continent'] = cc[row['home_team']]

for index, row in df.iterrows():
    if unidecode.unidecode(row['away_team']).lower() in [unidecode.unidecode(c).lower() for c in african]:
        df.at[index, 'away_continent'] = 'Africa'
    elif unidecode.unidecode(row['away_team']).lower() in [unidecode.unidecode(c).lower() for c in asian]:
        df.at[index, 'away_continent'] = 'Asia'
    elif unidecode.unidecode(row['away_team']).lower() in [unidecode.unidecode(c).lower() for c in europian]:
        df.at[index, 'away_continent'] = 'Europe'
    elif unidecode.unidecode(row['away_team']).lower() in [unidecode.unidecode(c).lower() for c in s_american]:
        df.at[index, 'away_continent'] = 'South America'
    elif unidecode.unidecode(row['away_team']).lower() in [unidecode.unidecode(c).lower() for c in n_american]:
        df.at[index, 'away_continent'] = 'North America'
    elif unidecode.unidecode(row['away_team']).lower() in [unidecode.unidecode(c).lower() for c in oceanian]:
        df.at[index, 'away_continent'] = 'Oceania'
    else:
        df.at[index, 'away_continent'] = cc[row['away_team']]


df.rename(columns = {'Wining_team':'wining_team', 'Difference':'difference', 'Home_continent':'home_continent'}, inplace = True)


df.to_csv('/Users/ammar/Downloads/tmp/t.csv', encoding='utf-8')