import streamlit as st 
import pandas as pd
import joblib
joblib.load("My_First_Model.h5")
    
    
    
    
    
st.markdown("<h1 style='text-align:center;'>Heart Disease Prediction</h1>",unsafe_allow_html=True)

st.markdown("<i><h3 style='text-align:center;color:red'>To check whether a person is prone to heart disease<h3><i>",unsafe_allow_html=True)
 

 
age = st.sidebar.number_input("Enter your age: ")

sex = st.sidebar.radio("Sex",["Male","Female","Helicopter","I do not wish to provide this information"])

cp = st.sidebar.radio("Chest pain type",(0,1,2,3))

trestbps = st.sidebar.number_input("Resting blood pressure: ")

chol = st.sidebar.number_input("serum cholestrol in mg/dl: ")

fbs = st.sidebar.radio("Fasting blood sugar",(0,1))

restecg = st.sidebar.number_input("Resting electrocardiographic result: ")

thalach = st.sidebar.number_input("Maximum heat rate acheived: ")

exang = st.sidebar.radio("Exercise induced angina: ",(0,1,2,3))

oldpeak = st.sidebar.number_input(" oldpeak")

slope = st.sidebar.number_input("he slope of the peak exercise ST segmen")

ca = st.sidebar.radio("Number of major vessels", (0,1,2,3))

thal = st.sidebar.radio("thal",(0,1,2))



if st.button("Predict !"):
    st.success("Thanks for submitting")
    prediction = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    st.sucsess(prediction)
