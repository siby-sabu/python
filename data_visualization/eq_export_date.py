import json
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    file_cnt = json.load(f)
    # print(file_cnt)
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(file_cnt, f, indent=4)

