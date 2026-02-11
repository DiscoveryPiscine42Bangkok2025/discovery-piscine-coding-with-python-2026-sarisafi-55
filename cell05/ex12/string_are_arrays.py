#!/usr/bin/env python3
import sys
# ต้องมี parameter แค่ 1 ตัว
if len(sys.argv) != 2:
    print("none")
else:
    s = sys.argv[1]
    count = 0

    for ch in s:
        if ch == 'z':
            count += 1

    if count == 0:
        print("none")
    else:
        print('z' * count)

