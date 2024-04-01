import pandas as pd
import numpy as np

def select(df, columns):
    return df[columns]

def get_numeric_cols(df):
    return df.select_dtypes(include=np.number).columns.tolist()

def get_min_max(df, col):
    return df[col].min(), df[col].max()

def filter_number(df, column, min=None, max=None):
    if (min is None) and (max is None):
        return df
    elif min is None:
        return df[df[column]<=max]
    elif max is None:
        return df[min<=df[column]]
    else:
        return df[df[column].map(lambda x: min<=x<=max)]

def dropna(df, columns=None):
    if columns=="all":
        return df.dropna()
    elif columns is not None:
        return df.dropna(subset=columns)

def group(df, by, funcs):
    cols = df.columns[(df.dtypes!=object) | (df.columns.isin(by))]
    return df[cols].groupby(by=by).agg(funcs)

def info(df):
    df1 = df.count()
    df2 = pd.Series(df.dtypes)
    
    df3 = pd.concat([df1, df2], axis=1)
    df3.columns = ["non-Null Values", "dtypes"]
    
    return df3.astype(str)

def describe(df):
    if (len(df)*len(df.columns))>0:
        return df.describe()
    else:
        return df