import csv

# CSV 파일 경로 설정
file_path = r"/Users/shingidong/Documents/kakao/1.2message.csv"

# CSV 파일 열기 및 각 행 출력
with open(file_path, mode='r', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    
    # 첫 번째 줄(헤더) 출력
    header = next(csv_reader)
    print("Header:", header)
    
    # 첫 번째 데이터 행 확인
    first_data_row = next(csv_reader)
    print("First data row:", first_data_row)