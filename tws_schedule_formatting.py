

import sys
import os
import re

with open('C:\\Users\\ramkrushna\\schedules.txt', 'r') as f:
    line = f.readline()
    cnt=0
    linecount=0
    exit_count = 0
    str1 = []
    with open('C:\\Users\\ramkrushna\\schedules.txt', 'a') as wf:
        while line:
            if line.startswith('SCHEDULE'):
                str1.append(line.split('#')[1].strip())
            if line.startswith('DESCRIPTION'):
                str1.append(line.split('"')[1])
            if line.startswith('ON'):
                str1.append(re.sub(r"[,]", ";", line.strip()))
            if line.startswith('AT'):
                str1.append(line.strip())
            if line.startswith(':'):
                linecount += 1
            if line.startswith('HOSTNAME'):
                str1.append(line.strip())
            if line.startswith(' AT'):
                str1.append(line.strip())
            if line.startswith(' EVERY'):
                str1.append(line.strip())
            if line.startswith(' FOLLOWS'):
                str1.append(line.strip())
            if line.startswith('OPENS'):
                str1.append(line.strip())
            if line.startswith('END'):
                str1.append('\n')
                wf.write(','.join(str1))
                #print(','.join(str1))
                str1 = []
            
            line = f.readline()
            cnt += 1

    print(cnt)
    os.rename('C:\\Users\\ramkrushna\\schedules.txt', 'C:\\Users\\ramkrushna\\sched_1.csv')
