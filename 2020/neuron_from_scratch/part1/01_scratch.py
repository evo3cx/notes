import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [
   [0.2, 0.8, -0.5, 1.0],
   [0.5, -0.91, 0.26, -0.5],
   [-0.26, -0.27, 0.17, 0.87]
]
bias1 = 2.0
bias2 = 3.0
bias3 = 0.5

# STEP 1 neuron 1 layer dengan cara sederhana
output = [
    inputs[0]*weights[0][0]+inputs[1]*weights[0][1] +    inputs[2]*weights[0][2]+inputs[3]*weights[0][3]+bias1,
    inputs[0]*weights[1][0]+inputs[1]*weights[1][1] +    inputs[2]*weights[1][2]+inputs[3]*weights[1][3]+bias2,
    inputs[0]*weights[2][0]+inputs[1]*weights[2][1] +    inputs[2]*weights[2][2]+inputs[3]*weights[2][3]+bias3,
]
print(output)


# STEP 2 neuron 1 layer menggunakan loop
biases = [2.0, 3.0, 0.5]
output_loop = []
for weight, bias in zip(weights, biases):
    current_output = 0

    for i, w in zip(inputs, weight):
        current_output += i * w

    current_output += bias
    output_loop.append(current_output)
print("output loop", output_loop)


# STEP 3 neuron 1 layer menggunakan numpy
output_np = np.dot(weights, inputs) + biases
print("output np.dot", output_np)


weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2.0
bias2 = 3.0
bias3 = 0.5

output = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,
          inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
          inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3]
print(output)


print("bfore np", weights, inputs, biases)
output = np.dot(weights, inputs) + biases
print(output)
