import sys
from datetime import datetime, timedelta

# read 2 file name arguments
argc = len(sys.argv) - 1
if argc < 3:
    print('Usage: python timetable_transfer.py [timetable1.txt] [timetable2.txt] [transfer_walk_minute]')
    sys.exit(1)

filename1 = sys.argv[1]
filename2 = sys.argv[2]
transfer_walk_minute_int = int(sys.argv[3])

# 2 time arrays
timetable1 = []
timetable2 = []
transfer_walk_minute = timedelta(minutes=transfer_walk_minute_int)

# first file -> make timetable array
f1 = open(filename1, 'r')
while True:
    line = f1.readline()
    if not line:
        break
    # time format: %H:%M:%S
    # but, %H can be 24 (12 am) or 25 (1 am)
    timesplit = line.split(':')
    hour = int(timesplit[0])
    minute = int(timesplit[1])
    second = int(timesplit[2])
    timetable1.append(datetime(2020,1,1+hour//24,hour%24,minute,second))
f1.close()

# second file
f2 = open(filename2, 'r')
while True:
    line = f2.readline()
    if not line:
        break
    # time format: %H:%M:%S
    # but, %H can be 24 (12 am) or 25 (1 am)
    timesplit = line.split(':')
    hour = int(timesplit[0])
    minute = int(timesplit[1])
    second = int(timesplit[2])
    timetable2.append(datetime(2020,1,1+hour//24,hour%24,minute,second))
f2.close()

# comparison station1 -> station2
print('Transfer Timetable Result')
print('{} -> {} ({} minutes)'.format(filename1, filename2, transfer_walk_minute_int))
print()
i = 0
j = 0
result = []
while i < len(timetable1) and j < len(timetable2):
    if timetable1[i] + transfer_walk_minute <= timetable2[j]:
        result.append((timetable1[i], timetable2[j], timetable2[j] - timetable1[i]))
        i += 1
    else:
        j += 1

# print result
for tup in result:
    print('{:%H:%M:%S} -> {:%H:%M:%S} (+{})'.format(tup[0], tup[1], tup[2]))
