"""
This is a boilerplate pipeline 'feature_extraction'
generated using Kedro 0.18.9
"""
import hopsworks
import pandas as pd
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split


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
    
    project = hopsworks.login()

    fs = project.get_feature_store()


    trans_fg = fs.get_or_create_feature_group(
    name="test",
    version=1,
    description="Transaction data",
    primary_key=['ID_COL'],
    event_time=None,
    online_enabled=True
    )
    
    data_with_primary_key = data
    data_with_primary_key['ID_COL'] = data_with_primary_key.index
    # will crash if ran with whole dataset 
    trans_fg.insert(data_with_primary_key.head(10))

    return data


def split_data(data: pd.DataFrame, parameters: dict) -> tuple:
    X = data.drop(parameters["target"], axis=1)
    y = data[parameters["target"]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


def set_column_types(dataframe: pd.DataFrame) -> pd.DataFrame:
    COLUMNS = [
        "FLAG_OWN_CAR",
        "FLAG_OWN_REALTY",
        "FLAG_MOBIL",
        "FLAG_EMP_PHONE",
        "FLAG_WORK_PHONE",
        "FLAG_CONT_MOBILE",
        "FLAG_PHONE",
        "FLAG_EMAIL",
        "REGION_RATING_CLIENT",
        "REGION_RATING_CLIENT_W_CITY",
        "REG_REGION_NOT_LIVE_REGION",
        "REG_REGION_NOT_WORK_REGION",
        "LIVE_REGION_NOT_WORK_REGION",
        "REG_CITY_NOT_LIVE_CITY",
        "REG_CITY_NOT_WORK_CITY",
        "FLAG_DOCUMENT_2",
        "FLAG_DOCUMENT_3",
        "FLAG_DOCUMENT_4",
        "FLAG_DOCUMENT_5",
        "FLAG_DOCUMENT_6",
        "FLAG_DOCUMENT_7",
        "FLAG_DOCUMENT_8",
        "FLAG_DOCUMENT_9",
        "FLAG_DOCUMENT_10",
        "FLAG_DOCUMENT_11",
        "FLAG_DOCUMENT_12",
        "FLAG_DOCUMENT_13",
        "FLAG_DOCUMENT_14",
        "FLAG_DOCUMENT_15",
        "FLAG_DOCUMENT_16",
        "FLAG_DOCUMENT_17",
        "FLAG_DOCUMENT_18",
        "FLAG_DOCUMENT_19",
        "FLAG_DOCUMENT_20",
        "FLAG_DOCUMENT_21",
        "NFLAG_INSURED_ON_APPROVAL",
    ]
    dataframe[COLUMNS] = dataframe[COLUMNS].astype("category")

    return dataframe


def attach_dummies(dataframe: pd.DataFrame) -> pd.DataFrame:
    COLUMNS = [
        "FLAG_OWN_CAR",
        "FLAG_OWN_REALTY",
        "FLAG_MOBIL",
        "FLAG_EMP_PHONE",
        "FLAG_WORK_PHONE",
        "FLAG_CONT_MOBILE",
        "FLAG_PHONE",
        "FLAG_EMAIL",
        "REGION_RATING_CLIENT",
        "REGION_RATING_CLIENT_W_CITY",
        "REG_REGION_NOT_LIVE_REGION",
        "REG_REGION_NOT_WORK_REGION",
        "LIVE_REGION_NOT_WORK_REGION",
        "REG_CITY_NOT_LIVE_CITY",
        "REG_CITY_NOT_WORK_CITY",
        "FLAG_DOCUMENT_2",
        "FLAG_DOCUMENT_3",
        "FLAG_DOCUMENT_4",
        "FLAG_DOCUMENT_5",
        "FLAG_DOCUMENT_6",
        "FLAG_DOCUMENT_7",
        "FLAG_DOCUMENT_8",
        "FLAG_DOCUMENT_9",
        "FLAG_DOCUMENT_10",
        "FLAG_DOCUMENT_11",
        "FLAG_DOCUMENT_12",
        "FLAG_DOCUMENT_13",
        "FLAG_DOCUMENT_14",
        "FLAG_DOCUMENT_15",
        "FLAG_DOCUMENT_16",
        "FLAG_DOCUMENT_17",
        "FLAG_DOCUMENT_18",
        "FLAG_DOCUMENT_19",
        "FLAG_DOCUMENT_20",
        "FLAG_DOCUMENT_21",
        "NFLAG_INSURED_ON_APPROVAL",
        "NAME_CONTRACT_TYPE_x",
        "CODE_GENDER",
        "NAME_TYPE_SUITE_x",
        "NAME_INCOME_TYPE",
        "NAME_EDUCATION_TYPE",
        "NAME_FAMILY_STATUS",
        "NAME_HOUSING_TYPE",
        "WEEKDAY_APPR_PROCESS_START_x",
        "ORGANIZATION_TYPE",
        "NAME_CONTRACT_TYPE_y",
        "WEEKDAY_APPR_PROCESS_START_y",
        "NAME_CASH_LOAN_PURPOSE",
        "NAME_CONTRACT_STATUS",
        "NAME_PAYMENT_TYPE",
        "CODE_REJECT_REASON",
        "NAME_TYPE_SUITE_y",
        "NAME_CLIENT_TYPE",
        "NAME_GOODS_CATEGORY",
        "NAME_PORTFOLIO",
        "NAME_PRODUCT_TYPE",
        "CHANNEL_TYPE",
        "NAME_SELLER_INDUSTRY",
        "NAME_YIELD_GROUP",
        "PRODUCT_COMBINATION",
    ]
      
    
    dummies = pd.get_dummies(dataframe[COLUMNS], drop_first=True)
    
    # data sanitization for feature store
    dummies.columns = dummies.columns.str.upper()
    dummies.columns = dummies.columns.str.replace(' ', '_')
    dummies.columns = dummies.columns.str.replace('/', '')
    dummies.columns = dummies.columns.str.replace(':', '')
    dummies.columns = dummies.columns.str.replace(',', '')
    dummies.columns = dummies.columns.str.replace('-', '_')

<<<<<<< Updated upstream

    dataframe = pd.concat([dataframe, dummies], axis=1)
          

    return dataframe.drop(COLUMNS, axis=1)
=======
    return dataframe.drop(COLUMNS, axis=1)


def export_schema(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.sample(5)
>>>>>>> Stashed changes
