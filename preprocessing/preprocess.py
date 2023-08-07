import numpy as np
import pandas as pd

def low_case_columns(df):
    """AI is creating summary for low_case_columns

    [extended_summary]

    Parameters
    ----------
    df : pandas dataframe
        pandas data frame for which you need lower case columns

    Returns
    -------
    df: pandas data frame
        dataframe with transformed column headers to lower case
    """
    df.columns = df.columns.str.lower()
    return df

def impute_numeric_values(df,method=np.mean):
    """Takes a data frame and imputes missing values for the all the numeric columns


    Parameters
    ----------
    df : pandas dataframe
        data frame with missing values
    method : func, optional
        method used to impute missing values, by default np.mean
        
    Returns
    -------
    df : pandas data frame
        dataframe with missing values imputed
    """
    num_cols=df.select_dtypes(include=['int','float']).columns
    for col in num_cols:
        df[col] = df[col].fillna(value=np.mean(df[col]))
    return(df)
def impute_object_columns(df):
    """Takes a dataframe and imputes using mode for object columns with nan

    Parameters
    ----------
    df : pandas dataframe
        Dataframe with missing values
        
    """
    obj_cols=df.select_dtypes(include='object').columns
    for col in obj_cols:
        df[col] = df[col].fillna(value = df[col].value_counts()[0])
    


