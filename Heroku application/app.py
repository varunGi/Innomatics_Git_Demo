import numpy as np
import streamlit as st
from PIL import Image
from pickle import load

knn_model=load(open('models/knn_regressor.pkl','rb'))
cut_class_dict = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5, }
clarity_dict   = {'I1': 1, 'SI2': 2, 'SI1': 3, 'VS1': 5, 'VS2': 4, 'VVS2': 6, 'VVS1': 7, 'IF': 8 }
color_dict     = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6,'D': 7,} 

def main():
    st.header("**💎 Welcome to Diamond Price Prediction 💎**")
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
    q=[carat,cut,color,clarity,x,y,z]

    btn_click= st.button("Predict")
    q=np.array(q).reshape(1,-1)
    if btn_click==True:
        if carat and cut and color and clarity and x and y and z:
            pred= knn_model.predict(q)
            st.success("Price of Diamond is "+str(int(pred[0]))+"$")
            st.balloons()
        else:
            st.error("Enter the value properly")
        
if __name__ == "__main__":
    main()
