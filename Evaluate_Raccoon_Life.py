"""
 Header
 Feb. 5th 2020
 Shizhang Wang
 0027521360
 This program takes an input file of a simulated racoon movement file and
 outputs a report of some statistics of this simulation
"""

import math

f = open('2008Male00006.txt')  # open file as read
# put each line in the file into a list, stripe \n at the end of each line
lines_raw = [line.rstrip() for line in f]
# check for the end of the simulation (one field), store in separated lists
lines = [line for line in lines_raw if line.count(',') > 1]
sim_end = [line for line in lines_raw if line.count(',') < 1]
# split each line using comma as separator
data_raw = [line.split(',') for line in lines]
# separate key from value
keys = data_raw[0]
val = data_raw[1::]
# create lists for each column of value
val_lists = [[] for i in range(len(keys))]
'''
populated each list with values in each column
for i, lst in enumerate(val_lists):
    for j in val:
        lst.append(j[i])
'''
# some of the for loop is converted within reasonable amount of time
# others kept as is
[lst.append(j[i]) for i, lst in enumerate(val_lists) for j in val]
'''
create dict with header as key and list of values as paired value of the key
data_dict = dict()
for i, key in enumerate(keys):
    data_dict[key] = val_lists[i]
'''
data_dict = {key: val_lists[i] for i, key in enumerate(keys)}
data_dict['result'] = sim_end[0]  # end line stored
f.close()   # close the input file

# list of column where values should be number (float)
flo_lst = [' X', ' Y', 'Energy Level', 'Risk', 'ProbFoodCap', 'MVL', 'MSL', 'PercptionDist', 'Percent Step']
'''
convert columns of number to appropriate data type, datetime/string left alone
'''
for key, val in data_dict.items():
    if key in flo_lst:
        # [float(item) for i, item in enumerate(val)]
        for i, item in enumerate(val):
            val[i] = float(item)

# this block shows the thought process, skip if not needed
'''
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist
# calculate distance
# dist_lst = []
# for i in range(len(x_val)):
#     if i == 0:
#         dist_lst.append(0)
#     else:
#         dist_lst.append(distance(x_val[i-1], y_val[i-1], x_val[i], y_val[i]))
dist_lst = [distance(x_val[i - 1], y_val[i - 1], x_val[i], y_val[i]) if i != 0 else 0 for i in range(len(x_val))]
def mean_sum_distance(df):
    x_val = df[' X']    # set X and Y values out for distance calculation
    y_val = df[' Y']
    return {'list_mean': {key: sum(val1) / len(val1) for key, val1 in df.items() if key in flo_lst},
            'list_sum': {key: sum(val2) for key, val2 in df.items() if key in flo_lst},
            'distance_list': [distance(x_val[i - 1], y_val[i - 1], x_val[i], y_val[i])
                              if i != 0 else 0 for i in range(len(x_val))]}
values_dict = mean_sum_distance(data_dict)
'''


# distance function
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist

'''
# compute mean and sum for lists of floats value and distance traveled
# i'm not sure if list comprehension is considered function
# but included in function nonetheless
'''
def mean_dict(df):
    return {key: sum(val1) / len(val1) for key, val1 in df.items() if key in flo_lst}


lst_mean = mean_dict(data_dict)


def sum_dict(df):
    return {key: sum(val2) for key, val2 in df.items() if key in flo_lst}


lst_sum = sum_dict(data_dict)


def dist_list(df):
    x_val = df[' X']
    y_val = df[' Y']
    dist = [distance(x_val[i - 1], y_val[i - 1], x_val[i], y_val[i]) if i != 0 else 0 for i in range(len(x_val))]
    df['Distance'] = dist
    return dist


distance_list = dist_list(data_dict)

# retrieve some of the mean values
energy_average = lst_mean['Energy Level']
x_loc = lst_mean[' X']
y_loc= lst_mean[' Y']
total_dist = sum(distance_list)


def final_dict(df):
    # since the order in original dict is ask requested, pop method is used, otherwise a new dict could be constructed
    unwanted = ['Year', 'George #', 'Energy Level', 'ProbFoodCap', 'MVL', 'MSL', 'PercptionDist', 'Percent Step',
                'Risk', 'result']
    # some key have white space, if that's concern, a new constructed dict maybe faster
    # i.e. final = ['Year': df['Year], 'X': df[' X']...}, then return final
    [df.pop(i) for i in unwanted]
    return df

# contents below are singled out for easier writing into the file
result = str(data_dict['result'])
final_out = final_dict(data_dict)
final_keys = list(final_out.keys())
final_vals = list(final_out.values())


with open('Georges_life.txt', 'w') as f:
    # write header block in file as requested
    f.write('Raccoon name: George\nAverage location: %f, %f\nDistance traveled: %f\nAverage energy level: %f\nRaccoon '
            'end state: %s\n\n' % (float(x_loc), float(y_loc), float(total_dist), float(energy_average), str(result)))
    # [f.write(item + '\t') for item in final_keys] # tab delimited headers created from keys
    # f.write('\n')
    f.write('\t'.join(final_keys)+'\n')    # same output as commented portion as above
    # create tab delimited value table with each hour as row
    for i in range(len(final_vals[0])):
        for item in final_vals:
            f.write(str(item[i])+'\t')
        f.write('\n')
    f.close()
