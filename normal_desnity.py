#normal density
import math
x = 12
mean_k = 10
standard_deviation_k = 2

# (x - μ_k)²
squared_distance = (x - mean_k) ** 2

# 2σ_k²
variance_part = 2 * standard_deviation_k ** 2

# -(x - μ_k)² / 2σ_k²
exponent = -squared_distance / variance_part

# # 1 / (sqrt(2π)σ_k)
scaling_part = 1 / (math.sqrt(2 * math.pi) * standard_deviation_k)

# complete normal density
density = scaling_part * math.exp(exponent)

print("Squared distance: ", squared_distance)
print("Exponent: ", exponent)
print("Scaling part: ", scaling_part)
print("Density: ", density)
