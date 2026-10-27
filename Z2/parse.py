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
        res += x
    return res

def fix_delimiter(s):
    res = ""
    for x in s:
        if x == ',':
            res += '.'
        else:
            res += x
    return res

# print(correct_string('x\'d'))
df = pd.read_csv('Prace.csv')

df = df.astype(str)

df['Tytuł'] = df['Tytuł'].apply(correct_string)

df['SQL'] = "INSERT INTO Praca VALUES (" + df['ID'] + ", '" + df['Tytuł'] + "', " + df['Rok'] + ", " + df['Autorzy'] + ", " + df['Punkty'] + ");"

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_colwidth', None)
# df.style.set_properties(**{'text-align': 'right'})
with open("instrukcje_prace.sql", "w") as f:
    f.write("\n".join(df['SQL']))
    f.write("\n")

#######################################################################################################################################################
df = pd.read_csv('Autorzy.csv')

df = df.astype(str)

df['Sloty'] = df['Sloty'].apply(fix_delimiter)

df['SQL'] = "INSERT INTO Autor VALUES (" + "'" + df['ID'] + "', " + df['Ryzyko'] + ", " + df['Sloty'] + ");"


# df.style.set_properties(**{'text-align': 'right'})
with open("instrukcje_prace.sql", "a") as f:
    f.write("\n".join(df['SQL']))
    f.write("\n")

#######################################################################################################################################################
df = pd.read_csv('Autorstwo.csv')

df = df.astype(str)


df['SQL'] = "INSERT INTO Autorstwo VALUES (" + df['Praca'] + ", '" + df['Autor'] + "'" + ");"


# df.style.set_properties(**{'text-align': 'right'})
with open("instrukcje_prace.sql", "a") as f:
    f.write("\n".join(df['SQL']))
    f.write("\n")

# print(df.loc[[107]].to_string())
