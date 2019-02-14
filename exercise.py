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
# You probably just ended up rewriting some of the same code. Move this repeated code into a function that accepts a direction and a list of trains as arguments, and returns a list of just the trains that go in that direction. Call this function once for north and once for east in order to DRY up your code.
# Pick one train and add another key/value pair for the first_departure_time. For simplicity, assume the first train always leave on the hour. You can represent this hour as an integer: 6 for 6:00am, 12 for noon, 13 for 1:00pm, etc.
# Now we want to (programmatically) make a new dictionary where the train frequencies are the keys and the values are a list of train names, like so: python { 15: ['72C', '72D', '110', '111'], 5: ['610', '611'], 30: ['80A', '80B'] }
