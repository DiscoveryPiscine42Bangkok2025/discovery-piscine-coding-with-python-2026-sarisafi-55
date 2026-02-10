#!/usr/bin/env python3

def average(class_scores):
    total = sum(class_scores.values())
    count = len(class_scores)
    return total / count


# ทดสอบตามโจทย์
if __name__ == "__main__":
    class_3B = {
        "marie": 18,
        "jean": 15,
        "coline": 8,
        "luci": 9
    }

    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }

    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")
