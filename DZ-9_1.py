import pandas as pd

def form_med_in_range(data, max_value, first_col, second_col):
    medium = data[data[first_col]<max_value][second_col].mean().round()
    return medium

path = 'sample data\california_housing_train.csv'
data = pd.read_csv(path)

print(form_med_in_range(data, 500, 'population', 'median_house_value'))