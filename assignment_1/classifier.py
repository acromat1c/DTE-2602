import pickle
import os.path

#retrueves the the Ai
def getSkynet():
    #if Ai is not created. it creates it
    if  not os.path.isfile("skynet"):
        import createSkynet
        createSkynet.createSkynet()

    #loades Ai
    with open('skynet', 'rb') as sn:
        return pickle.load(sn)

#takes variables X and classifies the animal
def classify_animal(*X):
    #formats input so that its correct in case its wrong
    if type(X[0]) != list: X = [X]
    elif type(X[0][0]) != list: ...
    elif type(X[0][0][0]) != list: X = X[0]
    #runs input through ai and returns output
    return getSkynet().predict(X)


# lets you manualy enter data if you run the file
if __name__ == "__main__":
    inp= []
    for i in ["hair", "feathers", "eggs", "milk", "airborne", "aquatic", "predator", "toothed", "backbone", "breathes", "venomous", "fins", "legs", "tail", "domestic", "catsize"]:
        print(i,": ",sep="",end="");inp.append(input())
    classify_animal(inp)