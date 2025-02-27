import pandas as pd
import torch
from sklearn.model_selection import train_test_split # type: ignore
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from torch.utils.data import Dataset

# 1. 데이터 준비
data = {
    "Symptom": [
        "머리가 너무 아프고 속이 울렁거려요",  # 두통
        "기침이 너무 심하고 목이 따가워요",  # 기침
        "열이 나고 온몸이 으슬으슬 떨려요",  # 발열
        "배가 아프고 토할 것 같아요",        # 복통
        "가래가 많이 끓고 숨이 차요",        # 가래
        "피부에 붉은 반점이 생기고 간지러워요"  # 피부 발진
    ],
    "Disease": [
        "편두통",
        "기관지염",
        "감기",
        "소화불량",
        "폐렴",
        "알레르기"
    ],
    "Medication": [
        "아세트아미노펜(타이레놀)",
        "덱스트로메토르판",
        "이부프로펜",
        "알마겔",
        "암브록솔",
        "항히스타민제"
    ]
}

df = pd.DataFrame(data)

# 2. 데이터셋 클래스 정의
class SymptomDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        encoding = self.tokenizer(
            text,
            max_length=self.max_len,
            padding='max_length',
            truncation=True,
            return_tensors="pt"
        )
        return {
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_mask"].squeeze(0),
            "labels": torch.tensor(label, dtype=torch.long)
        }

# 3. 데이터 분할 및 전처리
train_texts, val_texts, train_labels, val_labels = train_test_split(
    df['Symptom'], df.index, test_size=0.2, random_state=42
)

# BERT 모델과 토크나이저 로드
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=len(df['Disease'].unique()))

# 데이터셋 생성
train_dataset = SymptomDataset(train_texts.tolist(), train_labels.tolist(), tokenizer, max_len=32)
val_dataset = SymptomDataset(val_texts.tolist(), val_labels.tolist(), tokenizer, max_len=32)

# 4. 학습 설정
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs",
    save_total_limit=1,
    load_best_model_at_end=True
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset
)

# 5. 모델 학습
trainer.train()

# 6. 추론 함수
def predict_disease(input_text):
    encoding = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True, max_length=32)
    outputs = model(**encoding)
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=1).item()

    # 질병 및 약 추천
    disease = df.iloc[prediction]["Disease"]
    medication = df.iloc[prediction]["Medication"]
    return f"추천 질병: {disease}\n추천 약: {medication}"

# 사용자 입력 테스트
print("증상 관련 문장을 입력하세요:")
user_input = input()
result = predict_disease(user_input)
print(result)