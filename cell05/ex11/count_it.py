#!/usr/bin/env python3
import sys

# ถ้าไม่มี parameter
if len(sys.argv) == 1:
    print("none")
else:
    params = sys.argv[1:]          # ตัดชื่อไฟล์ออก
    print(f"parameters: {len(params)}")

    for p in params:
        print(f"{p}: {len(p)}")

