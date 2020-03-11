def Q_03(self, full_dataset):
    # Task 3: Given the full_dataset (Pandas Dataframe), check if there are missing values, and if yes,
    # count how many, and impute the missing values with corresponding mean values.
    # Finally, return the counting result as a Pandas dataframe with 2 columns
    #  {variable_name,num_of_missing_values).  Please make sure the result lists all the variables
    #  (including the target) in the given dataset. Also, return the revised full_dataset after the missing
    # value imputations is done. Return these two pandas dataframe as tuple.
    import pandas as pd
    import numpy as np

    missing_count = pd.DataFrame()
    revised_full_dataset = pd.DataFrame()

    # YOUR CODE HERE
    revised_full_dataset = full_dataset
    dict = {'Name': [], 'MissingCount': []}
    for name, series in full_dataset.iteritems():
        dict['Name'].append(name)
        dict['MissingCount'].append(series.isnull().sum())

        mean = np.mean(series.array)
        revised_full_dataset.loc[:, name] = full_dataset.loc[:, name].fillna(mean)

    missing_count = pd.DataFrame(dict)
    
#    for i in len(full_dataset.columns):

    return (missing_count, revised_full_dataset)
