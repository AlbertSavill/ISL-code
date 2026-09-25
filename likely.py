#likelihood function
import math

x_values = [1, 2, 3, 4]
y_values = [0, 0, 1, 1]

beta_0 = -3
beta_1 = 1

likelihood = 1.0

for i in range(len(x_values)):

    linear_score = beta_0 + beta_1 * x_values[i]

    expotential_score = math.exp(linear_score)

    probability = expotential_score / (1 + expotential_score)

    if y_values[i] == 1:
        likelihood *= probability

    else:
        likelihood *= (1 - probability)

    print(
            "X:", x_values[i],
            "Y:", y_values[i],
            "Probability:", probability
    )

print("Likelihood:", likelihood)



