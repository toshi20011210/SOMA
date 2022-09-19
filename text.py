import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

def imageToData(filename):
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8,8),PIL.Image.ANTIALIAS)

    numImage = numpy.asarray(grayImage, dtype = float)
    numImage = numpy.floor(16-16*(numImage/256))
    numImage = numImage.flatten()

    return numImage


def predictDigits(data): 
    digits = sklearn.datasets.load_digits()

    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data, digits.target)

    n = clf.predict([data])
    print("PREDICTION=",n)


data = imageToData("6.png")
predictDigits(data)

