#Initial Data
train_list = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]
# Save the direction of train 111 into a variable.
tr_111_dir = train_list[7]['direction']

# Save the frequency of train 80B into a variable.
tr_80b_frqq = train_list[5]['frequency_in_minutes']

# Save the direction of train 610 into a variable.
tr_610_dir = train_list[2]['direction']

# Create an empty list. Iterate through each train and add the name of the train into the list if it travels north.
new_list = []
for num in range(0,len(train_list)):
    new_list.append(train_list[num]['train'])

# Do the same thing for trains that travel east.
east_trains = []
for num in range(0,len(train_list)):
    if train_list[num]['direction'] == 'east':
        east_trains.append(train_list[num]['train'])

# You probably just ended up rewriting some of the same code. Move this repeated code into a function that accepts a direction and a list of trains as
#arguments, and returns a list of just the trains that go in that direction. Call this function once for north and once for east in order to DRY up your code.
def trains_of_direction(trains,direction):
    train_list = []
    for num in range(0,len(trains)):
        if trains[num]['direction'] == direction:
            train_list.append(trains[num]['train'])
    return train_list

print('The list of trains heading north is: {}'.format(trains_of_direction(train_list,'north')))
print('The list of trains heading east is: {}'.format(trains_of_direction(train_list,'east')))

# Pick one train and add another key/value pair for the first_departure_time. For simplicity, assume the first train always leave on the hour. You can
#represent this hour as an integer: 6 for 6:00am, 12 for noon, 13 for 1:00pm, etc.
train_list[3]['first_departure_time'] = 5

# Now we want to (programmatically) make a new dictionary where the train frequencies are the keys and the values are a list of train names, like so:
#python { 15: ['72C', '72D', '110', '111'], 5: ['610', '611'], 30: ['80A', '80B'] }
#Initialize an empty list to use
frq_dict = {}
#For each item in our list
for num in range(0,len(train_list)):
    #These are just placeholder names, makes the following code a bit easier to read
    curr_train = train_list[num]['train']
    curr_frq = train_list[num]['frequency_in_minutes']
    if not frq_dict.get(curr_frq, False): #If our frequency dict doesn't already contain a keyvalue of the current train's frequency
        frq_dict[curr_frq] = [] #Add an key to the dictionary of that frequency, and make it an empty list
    frq_dict[curr_frq].append(curr_train) #Finally, add the name of the current train to the list in our dictionary corresponding to the current frequency

print(frq_dict)
#Oh dang, I should have read the whole thing before starting :(
# Rearrange the order of the following lines of code to achieve this task. You can (and should) adjust the indenting but don't otherwise modify the code:

trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]
trains_by_frequency = {}
for train in trains:
    name = train['train']
    freq = train['frequency_in_minutes']
    if freq in trains_by_frequency:
        trains_by_frequency[freq].append(name)
    else:
        trains_by_frequency[freq] = [name]
print(trains_by_frequency)
