import pandas as pd

def form_med_in_range(data, min_value, max_value, first_col, second_col):
    range_pop = data[data[first_col]>=min_value]
    range_pop = range_pop[range_pop[first_col]<=max_value]
    medium_cost = range_pop[second_col].mean()
    return medium_cost

path = 'sample data\california_housing_train.csv'
data = pd.read_csv(path)

print(form_med_in_range(data, 0, 500, 'population', 'median_house_value'))