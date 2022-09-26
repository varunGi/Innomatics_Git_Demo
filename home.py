import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
image = Image.open('C:/Users/Varshith/OneDrive/Desktop/Streamlit/Uk_pubs.jpg')
image1 =Image.open('C:/Users/Varshith/OneDrive/Desktop/Streamlit/pub.jpg')
image3 =Image.open('C:/Users/Varshith/OneDrive/Desktop/Streamlit/end.jpg')

df=pd.read_csv("open_pubs.csv")
df.columns=['fsa_id','name','address','postcode','easting','northing','latitude','longitude','local_authority']
df = df.replace(r'\\N',' ', regex=True)
df.drop(df.index[df['latitude']==' '],axis=0,inplace=True)
df['latitude']=df['latitude'].astype('float')
df['longitude']=df['longitude'].astype('float')

def home():

    st.title("Open Pubs Near by You")
    st.image(image1)
    st.subheader("Basic Information and Statistics")
    
    st.markdown("Given Data")
    st.write(df.head())

    st.markdown("*Description of Attributes*")
    st.write("fsa_id - Food Standard Agency's ID for this Pub")
    st.write("name - Name of the pub")
    st.write("address - Address felids separated by commas")
    st.write("postcode - Postcode of the pub")
    st.write("local_authority - Local authority this pub falls under")

    st.markdown("*Description of the data*")
    st.write(df.describe())
    st.sidebar.markdown("# Home Page")
def pub_loc():
    st.write("# Pub Locations")
    st.sidebar.markdown("# Pub Locations")
    st.image(image)
    local_auth=st.selectbox("Select the local authority",df.local_authority.unique())
    st.subheader("Here are the pubs in your local Authority")
    for i in range(50563):
        if(df.iloc[i,-1]==local_auth):
            st.write(df.iloc[i,1])



def Nearest_Pubs():
    st.write("# The 5 Pubs near You")
    st.sidebar.markdown("# Nearest Pubs")
    latitude=st.number_input("Enter your Latitude ",min_value=48,max_value=61)
    longitude=st.number_input("Enter your Longitude ",min_value=-8,max_value=2)
    near_pubs=[]
    for i in range(50563):
        x=((latitude-df.iloc[i,6])**2+(longitude-df.iloc[i,7])**2)**0.5
        near_pubs.append([df.iloc[i,1],x])
    near_pubs.sort(key=lambda x:x[1])
    st.write("Here are the 5 Pubs nearer to you")
    def pub():
        for i in range(5):
            st.write("# "+str(near_pubs[i][0]))
        st.balloons()
        st.image(image3,caption="Enjoy your Day")

    st.button("Enter",on_click=pub)
    

page_names_to_fun={
    "Home":home,
    "Pub Locations":pub_loc,
    "Nearest Pub":Nearest_Pubs
}
selected_page = st.sidebar.selectbox("Select a page", page_names_to_fun.keys())
page_names_to_fun[selected_page]()
