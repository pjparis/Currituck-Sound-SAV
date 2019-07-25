'''
DataframePickleJar is designed to one simple thing: write one or more pandas dataframes to a Python 'pickle' container.

Dependencies:

Pandas 0.24.2 (though I'm pretty sure that earlier versions back to and including 0.21, and later 0.25, will work just fine).

Python 3.7, but again, this should work in any python that can import pandas 0.21 or later.

7/25/2019

'''
import pandas as pd

data_path = '../datasets/'
files = ['CS05_Current.csv','CS05_WQ.csv','CS05_Waves.csv']    # 'CS03_Kd.csv',

for file in files:
    dft = pd.read_csv(data_path+file)
    dft.to_pickle(data_path+'pickles/'+file+'.pkl')
