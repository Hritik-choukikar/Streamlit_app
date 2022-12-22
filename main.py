import streamlit as st

from sklearn import linear_model
import pandas as pd
import numpy as np
import pickle

def load_model():
    with open('model_pickle','rb') as f:
        data=pickle.load(f)
    return data
data=load_model()


def show_predict_page():


    st.title("Home Price Prediction Model")
    st.write('We need some information to predict the Home price')
    area=st.slider("area",0,10000,2500,key='HG1325')


    bedrooms = st.slider("bedrooms", 0, 25, 2,key='658579')
    age = st.slider("age", 0, 100, 3,key='yfikf')
    print(type(area),bedrooms,age)

    predict=st.button("Calculate Price")

    if predict:

         pre=data.predict([[area,bedrooms,age]])
         pre=int(pre)
         st.subheader(f"The Estimated Price Is : Rs {pre}")







