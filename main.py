def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
import os
import json


def get_data(base_dir):
    data_file_names = [x for x in os.listdir(base_dir) if x.endswith('.csv')]
    data = {}
    for name in data_file_names:
        path_file = os.path.join(base_dir, name)
        df = pd.read_csv(r"C:\Users\user\PycharmProjects\pythongreatlearning\Iris\iris.csv")
    return data


def split_data(data, test_size=0.2, random_state=42):
    # Assuming 'target' is the column you want to predict
    df = data['iris.csv']
    X = df.drop('variety', axis=1)
    y = df['variety']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    return {'X_train': X_train, 'X_test': X_test, 'y_train': y_train, 'y_test': y_test}


def train_model(X_train, y_train):
    log_reg = LogisticRegression()
    model = log_reg.fit(X_train, y_train)
    return model


def save_model(model):
    dump(model, "lr_model.joblib")
    print("Model saved")


def create_metrics(X_test, y_test, model):
    model_report = classification_report(y_test, model.predict(X_test))
    scores = roc_auc_score(y_test, model.predict_proba(X_test), multi_class='ovr')

    return {'scores': scores, 'model_report': model_report}




if _name_ == "main":
    base_dir = sys.argv[1]
    data = get_data(base_dir)

    # Assuming 'your_csv_file.csv' is one of the CSV files in the directory
    split_data = split_data(data['iris.csv'])

    model = train_model(split_data['X_train'], split_data['y_train'])
    metrics = create_metrics(split_data['X_test'], split_data['y_test'], model)
    save_model(model)
    save_metrics(metrics)
