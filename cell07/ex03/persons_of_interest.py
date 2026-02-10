#!/usr/bin/env python3

#!/usr/bin/env python3

def famous_births(people: dict):
    # เรียงตามปีเกิด (แปลงเป็น int ก่อน)
    sorted_people = sorted(
        people.values(),
        key=lambda p: int(p["date_of_birth"])
    )

    for person in sorted_people:
        print(
            f'{person["name"]} is a great scientist born in {person["date_of_birth"]}.'
        )


women_scientists = {
    "ada": {
        "name": "Ada Lovelace",
        "date_of_birth": "1815",
    },
    "cecilia": {
        "name": "Cecilia Payne",
        "date_of_birth": "1900",
    },
    "lise": {
        "name": "Lise Meitner",
        "date_of_birth": "1878",
    },
    "grace": {
        "name": "Grace Hopper",
        "date_of_birth": "1906",
    },
}

# 👇 สำคัญมาก: ต้องเรียกฟังก์ชัน
famous_births(women_scientists)
