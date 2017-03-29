thing = open('fake-queue.csv')
header = thing.readline().strip()
print(header)
header = header.split(',')
print(header)
third_column = header[2]
print(third_column)

count = 0
total = 0
last_request = 0
for line in thing:
    line = line.strip()
    row = line.split(',')
    count += 1
    total += int(row[3])
    request = int(row[4])
    if request > last_request:
        last_request = request
    # print(header, row)

print(total / count, last_request)
# find max of request column