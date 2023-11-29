from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
housing_df = pd.read_csv('HousingData.csv')
housing_df['AGE']=housing_df['AGE'].fillna(housing_df['AGE'].mean())
housing_df['CHAS']=housing_df['CHAS'].fillna(0)
housing_df['ZN']=housing_df['ZN'].fillna(housing_df['ZN'].mean())
housing_df['INDUS']=housing_df['INDUS'].fillna(housing_df['INDUS'].mean())
housing_df['CRIM']=housing_df['CRIM'].fillna(housing_df['CRIM'].mean())
housing_df['LSTAT']=housing_df['LSTAT'].fillna(housing_df['LSTAT'].mean())


dy=housing_df['MEDV']
dx=housing_df.drop(['MEDV'], axis=1)
dx_std=StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2, random_state=0)

knn = KNeighborsRegressor(n_neighbors=5)

knn.fit(dx_train, dy_train)

predictions = knn.predict(dx_test)

print(dy_test)
print(predictions)
print(knn.score(dx_train, dy_train))
print(knn.score(dx_test, dy_test))

