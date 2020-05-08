#!/usr/bin/env python3

import sys
import os

for line in sys.stdin:
    try:
        words = line.split("}")
        name = "}".join(words[0:-1])
        [date, views] = words[-1].split()
        date = str(date)
        views = str(views)

        print(name + "}" + date + " " + views)
    except:
        continue
