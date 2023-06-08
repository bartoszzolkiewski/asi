"""
This is a boilerplate pipeline 'decision_tree'
generated using Kedro 0.18.9
"""
import logging
from typing import Dict, Tuple

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import mlflow
from kedro_mlflow.io.metrics import MlflowMetricDataSet


def feature_scaling(data: pd.DataFrame) -> pd.DataFrame:
    COLUMNS = [
        "CNT_CHILDREN",
        "AMT_INCOME_TOTAL",
        "AMT_CREDIT_x",
        "AMT_ANNUITY_x",
        "AMT_GOODS_PRICE_x",
        "REGION_POPULATION_RELATIVE",
        "DAYS_BIRTH",
        "DAYS_EMPLOYED",
        "DAYS_REGISTRATION",
        "DAYS_ID_PUBLISH",
        "CNT_FAM_MEMBERS",
        "HOUR_APPR_PROCESS_START_x",
        "LIVE_CITY_NOT_WORK_CITY",
        "OBS_30_CNT_SOCIAL_CIRCLE",
        "DEF_30_CNT_SOCIAL_CIRCLE",
        "OBS_60_CNT_SOCIAL_CIRCLE",
        "DEF_60_CNT_SOCIAL_CIRCLE",
        "DAYS_LAST_PHONE_CHANGE",
        "AMT_REQ_CREDIT_BUREAU_HOUR",
        "AMT_REQ_CREDIT_BUREAU_DAY",
        "AMT_REQ_CREDIT_BUREAU_WEEK",
        "AMT_REQ_CREDIT_BUREAU_MON",
        "AMT_REQ_CREDIT_BUREAU_QRT",
        "AMT_REQ_CREDIT_BUREAU_YEAR",
        "AMT_ANNUITY_y",
        "AMT_APPLICATION",
        "AMT_CREDIT_y",
        "AMT_GOODS_PRICE_y",
        "HOUR_APPR_PROCESS_START_y",
        "FLAG_LAST_APPL_PER_CONTRACT",
        "NFLAG_LAST_APPL_IN_DAY",
        "DAYS_DECISION",
        "SELLERPLACE_AREA",
        "CNT_PAYMENT",
        "DAYS_FIRST_DRAWING",
        "DAYS_FIRST_DUE",
        "DAYS_LAST_DUE_1ST_VERSION",
        "DAYS_LAST_DUE",
        "DAYS_TERMINATION",
    ]
    scaler = StandardScaler()
    data[COLUMNS] = scaler.fit_transform(data[COLUMNS])

    return data


def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    X = data.drop(parameters["target"], axis=1)
    y = data[parameters["target"]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> DecisionTreeClassifier:
    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    return model


def evaluate_model(model: DecisionTreeClassifier, X_test: pd.DataFrame, y_test: pd.Series):
    y_pred = model.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has a accuracy score of %.3f on test data.", score)
    
    #mlflow metric logging 
    metric_ds = MlflowMetricDataSet(key="accuracy_score")
    metric_ds.save(score)  # create a "score" value in the "metric" field in mlflow UI 



