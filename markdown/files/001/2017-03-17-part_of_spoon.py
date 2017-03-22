import random

restaurants = ["Sticks", "Yuan Ho", "Melting Pot", "East Garden"]
styles = ["Casual", "Chinese", "Fancy", "Chinese"]
costs = ["$", "$", "$$$", "$$"]

print(styles.index('Chinese'))

'''There are several ways to go about this,
but one of the simplest is to make a list of indices.
Loop over all indices and if styles[index] == chosen_style
add the index to a list of correctly-styled indices.'''

chosen_style = 'Chinese'
correctly_styled_indices = []
# length_of_list = len(styles)
# for index in range(length_of_list):
for index in range(len(styles)):
    if styles[index] == chosen_style:
        correctly_styled_indices.append(index)
        print('indices is now', correctly_styled_indices)
    else:
        print('ignoring index', index)

print(correctly_styled_indices)

index = random.choice(correctly_styled_indices)
print(restaurants[index], 'costs', costs[index])