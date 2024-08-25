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
    return getSkynet().predict([X])