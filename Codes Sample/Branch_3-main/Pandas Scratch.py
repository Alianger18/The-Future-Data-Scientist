import pandas as pd
data = {}
data['Country'] = ['Moroccoo', 'Canada', 'UK', 'United States']
data['Year'] = [1956, 1998, 1975, 1999]
data['Rank'] = [58, 6, 3, 1]
df = pd.DataFrame(data, index=[1,2,3,4])
print(df[(df['Year'] > 1974) | (df['Rank'] > 2)])
