# numpy is used for array operations
import numpy as np
# pickle is used to load the saved model
import pickle
# pandas is used to read the csv file
import pandas as pd

import streamlit as st


#  loading the saved model
loadedModel = pickle.load(
    open('G:\python_workspaces/modelDeploying/trainedModel.sav', 'rb'))

# creating a function for prediction


def diabetesPrediction(inputData):
    # predicts whether the person is diabetic or not ( 1 or 0 )
    inputData = (0, 137, 40, 35, 168, 43.1, 2.288, 33
                 )

    inputDataNumpyArray = np.asarray(inputData)

    # parameter for reshaping for only one instance 1, -1 tells you this.
    inputDataReshaped = inputDataNumpyArray.reshape(1, -1)

    prediction = loadedModel.predict(inputDataReshaped)

    print(prediction)

    if (prediction[0] == 0):
        print("The person is not Diabetic")

    else:
        print("The person is diabetic")


def main():
    # giving the title

    st.title("Diabetes Prediction Web App")

    # we have to create a sidebar for the user to enter the data
    # we have to remove the last column from the dataset
    # Names of Columns of dataset are below
    # Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age

    # below are the datafields in which user can enter the data

    pregnancy = st.text_input("Pregnancy", "Type Here")
    glucose = st.text_input("Glucose", "Type Here")
    bloodPressure = st.text_input("Blood Pressure", "Type Here")
    skinThickness = st.text_input("Skin Thickness", "Type Here")
    insulin = st.text_input("Insulin", "Type Here")
    bmi = st.text_input("BMI", "Type Here")
    diabetesPedigreeFunction = st.text_input(
        'Diabetes Pedigree Function', "Type Here")
    age = st.text_input("Age", "Type Here")

    # code for prediction

    # a null string which does not have any value, if the user has not entered any data

    diagnosis = ""

    # creating a button for prediction

    if st.button("Diabetes Test Result"):

        # final output
        diagnosis =
