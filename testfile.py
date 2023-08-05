import numpy

file = open("array", "rb")
arr1 = numpy.load(file)
print(arr1)