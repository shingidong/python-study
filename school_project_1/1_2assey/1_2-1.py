import csv

messages_list = []

with open('/Users/shingidong/Desktop/1-2 자유주제탐구 보고서 수정본.csvcsv_file_path', mode='r', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    
    next(csv_reader)
    
    for row in csv_reader:
        messages_list.append(row[2])  
