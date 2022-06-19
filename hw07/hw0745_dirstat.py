import os
import json

root_dir = os.path.join('C:', '\Program Files', 'Adobe')
file_stat_path = os.path.join(root_dir, os.path.basename(root_dir) + '_summary.json')
# file_stat_path = "_summary.json"

file_stat = {}
file_stat_extended = {}

for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        file_extension = file.split('.')[-1].lower()

        file_group = 10 ** len(str(file_size))

        file_stat.setdefault(file_group, 0)
        file_stat_extended.setdefault(file_group,  (0, []))

        file_stat[file_group] += 1

        extended_stat = file_stat_extended[file_group]
        if file_extension not in extended_stat[1]:
            extended_stat[1].append(file_extension)
        file_stat_extended[file_group] = (extended_stat[0] + 1, extended_stat[1])

with open(file_stat_path, 'w', encoding='utf-8') as f:
    json.dump(file_stat_extended, f)

print(file_stat_extended)
print(file_stat)