# numpy is used for array operations
import numpy as np
# pickle is used to load the saved model
import pickle
# pandas is used to read the csv file
import pandas as pd


#  loading the saved model
loadedModel = pickle.load(
    open('G:\python_workspaces/modelDeploying/trainedModel.sav', 'rb'))

# creating a function for prediction