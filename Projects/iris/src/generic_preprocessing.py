####### Pre-processing ############    
## Importing required libraries
import pandas as pd ## For DataFrame operation
import numpy as np ## Numerical python for matrloc operations
from sklearn.preprocessing import LabelEncoder

def drop_allsame(df):
    '''
    Function to remove any columns which have same value all across
    Required Input - 
        - df = Pandas DataFrame
    Expected Output -
        - Pandas dataframe with dropped no variation columns
    '''
    to_drop = list()
    for i in df.columns:
        if len(df.loc[:,i].unique()) == 1:
            to_drop.append(i)
    return df.drop(to_drop,axis =1)

def treat_missing_numeric(df,columns,how = 'mean'):
    '''
    Function to treat missing values in numeric columns
    Required Input - 
        - df = Pandas DataFrame
        - columns = List input of all the columns need to be imputed
        - how = valid values are 'mean', 'mode', 'median','ffill', numeric value
    Expected Output -
        - Pandas dataframe with imputed missing value in mentioned columns
    '''
    if how == 'mean':
        for i in columns:
            print("Filling missing values with mean for columns - {0}".format(i))
            df.loc[:,i] = df.loc[:,i].fillna(df.loc[:,i].mean()[0])
            
    elif how == 'mode':
        for i in columns:
            print("Filling missing values with mode for columns - {0}".format(i))
            df.loc[:,i] = df.loc[:,i].fillna(df.loc[:,i].mode()[0],inplace=True)
    
    elif how == 'median':
        for i in columns:
            print("Filling missing values with median for columns - {0}".format(i))
            df.loc[:,i] = df.loc[:,i].fillna(df.loc[:,i].median()[0])
    
    elif how == 'ffill':
        for i in columns:
            print("Filling missing values with forward fill for columns - {0}".format(i))
            df.loc[:,i] = df.loc[:,i].fillna(method ='ffill')
    
    elif type(how) == int or type(how) == float:
        for i in columns:
            print("Filling missing values with {0} for columns - {1}".format(how,i))
            df.loc[:,i] = df.loc[:,i].fillna(how)
    else:
        print("Missing value fill cannot be completed")
    return df

def treat_missing_categorical(df,columns,how = 'mode'):
    '''
    Function to treat missing values in numeric columns
    Required Input - 
        - df = Pandas DataFrame
        - columns = List input of all the columns need to be imputed
        - how = valid values are 'mode', any string or numeric value
    Expected Output -
        - Pandas dataframe with imputed missing value in mentioned columns
    '''
    if how == 'mode':
        for i in columns:
            print("Filling missing values with mode for columns - {0}".format(i))
            df.loc[:,i] = df.loc[:,i].fillna(df.loc[:,i].mode()[0])
    elif type(how) == str:
        for i in columns:
            print("Filling missing values with {0} for columns - {1}".format(how,i))
            df.loc[:,i] = df.loc[:,i].fillna(how)
    elif type(how) == int or type(how) == float:
        for i in columns:
            print("Filling missing values with {0} for columns - {1}".format(how,i))
            df.loc[:,i] = df.loc[:,i].fillna(str(how))
    else:
        print("Missing value fill cannot be completed")
    return df
    
def min_max_scaler(df,columns):
    '''
    Function to do Min-Max scaling
    Required Input - 
        - df = Pandas DataFrame
        - columns = List input of all the columns which needs to be min-max scaled
    Expected Output -
        - df = Python DataFrame with Min-Max scaled attributes
        - scaler = Function which contains the scaling rules
    '''
    scaler = MinMaxScaler()
    data = pd.DataFrame(scaler.fit_transform(df.loc[:,columns]))
    data.index = df.index
    data.columns = df.columns
    return data, scaler

def z_scaler(df,columns):
    '''
    Function to standardize features by removing the mean and scaling to unit variance
    Required Input - 
        - df = Pandas DataFrame
        - columns = List input of all the columns which needs to be min-max scaled
    Expected Output -
        - df = Python DataFrame with Min-Max scaled attributes
        - scaler = Function which contains the scaling rules
    '''
    scaler = StandardScaler()
    data = pd.DataFrame(scaler.fit_transform(df.loc[:,columns]))
    data.index = df.index
    data.columns = df.columns
    return data, scaler
    
def label_encoder(df,columns):
    '''
    Function to label encode
    Required Input - 
        - df = Pandas DataFrame
        - columns = List input of all the columns which needs to be label encoded
    Expected Output -
        - df = Pandas DataFrame with lable encoded columns
        - le_dict = Dictionary of all the column and their label encoders
    '''
    le_dict = {}
    for c in columns:
        print("Label encoding column - {0}".format(c))
        lbl = LabelEncoder()
        lbl.fit(list(df[c].values.astype('str')))
        df[c] = lbl.transform(list(df[c].values.astype('str')))
        le_dict[c] = lbl
    return df, le_dict

def one_hot_encoder(df, columns):
    '''
    Function to do one-hot encoded
    Required Input - 
        - df = Pandas DataFrame
        - columns = List input of all the columns which needs to be one-hot encoded
    Expected Output -
        - df = Pandas DataFrame with one-hot encoded columns
    '''
    for each in columns:
        print("One-Hot encoding column - {0}".format(each))
        dummies = pd.get_dummies(df[each], prefloc=each, drop_first=False)
        df = pd.concat([df, dummies], axis=1)
    return df.drop(columns,axis = 1)

####### Feature Engineering ############
def create_date_features(df,column, date_format = None, more_features = False, time_features = False):
    '''
    Function to extract date features
    Required Input - 
        - df = Pandas DataFrame
        - date_format = Date parsing format
        - columns = Columns name containing date field
        - more_features = To get more feature extracted
        - time_features = To extract hour from datetime field
    Expected Output -
        - df = Pandas DataFrame with additional extracted date features
    '''
    if date_format is None:
        df.loc[:,column] = pd.to_datetime(df.loc[:,column])
    else:
        df.loc[:,column] = pd.to_datetime(df.loc[:,column],format = date_format)
    df.loc[:,column+'_Year'] = df.loc[:,column].dt.year
    df.loc[:,column+'_Month'] = df.loc[:,column].dt.month.astype('uint8')
    df.loc[:,column+'_Week'] = df.loc[:,column].dt.week.astype('uint8')
    df.loc[:,column+'_Day'] = df.loc[:,column].dt.day.astype('uint8')
    
    if more_features:
        df.loc[:,column+'_Quarter'] = df.loc[:,column].dt.quarter.astype('uint8')
        df.loc[:,column+'_DayOfWeek'] = df.loc[:,column].dt.dayofweek.astype('uint8')
        df.loc[:,column+'_DayOfYear'] = df.loc[:,column].dt.dayofyear
        
    if time_features:
        df.loc[:,column+'_Hour'] = df.loc[:,column].dt.hour.astype('uint8')
    return df

def target_encoder(train_df, col_name, target_name, test_df = None, how='mean'):
    '''
    Function to do target encoding
    Required Input - 
        - train_df = Training Pandas Dataframe
        - test_df = Testing Pandas Dataframe
        - col_name = Name of the columns of the source variable
        - target_name = Name of the columns of target variable
        - how = 'mean' default but can also be 'count'
	Expected Output - 
		- train_df = Training dataframe with added encoded features
		- test_df = Testing dataframe with added encoded features
    '''
    aggregate_data = train_df.groupby(col_name)[target_name] \
                    .agg([how]) \
                    .reset_index() \
                    .rename(columns={how: col_name+'_'+target_name+'_'+how})
    if test_df is None:
        return join_df(train_df,aggregate_data,left_on = col_name)
    else:
        return join_df(train_df,aggregate_data,left_on = col_name), join_df(test_df,aggregate_data,left_on = col_name)