import sys
import os

data_path = "bakery.csv"


def show_sales(start_pos=0, end_pos=None):
    print(f'start_pos = {start_pos};  end_pos = {end_pos}')
    with open(data_path, "r", encoding='utf-8') as sales_data:
        for pos, line in enumerate(sales_data):
            if pos >= start_pos and (end_pos is None or pos <= end_pos):
                print(line.strip())


if not os.path.exists(data_path):
    print("data n/a")
    exit(1)

try:
    start_pos = int(sys.argv[1].strip())
except Exception:
    start_pos = 0

try:
    end_pos = int(sys.argv[2].strip())
except Exception:
    end_pos = None

show_sales(start_pos, end_pos)
