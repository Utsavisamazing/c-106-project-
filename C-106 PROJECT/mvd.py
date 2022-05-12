import pandas as pd 
import plotly.express as px
import numpy as np

df = pd.read_csv("marksvsdayspresent.csv")

input = df ["Days Present"].to_list()
output = df["Marks In Percentage"].to_list()


figure = px.scatter(x=input , y=output )
figure.show()

data1=np.corrcoef(input,output)
print(data1[0][1]) 


