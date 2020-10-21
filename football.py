import csv

# opening fantasy_points_allowed.csv which was downloaded from fantasypros.com, the data set contains every team and how many fantasy points they allow to each position

f = open('fantasy_points_allowed.csv')
r = csv.reader(f)
data = list(r)

# storing header inside header variable and the data set into data variable which excludes header
header = data[0]
data = data[1:]

# print(header)


# a function that extracts entire columns for us
def extract(index):
    column = []
    for v in data:
        col = v[index]
        column.append(col)
    return column

qb_ppg = extract(2)
# print(qb_ppg)

# function that converts extracted string values to floats and then integers
def convert_to_int(a_list):
    converted = []
    for v in a_list:
        v = float(v)
        if type(v) == float:
            v = int(v)
        converted.append(v)
    return converted

# print(convert_to_int(qb_ppg))

# function that combines both extract and convert_to_int function just pass in the index you want to extract and an int list of the values will be returned
def extract_and_convert(index):
    column = extract(index)
    conversion = convert_to_int(column)
    return conversion

print(extract_and_convert(2))
print(extract_and_convert(3))
