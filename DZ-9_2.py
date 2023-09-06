import pandas as pd

def max_in_min(data, first_col, second_col):
    result = data[first_col][data[second_col] == data[second_col].min()].max()
    return result

path = 'sample data\california_housing_train.csv'
data = pd.read_csv(path)

print(max_in_min(data, 'households', 'population'))