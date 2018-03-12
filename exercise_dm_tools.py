import pandas as pd

def preprocess_data(df):
    # Q1.4 and Q6.2
    df = df.drop(['Address', 'Landsize', 'BuildingArea', 'YearBuilt', 'Price', 'Bedroom2', 'SellerG'], axis=1)
    
    # Q1.1
    cols_miss_drop =['Postcode', 'CouncilArea', 'Regionname', 'Propertycount']
    mask = pd.isnull(df['Distance'])

    for col in cols_miss_drop:
        mask = mask | pd.isnull(df[col])

    df = df[~mask]
    
    # Q1.2
    df['Bathroom'].fillna(df['Bathroom'].mean(), inplace=True)
    df['Car'].fillna(df['Car'].mean(), inplace=True)
    
    df['Latitude_nan'] = pd.isnull(df['Lattitude'])
    df['Longtitude_nan'] = pd.isnull(df['Longtitude'])
    df['Lattitude'].fillna(0, inplace=True)
    df['Longtitude'].fillna(0, inplace=True)
    
    # Q6.1. Change date into weeks and months
    df['Sales_week'] = pd.to_datetime(df['Date']).dt.week
    df['Sales_month'] = pd.to_datetime(df['Date']).dt.month
    df = df.drop(['Date'], axis=1)  # drop the date, not required anymore
    
    # Q4
    df = pd.get_dummies(df)
    
    return df