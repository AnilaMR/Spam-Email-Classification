import streamlit as st
import pickle

st.title("Email Spam Classifier")
message = st.text_area("Enter the email text:")

Detector = pickle.load(open('Detector.pkl','rb'))
feature_extraction = pickle.load(open('feature_extraction.pkl','rb'))

if st.button("Classify"):
    if message:
        vector= feature_extraction.transform([message])
        result=Detector.predict(vector)
        if result==[1]:
            st.header("Not Spam")
        else:
            st.header("Spam")










        

       
    
