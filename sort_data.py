import re
import csv
with open('recordings.csv', 'r', encoding='utf-8') as file:
    content = file.read()

d = {}
newline_split = content.split('\n')

for i in newline_split:
    if(i!=''):
        split_string = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', i)
        split_string = [item.strip('"').strip() for item in split_string]   
        d[split_string[0]] = {'count': split_string[1], 'french': split_string[2]}

def extract_numeric_count(item):
    key, value = item
    try:
        return int(value['count'])
    except ValueError:
        return float('inf')

sorted_items = sorted(d.items(), key=extract_numeric_count, reverse=True)
sorted_dict = {k: v for k, v in sorted_items}
print('sorted_dict: ', sorted_dict)

with open("sorted_recordings.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    for key, value in sorted_dict.items():
        writer.writerow([key, value['count'], value['french']])