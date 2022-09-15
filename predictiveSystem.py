

import numpy as np
import pickle

# loading the saved model
# use forward slashes always in python

loadedModel = pickle.load(
    open('G:\python_workspaces/modelDeploying/trainedModel.sav', 'rb'))

# copy the prediction code from diaberesPrediction.ipynb

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
