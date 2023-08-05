import numpy

training_data = ["hi", "yes"]

file = open("data\\training_data", "wb") # writing in binary
numpy.save(file, training_data)
file.close
