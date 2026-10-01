#LDA Mean and shared variance
import math

x_values = [2, 4, 6, 8, 10, 12]
y_values = [1, 1, 1, 2, 2, 2]

classes = [1, 2]

class_means = {}

# estimate u_k for each class
for k in classes:
    total = 0
    class_count = 0

    for i in range(len(x_values)):
        if y_values[i] == k:
            total += x_values[i]
            class_count += 1
    class_means[k] = total / class_count

print("Class means:", class_means)

squared_difference_total = 0

for k in classes:
    for i in range(len(x_values)):
        if y_values[i] == k:
            difference = x_values[i] - class_means[k]
            squared_difference_total += difference ** 2

n = len(x_values)
K = len(classes)

shared_variance = squared_difference_total / (n - K)
shared_standard_deviation = math.sqrt(shared_variance)

print("Shared variance:", shared_variance)
print("Shared standard deviation:", shared_standard_deviation)

