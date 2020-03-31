# # from random import seed
# from random import random

# # Initialize a network
# def initialize_network(n_inputs, n_hidden, n_outputs):
# 	network = list()
# 	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
# 	network.append(hidden_layer)
# 	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
# 	network.append(output_layer)
# 	return network

# seed(1)
# network = initialize_network(2, 1, 2)
# for layer in network:
# 	print(layer)
# [{'weights': [0.13436424411240122, 0.8474337369372327, 0.763774618976614]}]
# [{'weights': [0.2550690257394217, 0.49543508709194095]}, {'weights': [0.4494910647887381, 0.651592972722763]}]

# # Calculate neuron activation for an input
# def activate(weights, inputs):
# 	activation = weights[-1]
# 	for i in range(len(weights)-1):
# 		activation += weights[i] * inputs[i]
# 	return activation

# output = 1 / (1 + e^(-activation))

# # Transfer neuron activation
# def transfer(activation):
# 	return 1.0 / (1.0 + exp(-activation))
# # Forward propagate input to a network output
# def forward_propagate(network, row):
# 	inputs = row
# 	for layer in network:
# 		new_inputs = []
# 		for neuron in layer:
# 			activation = activate(neuron['weights'], inputs)
# 			neuron['output'] = transfer(activation)
# 			new_inputs.append(neuron['output'])
# 		inputs = new_inputs
# 	return inputs

# from math import exp

# # Calculate neuron activation for an input
# def activate(weights, inputs):
# 	activation = weights[-1]
# 	for i in range(len(weights)-1):
# 		activation += weights[i] * inputs[i]
# 	return activation

# # Transfer neuron activation
# def transfer(activation):
# 	return 1.0 / (1.0 + exp(-activation))

# # Forward propagate input to a network output
# def forward_propagate(network, row):
# 	inputs = row
# 	for layer in network:
# 		new_inputs = []
# 		for neuron in layer:
# 			activation = activate(neuron['weights'], inputs)
# 			neuron['output'] = transfer(activation)
# 			new_inputs.append(neuron['output'])
# 		inputs = new_inputs
# 	return inputs

# # test forward propagation
# network = [[{'weights': [0.13436424411240122, 0.8474337369372327, 0.763774618976614]}],
# 		[{'weights': [0.2550690257394217, 0.49543508709194095]}, {'weights': [0.4494910647887381, 0.651592972722763]}]]
# row = [1, 0, None]
# output = forward_propagate(network, row)
# print(output)

# derivative = output * (1.0 - output)

# # Calculate the derivative of an neuron output
# def transfer_derivative(output):
# 	return output * (1.0 - output)

# error = (expected - output) * transfer_derivative(output)

# # Backpropagate error and store in neurons
# def backward_propagate_error(network, expected):
# 	for i in reversed(range(len(network))):
# 		layer = network[i]
# 		errors = list()
# 		if i != len(network)-1:
# 			for j in range(len(layer)):
# 				error = 0.0
# 				for neuron in network[i + 1]:
# 					error += (neuron['weights'][j] * neuron['delta'])
# 				errors.append(error)
# 		else:
# 			for j in range(len(layer)):
# 				neuron = layer[j]
# 				errors.append(expected[j] - neuron['output'])
# 		for j in range(len(layer)):
# 			neuron = layer[j]
# 			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

# # Calculate the derivative of an neuron output
# def transfer_derivative(output):
# 	return output * (1.0 - output)

# # Backpropagate error and store in neurons
# def backward_propagate_error(network, expected):
# 	for i in reversed(range(len(network))):
# 		layer = network[i]
# 		errors = list()
# 		if i != len(network)-1:
# 			for j in range(len(layer)):
# 				error = 0.0
# 				for neuron in network[i + 1]:
# 					error += (neuron['weights'][j] * neuron['delta'])
# 				errors.append(error)
# 		else:
# 			for j in range(len(layer)):
# 				neuron = layer[j]
# 				errors.append(expected[j] - neuron['output'])
# 		for j in range(len(layer)):
# 			neuron = layer[j]
# 			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

# # test backpropagation of error
# network = [[{'output': 0.7105668883115941, 'weights': [0.13436424411240122, 0.8474337369372327, 0.763774618976614]}],
# 		[{'output': 0.6213859615555266, 'weights': [0.2550690257394217, 0.49543508709194095]}, {'output': 0.6573693455986976, 'weights': [0.4494910647887381, 0.651592972722763]}]]
# expected = [0, 1]
# backward_propagate_error(network, expected)
# for layer in network:
# 	print(layer)

# weight = weight + learning_rate * error * input

# # Update network weights with error
# def update_weights(network, row, l_rate):
# 	for i in range(len(network)):
# 		inputs = row[:-1]
# 		if i != 0:
# 			inputs = [neuron['output'] for neuron in network[i - 1]]
# 		for neuron in network[i]:
# 			for j in range(len(inputs)):
# 				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
# 			neuron['weights'][-1] += l_rate * neuron['delta']

# # Train a network for a fixed number of epochs
# def train_network(network, train, l_rate, n_epoch, n_outputs):
# 	for epoch in range(n_epoch):
# 		sum_error = 0
# 		for row in train:
# 			outputs = forward_propagate(network, row)
# 			expected = [0 for i in range(n_outputs)]
# 			expected[row[-1]] = 1
# 			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
# 			backward_propagate_error(network, expected)
# 			update_weights(network, row, l_rate)
# 		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))

from math import exp
from random import seed
from random import random
import os
import matplotlib.pyplot as plt


# Initialize a network
x1=[]
y1=[]

def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network

# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
# 	print(weights[-1])
	for pp in range(len(weights)-1):
# 		print(weights[i],inputs[i])
		# print("w=",len(weights),"pp=",pp,"cc=",cc)
		w1=str(weights[pp]*10000)
		i1=str(inputs[pp]*10000)
		a1=str(activation*100000000)      
		w1=w1.split(".") 
		w2=bin(int(w1[0]))
		w3=w2.split("b")[1]
		for j in range(16-len(w3)):
			w3=reverse(reverse(w3)+"0")
		i1=i1.split(".")
		i2=bin(int(i1[0]))
		i3=i2.split("b")[1]
		for j in range(16-len(i3)):
			i3=reverse(reverse(i3)+"0")
		a1=a1.split(".")
		a2=bin(int(a1[0]))
		a3=a2.split("b")[1]
		for j in range(32-len(a3)):
			a3=reverse(reverse(a3)+"0")
		file1 = open("MyFile1.txt","w")
		file2 = open("MyFile2.txt","w")
		file3 = open("MyFile3.txt","w")
		file1.write(w3)
		file2.write(i3)
		file3.write(a3)       
		file1.close()
		file2.close()
		file3.close()
		cmd = "iverilog mult.v && ./a.out"
		os.system(cmd)
		file4 = open("MyFile.txt","r+")
		rr1=file4.read()
		file4.close()
		rr2=int(rr1,2)

		if (w2[0]==i2[0]):
			if (a2[0]!='-'):
				cmd1 = "iverilog add.v && ./a.out"
				os.system(cmd1)
				file0 = open("MyFilef.txt","r+")
				r1=file0.read()
				file0.close()
				r2=float(int(r1,2))/100000000  
			else:
				if(rr2>int(a1[0])):
					cmd1 = "iverilog sub1.v && ./a.out"
					os.system(cmd1)
					file0 = open("MyFilef.txt","r+")
					r1=file0.read()
					file0.close()
					r2=float(int(r1,2))/100000000 
				else:
					cmd1 = "iverilog add.v && ./a.out"
					os.system(cmd1)
					file0 = open("MyFilef.txt","r+")
					r1=file0.read()
					file0.close()
					r2=-1*(float(int(r1,2))/100000000)
		else:
			if (a2[0]=='-'):
				 cmd1 = "iverilog add.v && ./a.out"
				 os.system(cmd1)
				 file0 = open("MyFilef.txt","r+")
				 r1=file0.read()
				 file0.close()
				 r2=-1*(float(int(r1,2))/100000000)
			else:
				if(rr2>int(a1[0])):
					cmd1 = "iverilog sub1.v && ./a.out"
					os.system(cmd1)
					file0 = open("MyFilef.txt","r+")
					r1=file0.read()
					file0.close()
					r2=-1*(float(int(r1,2))/100000000)
				else:
					cmd1 = "iverilog sub1.v && ./a.out"
					os.system(cmd1)
					file0 = open("MyFilef.txt","r+")
					r1=file0.read()
					file0.close()
					r2=-1*(float(int(r1,2))/100000000)
					
		
		# activation += weights[pp] * inputs[pp]
		activation=r2
	return activation

# Transfer neuron activation
def transfer(activation):
	return 1.0 / (1.0 + exp(-activation))

# Forward propagate input to a network output
def forward_propagate(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs

# Calculate the derivative of an neuron output
def transfer_derivative(output):
	return output * (1.0 - output)

# Backpropagate error and store in neurons
def backward_propagate_error(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					w1=str(neuron['weights'][j]*10000)
					i1=str(neuron['delta']*10000)
					a1=str(error*100000000)      
					w1=w1.split(".") 
					w2=bin(int(w1[0]))
					w3=w2.split("b")[1]
					for jj in range(16-len(w3)):
						w3=reverse(reverse(w3)+"0")
					i1=i1.split(".")
					i2=bin(int(i1[0]))
					i3=i2.split("b")[1]
					for jj in range(16-len(i3)):
						i3=reverse(reverse(i3)+"0")
					a1=a1.split(".")
					a2=bin(int(a1[0]))
					a3=a2.split("b")[1]
					for jj in range(32-len(a3)):
						a3=reverse(reverse(a3)+"0")
					file1 = open("MyFile1.txt","w")
					file2 = open("MyFile2.txt","w")
					file3 = open("MyFile3.txt","w")	
					file1.write(w3)
					file2.write(i3)
					file3.write(a3)       
					file1.close()
					file2.close()
					file3.close()
					cmd = "iverilog mult.v && ./a.out"
					os.system(cmd)
					file4 = open("MyFile.txt","r+")
					rr1=file4.read()
					file4.close()
					rr2=int(rr1,2)

					if (w2[0]==i2[0]):	
						if (a2[0]!='-'):
							cmd1 = "iverilog add.v && ./a.out"
							os.system(cmd1)
							file0 = open("MyFilef.txt","r+")
							r1=file0.read()
							file0.close()
							r2=float(int(r1,2))/100000000  
						else:
							if(rr2>int(a1[0])):
								cmd1 = "iverilog sub1.v && ./a.out"
								os.system(cmd1)
								file0 = open("MyFilef.txt","r+")
								r1=file0.read()
								file0.close()
								r2=float(int(r1,2))/100000000 
							else:
								cmd1 = "iverilog add.v && ./a.out"
								os.system(cmd1)
								file0 = open("MyFilef.txt","r+")
								r1=file0.read()
								file0.close()
								r2=-1*(float(int(r1,2))/100000000)	
					else:
						if (a2[0]=='-'):
							cmd1 = "iverilog add.v && ./a.out"
							os.system(cmd1)
							file0 = open("MyFilef.txt","r+")
							r1=file0.read()
							file0.close()
							r2=-1*(float(int(r1,2))/100000000)
						else:
							if(rr2>int(a1[0])):
								cmd1 = "iverilog sub1.v && ./a.out"
								os.system(cmd1)
								file0 = open("MyFilef.txt","r+")
								r1=file0.read()
								file0.close()
								r2=-1*(float(int(r1,2))/100000000)
							else:
								cmd1 = "iverilog sub1.v && ./a.out"
								os.system(cmd1)
								file0 = open("MyFilef.txt","r+")
								r1=file0.read()
								file0.close()
								r2=-1*(float(int(r1,2))/100000000)	
					#error += (neuron['weights'][j] * neuron['delta'])
				errors.append(r2)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

# Update network weights with error
def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']

# print(float_bin(n, places = p)) 

# Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			outputs = forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[row[-1]] = 1
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)
		x1.append(epoch)
		y1.append(sum_error)
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
        
def reverse(string): 
	string = "".join(reversed(string)) 
	return string 

# Test training backprop algorithm
seed(1)
dataset = [[12.781,2.550,0],
	[11.465,2.362,0],
	[13.396,4.411,0],
	[11.388,1.850,0],
	[13.064,3.405,0],
	[17.627,2.759,1],
	[15.332,2.188,1],
	[16.922,1.771,1],
	[18.675,-0.242,1],
	[17.673,3.518,1]]
n_inputs = len(dataset[0]) - 1
n_outputs = len(set([row[-1] for row in dataset]))
network = initialize_network(n_inputs, 2, n_outputs)
train_network(network, dataset, 0.45, 25, n_outputs)

	# print(layer)

print(x1)
print(y1)
plt.plot(x1,y1,color='r')
plt.xlabel("epochs")
plt.ylabel("Errors")
plt.title("Back Propagation")
plt.show()