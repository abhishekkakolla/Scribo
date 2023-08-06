import numpy

# Loading the data
file = open("data\\training_data.npy", "rb")
array = numpy.load(file, allow_pickle=True)

data = [10, 20, 30, 40, 50]
std = numpy.std(data)
print(std)