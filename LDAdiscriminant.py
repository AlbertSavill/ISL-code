#LDA Discriminant
import math

x = 7
variance = 4

means = [4, 8]
priors = [0.5, 0.5]

scores = []

for k in range(len(means)):
    mean_k = means[k]
    prior_k = priors[k]

    first_term = (x * mean_k) / variance
    second_term = (mean_k ** 2) / (2 * variance)
    prior_term = math.log(prior_k)

    discriminant_score = (first_term - second_term + prior_term)
    scores.append(discriminant_score)

    print("Class", k + 1, "score:", discriminant_score)

predicted_class = scores.index(max(scores)) + 1
