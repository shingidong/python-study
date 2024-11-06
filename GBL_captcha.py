import streamlit as st
import sqlite3
from PIL import Image
import os
import random

conn = sqlite3.connect('image_labeling.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS labeling_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_name TEXT,
    grid_x INTEGER,
    grid_y INTEGER,
    is_damaged BOOLEAN
)
''')
conn.commit()

# 'images' 폴더에서 이미지 로드
def load_images(folder_path='images'):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpeg") or filename.endswith(".png"):
            images.append(os.path.join(folder_path, filename))
    return images

def reset_checkbox_states():
    for key in list(st.session_state.keys()):
        if key.startswith("checkbox_"):
            del st.session_state[key]

def mark_as_submitted():
    st.session_state.submitted = True

def display_image_grid(image_path, image_name):
    # 새로운 이미지가 로드되면 기존 체크박스 상태 초기화
    if "submitted" in st.session_state:
        print(st.session_state.submitted)
    
    if not "submitted" in st.session_state or not st.session_state.submitted:
        reset_checkbox_states()
        st.session_state.current_image = image_name  # 현재 이미지를 세션에 저장

    image = Image.open(image_path)
    width, height = image.size
    cell_width = width // 4
    cell_height = height // 4

    st.write("손상된 블록을 선택하세요")

    with st.form("labeling_form"):
        for i in range(4):
            cols = st.columns(4)
            for j in range(4):
                cell = image.crop(
                    (j * cell_width, i * cell_height, (j + 1) * cell_width, (i + 1) * cell_height)
                )
                with cols[j]:
                    st.image(cell, use_column_width=True)
                    cell_key = f"checkbox_{image_name}_{i}_{j}"
                    if cell_key not in st.session_state:
                        st.session_state[cell_key] = False
                    st.checkbox(f"손상됨 ({i},{j})", key=cell_key)

        submitted = st.form_submit_button("선택 저장", on_click=mark_as_submitted)

    if "submitted" in st.session_state and st.session_state.submitted:
        st.write("폼이 제출되었습니다!")  # 디버깅용 출력
        # 세션에서 `current_image`와 체크박스 상태를 가져와 저장
        saved_image_name = st.session_state.current_image  # 제출된 이미지 이름을 저장
        for i in range(4):
            for j in range(4):
                cell_key = f"checkbox_{saved_image_name}_{i}_{j}"
                is_damaged = st.session_state.get(cell_key, False)
                c.execute("INSERT INTO labeling_data (image_name, grid_x, grid_y, is_damaged) VALUES (?, ?, ?, ?)",
                          (saved_image_name, i, j, is_damaged))
        conn.commit()
        st.success("선택이 저장되었습니다!")

        # 상태 초기화
        st.session_state.submitted = False

        st.rerun()
        # reset_checkbox_states()

st.title("보도블록 손상 라벨링")

images = load_images()

if images:
    selected_image = random.choice(images)
    image_name = os.path.basename(selected_image)
    display_image_grid(selected_image, image_name)
else:
    st.error("이미지를 찾을 수 없습니다. 'images' 폴더에 이미지를 추가하세요.")

st.write("손상된 블록 라벨링에 참여해주셔서 감사합니다.")