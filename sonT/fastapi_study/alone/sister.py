from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3

# FastAPI 앱 생성
app = FastAPI(title="누나 멍청이 누나 바보 API")

# SQLite 데이터베이스 연결
conn = sqlite3.connect("nuna.db", check_same_thread=False)
cursor = conn.cursor()

# 데이터베이스 테이블 생성 (메시지 기록)
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT NOT NULL
)
""")
conn.commit()

# 🎭 모델 정의
class Message(BaseModel):
    message: str

# 📢 1️⃣ 메시지 저장 (누나에게 남긴 말)
@app.post("/messages/", response_model=Message)
async def save_message(msg: Message):
    cursor.execute("INSERT INTO messages (message) VALUES (?)", (msg.message,))
    conn.commit()
    return msg

# 📜 2️⃣ 메시지 조회
@app.get("/messages/", response_model=List[Message])
async def get_messages():
    cursor.execute("SELECT message FROM messages")
    messages = [Message(message=row[0]) for row in cursor.fetchall()]
    return messages

# 🎭 3️⃣ 누나의 특징 조회
@app.get("/nuna-traits/")
async def get_nuna_traits():
    traits = {
        "장점": ["똑똑함", "밥 사줌 (가끔)", "MZ 감성 충만", "문화생활 즐김"],
        "단점": ["라면 안 먹음", "집에 잘 안 옴", "SNS 중독", "틱톡 챌린지 찍음"]
    }
    return traits

# 📸 4️⃣ 누나의 서울 라이프 분석
@app.get("/nuna-seoul-life/")
async def get_nuna_seoul_life():
    activities = {
        "서울 간 누나의 일상": [
            "☕ 홍대 카페 투어",
            "💄 명동에서 쇼핑",
            "🎤 노래방에서 고음 도전",
            "📸 인스타 스토리 업로드",
            "🍕 새벽에 배달음식 시킴"
        ]
    }
    return activities

# 🏃 실행 방법
# 터미널에서 실행: uvicorn nuna_backend:app --reload