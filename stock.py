import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from keras.models import Sequential
from keras.layers import Dense, LSTM, Input
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
data = pd.read_csv('/kaggle/input/meta-dataset/Download Data - STOCK_US_XNAS_META.csv')
# Reverse the data
data = data.iloc[::-1]

# Save the reversed index for later use
date = data.index
data
print(data.head())
print(data.info())
data['Date'] = pd.to_datetime(data['Date'])
# Normalize the 'Close' prices to a range between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data)
train_size = int(len(data_scaled) * 0.6)
train_data = data_scaled[:train_size]
test_data = data_scaled[train_size:]
def create_dataset(data, time_step=1):
    X, y = [], []
    for i in range(len(data) - time_step ):
        X.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 0])
    return np.array(X), np.array(y)
time_step = 4  # Number of previous days to consider
X_train, y_train = create_dataset(train_data, time_step )
X_test, y_test = create_dataset(test_data, time_step)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
model = Sequential()
model.add(Input(shape=(X_train.shape[1], 1)))
model.add(LSTM(100, return_sequences=True))
model.add(LSTM(100, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.compile(optimizer='adam',metrics=['accuracy'], loss='mean_squared_error')
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3)
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=32, epochs=100)
y_pred = model.predict(X_test)
y_pred = scaler.inverse_transform(y_pred)
y_test_actual = scaler.inverse_transform(y_test.reshape(-1, 1))
rmse = np.sqrt(np.mean((y_pred - y_test_actual) ** 2))
mae = mean_absolute_error(y_test_actual,y_pred)
print(f'Root Mean Squared Error: {rmse}')
print(f'ean Absolute Error: {mae}')
r2=r2_score(y_test_actual,y_pred)
print("R2 Score :", r2)
last_4_days = data_scaled[-4:]
last_4_days = last_4_days.reshape((1, last_4_days.shape[0], 1))
predicted_close_price = model.predict(last_4_days)
predicted_close_price = scaler.inverse_transform(predicted_close_price)
print(f'Predicted Close Price on 07/22/2024: {predicted_close_price[0][0]}')
evaluate = model.evaluate(X_test, y_test)
print(evaluate)
