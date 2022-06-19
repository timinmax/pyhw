import sys

if len(sys.argv) != 2:
    print("wrong parameters count")
    exit(1)

sale_val = sys.argv[1].replace(",", ".")
try:
    float(sale_val)
except ValueError:
    print(f"{sys.argv[1]} is wrong sale value")
    exit(2)

with open("bakery.csv", 'a', encoding='utf-8') as sales_data:
    sales_data.write(f'{sale_val}\n')
