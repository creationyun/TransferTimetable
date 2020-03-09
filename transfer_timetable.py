#!/usr/bin/env python3
''' Transfer Timetable source code '''
import sys
from datetime import datetime, timedelta
from colorama import init, Fore


def main():
    ''' Main Function '''
    # read 2 file name arguments
    argc = len(sys.argv) - 1
    if argc < 3:
        print(
            ('Usage: ./transfer_timetable.py'
             ' <timetable1.txt> <timetable2.txt> <transfer_walk_minute>')
        )
        sys.exit(1)

    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    transfer_walk_minute = float(sys.argv[3])

    # initial variables
    init()  # colorama init
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
    print(
        (f'{timetable1_info["station"]} {timetable1_info["line"]}'
         f' ({timetable1_info["week"]}, {timetable1_info["direction"]})'
         f' -> {timetable2_info["station"]} {timetable2_info["line"]}'
         f' ({timetable2_info["week"]}, {timetable2_info["direction"]})'
         f' ({transfer_walk_minute} minutes)')
    )
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
        # set screen colors
        if info['transfer_time_needed'] > timedelta(minutes=10) + transfer_walk_time:
            # over 10 minutes + walk...
            print(Fore.RED, end='')   # Red
        elif info['transfer_time_needed'] > timedelta(minutes=3) + transfer_walk_time:
            # over 3 minutes + walk...
            print(Fore.WHITE, end='')   # White
        else:
            # less 3 minutes + walk...
            print(Fore.GREEN, end='')    # Green

        # print timeline
        print('{}\t{:%H:%M:%S}  ->  {}\t{:%H:%M:%S} (+{})'.format(
            info['before_transfer_train_bound'], info['before_transfer_train_time'],
            info['after_transfer_train_bound'], info['after_transfer_train_time'],
            info['transfer_time_needed']))

    # save result as a HTML file
    print(Fore.RESET)   # reset color
    print('Do you want to create a HTML file to save (y/n)? ', end='')
    response = input()
    if response in ('Y', 'y'):
        write_html_file(result, timetable1_info,
                        timetable2_info, transfer_walk_time)


def write_html_file(result, timetable1_info, timetable2_info, transfer_walk_time):
    ''' Write Timetable to HTML '''
    result_file = open('result.html', 'w')

    # head of HTML
    result_file.write(
        ('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n'
         '<link rel="stylesheet" '
         'href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" '
         'integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" '
         'crossorigin="anonymous">\n'
         '<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" '
         'integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" '
         'crossorigin="anonymous"></script>\n'
         '<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" '
         'integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" '
         'crossorigin="anonymous"></script>\n'
         '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" '
         'integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" '
         'crossorigin="anonymous"></script>\n'
         '<style>th {text-align:center;} '
         'td {text-align:center;} '
         'h3 {text-align:center;}</style>\n'
         '<title>TransferTimetable Results</title>\n'
         '</head>\n')
    )

    # body of HTML (title)
    result_file.write(
        ('<body>\n<div class="container-fluid">\n'
         f'<h3>{timetable1_info["station"]} {timetable1_info["line"]}'
         f' ({timetable1_info["week"]}, {timetable1_info["direction"]})'
         f' -> {timetable2_info["station"]} {timetable2_info["line"]}'
         f' ({timetable2_info["week"]}, {timetable2_info["direction"]})'
         f' ({transfer_walk_time.seconds / 60} minutes)</h3>\n<br>\n')
    )

    # body of HTML (table)
    result_file.write(
        ('<table class="table">\n<thead>\n<tr>\n'
         '<th scope="col"></th>\n'
         '<th scope="col" colspan="2">Before Transfer</th>\n'
         '<th scope="col" colspan="2">After Transfer</th>\n'
         '<th scope="col"></th>\n'
         '</tr>\n'
         '<tr>\n'
         '<th scope="col">#</th>\n'
         '<th scope="col">Bound for</th>\n'
         '<th scope="col">Arrival time</th>\n'
         '<th scope="col">Bound for</th>\n'
         '<th scope="col">Arrival time</th>\n'
         '<th scope="col">Wait time</th>\n'
         '</tr>\n</thead>\n<tbody>\n')
    )

    for i, info in enumerate(result):
        # start of row
        result_file.write(
            (f'<tr>\n<th scope="row">{i + 1}</th>\n')
        )

        # set HTML <p> tag colors
        if info['transfer_time_needed'] > timedelta(minutes=10) + transfer_walk_time:
            # over 10 minutes + walk... => Red
            result_file.write(
                (f'<td><p style="color:red">{info["before_transfer_train_bound"]}</p></td>\n'
                 '<td><p style="color:red">'
                 f'{"{:%H:%M:%S}".format(info["before_transfer_train_time"])}</p></td>\n'
                 f'<td><p style="color:red">{info["after_transfer_train_bound"]}</p></td>\n'
                 '<td><p style="color:red">'
                 f'{"{:%H:%M:%S}".format(info["after_transfer_train_time"])}</p></td>\n'
                 f'<td><p style="color:red">+{info["transfer_time_needed"]}</p></td>\n')
            )
        elif info['transfer_time_needed'] > timedelta(minutes=3) + transfer_walk_time:
            # over 3 minutes + walk... => Black
            result_file.write(
                (f'<td><p style="color:black">{info["before_transfer_train_bound"]}</p></td>\n'
                 '<td><p style="color:black">'
                 f'{"{:%H:%M:%S}".format(info["before_transfer_train_time"])}</p></td>\n'
                 f'<td><p style="color:black">{info["after_transfer_train_bound"]}</p></td>\n'
                 '<td><p style="color:black">'
                 f'{"{:%H:%M:%S}".format(info["after_transfer_train_time"])}</p></td>\n'
                 f'<td><p style="color:black">+{info["transfer_time_needed"]}</p></td>\n')
            )
        else:
            # less 3 minutes + walk... => Green
            result_file.write(
                (f'<td><p style="color:green">{info["before_transfer_train_bound"]}</p></td>\n'
                 '<td><p style="color:green">'
                 f'{"{:%H:%M:%S}".format(info["before_transfer_train_time"])}</p></td>\n'
                 f'<td><p style="color:green">{info["after_transfer_train_bound"]}</p></td>\n'
                 '<td><p style="color:green">'
                 f'{"{:%H:%M:%S}".format(info["after_transfer_train_time"])}</p></td>\n'
                 f'<td><p style="color:green">+{info["transfer_time_needed"]}</p></td>\n')
            )

        # end of row
        result_file.write('</tr>\n')

    # foot of HTML
    result_file.write('</tbody>\n</table>\n</div>\n</body>\n</html>\n')

    # file close and finish
    result_file.close()
    print('result.html saved.')


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
