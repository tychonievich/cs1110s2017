# to read file:
# open(filename)
# for line in file:

post_box = open('vastats.csv')
header = post_box.readline()

header = header.strip().split(',')
print(header)
print(header.index('Total Population'))

name_column = header.index('Name')
population_column = header.index('Renter-occupied Housing')


total = 0
count = 0
for line in post_box:
    # a line is a list of cells
    cells = line.split(',')
    name = cells[name_column]
    if 'town' in name:
#        print(cells[name_column], 'has', cells[population_column], 'people')
        count += 1
        total += int(cells[population_column])

# task: find the average population of jurisdictions
print('average renters:', total/count)
# task: only count things with "town" in the name