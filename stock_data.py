# import pandas_datareader.data as web
# from pandas_datareader import data
# import fix_yahoo_finance as yf
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("CSV_test.csv", index_col='Date')
print(dataset.head())

print (type(dataset['Open'][0]))
training_set = dataset[:'2016'].iloc[:,1:2].values
print (training_set[4])


print (type(training_set))

print (training_set.shape)

