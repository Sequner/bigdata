import pandas as pd

df = pd.read_excel(r'data_academic_performance.xlsx')
newdf = df[['UNIVERSITY', 'ACADEMIC_PROGRAM']]
print(newdf)
