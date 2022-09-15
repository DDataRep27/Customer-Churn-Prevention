# -*- coding: utf-8 -*-

#Import Libraries
import pandas as pd
import streamlit as st 
from pickle import load
import sklearn
from PIL import Image


#Title of web page
st.title('Welcome to Customer Churn - Telecom Prediction')


#Image on webpage
img = Image.open("bck.jpg")
st.image(img)


#Header for column
st.header("User Input Parameters")


#Input variables 
def user_input_features():
    col1, col2, col3 = st.columns(3)
    with col1:
        ctr = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
   
    with col2:
        isr = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
   
    with col3:
       mtl = st.selectbox("Multiple-Lines", ['No phone service', 'No', 'Yes'])
   
    with col1:
        tcg = st.number_input("Total Charges", min_value=0, step=1)
   
    with col2:
        ten = st.number_input("Tenure (months)",min_value=0, step=1)
   
    with col3:
        obp = st.selectbox("Online-Backup", ['Yes', 'No', 'No internet service'])
   
    with col1:
        tst = st.selectbox("Tech_Support", ['No', 'Yes', 'No internet service'])
   
    with col2:
        dpn = st.selectbox("Device-Protection", ['No', 'Yes', 'No internet service'])
   
    with col3:
        pse = st.selectbox("Phone_Service", ['No', 'Yes'])
   

    new = {'Contract': ctr,
           'InternetService': isr,
           'MultipleLines':mtl,
           'TotalCharges':tcg,
           'tenure': ten,
           'OnlineBackup': obp,
           'TechSupport': tst,
           'DeviceProtection': dpn,
           'PhoneService':pse
              }

    features = pd.DataFrame(new, index=[0])
    
    return features

#Running the function
df = user_input_features()


#Loading the model
model = load(open('Tchurn_intelligence.pkl', 'rb'))


#Predicting the model
result = model.predict(df)

st.empty()

if st.button('Predict'):
    #st.balloons()
    st.header('Predicted Result:')
    if result[0]==0:
        st.success("Customer will retain!!", icon='💰')
        good = Image.open("rnc.jpg")
        st.image(good)
        
        
    else:
        st.error('Customer will Churn!!', icon="🚨")
        bad  = Image.open("churn.png")
        st.image(bad)


if __name__=='__user_input_features__':
    user_input_features()


