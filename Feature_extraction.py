import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 데이터 불러오기
# 한글 폰트 경로 설정 (실제 경로에 따라 변경해야 함)
font_path = "C:/Windows/Fonts/gulim.ttc"  # 예시 경로, 실제 경로를 지정해야 합니다.

# 폰트 매니저에 추가
font_manager.fontManager.addfont(font_path)

# 폰트 설정
plt.rcParams['font.family'] = 'gulim'

data = pd.read_csv('C:/Users/lsm/Desktop/test_model.csv')

# 상관 행렬 계산
correlation_matrix = data.corr()

# Feature importance for 'accident' excluding 'accident' itself
accident_importance = correlation_matrix['accident'].drop('accident').abs().sort_values(ascending=False)

# Plotting feature importance
plt.figure(figsize=(10, 6))
sns.barplot(x=accident_importance, y=accident_importance.index, palette="viridis")
plt.title('특성 중요도')

plt.show()