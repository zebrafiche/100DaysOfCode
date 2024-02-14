import csv
import os

print(os.getcwd())
with open('cafe-data.csv', mode='r', encoding='UTF-8', newline='') as csv_file:
    csv_view = csv.reader(csv_file, delimiter=',')
    for line in csv_view:
        print(line)
with open('cafe-data.csv', mode='a', encoding='UTF-8', newline='') as csv_file:
    csv_edit = csv.writer(csv_file, delimiter=',')
    line = ["North End", 'https://goo.gl/maps/ALR8iBiNN6tVfuAA8', '8AM', '1PM', '☕☕', '💪💪💪', '🔌🔌🔌']
    csv_edit.writerow(line)
with open('cafe-data.csv', mode='r', encoding='UTF-8', newline='') as csv_file:
    csv_view = csv.reader(csv_file, delimiter=',')
    for line in csv_view:
        print(line)
with open('cafe-data.csv', mode='r', encoding='UTF-8', newline='') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)
    print(list_of_rows)

