#!/usr/bin/env python
import os
import datetime
import re
import statistics
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20, 3)

def parse_result(results_fd):
    thetime = parse_time(results_fd.readline().strip())
    ping = parse_speed(results_fd.readline().strip())
    download = parse_speed(results_fd.readline().strip())
    upload = parse_speed(results_fd.readline().strip())
    return [thetime, ping, download, upload]

def parse_time(timestring):
    splitted = timestring.split('-')
    thetime = '2017-06-' + splitted[0] + ' ' + splitted[1]
    return datetime.datetime.strptime(thetime, '%Y-%m-%d %H:%M:%S')

def parse_speed(speed_string):
    return float(re.findall(':\s+(\d+\.\d+)', speed_string)[0])

with open('latestresults.log', 'r') as results_fd:
    results = []
    times = []
    pings = []
    downloads = []
    uploads = []
    parsed = 0
    while True:
        try:
            temp = parse_result(results_fd)
            parsed += 1
            results.append(temp)
            times.append(temp[0])
            pings.append(temp[1])
            downloads.append(temp[2])
            uploads.append(temp[3])
        except Exception as e:
            print('Parsed {}'.format(parsed))
            print(e)
            break
    print(statistics.mean(downloads))
    print(statistics.mean(uploads))
    print(statistics.median(downloads))
    print(statistics.median(uploads))
    print(statistics.pvariance(downloads))
    print(statistics.pvariance(uploads))
    print(statistics.pstdev(downloads))
    print(statistics.pstdev(uploads))
    plt.plot(times, downloads, 'r-', label='Downloads')
    plt.plot(times, uploads, 'b-', label='Uploads')
    plt.plot(times, pings, 'g-', label='Pings')
    plt.legend(loc='best')
    plt.savefig('graph.png')
    plt.close()
