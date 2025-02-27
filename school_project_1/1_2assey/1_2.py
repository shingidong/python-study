import csv
from collections import Counter
import pandas as pd

print("프로그램 시작")

# CSV 파일 경로 설정
file_path = r"/Users/shingidong/Documents/kakao/1.2message.csv"

# 메시지를 저장할 리스트
messages_list = []

# CSV 파일 열기 및 메시지 추출
with open(file_path, mode='r', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # 첫 번째 줄(헤더) 건너뛰기
    
    # 모든 메시지를 한 번에 추출 (메시지가 첫 번째 열에 있으므로 row[0] 사용)
    for row in csv_reader:
        if len(row) > 0:
            messages_list.append(row[0])  # 메시지 열이 첫 번째 열에 있음

# 모든 메시지를 하나의 텍스트로 결합
all_messages = ' '.join(messages_list)

# 단어 단위로 분리
words = all_messages.split()

# 단어 빈도 계산
word_counts = Counter(words)

# DataFrame으로 변환하여 상위 10개 단어 확인
word_counts_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency']).sort_values(by='Frequency', ascending=False)

# 상위 10개 단어 출력
print(word_counts_df.head(10))