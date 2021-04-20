#!/usr/bin/env python3
""" Transfer Timetable source code """
import sys
from datetime import datetime, timedelta
from colorama import init, Fore


def main():
    """
    Main function when running
    """
    if sys.version_info.major < 3:
        print('This program supports Python 3 or higher.')
        return

    # read 2 file name arguments
    argc = len(sys.argv) - 1
    if argc < 3:
        print(
            ('Usage: ./transfer_timetable.py'
             ' <timetable1.txt> <timetable2.txt> <transfer_walk_minute>')
        )
        return

    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    transfer_walk_minute = float(sys.argv[3])

    # initial variables
    init()  # colorama init
    transfer_walk_time = timedelta(minutes=transfer_walk_minute)

    # # first file -> make timetable array
    # load info
    timetable1, timetable1_info = read_timetable(filename1)

    # # second file
    # load info
    timetable2, timetable2_info = read_timetable(filename2, allow_terminal=False)

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
    result = derive_transfer_timetable(timetable1, timetable2, transfer_walk_time)

    # print result
    for info in result:
        # set screen colors by degree
        if info['transfer_time_degree'] == 'high':
            print(Fore.RED, end='')   # Red
        elif info['transfer_time_degree'] == 'middle':
            print(Fore.WHITE, end='')   # White
        else:
            print(Fore.GREEN, end='')    # Green

        # print timeline
        print('{}\t{:%H:%M:%S}  ->  {}\t{:%H:%M:%S} (+{})'.format(
            info['before_transfer_train_bound'], info['before_transfer_train_time'],
            info['after_transfer_train_bound'], info['after_transfer_train_time'],
            info['transfer_time_needed']))

    # save result as a HTML file
    print(Fore.RESET)   # reset color
    response = input("Do you want to create a HTML file to save (y/n)? ")
    if response in ('Y', 'y'):
        write_html_file('result.html', result, timetable1_info,
                        timetable2_info, transfer_walk_time)


def derive_transfer_timetable(timetable1, timetable2, transfer_walk_time: timedelta):
    """
    Make the transfer (connection) timetable using 2 timetables and walking time.

    :param timetable1: a station timetable before transfer
    :param timetable2: a station timetable after transfer
    :param transfer_walk_time: estimated walking time to transfer (only allows timedelta type)
    :return: array of dictionaries containing each of the possible transfers
    """
    i = 0
    j = 0
    result = []
    while i < len(timetable1) and j < len(timetable2):
        # test if the [time1 + walk] and time2
        if timetable1[i]['time'] + transfer_walk_time <= timetable2[j]['time']:
            # transfer possible
            info = {
                'before_transfer_train_bound': timetable1[i]['bound_for'],
                'after_transfer_train_bound': timetable2[j]['bound_for'],
                'before_transfer_train_time': timetable1[i]['time'],
                'after_transfer_train_time': timetable2[j]['time'],
                'transfer_time_needed': timetable2[j]['time'] - timetable1[i]['time'],
                'transfer_time_degree': None
            }

            if info['transfer_time_needed'] > timedelta(minutes=10) + transfer_walk_time:
                # over 10 minutes + walk...
                info['transfer_time_degree'] = 'high'
            elif info['transfer_time_needed'] > timedelta(minutes=3) + transfer_walk_time:
                # over 3 minutes + walk...
                info['transfer_time_degree'] = 'middle'
            else:
                # less 3 minutes + walk...
                info['transfer_time_degree'] = 'low'

            result.append(info)
            i += 1
        else:
            # transfer impossible
            j += 1

    return result


def write_html_file(filepath, result, timetable1_info, timetable2_info, transfer_walk_time):
    """
    Write transfer timetable to HTML

    :param filepath: file name (and its parent directory) to save html file
    :param result: result of derived transfer timetable
    :param timetable1_info: information of timetable before transfer
    :param timetable2_info: information of timetable after transfer
    :param transfer_walk_time: estimated walking time to transfer (only allows timedelta type)
    """
    result_file = open(filepath, 'w', encoding='UTF8')

    # head of HTML
    result_file.write(
        ('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n'
         '<link rel="stylesheet" '
         'href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" '
         'integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" '
         'crossorigin="anonymous">\n'
         '<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" '
         'integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" '
         'crossorigin="anonymous"></script>\n'
         '<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" '
         'integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" '
         'crossorigin="anonymous"></script>\n'
         '<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" '
         'integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" '
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
         '<div class="row">\n<div class="col-md-12">\n'
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
            f'<tr>\n<th scope="row">{i + 1}</th>\n'
        )

        # set HTML <p> tag colors
        if info['transfer_time_degree'] == 'high':
            # Red
            result_file.write(
                (f'<td><p style="color:red">{info["before_transfer_train_bound"]}</p></td>\n'
                 '<td><p style="color:red">'
                 f'{"{:%H:%M:%S}".format(info["before_transfer_train_time"])}</p></td>\n'
                 f'<td><p style="color:red">{info["after_transfer_train_bound"]}</p></td>\n'
                 '<td><p style="color:red">'
                 f'{"{:%H:%M:%S}".format(info["after_transfer_train_time"])}</p></td>\n'
                 f'<td><p style="color:red">+{info["transfer_time_needed"]}</p></td>\n')
            )
        elif info['transfer_time_degree'] == 'middle':
            # Black
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
            # Green
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
    result_file.write(
        (
            '</tbody>\n</table>\n'
            '</div>\n</div>\n</div>\n'
            '</body>\n</html>\n'
        )
    )

    # file close and finish
    result_file.close()
    print(f'{filepath} saved.')


def read_timetable(filename, allow_terminal=True, exclude_bound_for=None):
    """
    Read timetable file and its information

    :param filename: file name you want to read as timetable
    :param allow_terminal: whether the train terminates in this station or not
    :param exclude_bound_for: list of destinations to exclude in timetable
    :return: timetable list and information
    """
    if exclude_bound_for is None:
        exclude_bound_for = []
    timetable = []
    timetable_info = {}

    # load info
    timetable_file = open(filename, 'r', encoding='UTF8')
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
        
        # filtering terminal
        if not allow_terminal:
            if timetable_info['station'] == bound_for:
                continue
            elif timetable_info['station'][-1:] == '역':
                if timetable_info['station'][:-1] == bound_for:
                    continue
            elif len(timetable_info['station']) <= 7:
                continue
            elif timetable_info['station'][-7:].lower() == 'station':
                if timetable_info['station'][:-7].lower() == bound_for.lower():
                    continue
                elif timetable_info['station'][-8] == '_':
                    if timetable_info['station'][:-8].lower() == bound_for.lower():
                        continue

        # filtering as train destination
        if bound_for in exclude_bound_for:
            continue

        timetable.append({
            'bound_for': bound_for,
            'time': datetime(2020, 1, 1+hour//24, hour % 24, minute, second)
        })
    timetable_file.close()

    return timetable, timetable_info


if __name__ == "__main__":
    main()
