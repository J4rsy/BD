import pandas as pd
import csv

def correct_string(s):
    res = ""
    for x in s:
        if x == '&':
            res += "'||chr(38)||'"
            continue
        if x == '\'':
            res += '\''
        if x == '"':
            res += '"'
        res += x
    return res

# print(correct_string('x\'d'))
df = pd.read_csv('Publikacje.csv')

df = df.astype(str)

df['Tytuł'] = df['Tytuł'].apply(correct_string)

df['SQL'] = "INSERT INTO articles VALUES (" + df['ID'] + ", '" + df['Tytuł'] + "', " + df['Rok'] + ", " + df['Autorzy'] + ", " + df['Punkty'] + ");"

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_colwidth', None)
# df.style.set_properties(**{'text-align': 'right'})
print("\n".join(df['SQL']))

# print(df.loc[[107]].to_string())
