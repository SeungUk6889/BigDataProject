import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.svm import LinearSVR
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


# 데이터 불러오기 (예시 데이터 형식에 맞게 수정 필요)
data = pd.read_csv('C:/Users/lsm/Desktop/test_model.csv')

# 예측 변수와 레이블 나누기
X = data.drop('accident', axis=1)  # 'Accident' 열이 교통사고 여부를 나타내는 열
y = data['accident']

# 학습 데이터와 테스트 데이터로 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# RandomForestRegressor 모델 생성 및 학습
model = RandomForestRegressor(n_estimators=1000, random_state=42)
model.fit(X_train, y_train)

# XGVRegressor 모델 생성 및 학습
model1 = XGBRegressor(n_estimators=1000, random_state=42)
model1.fit(X_train, y_train)

# LinearSVR 모델 생성 및 학습
model2 = LinearSVR(random_state=42)
model2.fit(X_train, y_train)

# 테스트 데이터에 대한 예측
y_pred = model.predict(X_test)
y_pred1 = model1.predict(X_test)
y_pred2 = model2.predict(X_test)

# 모델 평가
mse = mean_squared_error(y_test, y_pred)
mse1 = mean_squared_error(y_test,y_pred1)
mse2 = mean_squared_error(y_test,y_pred2)

models = ['RandomForestRegressor', 'XGBRegressor', 'Linear SVR']
mse_values = [mse, mse1, mse2]

print(f'RandomForestRegressor Mean Squared Error: {mse}')
print(f'XGBRegressor Mean Squared Error         : {mse1}')
print(f'Linear SVR Mean Squared Error           : {mse2}')
plt.figure(figsize=(10, 6))
plt.barh(models, mse_values, color=['steelblue', 'forestgreen', 'firebrick'])
plt.xlabel('Mean Squared Error')
plt.title('Comparison of Mean Squared Error for Different Models')
plt.show()