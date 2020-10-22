import csv

# opening fantasy_points_allowed.csv which was downloaded from fantasypros.com, the data set contains every team and how many fantasy points they allow to each position

f = open('fantasy_points_allowed.csv')
r = csv.reader(f)
data = list(r)

# storing header inside header variable and the data set into data variable which excludes header
header = data[0]
data = data[1:]


# a function that extracts entire columns for us
def extract(index):
    column = []
    for v in data:
        col = v[index]
        column.append(col)
    return column


# function that converts extracted string values to floats and then integers
def convert_to_int(a_list):
    converted = []
    for v in a_list:
        v = float(v)
        if type(v) == float:
            v = int(v)
        converted.append(v)
    return converted


# function that combines both extract and convert_to_int function just pass in the index you want to extract and an int list of the values will be returned
def extract_and_convert(index):
    column = extract(index)
    conversion = convert_to_int(column)
    return conversion

# function that takes in a team name, splits it and upper cases the first 3 characters
# if the team name has 3 words ex: New York Giants; it will split and take the first character of each string and upper case them
def clean_team(team):
    team = team.split()
    if len(team) == 3:
        first_three = team[0][0] + team[1][0] + team[2][0]
    else:
        first_three = team[0][:3]

    first_three = first_three.upper()
    return first_three
