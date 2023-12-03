
#--------------------------------------------------------------
# import pandas as pd
# from haversine import haversine
#
# # Limrestrant 데이터 읽기
# limrestrant_path = "C:/Users/JY/Desktop/data/ALL.csv"
# limrestrant_data = pd.read_csv(limrestrant_path, encoding="euc-kr")
# limrestrant_coords = limrestrant_data[['Latitude', 'Longitude']].values
#
# # Limcharge 데이터 읽기
# limcharge_path = "C:/Users/JY/Desktop/noinboho.csv"
# limcharge_data = pd.read_csv(limcharge_path, encoding="euc-kr")
# limcharge_coords = limcharge_data[['Latitude', 'Longitude']].values
# limcharge_numbers = limcharge_data['id'].values
#
# result = []
#
# for i, limcharge_coord in enumerate(limcharge_coords):
#     num = sum(haversine(limcharge_coord, limrestrant_coord, unit='m') < 300 for limrestrant_coord in limrestrant_coords)
#     print(f'사고 번호: {limcharge_numbers[i]}, 보호구역근처 사고 개수: {num}')
#     result.append({'사고 번호': limcharge_numbers[i], '보호구역 주변 사고개수': num})
#
# result_df = pd.DataFrame(result)
# result_df.to_csv("C:/Users/JY/Desktop/bohoAcciresult.csv", index=True)
#
# result = [(limcharge_numbers[i], num) for i, limcharge_coord in enumerate(limcharge_coords)]
# print(result)
#
#
# # 다발지 주변 보호시설
# import pandas as pd
# from haversine import haversine
#
# # Limrestrant 데이터 읽기
# limrestrant_path = "C:/Users/JY/Desktop/noinboho.csv"
# limrestrant_data = pd.read_csv(limrestrant_path, encoding="euc-kr")
# limrestrant_coords = limrestrant_data[['Latitude', 'Longitude']].values
#
# # Limcharge 데이터 읽기
# limcharge_path = "C:/Users/JY/Desktop/data/ALL.csv"
# limcharge_data = pd.read_csv(limcharge_path, encoding="euc-kr")
# limcharge_coords = limcharge_data[['Latitude', 'Longitude']].values
# limcharge_numbers = limcharge_data['id'].values
#
# result = []
#
# for i, limcharge_coord in enumerate(limcharge_coords):
#     num = sum(haversine(limcharge_coord, limrestrant_coord, unit='m') < 300 for limrestrant_coord in limrestrant_coords)
#     print(f'사고 번호: {limcharge_numbers[i]}, 보호구역 개수: {num}')
#     result.append({'사고 번호': limcharge_numbers[i], '보호구역 개수': num})
#
# result_df = pd.DataFrame(result)
# result_df.to_csv("C:/Users/JY/Desktop/data/bohoresult.csv", index=True)
#
# result = [(limcharge_numbers[i], num) for i, limcharge_coord in enumerate(limcharge_coords)]
# print(result)


# import pandas as pd
# from haversine import haversine
#
# # Limrestrant 데이터 읽기
# limrestrant_path = "C:/Users/JY/Desktop/test.csv"
# limrestrant_data = pd.read_csv(limrestrant_path, encoding="euc-kr")
# limrestrant_coords = limrestrant_data[['Latitude', 'Longitude']].values
#
# # Limcharge 데이터 읽기
# limcharge_path = "C:/Users/JY/Desktop/data/ALL.csv"
# limcharge_data = pd.read_csv(limcharge_path, encoding="euc-kr")
# limcharge_coords = limcharge_data[['Latitude', 'Longitude']].values
# limcharge_numbers = limcharge_data['id'].values
#
# result = []
#
# for i, limcharge_coord in enumerate(limcharge_coords):
#     num = sum(haversine(limcharge_coord, limrestrant_coord, unit='m') < 300 for limrestrant_coord in limrestrant_coords)
#     print(f'사고 번호: {limcharge_numbers[i]}, 복지시설 개수: {num}')
#     result.append({'사고 번호': limcharge_numbers[i], '복지시설 개수': num})
#
# result_df = pd.DataFrame(result)
# result_df.to_csv("C:/Users/JY/Desktop/Bokji.csv", index=True)
#
# result = [(limcharge_numbers[i], num) for i, limcharge_coord in enumerate(limcharge_coords)]
# print(result)



#----------------------------
# 다발지 주변 보호구역
# import pandas as pd
# from haversine import haversine
#
# noinBoho_path = "C:/Users/JY/Desktop/data/ALL.csv"
# noinBoho_data = pd.read_csv(noinBoho_path, encoding="euc-kr")
# noinBoho_coords = noinBoho_data[['Latitude', 'Longitude']].values
# noinBoho_numbers = noinBoho_data['id'].values
#
# accident_path = "C:/Users/JY/Desktop/noinboho.csv"
# accident_data = pd.read_csv(accident_path, encoding="euc-kr")
# accident_coords = accident_data[['Latitude', 'Longitude']].values
#
#
# result = []
#
# for i, noinBoho_coord in enumerate(noinBoho_coords):
#     num = sum(haversine(noinBoho_coord, noinBoho_coord, unit='m') < 300 for accident_coord in accident_coords)
#     print(f'사고 번호: {noinBoho_numbers[i]}, 보호구역 개수: {num}')
#     result.append({'사고 번호': noinBoho_numbers[i], '보호구역 개수': num})
#
# result_df = pd.DataFrame(result)
# result_df.to_csv("C:/Users/JY/Desktop/bohoguyuk.csv", index=True)

import pandas as pd
from haversine import haversine

# Limrestrant 데이터 읽기
# limrestrant_path = "C:/Users/JY/Desktop/noinboho.csv"
# limrestrant_data = pd.read_csv(limrestrant_path, encoding="euc-kr")
# limrestrant_coords = limrestrant_data[['Latitude', 'Longitude']].values
#
# # Limcharge 데이터 읽기
# limcharge_path = "C:/Users/JY/Desktop/nointest.csv"
# limcharge_data = pd.read_csv(limcharge_path, encoding="euc-kr")
# limcharge_coords = limcharge_data[['Latitude', 'Longitude']].values
# limcharge_numbers = limcharge_data['FID'].values
#
# result = []
#
# for i, limcharge_coord in enumerate(limcharge_coords):
#     num = sum(haversine(limcharge_coord, limrestrant_coord, unit='m') < 300 for limrestrant_coord in limrestrant_coords)
#     print(f'사고 번호: {limcharge_numbers[i]}, 보호구역 개수: {num}')
#     result.append({'사고 번호': limcharge_numbers[i], '보호구역 개수': num})
#
# result_df = pd.DataFrame(result)
# result_df.to_csv("C:/Users/JY/Desktop/result.csv", index=True)

#-------------------------
#다발지 주변 교통량
# import pandas as pd
# from haversine import haversine
#
# # Limcharge 데이터 읽기
# accident_path = "C:/Users/JY/Desktop/nointest.csv"
# accident_data = pd.read_csv(accident_path, encoding="euc-kr")
# accident_coords = accident_data[['Latitude', 'Longitude']].values
# accident_numbers = accident_data['FID'].values
# # 교통량 좌표 데이터 읽기
# traffic_path = "C:/Users/JY/Desktop/jjingyotong.csv"
# traffic_data = pd.read_csv(traffic_path, encoding="euc-kr")
# traffic_coords = traffic_data[['Latitude', 'Longitude']].values
# traffic_numbers = traffic_data['Traffic Number'].values
#
# result = []
#
# for i, accident_coord in enumerate(accident_coords):
#     min_distance = float('inf')
#     closest_traffic_coord = None
#     closest_traffic_number = None
#
#     for j, traffic_coord in enumerate(traffic_coords):
#         distance = haversine(accident_coord, traffic_coord, unit='m')
#         if distance < min_distance:
#             min_distance = distance
#             closest_traffic_coord = traffic_coord
#             closest_traffic_number = traffic_numbers[j]
#
#     result.append({'사고 번호': accident_numbers[i], '가장 가까운 교통량 번호': closest_traffic_number, '거리': min_distance})
#
# result_df = pd.DataFrame(result)
# result_df.to_csv("C:/Users/JY/Desktop/closest_traffic_to_accidents.csv", index=True)
#--------------------------------------------
import pandas as pd
# from haversine import haversine
#
# # Limcharge 데이터 읽기
# accident_path = "C:/Users/JY/Desktop/nointest.csv"
# accident_data = pd.read_csv(accident_path, encoding="euc-kr")
# accident_coords = accident_data[['Latitude', 'Longitude']].values
# accident_numbers = accident_data['FID'].values
# # 교통량 좌표 데이터 읽기
# traffic_path = "C:/Users/JY/Desktop/jjingyotong.csv"
# traffic_data = pd.read_csv(traffic_path, encoding="euc-kr")
# traffic_coords = traffic_data[['Latitude', 'Longitude']].values
# traffic_numbers = traffic_data['Traffic Number'].values
#
# result = []
#
# for i, accident_coord in enumerate(accident_coords):
#     min_distance = float('inf')
#     closest_traffic_coord = None
#     closest_traffic_number = None
#
#     for j, traffic_coord in enumerate(traffic_coords):
#         distance = haversine(accident_coord, traffic_coord, unit='m')
#         if distance < min_distance:
#             min_distance = distance
#             closest_traffic_coord = traffic_coord
#             closest_traffic_number = traffic_numbers[j]
#
#     result.append({'사고 번호': accident_numbers[i], '가장 가까운 교통량 번호': closest_traffic_number, '거리': min_distance})
#
# result_df = pd.DataFrame(result)
# result_df.to_csv("C:/Users/JY/Desktop/closest_traffic_to_accidents.csv", index=True)
#---------------------------------------------------
#다발지 주변 카메라 개수
# import pandas as pd
# from haversine import haversine
#
# # Limrestrant 데이터 읽기
# limrestrant_path = "C:/Users/JY/Desktop/data/ALL.csv"
# limrestrant_data = pd.read_csv(limrestrant_path, encoding="euc-kr")
# limrestrant_coords = limrestrant_data[['Latitude', 'Longitude']].values
#
# # Limcharge 데이터 읽기
# limcharge_path = "C:/Users/JY/Desktop/data/ALL.csv"
# limcharge_data = pd.read_csv(limcharge_path, encoding="euc-kr")
# limcharge_coords = limcharge_data[['Latitude', 'Longitude']].values
# limcharge_numbers = limcharge_data['id'].values
#
# result = []
#
# for i, limcharge_coord in enumerate(limcharge_coords):
#     num = sum(haversine(limcharge_coord, limrestrant_coord, unit='m') < 50 for limrestrant_coord in limrestrant_coords)
#     print(f'사고 번호: {limcharge_numbers[i]}, 사고반경50m 건수: {num}')
#     result.append({'사고 번호': limcharge_numbers[i], '사고반경50m 건수': num})
# # for i, limcharge_coord in enumerate(limcharge_coords):
# #     num = sum(haversine(limcharge_coord, limrestrant_coord, unit='m') < 100 for j, limrestrant_coord in enumerate(limrestrant_coords) if i != j)
# #     num = 1 if num >= 1 else 0
# #     print(f'사고 번호: {limcharge_numbers[i]}, 사고반경100m 건수: {num}')
# #     result.append({'사고 번호': limcharge_numbers[i], '사고반경100m 건수': num})
# result_df = pd.DataFrame(result)
# result_df.to_csv("C:/Users/JY/Desktop/sagogunsu3.csv", index=True)

#----------------------

# import pandas as pd
# from haversine import haversine
#
# accident_path = "C:/Users/JY/Desktop/accident.csv"
# accident_data = pd.read_csv(accident_path, encoding="euc-kr")
# accident_coords = accident_data[['Latitude', 'Longitude']].values
#
# accident_path2 = "C:/Users/JY/Desktop/nointest.csv"
# accident_data2 = pd.read_csv(accident_path2, encoding="euc-kr")
# accident_coords2 = accident_data2[['Latitude', 'Longitude']].values
# accident_numbers2 = accident_data2['FID'].values
#
# result = []
#
# for i, accident_coord in enumerate(accident_coords):
#     num = sum(haversine(accident_coord, accident_coord, unit='m') < 300 for accident_coord2 in accident_coords2)
#     print(f'사고 번호: {accident_numbers[i]}, 사고건수: {num}')
#     result.append({'사고 번호': accident_numbers[i], '사고건수': num})
#
# result_df = pd.DataFrame(result)
# result_df.to_csv("C:/Users/JY/Desktop/result.csv", index=True)



# import pandas as pd
# from haversine import haversine
# #
# # # 교통 데이터 읽기
# accident_path = "C:/Users/JY/Desktop/data/eighteen.csv"
# accident_data = pd.read_csv(accident_path, encoding="euc-kr")
# print(accident_data.columns)
# accident_coords = accident_data[['Latitude', 'Longitude']].values
# accident_numbers = accident_data['id'].values
#
# #  교통량 좌표 데이터 읽기
# traffic_path = "C://Users//JY//Desktop//data//eighteengyotong.csv"
# traffic_data = pd.read_csv(traffic_path, encoding="euc-kr")
# print(traffic_data.columns)
# traffic_coords = traffic_data[['Latitude', 'Longitude']].values
# traffic_numbers = traffic_data['trafficnum'].values
# traffic = traffic_data['Traffic'].values
#
# result = []
#
# for i, accident_coord in enumerate(accident_coords):
#     min_distance = float('inf')
#     closest_traffic_coord = None
#     closest_traffic_number = None
#     closest_traffic = None
#
#     for j, traffic_coord in enumerate(traffic_coords):
#         distance = haversine(accident_coord, traffic_coord, unit='m')
#         if distance < min_distance:
#             min_distance = distance
#             closest_traffic_coord = traffic_coord
#             closest_traffic_number = traffic_numbers[j]
#             closest_traffic = traffic[j]
#     result.append({'사고 번호': accident_numbers[i], '가장 가까운 교통량 번호': closest_traffic_number, '가장 가까운 교통량의 교통량': closest_traffic, '거리': min_distance})
#
# result_df = pd.DataFrame(result)
# result_df.to_csv("C://Users//JY//Desktop//twentyGyotongResult.csv", index=True)


#-----------------------------------------------------------------
