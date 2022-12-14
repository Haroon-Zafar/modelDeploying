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
        return("not Diabetic")

    else:
        return("diabetic")


def main():
    # giving the title

    st.title("Diabetes Prediction Web App")

    # we have to create a sidebar for the user to enter the data
    # we have to remove the last column from the dataset
    # Names of Columns of dataset are below
    # Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age

    # below are the datafields in which user can enter the data

    pregnancy = st.text_input("Pregnancy")
    glucose = st.text_input("Glucose")
    bloodPressure = st.text_input("Blood Pressure")
    skinThickness = st.text_input("Skin Thickness")
    insulin = st.text_input("Insulin")
    bmi = st.text_input("BMI")
    diabetesPedigreeFunction = st.text_input(
        'Diabetes Pedigree Function')
    age = st.text_input("Age")

    # code for prediction

    # a null string which does not have any value, if the user has not entered any data

    diagnosis = ""

    # creating a button for prediction

    if st.button("Diabetes Test Result"):

        # final output
        # Passing Column's variables into the function

        diagnosis = diabetesPrediction(
            [pregnancy, glucose, bloodPressure, skinThickness, insulin, bmi, age])

    # .success() is used to give a green color to the text
    # if you come out of the if block, it will print the diagnosis
    st.success('The person is {}'.format(diagnosis))


# this predicts the output but won't run from here you have to run it from anaconda cmd


if __name__ == "__main__":
    main()
