
import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("house_model.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(MedInc,HouseAge,Population,AveOccup):
   
    prediction=classifier.predict([[MedInc,HouseAge,Population,AveOccup]])
    print(prediction)
    return prediction



def main():
    st.title("House Prediction: Boston City")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit House Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    MedInc = st.text_input("MedInc","Type Here")
    HouseAge = st.text_input("HouseAge","Type Here")
    Population = st.text_input("Population","Type Here")
    AveOccup = st.text_input("AveOccup","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(eval(MedInc), 
                                           eval(HouseAge), 
                                           eval(Population), 
                                           eval(AveOccup)
                                          )
        st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("This is about House Prediction")

if __name__=='__main__':
    main()
    
    
    