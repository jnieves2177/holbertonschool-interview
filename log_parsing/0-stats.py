#!/usr/bin/python3
"""This script gets stats from a request"""

from collections import Counter
from sys import stdin


line_number = 1
total_file_size = 0
status_code_counts = Counter()

try:
    for line in stdin:
        if len(line) == 1:
            break

        try:
            status_code, file_size = line.split()[-2:]
            total_file_size += int(file_size)
            status_code_counts[int(status_code)] += 1
        except ValueError:
            pass

        if line_number % 10 == 0:
            print('File size:', total_file_size)
            for code, count in sorted(status_code_counts.items()):
                print('{}: {}'.format(code, count))

        line_number += 1
except KeyboardInterrupt:
    pass
finally:
    print('File size:', total_file_size)
    for code, count in sorted(status_code_counts.items()):
        print('{}: {}'.format(code, count))
