 #import all required library:

import pandas as pd
import numpy as np
import matplotlib as plt
import plotly
import cufflinks as cf
cf.go_offline()
import re
import seaborn as sns
import numpy as np



# read the data which is fetched from web:
df = pd.read_csv('D:/ts-mesh-pipeline/dummy-data-product/src/dependencies/scraping/final_output.csv',low_memory=False)
# check null value in region column:
df[df['region'].isnull()]
#print(df)
# create two more column to store the date and value:
df1=df.melt(id_vars=["geo_type","region","transportation_type","alternative_name","sub-region","country"],
        var_name="Date",
        value_name="Value")
# to remove the "Unnamed:0" value from created data column:
df2= df1[~df1.Date.str.contains("Unnamed: 0")]


def check_dir(data_frame):
         directory = os.path.dirname("D:/ts-mesh-pipeline/dummy-data-product/src/dependencies/cleaning")
         if not os.path.exists(directory):
                 os.makedirs(directory)
                 data_frame = pd.DataFrame(df2)
                 data_frame.to_csv('cleaned.csv')

#print df2[df2['region'] == "Argentina","Australia","Austria","Estonia","Finland","France","Germany","Greece","Hong Kong","Hungary","Iceland","India","Belgium","Brazil","Bulgaria","Cambodia","Canada","Chile","Colombia","Croatia","Czech Republic","Denmark","Egypt","United States","Switzerland"
#]
#df3=df2.plot(kind = 'area' , figsize = (20,10), alpha = .4,stacked = True)
df3=df2.plot.line(x = 'Date' , y = 'Value',c = 'BLUE',figsize = (20,10))
df3
print(df3)
# for description of data:
#df3.describe()









#max(df_groupby.loc['telephone','yes'][0],df_groupby.loc['unknown','yes'][0],df_groupby.loc['cellular','yes'][0])

#return (df) 

#len(df1['campaign'].unique())
#len(set(list(df1['campaign'])))
#df1["month"].value_counts().index[0]

#df.plot(figsize  = (20,10))

#df.plot.hexbin(x = 'SepalLengthCm' , y = 'PetalLengthCm' , gridsize= 10 ,C ='SepalWidthCm' )

#df.iplot(kind ='bubble3d' , x ='SepalLengthCm' , y ='SepalWidthCm' , z= 'PetalLengthCm' ,size =  'PetalWidthCm')

