#LDA no loops
# Prior probabilities: pie_k
prior_default = 0.10
prior_no_default = 0.90

# Density values: f_k(x)
# These represent how well this customer's x value fits each class
density_default = 0.80
density_no_default = 0.133333

# Numerator: pie_k * f_k(x)
default_score = prior_default * density_default
no_default_score = prior_no_default * density_no_default

# Denominator: sum of the scores for every class
denominator = default_score + no_default_score

# Posterior probabilities
probability_default = default_score / denominator
probability_no_default = no_default_score / denominator

print("Probability of default: ", probability_default)
print("Probability of no default: ", probability_no_default)
