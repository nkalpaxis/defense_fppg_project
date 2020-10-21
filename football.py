import csv

# opening fantasy_points_allowed.csv which was downloaded from fantasypros.com, the data set contains every team and how many fantasy points they allow to each position

f = open('fantasy_points_allowed.csv')
r = csv.reader(f)
data = list(r)

# storing header inside header variable and the data set into data variable which excludes header
header = data[0]
data = data[1:]

# print(header)


# since all the values in the csv are strings we'll create a function that converts strings to integers

def convert_string(string):
    for v in string:
        string = int(string)
    return string

# a function that extracts entire columns for us
def extract(index):
    column = []
    for v in data:
        col = v[index]
        column.append(col)
    return column

teams = extract(0)
print(teams)

def extract_and_convert(index):
    column = extract(index)
    conversion = convert_string(column)
    return conversion

print(extract_and_convert(2))