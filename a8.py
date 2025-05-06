from neural import *
import csv 
training_data = [
 
 ]
with open ('Politics.csv', 'r') as csvfile:
     reader = csv.reader(csvfile)
     for row in reader:
         # Process each row
         training_data.append(row)
print("<<<<<<<<<<<<<< XOR >>>>>>>>>>>>>>\n")


politics = NeuralNet(5,6,1)
politics.train(training_data, learning_rate = 0.7, iters = 10000, print_interval = 1000)
print(politics.test_with_expected(training_data))

print(politics.evaluate([1.0, 1.0, 1.0, 0.1, 0.1]))
print(politics.evaluate([0.5, 0.2, 0.1, 0.7, 0.7]))
print(politics.evaluate([0.8, 0.3, 0.3, 0.3, 0.8]))
print(politics.evaluate([0.8, 0.3, 0.3, 0.8, 0.3]))
print(politics.evaluate([0.9, 0.8, 0.8, 0.3, 0.6]))