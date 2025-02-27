import os
import pandas as pd

label_path = "/Users/shingidong/Desktop/python-study/school_project_1/emengency/labels"
image_path = "/Users/shingidong/Desktop/python-study/school_project_1/emengency/images 1"
output_csv = "/Users/shingidong/Desktop/python-study/school_project_1/emengency/data/yolo_data.csv"  # ⬅ 파일명 추가


# 클래스 라벨이 정의된 파일 (선택 사항)
class_labels = {0: "medicine_1", 1: "medicine_2", 2: "medicine_3",3: "medicine_4",4: "medicine_5",5: "medicine_6"}  # ⬅ 필요에 따라 수정

# YOLO 형식 데이터를 저장할 리스트
data_list = []

# 라벨 폴더에서 모든 .txt 파일 읽기
for label_file in os.listdir(label_path):
    if label_file.endswith(".txt"):  # YOLO 라벨 파일만 처리
        file_path = os.path.join(label_path, label_file)
        image_filename = label_file.replace(".txt", ".jpg")  # 이미지 파일명 추정 (확장자는 다를 수도 있음)

        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5:  # YOLO 라벨 형식: class_id x_center y_center width height
                    class_id = int(parts[0])
                    x_center, y_center, width, height = map(float, parts[1:])

                    # 클래스 ID를 실제 클래스 이름으로 변환 (선택 사항)
                    class_name = class_labels.get(class_id, str(class_id))

                    # 데이터 저장
                    data_list.append([image_filename, class_id, class_name, x_center, y_center, width, height])

# Pandas 데이터프레임 생성
df = pd.DataFrame(data_list, columns=["image", "class_id", "class_name", "x_center", "y_center", "width", "height"])

# CSV 파일로 저장
df.to_csv(output_csv, index=False)

print(f"CSV 파일이 저장되었습니다: {output_csv}")