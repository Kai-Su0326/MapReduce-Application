#!/usr/bin/env python3

import os
import sys
last_date = "20160601"
last_name = ""
sum_view = 0
for line in sys.stdin:
    try:
        words = line.split("}")
        date = str(words[0])
        views = int(words[-1])
        name = "}".join(words[1:-1])

        if last_date != date or last_name != name:
            if last_name != "":
                print(str(last_name) + "}" + str(last_date) + " " + str(sum_view))
                sum_view = 0
            last_date = date
            last_name = name

        sum_view += views

    except:
        continue

print(str(last_name) + "}" + str(last_date) + " " + str(sum_view))
