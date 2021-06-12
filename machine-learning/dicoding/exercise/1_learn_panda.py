import os
import pandas as pd

os.listdir('sample_data')


# load file from sample data
df = pd.read_csv('sample_data/california_housing_train.csv');

print(df.head());
print ("nothing happend?");
