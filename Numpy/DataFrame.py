import pandas as pd
import pyperclip
from pandas import Series, DataFrame

#Analysis of largest companies in the world by revenue

revenue_df = pd.DataFrame([[pyperclip.paste(),columns = ['Rank', 'Name','Industry Revenue','Profit','Employees','Country']])
#rev_df = Series(pyperclip.paste())
#revenue_df = pd.DataFrame([revenue_df, columns = 'Rank','Name','Industry	Revenue(USD millions)',	'Profit(USD millions)','Employees','CountryRef'])
#print(revenue_df)

print(rev_df.head(5))