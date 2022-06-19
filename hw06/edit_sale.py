import sys
import os

data_path = "bakery.csv"
data_tmp = "bakery.tmp"


def edit_sale_record(edit_pos, new_val):
    with open(data_path, "r+", encoding='utf-8') as sales_data,\
            open(data_tmp, "w", encoding='utf-8') as sales_tmp:
        for pos, line in enumerate(sales_data):
            sales_tmp.write(f'{new_val}\n' if pos == edit_pos else line)
    with open(data_path, "w", encoding='utf-8') as sales_data,\
            open(data_tmp, "r", encoding='utf-8') as sales_tmp:
        for line in sales_tmp:
            sales_data.write(line)
    os.remove(data_tmp)

if not os.path.exists(data_path):
    print("data n/a")
    exit(1)

if len(sys.argv) != 3:
    print("wrong parameters count")
    exit(1)

edit_pos = sys.argv[1].strip()
try:
    edit_pos = int(edit_pos)
except ValueError:
    print(f"{edit_pos} is wrong position")
    exit(2)

new_val = sys.argv[2].replace(",", ".").strip()
try:
    float(new_val)
except ValueError:
    print(f"{new_val} is wrong sale value")
    exit(2)

with open(data_path, "r", encoding='utf-8') as sales_data:
    lines_count = sum(1 for line in sales_data)

if not (edit_pos >= 0 and edit_pos < lines_count):
    print(f"{edit_pos} is out of range. There is {lines_count} sale records")
    exit(2)

edit_sale_record(edit_pos, new_val)
