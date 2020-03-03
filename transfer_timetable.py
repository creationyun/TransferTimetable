''' Transfer Timetable source code '''
import sys
from datetime import datetime, timedelta


def main():
    ''' Main Function '''
    # read 2 file name arguments
    argc = len(sys.argv) - 1
    if argc < 3:
        print('Usage: python timetable_transfer.py \
<timetable1.txt> <timetable2.txt> <transfer_walk_minute>')
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
    timetable1, timetable1_info = read_timetable(filename1)

    # # second file
    # load info
    timetable2, timetable2_info = read_timetable(filename2)

    # comparison station1 -> station2
    print('Transfer Timetable Result')
    print(f'\
{timetable1_info["station"]} {timetable1_info["line"]} ({timetable1_info["week"]}, {timetable1_info["direction"]}) \
 -> {timetable2_info["station"]} {timetable2_info["line"]} ({timetable2_info["week"]}, {timetable2_info["direction"]}) \
({transfer_walk_minute} minutes)')
    print()
    i = 0
    j = 0
    result = []
    while i < len(timetable1) and j < len(timetable2):
        # test if the [time1 + walk] and time2
        if timetable1[i]['time'] + transfer_walk_time <= timetable2[j]['time']:
            # transfer possible
            result.append({
                'before_transfer_train_bound': timetable1[i]['bound_for'],
                'after_transfer_train_bound': timetable2[j]['bound_for'],
                'before_transfer_train_time': timetable1[i]['time'],
                'after_transfer_train_time': timetable2[j]['time'],
                'transfer_time_needed': timetable2[j]['time'] - timetable1[i]['time']
            })
            i += 1
        else:
            # transfer impossible
            j += 1

    # print result
    for info in result:
        # set colors
        if info['transfer_time_needed'] > timedelta(minutes=10) + transfer_walk_time:
            # over 10 minutes + walk...
            print('\033[38;5;160m', end='')   # Red
        elif info['transfer_time_needed'] > timedelta(minutes=3) + transfer_walk_time:
            # over 3 minutes + walk...
            print('\033[38;5;255m', end='')   # White
        else:
            # less 3 minutes + walk...
            print('\033[38;5;40m', end='')    # Green

        # print timeline
        print('{}\t{:%H:%M:%S}  ->  {}\t{:%H:%M:%S} (+{})'.format(
            info['before_transfer_train_bound'], info['before_transfer_train_time'],
            info['after_transfer_train_bound'], info['after_transfer_train_time'],
            info['transfer_time_needed']))

    # save result as a file
    print('\033[0m')   # reset color
    print('Do you want to create a file to save (y/n)? ', end='')
    response = input()
    if response in ('Y', 'y'):
        result_file = open('result.txt', 'w')
        for info in result:
            result_file.write('{}\t{:%H:%M:%S}  ->  {}\t{:%H:%M:%S} (+{})\n'.format(
                info['before_transfer_train_bound'], info['before_transfer_train_time'],
                info['after_transfer_train_bound'], info['after_transfer_train_time'],
                info['transfer_time_needed']))
        result_file.close()
        print('result.txt saved.')


def read_timetable(filename):
    '''file -> make timetable array'''
    timetable = []
    timetable_info = {}

    # load info
    timetable_file = open(filename, 'r')
    timetable_info['station'], timetable_info['line'], timetable_info[
        'week'], timetable_info['direction'] = timetable_file.readline().split()

    # read timetable
    while True:
        line = timetable_file.readline()
        if not line:
            break
        # time format: %H:%M:%S
        # but, %H can be 24 (12 am) or 25 (1 am)
        bound_for, train_time = line.split()
        timesplit = train_time.split(':')
        hour = int(timesplit[0])
        minute = int(timesplit[1])
        second = int(timesplit[2])
        timetable.append({
            'bound_for': bound_for,
            'time': datetime(2020, 1, 1+hour//24, hour % 24, minute, second)
        })
    timetable_file.close()

    return timetable, timetable_info


if __name__ == "__main__":
    main()
