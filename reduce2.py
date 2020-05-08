#!/usr/bin/env python3

import sys
import os

storage = {}
last_name = ""


def do():
    dates = list(storage.keys())
    views = list(storage.values())
    total_views = 0
    first = 0
    second = 0
    for i in range(len(views)):
        total_views += views[i]
        if dates[i] < 20160603:
            first += views[i]
        else:
            second += views[i]
    if total_views >= 10:
        print(last_name + "\t" + str(dates) + "\t" + str(views) + "\t" + str(total_views) + "\t" + str(
            second - first))


for line in sys.stdin:
    try:
        words = line.split("}")
        name = "}".join(words[0:-1])
        [date, view] = words[-1].split()
        date = int(date)
        view = int(view)
        if last_name != name:
            if last_name != "":
                do()
                storage = {}
            last_name = name

        if date in storage:
            storage[date] += view
        else:
            storage[date] = view

    except:
        continue
do()
