questions = '''
what functions are tested?

what datatype come from urlopen
why not read url?
book uses readline and readlines

connection.read() -> a byte string (all the data)
connection.readline() -> a byte string for the next line
connection.readlines() -> a byte string for each line, in a list
for dfgsfdhgsdhgs in connection: -> a byte string for each line, one at a time

headers
make for loop over elements in a single column
    loop over rows:
        look only at row[3] or whatever

dict - how differ from list
    d[key] = value
'''

connection = open('fake-queue.csv')
header = connection.readline().strip().split(',')
print(header)

table = []
for line in connection:
    row = line.strip().split(',')
    # print(row)
    table.append(row)

# print(table)
#
# for row in table:
#     print(row[0])
#
# for row in table:
#     print(row[1])

print(table[2][1])

total = 0
count = 0
for row in table:
    total += int(row[4])
    count += 1

print(total, count, total / count / 60)

# which student uses the most TA time

time_used = {}

for row in table:
    student = row[0]
    used = int(row[6]) - int(row[5])
    if student in time_used:
        time_used[student] += used
    else:
        time_used[student] = used

print(time_used)
most_time = max(time_used.values())
print(most_time)

for stud in time_used:
    used = time_used[stud]
    if used == most_time:
        print('Student', stud, 'used the most TA time')
