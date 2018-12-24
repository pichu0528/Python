'''
Code challenge from HackerRank

Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Function Description

Complete the timeConversion function in the editor below. It should return a new 
string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

s: a string representing time in 12 hour format
'''

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == 'AM' and s[:2] == '12':
        return '00'+s[2:-2]
    elif s[-2:] == 'PM' and s[:2] == '12':
        return s[:-2]
    elif s[-2:] == 'PM':
        return str(int(s[:2])+12)+s[2:-2]
    elif s[-2:] == 'AM':
        return s[:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
