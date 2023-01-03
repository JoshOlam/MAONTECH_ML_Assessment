# API Dependencies
import json

import numpy as np
import pandas as pd
import psycopg2
from flask import Flask, jsonify, request
from sklearn.ensemble._forest import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

columns = ["region", "depot", "item_no", "tms", "ams", "month", "year"]
conn = psycopg2.connect("host=maontech-db.cuslngvsj13a.eu-west-1.rds.amazonaws.com dbname=maontech_db user=postgres password=LbELB4tyVt7F2DrYk9nS")
cursor = conn.cursor()
cursor.execute("SELECT * FROM maontech_dataset")
data = cursor.fetchall()
df = pd.DataFrame(data, columns=columns)
#df = pd.read_csv("data-1671661749260.csv")

def data_preprocessing(df):
    """Private helper function to preprocess data for model prediction.
    All the codes required for feature engineering/selection are defined here.
    Parameters
    ----------
    df : str
        The data payload received within POST requests sent to our API.
    Returns
    -------
    X_data : A dataframe of all relevant features asides the target variable

    y_data : the target variable; 'ams'.
    """
    df = df[df['region']=="SW"]
    df = df.drop(['region', 'tms', 'year'], axis = 1)#, inplace=True)
    df = df.sort_values(by='month')
    df['ams'] = abs(df['ams'])
    df_dummies = pd.get_dummies(df)#, drop_first=True)

    #reindex the columns to make the target variable the last
    cols = [col for col in df_dummies.columns if col != 'ams'] + ['ams']

    df_dummies = df_dummies.reindex(columns=cols)
    
    X_data = df_dummies[[col for col in df_dummies.columns if col != "ams"]]
    y_data = df_dummies['ams']

    return X_data, y_data

def _model(df):
    X, y = data_preprocessing(df)
    print("Done processing data...")
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.20,
                                                        random_state=42,
                                                        shuffle=False
                                                        )
    rfr = RandomForestRegressor()
    print("Fitting model...")
    rfr.fit(X_train, y_train)
    
    
    # Pickle model for use within our API
    save_path = 'assets/trained-models/randomforestmodel.pkl'
    print (f"Training completed. Saving model to: {save_path}")
    pickle.dump(rfr, open(save_path,'wb'))

    print("Running prediction")
    result = []
    y_pred = rfr.predict(X_test) #.score(X_train, y_train)
    MSE = mean_squared_error(y_test, y_pred)
    rmse = round(np.sqrt(MSE), 2)
    result.append('RandomForestRegression RMSE: SW')
    result.append(rmse)
    accuracy_ = round((r2_score(y_test, y_pred) *100), 2)
    #print(f"Accuracy: {accuracy_}%")
    result.append(f"Accuracy: {accuracy_}%")
    print(result)



app = Flask(__name__)
@app.route('/predict', methods=['GET'])
def index():
    return "Making Predictions..."
def predictions():
    prediction=_model(df)
    return jsonify(prediction)#=_model(df))
    

#@app.route('/', methods=['GET'])
#def index():
#    return 'Machine Learning Inference'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
