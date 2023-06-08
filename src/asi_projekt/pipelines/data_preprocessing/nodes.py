"""
This is a boilerplate pipeline 'data_preprocessing'
generated using Kedro 0.18.9
"""
import pandas as pd


def drop_previous_application_bad_columns(previous_application: pd.DataFrame) -> pd.DataFrame:
    COLUMNS_TO_DROP = [
        "AMT_DOWN_PAYMENT",
        "RATE_DOWN_PAYMENT",
        "RATE_INTEREST_PRIMARY",
        "RATE_INTEREST_PRIVILEGED",
    ]

    return previous_application.drop(COLUMNS_TO_DROP, axis=1)


def drop_application_data_bad_columns(application_data: pd.DataFrame) -> pd.DataFrame:
    COLUMNS_TO_DROP = [
        "EXT_SOURCE_1",
        "EXT_SOURCE_2",
        "EXT_SOURCE_3",
        "APARTMENTS_AVG",
        "BASEMENTAREA_AVG",
        "YEARS_BEGINEXPLUATATION_AVG",
        "YEARS_BUILD_AVG",
        "COMMONAREA_AVG",
        "ELEVATORS_AVG",
        "ENTRANCES_AVG",
        "FLOORSMAX_AVG",
        "FLOORSMIN_AVG",
        "LANDAREA_AVG",
        "LIVINGAPARTMENTS_AVG",
        "LIVINGAREA_AVG",
        "NONLIVINGAPARTMENTS_AVG",
        "NONLIVINGAREA_AVG",
        "APARTMENTS_MODE",
        "BASEMENTAREA_MODE",
        "YEARS_BEGINEXPLUATATION_MODE",
        "YEARS_BUILD_MODE",
        "COMMONAREA_MODE",
        "ELEVATORS_MODE",
        "ENTRANCES_MODE",
        "FLOORSMAX_MODE",
        "FLOORSMIN_MODE",
        "LANDAREA_MODE",
        "LIVINGAPARTMENTS_MODE",
        "LIVINGAREA_MODE",
        "NONLIVINGAPARTMENTS_MODE",
        "NONLIVINGAREA_MODE",
        "APARTMENTS_MEDI",
        "BASEMENTAREA_MEDI",
        "YEARS_BEGINEXPLUATATION_MEDI",
        "YEARS_BUILD_MEDI",
        "COMMONAREA_MEDI",
        "ELEVATORS_MEDI",
        "ENTRANCES_MEDI",
        "FLOORSMAX_MEDI",
        "FLOORSMIN_MEDI",
        "LANDAREA_MEDI",
        "LIVINGAPARTMENTS_MEDI",
        "LIVINGAREA_MEDI",
        "NONLIVINGAPARTMENTS_MEDI",
        "NONLIVINGAREA_MEDI",
        "FONDKAPREMONT_MODE",
        "HOUSETYPE_MODE",
        "TOTALAREA_MODE",
        "WALLSMATERIAL_MODE",
        "EMERGENCYSTATE_MODE",
        "OWN_CAR_AGE",
        "OCCUPATION_TYPE",
    ]

    return application_data.drop(COLUMNS_TO_DROP, axis=1)


def merge(dataframe_a: pd.DataFrame, dataframe_b: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(dataframe_a, dataframe_b, on="SK_ID_CURR").drop("SK_ID_CURR", axis=1)


def fix_merged_na(merged_df: pd.DataFrame) -> pd.DataFrame:
    enq_cs = [
        "AMT_REQ_CREDIT_BUREAU_DAY",
        "AMT_REQ_CREDIT_BUREAU_HOUR",
        "AMT_REQ_CREDIT_BUREAU_MON",
        "AMT_REQ_CREDIT_BUREAU_QRT",
        "AMT_REQ_CREDIT_BUREAU_WEEK",
        "AMT_REQ_CREDIT_BUREAU_YEAR",
    ]
    for i in enq_cs:
        merged_df[i] = merged_df[i].fillna(0)

    amt_cs = ["AMT_ANNUITY_y", "AMT_GOODS_PRICE_y"]
    for i in amt_cs:
        merged_df[i] = merged_df[i].fillna(merged_df[i].mean())

    cols = [
        "DAYS_FIRST_DRAWING",
        "DAYS_FIRST_DUE",
        "DAYS_LAST_DUE_1ST_VERSION",
        "DAYS_LAST_DUE",
        "DAYS_TERMINATION",
        "CNT_PAYMENT",
    ]
    for i in cols:
        merged_df[i] = merged_df[i].fillna(merged_df[i].median())

    cols = ["NAME_TYPE_SUITE_y", "NFLAG_INSURED_ON_APPROVAL"]
    for i in cols:
        merged_df[i] = merged_df[i].fillna(merged_df[i].mode()[0])

    # Rest missing values are under 1.5% so we can drop these rows.
    merged_df.dropna(inplace=True)

    varlist = ["FLAG_OWN_CAR", "FLAG_OWN_REALTY", "FLAG_LAST_APPL_PER_CONTRACT"]

    # Defining the map function
    def binary_map(x):
        return x.map({"Y": 1, "N": 0})

    # Applying the function to the housing list
    merged_df[varlist] = merged_df[varlist].apply(binary_map)
    return merged_df.drop(["SK_ID_PREV"], axis=1)
