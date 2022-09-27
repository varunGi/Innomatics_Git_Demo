import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
image = Image.open('C:/Users/Varshith/OneDrive/Desktop/Intership/ML_Application/diamond.jpg')


df=pd.read_csv("diamonds .csv")
st.header("**Welcome to Diamond Price Prediction**")
df.drop_duplicates(inplace=True)


df=df.drop(df[df['x']==0].index)
df=df.drop(df[df['y']==0].index)
df=df.drop(df[df['z']==0].index)

Q1 = df.price.quantile(0.25)
Q3 = df.price.quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5*IQR
upper_limit = Q3 + 1.5*IQR

df = df[(df.price>lower_limit)&(df.price<upper_limit)]  
X=df[['carat','cut','color','clarity','x','y','z']]
y=df['price']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 25)

cut_class_dict = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5, }
clarity_dict   = {'I1': 1, 'SI2': 2, 'SI1': 3, 'VS1': 5, 'VS2': 4, 'VVS2': 6, 'VVS1': 7, 'IF': 8 }
color_dict     = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6,'D': 7,} 

x_train['cut'] = x_train['cut'].map(cut_class_dict)
x_train['clarity'] = x_train['clarity'].map(clarity_dict)
x_train['color'] = x_train['color'].map(color_dict)

x_test['cut'] = x_test['cut'].map(cut_class_dict)
x_test['clarity'] = x_test['clarity'].map(clarity_dict)
x_test['color'] = x_test['color'].map(color_dict)

from sklearn.neighbors import KNeighborsRegressor
knn_regressor = KNeighborsRegressor(n_neighbors=6)
knn_regressor.fit(x_train, y_train)

st.image(image)
carat=st.number_input("Enter the diamond carat")
cut=st.selectbox("Enter the cut",('Ideal','Premium','Good','Very Good','Fair'))
color=st.selectbox("Enter the colour",('E','I','J','H','F','G','D'))
clarity=st.selectbox("Enter the clarity",('SI2','SI1','VS1','VS2','VVS2','VVS1','I1','IF'))
st.write("Enter dimensions")
x=st.number_input("Enter X value:")
y=st.number_input("Enter Y value:")
z=st.number_input("Enter Z value:")

cut=cut_class_dict[cut]
clarity=clarity_dict[clarity]
color=color_dict[color]

arr=[carat,cut,color,clarity,x,y,z]
res=knn_regressor.predict([arr])
if st.button("Predict Diamond Price"):

    st.write("Price of the diamond is  "+str(int(res[0]))+" $")

    st.balloons()
    
