# 필요한 라이브러리 다시 불러오기
import numpy as np
import time
from scipy.spatial import cKDTree
from sklearn.neighbors import BallTree, NearestNeighbors
import matplotlib.pyplot as plt

# 🔹 실험용 데이터 생성 함수
def generate_data(n_samples=1000, dim=2):
    return np.random.rand(n_samples, dim)  # 0~1 사이 랜덤값

# 🔹 KNN 검색 수행 및 실행 시간 측정
def knn_search(tree, query_points, k=5):
    start_time = time.time()
    distances, indices = tree.query(query_points, k)
    elapsed_time = (time.time() - start_time) * 1000  # 밀리초(ms) 변환
    return elapsed_time

# 🔹 KNN (Brute-Force) 검색 수행 및 실행 시간 측정
def knn_brute_force(data, query_points, k=5):
    start_time = time.time()
    nn = NearestNeighbors(n_neighbors=k, algorithm="brute").fit(data)
    nn.kneighbors(query_points)
    elapsed_time = (time.time() - start_time) * 1000  # 밀리초(ms) 변환
    return elapsed_time

# 🔹 KD-트리 vs 볼-트리 vs KNN Brute-Force 성능 비교 함수
def compare_knn_efficiency(dimensions=[2, 3, 10], n_samples=1000, n_queries=100, k=5):
    results = []
    
    for dim in dimensions:
        print(f"\n📌 {dim}차원 공간에서 KNN 성능 비교 중...")
        
        # 랜덤 데이터 생성
        data = generate_data(n_samples, dim)
        queries = generate_data(n_queries, dim)
        
        # ✅ KD-트리 구축 및 KNN 검색
        kd_tree = cKDTree(data)
        kd_time = knn_search(kd_tree, queries, k)
        
        # ✅ 볼-트리 구축 및 KNN 검색
        ball_tree = BallTree(data)
        ball_time = knn_search(ball_tree, queries, k)
        
        # ✅ Brute-Force (기본 KNN) 검색
        brute_time = knn_brute_force(data, queries, k)
        
        # 결과 저장
        results.append((dim, kd_time, ball_time, brute_time))
        print(f"✅ KD-트리 ({dim}D) 평균 검색 시간: {kd_time:.5f} ms")
        print(f"✅ 볼-트리 ({dim}D) 평균 검색 시간: {ball_time:.5f} ms")
        print(f"✅ 일반KNN ({dim}D) 평균 검색 시간: {brute_time:.5f} ms")
    
    return results

# 🔹 KNN 성능 비교 실행
knn_results = compare_knn_efficiency()

# 🔹 결과를 시각화
dimensions, kd_times, ball_times, brute_times = zip(*knn_results)

plt.figure(figsize=(8,5))
plt.plot(dimensions, kd_times, label="KD-Tree", marker='o')
plt.plot(dimensions, ball_times, label="Ball-Tree", marker='s')
plt.plot(dimensions, brute_times, label="일반KNN", marker='^', linestyle="--")
plt.xlabel("차원 (D)")
plt.ylabel("KNN 검색 시간 (ms)")
plt.title("KD-트리 vs 볼-트리 vs 일반KNN 성능 비교")
plt.legend()
plt.grid(True)
plt.show()