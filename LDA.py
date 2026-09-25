#LDA
priors = [0.10, 0.90]
densities = [0.80, 0.133333]
class_name = ["default", "no default"]

scores = []

for i in range(len(class_name)):
    score = priors[i] * densities[i]
    scores.append(score)

# sum from l = 1 to K
denominator = sum(scores)

for i in range(len(class_name)):
    posterioir_probability = scores[i] / denominator

    print(
            class_name[i],
            posterioir_probability
    )

