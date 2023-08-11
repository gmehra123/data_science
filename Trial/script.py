import preprocessing as ps
import pandas as pd

data=pd.DataFrame({'A':[1,2,4],'B':[1,4,5]})
data=ps.pre1.low_case_columns(data)
print(data)
