import pickle
import os.path

def createSkynet():

    # checks if training data file exists. if not, creates it.

    if  not os.path.isfile("traningData"):
        import data
        data.exportTrainingData()

    # retrives the training data and formates it into a 2d array [[input], [expected_output]]

    with open('trainingData', 'rb') as td:
        trainingData = pickle.load(td)
    trainingData = [[trainingData[i][:-1] for i in trainingData],[trainingData[i][-1] for i in trainingData]]

    # scikit is used for the machine learning part of the assignment

    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline

    #creats a pipeline. aka. sets up the Ai
    pipeline = Pipeline([("scale", StandardScaler()),("model",RandomForestClassifier())])

    #fits/trains the Ai
    skynet  = pipeline.fit(trainingData[0],trainingData[1])

    #exports the Ai as a file. makes it easy to just load and use as need be.
    with open("skynet","wb") as sn:
        pickle.dump(skynet,sn)


#recreats the Ai if the file is run
if __name__ == "__main__":
    createSkynet()
