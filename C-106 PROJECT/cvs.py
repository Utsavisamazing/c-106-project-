import pandas as pd 
import plotly.express as px
import numpy as np

df = pd.read_csv("coffeevssleep.csv")

input = df ["Coffee in ml"].to_list()
output = df["sleep in hours"].to_list()
week= df["week"].tolist()

figure = px.scatter(x=input , y=output, color=week )
figure.show()

data1=np.corrcoef(input,output)
print(data1[0][1]) 



