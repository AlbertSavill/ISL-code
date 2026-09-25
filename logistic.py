#logistic regression
import math
beta_0 = input()
beta_1 = input()
X = input()

print(f"Enter beta_0: {beta_0}")
print(f"Enter beta_1: {beta_1}")
print(f"Enter X: {X}")
#e = 2.71828

linear_score = beta_0 + beta_1 * X

exponential_score = math.exp(linear_score) # this takes e and turns linear score
# to z

probability = exponential_score / (1 + exponential_score)

print(probability)
