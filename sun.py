import geopandas as gpd
import matplotlib.pyplot as plt
from rasterio.plot import show
import rasterio

# 일조량 데이터를 불러오기
sunlight_data = rasterio.open('path_to_sunlight_data.tif')

# 대한민국 지형 데이터 불러오기
korea_map = gpd.read_file('path_to_korea_shapefile.shp')

# 지도에 일조량 데이터 오버레이
fig, ax = plt.subplots(figsize=(10, 10))
korea_map.plot(ax=ax, color='white', edgecolor='black')
show(sunlight_data, ax=ax, cmap='OrRd', alpha=0.5)
plt.title('Solar Irradiance in South Korea')
plt.show()