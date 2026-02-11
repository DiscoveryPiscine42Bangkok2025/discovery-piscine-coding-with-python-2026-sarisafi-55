#!/usr/bin/env python3
import sys
# ไม่มี parameter
if len(sys.argv) == 1:
    print("none")
else:
    printed = False

    for word in sys.argv[1:]:
        if not word.endswith("ism"):
            print(word + "ism")
            printed = True

    # กรณีมี parameter แต่โดนข้ามหมด
    if not printed:
        print("none")

