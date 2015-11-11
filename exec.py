#!/usr/bin/env python
import os
import random

map=tuple(open("map"))

commits=5

for week in range(52):
    for day in range(7):
        if map[day][week]=='#':
            rel_day=(52-week)*7-day
            print(week,day,rel_day)
            commits2=random.randrange(commits-2,commits+2)
            for c in range(commits2):
                hour = random.randrange(0,24)
                minutes = random.randrange(0,60)
                seconds = random.randrange(0,60)
                command = 'git commit --allow-empty --allow-empty-message -m "" --date="last Sunday -'+ str(rel_day)+' days '+str(hour)+':'+str(minutes)+':'+str(seconds)+'"'
                print(command)
                os.system(command)
