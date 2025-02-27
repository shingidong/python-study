import csv
from col lections import Counter
import  s as pd
# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline


tokenizer = AutoTokenizer.from_pretrained("hun3359/klue-bert-base-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("hun3359/klue-bert-base-sentiment")
pipe = pipeline("text-classification",model="hun3359/klue-bert-base-sentiment")

print("프로그램 시작")

# CSV 파일 경로 설정
file_path = r"/Users/shingidong/Documents/kakao/1.2message.csv"

include_words = ['사진', '이모티콘', '동영상', '삭제된', '메시지입니다']

# 메시지를 저장할 리스트
messages_list = []

# CSV 파일 열기 및 메시지 추출
with open(file_path, mode='r', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # 첫 번째 줄(헤더) 건너뛰기
    
    # 모든 메시지를 한 번에 추출 (메시지가 첫 번째 열에 있음)
    for row in csv_reader:
        if len(row) > 0:
            messages_list.append(row[0])  # 첫 번째 열에 있는 메시지 추출 

# VADER 감정 분석기 초기화

# 감정 분석 결과 저장할 리스트
sentiments = []

# 감정 분석 수행
for message in messages_list:
    try:
      sentiment = pipe(message)  # VADER로 감정 점수 계산
      sentiments.append((message, sentiment[0]['label']))  # 메시지와 감정 점수를 함께 저장
    except Exception as e:
      print(f"Error processing message: {message}")
      print(f"Error details: {e}")

# 감정 분석 결과 출력 (첫 5개)
for message, sentiment in sentiments[:5]:
    print(f"Message: {message}")
    print(f"Sentiment: {sentiment}")
    print("-" * 30)

# 모든 메시지를 하나의 텍스트로 결합하여 단어 빈도 분석
all_messages = ' '.join([message for message, _ in sentiments])
words = all_messages.split()

# 단어 빈도 계산
word_counts = Counter(words)

# DataFrame으로 변환하여 상위 10개 단어 확인
word_counts_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency']).sort_values(by='Frequency', ascending=False)

# 상위 10개 단어 출력
print(word_counts_df.head(10))