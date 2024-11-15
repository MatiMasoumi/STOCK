# Stock Price Prediction using Machine Learning ## Overview This project aims to predict stock prices using historical data and machine learning techniques.
The model was trained and evaluated using a dataset containing stock market information. ## Dataset - **Source**: Kaggle (`/kaggle/input/meta-dataset/Download-Data - STOCK_US_XNAS_META.csv`)
- **Features**: The dataset contains multiple columns with historical stock data such as: - Date - Open - High - Low - Close - Volume - **Target**:
-  The `Close` price column was used as the target variable for prediction. ## Project Workflow 1. **Data Loading**:
 The dataset was loaded using `pandas` and preprocessed to ensure compatibility with the model. 2. **Preprocessing**:
- Data was scaled using a `MinMaxScaler` to normalize features. - The last 4 days of data were extracted for future predictions. 3.
-  **Model Training**: - A deep learning model (likely an LSTM or similar recurrent neural network) was trained to predict stock prices.
-   4. **Evaluation**: - Performance metrics: - **Root Mean Squared Error (RMSE)**: `15.21` - **Mean Absolute Error (MAE)**: `11.20` - **R² Score**: `0.532`
5. 5. **Prediction**: - The model predicted a closing price of `483.23` for `07/22/2024`. ## Results - **Evaluation Metrics**:
6.  - Root Mean Squared Error: `15.21` - Mean Absolute Error: `11.20` - R² Score: `0.532` - **Predicted Closing Price**:
- Date: `07/22/2024` - Predicted Price: `483.23`
-  ## Usage ### Requirements Install the required libraries:
-   ```bash pip install numpy pandas scikit-learn tensorflow
