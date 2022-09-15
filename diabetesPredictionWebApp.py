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
