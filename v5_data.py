import pandas

data = pandas.read_excel('GVP2.xls', index_col=None, 
                         skiprows=1)

data2 = pandas.read_excel('GVP3.xls', index_col=None, 
                          skiprows=1)

data.dropna(axis=0, how='any', thresh=None, 
            subset=None, inplace=False)

data2.dropna(axis=0, how='any', thresh=None, 
             subset=None, inplace=False)

data.to_csv('GVP.csv', index=False, encoding='utf-8')
data2.to_csv('GVP2.csv', index=False, encoding='utf-8')