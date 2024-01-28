import csv
import os
def create_dir():
    if not os.path.isdir("images"):
        os.mkdir("images")
def get_table_head():
    table = []
    with open('good.csv', encoding='utf-8') as file:
        reader_object = csv.reader(file, delimiter=";")
        for row in reader_object:
            table.append(row)
    return table[0]
def write_table_head(table_head):
    with open("goods.csv", "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(table_head)
def write_table(table):
    with open("goods.csv", "a", encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=",")
        for i in table:
            writer.writerow(i)