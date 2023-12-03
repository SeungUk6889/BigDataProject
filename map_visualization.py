import folium
import json
import pandas as pd

# 서울의 좌표
seoul_coordinates = [37.5665, 126.9780]

# 서울을 중심으로 하는 지도 생성
m = folium.Map(location=seoul_coordinates, zoom_start=11)

# GeoJSON 파일을 'utf-8' 인코딩으로 읽기
with open('seouldong.json', 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)

# 읽은 데이터를 GeoJson에 추가
folium.GeoJson(
    geojson_data,
    name='geojson',
    style_function=lambda feature: {
        'fillColor': 'grey',
        'color': 'black',
        'weight': 1,
        'dashArray': '0, 0',
        'fillOpacity': 1
    }
).add_to(m)

# CSV 파일 읽기
df = pd.read_csv('C:/Users/JY/Desktop/data/ALL.csv', encoding='euc-kr')  # 여기에 CSV 파일 경로를 입력하세요

# DataFrame에서 좌표를 읽어와 마커 추가
for _, row in df.iterrows():
    folium.Circle(
        location=[row['Latitude'], row['Longitude']],
        radius=50,  # 원의 반지름을 설정합니다.
        color='#FFEBF0',  # 원의 테두리 색상을 설정합니다.
        fill=True,
        fill_color='#FFEBF0'  # 원의 내부 색상을 설정합니다.
    ).add_to(m)

# 어두운 백그라운드 설정
folium.TileLayer('cartodbpositron').add_to(m)



# 마커 추가
folium.CircleMarker(
    [37.65916,127.0732],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)


folium.CircleMarker(
    [37.4983835,127.1458778],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)
# folium.Circle(
#             [37.66566 ,127.037081],
#             radius=500,
#             color='red',
#             fill_color='red',
#             fill_opacity='1'
#             ).add_to(m)

folium.CircleMarker(
    [37.66566 ,127.037081],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)

folium.CircleMarker(
    [37.579782 ,127.038324],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)

folium.CircleMarker(
    [37.58052,127.038452],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)

folium.CircleMarker(
    [37.580244,127.040586],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)


folium.CircleMarker(
    [37.580304, 127.040709],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)

folium.CircleMarker(
    [37.580851 , 127.040534],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)


folium.CircleMarker(
    [37.580822 , 127.04057],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)

folium.CircleMarker(
    [37.58687,127.04133],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)

folium.CircleMarker(
    [37.586652,127.041548],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)


folium.CircleMarker(
    [37.601276,127.080518],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)

folium.CircleMarker(
    [37.605642,127.095381],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)

folium.CircleMarker(
    [37.605491,127.095389],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)

folium.CircleMarker(
    [37.497731,127.146429],
    radius=10,  # 원의 반지름을 설정합니다. 필요에 따라 조절 가능합니다.
    color='#cc0000',  # 원의 테두리 색상을 설정합니다.
    fill=True,
    fill_color='#cc0000',  # 원의 내부 색상을 설정합니다.
    fill_opacity='1'
).add_to(m)

# 지도를 HTML 파일로 저장
m.save('map.html')

# import folium
# import json
# import pandas as pd
#
# # 서울의 좌표
# seoul_coordinates = [37.5665, 126.9780]
#
# # 서울을 중심으로 하는 지도 생성
# m = folium.Map(location=seoul_coordinates, zoom_start=11)
#
# # GeoJSON 파일을 'utf-8' 인코딩으로 읽기
# with open('seouldong.json', 'r', encoding='utf-8') as f:
#     geojson_data = json.load(f)
#
# # 읽은 데이터를 GeoJson에 추가
# folium.GeoJson(
#     geojson_data,
#     name='geojson',
#     style_function=lambda feature: {
#         'fillColor': 'grey',
#         'color': 'black',
#         'weight': 1,
#         'dashArray': '0, 0',
#         'fillOpacity': 1
#     }
# ).add_to(m)
#
# # CSV 파일 읽기
# df = pd.read_csv('C:/Users/JY/Desktop/data/bokji5.csv', encoding='euc-kr')  # 여기에 CSV 파일 경로를 입력하세요
#
# # DataFrame에서 좌표를 읽어와 마커 추가
# for _, row in df.iterrows():
#     folium.Circle(
#         location=[row['Latitude'], row['Longitude']],
#         radius=50,  # 원의 반지름을 설정합니다.
#         color='#FFB399',  # 원의 테두리 색상을 설정합니다.
#         fill=True,
#         fill_color='#FFB399'  # 원의 내부 색상을 설정합니다.
#     ).add_to(m)
#
#     # 어두운 백그라운드 설정
# folium.TileLayer('cartodbpositron').add_to(m)
# m.save('mapBokji.html')

# import folium
# import json
# import pandas as pd
#
# # 서울의 좌표
# seoul_coordinates = [37.5665, 126.9780]
#
# # 서울을 중심으로 하는 지도 생성
# m = folium.Map(location=seoul_coordinates, zoom_start=11)
#
# # GeoJSON 파일을 'utf-8' 인코딩으로 읽기
# with open('seouldong.json', 'r', encoding='utf-8') as f:
#     geojson_data = json.load(f)
#
# # 읽은 데이터를 GeoJson에 추가
# folium.GeoJson(
#     geojson_data,
#     name='geojson',
#     style_function=lambda feature: {
#         'fillColor': 'grey',
#         'color': 'black',
#         'weight': 1,
#         'dashArray': '0, 0',
#         'fillOpacity': 1
#     }
# ).add_to(m)
#
# # CSV 파일 읽기
# df = pd.read_csv('C:/Users/JY/Desktop/data/gyotongryang.csv', encoding='euc-kr')  # 여기에 CSV 파일 경로를 입력하세요
#
# # DataFrame에서 좌표를 읽어와 마커 추가
# for _, row in df.iterrows():
#     folium.Circle(
#         location=[row['Latitude'], row['Longitude']],
#         radius=50,  # 원의 반지름을 설정합니다.
#         color='#C8FAC8',  # 원의 테두리 색상을 설정합니다.
#         fill=True,
#         fill_color='#C8FAC8'  # 원의 내부 색상을 설정합니다.
#     ).add_to(m)
#
#     # 어두운 백그라운드 설정
# folium.TileLayer('cartodbpositron').add_to(m)
# m.save('mapGyotong.html')

# import folium
# import json
# import pandas as pd
#
# # 서울의 좌표
# seoul_coordinates = [37.5665, 126.9780]
#
# # 서울을 중심으로 하는 지도 생성
# m = folium.Map(location=seoul_coordinates, zoom_start=11)
#
# # GeoJSON 파일을 'utf-8' 인코딩으로 읽기
# with open('seouldong.json', 'r', encoding='utf-8') as f:
#     geojson_data = json.load(f)
#
# # 읽은 데이터를 GeoJson에 추가
# folium.GeoJson(
#     geojson_data,
#     name='geojson',
#     style_function=lambda feature: {
#         'fillColor': 'grey',
#         'color': 'black',
#         'weight': 1,
#         'dashArray': '0, 0',
#         'fillOpacity': 1
#     }
# ).add_to(m)
#
# # CSV 파일 읽기
# df = pd.read_csv('C:/Users/JY/Desktop/data/people.csv', encoding='euc-kr')  # 여기에 CSV 파일 경로를 입력하세요
#
# # DataFrame에서 좌표를 읽어와 마커 추가
# for _, row in df.iterrows():
#     folium.Circle(
#         location=[row['Latitude'], row['Longitude']],
#         radius=50,  # 원의 반지름을 설정합니다.
#         color='#E62B00',  # 원의 테두리 색상을 설정합니다.
#         fill=True,
#         fill_color='#E62B00'  # 원의 내부 색상을 설정합니다.
#     ).add_to(m)
#
#     # 어두운 백그라운드 설정
# folium.TileLayer('cartodbpositron').add_to(m)
# m.save('mapPeople.html')