import sys
from datetime import datetime, timedelta

# read 2 file name arguments
argc = len(sys.argv) - 1
if argc < 3:
    print(
        'Usage: python timetable_transfer.py <timetable1.txt> <timetable2.txt> <transfer_walk_minute>')
    sys.exit(1)

filename1 = sys.argv[1]
filename2 = sys.argv[2]
transfer_walk_minute = float(sys.argv[3])

# initial variables
timetable1 = []
timetable1_info = {}
timetable2 = []
timetable2_info = {}
transfer_walk_time = timedelta(minutes=transfer_walk_minute)

# # first file -> make timetable array
# load info
f1 = open(filename1, 'r')
timetable1_info['station'], timetable1_info['line'], timetable1_info['week'], timetable1_info['direction'] = f1.readline().split()

# read timetable
while True:
    line = f1.readline()
    if not line:
        break
    # time format: %H:%M:%S
    # but, %H can be 24 (12 am) or 25 (1 am)
    destination, train_time = line.split()
    timesplit = train_time.split(':')
    hour = int(timesplit[0])
    minute = int(timesplit[1])
    second = int(timesplit[2])
    timetable1.append((destination, datetime(
        2020, 1, 1+hour//24, hour % 24, minute, second)))
f1.close()

# # second file
# load info
f2 = open(filename2, 'r')
timetable2_info['station'], timetable2_info['line'], timetable2_info['week'], timetable2_info['direction'] = f2.readline().split()

# read timetable
while True:
    line = f2.readline()
    if not line:
        break
    # time format: %H:%M:%S
    # but, %H can be 24 (12 am) or 25 (1 am)
    destination, train_time = line.split()
    timesplit = train_time.split(':')
    hour = int(timesplit[0])
    minute = int(timesplit[1])
    second = int(timesplit[2])
    timetable2.append((destination, datetime(
        2020, 1, 1+hour//24, hour % 24, minute, second)))
f2.close()

# comparison station1 -> station2
print('Transfer Timetable Result')
print(f'{timetable1_info["station"]} {timetable1_info["line"]} ({timetable1_info["week"]}, {timetable1_info["direction"]}) \
-> {timetable2_info["station"]} {timetable2_info["line"]} ({timetable2_info["week"]}, {timetable2_info["direction"]}) ({transfer_walk_minute} minutes)')
print()
i = 0
j = 0
result = []
while i < len(timetable1) and j < len(timetable2):
    # test if the [time1 + walk] and time2
    if timetable1[i][1] + transfer_walk_time <= timetable2[j][1]:
        # transfer possible
        result.append((timetable1[i][0], timetable2[j][0],
                       timetable1[i][1], timetable2[j][1],
                       timetable2[j][1] - timetable1[i][1]))
        i += 1
    else:
        # transfer impossible
        j += 1

# print result
for tup in result:
    print(
        '{}\t{:%H:%M:%S}  ->  {}\t{:%H:%M:%S} (+{})'.format(tup[0], tup[2], tup[1], tup[3], tup[4]))

# save result as a file
print()
print('Do you want to create a file to save (y/n)? ', end='')
response = input()
if response == 'Y' or response == 'y':
    f3 = open('result.txt', 'w')
    for tup in result:
        f3.write('{}\t{:%H:%M:%S}  ->  {}\t{:%H:%M:%S} (+{})\n'.format(
            tup[0], tup[2], tup[1], tup[3], tup[4]))
    f3.close()
    print('result.txt saved.')
