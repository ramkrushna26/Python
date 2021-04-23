

import sys
import os

with open('C:\\Users\\ramkrushna\\jobs.txt', 'r') as f:
    line = f.readline()
    cnt=0
    linecount=0
    exit_count = 0
    with open('C:\\Users\\ramkrushna\\jobs_1.txt', 'a') as wf:
        while line:   
            if cnt == 0:
                cnt += 1
                line = f.readline()
                continue
            linecount += 1
            if linecount == 1:
                str1=line.strip().split("#")
            if linecount == 2:
                str1.append(line.strip().split('"')[1])
            if linecount == 3:
                str1.append(line.split(' ')[2].strip())
            if linecount == 4:
                str1.append(line.strip().split('"')[1])
            if linecount == 5:
                str1.append(line.split(' ')[2].strip())
            if linecount == 6:
                str1.append(line.split(' ')[2])

            line = f.readline()
            cnt += 1
            if (cnt-1) % 8 == 0:
                linecount = 0
                #print(",".join(str1))
                wf.write(",".join(str1))
                str1=[]
            '''if line == "":
                exit_count += 1
                if exit_count == 3:
                    print(exit_count)
                    sys.exit()
            else:
                exit_count = 0
            '''
            '''if cnt == 41:
                #3104
                sys.exit()
            '''
    print(cnt)
    os.rename('C:\\Users\\ramkrushna\\jobs_1.txt', 'C:\\Users\\ramkrushna\\jobs_1.csv')
