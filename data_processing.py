# Data Preprocessing

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')

# Check if there are missing data
substitute = False
missing_col = []
print("The number of missing values in each column is:")
for i,l in dataset.isnull().sum().iteritems():
    print(i,l)
#    if there are missing values in a numeric column ask to substitute
    if(l>0 and pd.api.types.is_numeric_dtype(dataset[i])):
        missing_col.append(i)
        substitute = True

#if substitute ask the method and make the substitutions
if substitute: 
    s = input("\nSubstitute the missing numeric values? (y or n) ")
    fill = None
    if s=='y':
        from sklearn.impute import SimpleImputer
        v = input("Use mean('m'), median('d'), most_frequent('f') or constant('c')?")
        if v == 'm':
            var = 'mean'
        elif v == 'd':
            var = 'median'
        elif v == 'f':
            var = 'most_frequent'
        elif v == 'c':
            var = 'constant'
            f = input("Enter a numeric constant?")
            fill = f
                
        
        imputer = SimpleImputer(missing_values = np.nan, strategy = var, fill_value= fill)
        for i in missing_col:
            imputer.fit(dataset[[i]])
            dataset[i] = imputer.transform(dataset[[i]]).ravel()
        

#create a new csv
dataset.to_csv('Data_new.csv')